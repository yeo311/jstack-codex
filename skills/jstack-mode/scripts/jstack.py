#!/usr/bin/env python3
"""개인 jstack 상태만 읽고 쓰는 표준 라이브러리 도구."""
import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

KINDS = ('understanding', 'features', 'verification', 'plans', 'reports', 'program', 'evidence')
STATES = ('pending', 'running', 'needs-verification', 'verified', 'blocked', 'done', 'abandoned')


def git(repo, *args):
    try:
        result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, text=True,
                                timeout=10, check=False)
        return result.stdout.strip() if result.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def identity(repo):
    repo = Path(repo).expanduser().resolve(strict=True)
    if not repo.is_dir():
        raise ValueError('프로젝트는 디렉터리여야 합니다.')
    top = git(repo, 'rev-parse', '--show-toplevel')
    if top:
        canonical = Path(top).resolve()
        common = git(repo, 'rev-parse', '--path-format=absolute', '--git-common-dir')
        if not common:
            raise ValueError('Git 공통 경로를 확인하지 못했습니다.')
        common = Path(common).resolve(strict=True)
        anchor = 'git:' + str(common)
        protected = [canonical, common]
        roots = git(repo, 'worktree', 'list', '--porcelain', '-z')
        if roots is None:
            raise ValueError('worktree 목록을 확인하지 못했습니다.')
        for field in roots.split('\0'):
            if field.startswith('worktree '):
                protected.append(Path(field[9:]).resolve())
        branch = git(repo, 'symbolic-ref', '--short', 'HEAD') or ('detached-' + (git(repo, 'rev-parse', '--short', 'HEAD') or 'unborn'))
        commit = git(repo, 'rev-parse', 'HEAD')
    else:
        canonical, anchor, protected, branch, commit = repo, 'path:' + str(repo), [repo], 'no-git', None
    project_id = hashlib.sha256(anchor.encode()).hexdigest()[:24]
    branch_id = hashlib.sha256(branch.encode()).hexdigest()[:16]
    return {'project_id': project_id, 'branch_id': branch_id, 'branch': branch,
            'repository': str(canonical), 'head': commit}, protected


def data_home():
    explicit = os.environ.get('JSTACK_DATA_HOME')
    xdg = os.environ.get('XDG_DATA_HOME')
    if explicit:
        candidate = Path(explicit).expanduser()
    elif xdg:
        candidate = Path(xdg).expanduser() / 'jstack'
    elif sys.platform == 'win32':
        local = os.environ.get('LOCALAPPDATA')
        if not local:
            raise ValueError('LOCALAPPDATA 또는 JSTACK_DATA_HOME을 지정하세요.')
        candidate = Path(local) / 'jstack'
    else:
        candidate = Path.home() / '.local/share/jstack'
    if not candidate.is_absolute():
        raise ValueError('개인 상태 경로는 절대 경로여야 합니다.')
    if '..' in candidate.parts:
        raise ValueError('개인 상태 경로에 상위 경로 이동을 사용할 수 없습니다.')
    if candidate.is_symlink():
        raise ValueError('개인 상태 root는 symlink일 수 없습니다.')
    return candidate.resolve()


def within(path, parent):
    return path == parent or parent in path.parents


def scope(repo):
    info, protected = identity(repo)
    root = data_home()
    for p in protected:
        if within(root, p) or within(p, root):
            raise ValueError('개인 상태 root와 프로젝트/worktree/Git 경로는 겹칠 수 없습니다.')
    if git(root if root.exists() else next(p for p in root.parents if p.exists()), 'rev-parse', '--show-toplevel'):
        raise ValueError('개인 상태를 다른 Git 저장소 안에 둘 수 없습니다.')
    check_tree(root, root)
    project = root / 'projects' / info['project_id']
    return info, root, project


def check_tree(root, target):
    if not within(target, root):
        raise ValueError('개인 상태 경로를 벗어났습니다.')
    parts = [root]
    if target != root:
        relative = target.relative_to(root)
        parts.extend(root.joinpath(*relative.parts[:i]) for i in range(1, len(relative.parts) + 1))
    for p in parts:
        if p.is_symlink():
            raise ValueError('개인 상태 내부 symlink는 허용하지 않습니다.')
        if p.exists():
            st = p.stat()
            if hasattr(os, 'getuid') and st.st_uid != os.getuid():
                raise ValueError('다른 사용자가 소유한 상태 경로입니다.')
            if stat.S_ISDIR(st.st_mode) and os.name != 'nt' and st.st_mode & 0o077:
                raise ValueError('개인 상태 디렉터리 권한은 0700이어야 합니다.')


def slug(value):
    if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9._-]{0,95}', value) or '..' in value:
        raise ValueError('이름은 영문·숫자·점·밑줄·하이픈 1~96자로 지정하세요.')
    return value


def private_mkdir(root, directory):
    check_tree(root, directory)
    missing = []
    current = directory
    while not current.exists():
        missing.append(current)
        current = current.parent
    for p in reversed(missing):
        try:
            p.mkdir(mode=0o700)
        except FileExistsError:
            pass
    check_tree(root, directory)


@contextlib.contextmanager
def lock(root, directory):
    private_mkdir(root, directory)
    path = directory / '.writer.lock'
    deadline = time.monotonic() + 8
    fd = None
    while fd is None:
        check_tree(root, path)
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0), 0o600)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise ValueError('상태 writer가 사용 중입니다. 잠금 소유자를 확인한 뒤 재시도하세요.')
            time.sleep(0.025)
    try:
        os.write(fd, str(os.getpid()).encode())
        yield
    finally:
        os.close(fd)
        path.unlink()


def atomic(root, path, content):
    private_mkdir(root, path.parent)
    check_tree(root, path)
    fd, temporary = tempfile.mkstemp(prefix='.jstack-', dir=path.parent)
    try:
        if hasattr(os, "fchmod"):
            os.fchmod(fd, 0o600)
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        check_tree(root, path)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def now():
    return datetime.now(timezone.utc).isoformat()


def encode(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def artifact(project, args):
    if args.kind == 'program':
        return project / 'branches' / args.branch_id / 'program' / slug(args.name)
    if args.run:
        return project / 'branches' / args.branch_id / 'runs' / slug(args.run) / args.kind / slug(args.name)
    return project / args.kind / slug(args.name)


def main(argv=None):
    parser = argparse.ArgumentParser(description='팀 저장소 밖의 개인 jstack 상태 도구')
    parser.add_argument('--repo', required=True, help='읽을 대상 프로젝트 경로')
    parser.add_argument('--dry-run', action='store_true', help='파일 생성 없이 작업 계획만 출력')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('context', help='프로젝트 식별자와 개인 경로 확인')
    commands.add_parser('init', help='개인 상태 초기화')
    for command in ['path', 'read', 'write']:
        p = commands.add_parser(command, help={'path':'산출물 경로 확인', 'read':'산출물 읽기', 'write':'표준 입력을 개인 산출물로 저장'}[command])
        p.add_argument('--kind', choices=KINDS, required=True)
        p.add_argument('--name', required=True)
        p.add_argument('--run')
        if command == 'write':
            p.add_argument('--file', help='UTF-8 입력 파일. 생략하면 표준 입력을 읽음')
            p.add_argument('--replace', action='store_true', help='기존 파일 갱신을 명시적으로 허용')
    p = commands.add_parser('log', help='판단과 근거 기록 추가')
    p.add_argument('--run', required=True)
    p.add_argument('--phase', required=True)
    p.add_argument('--decision', required=True)
    p.add_argument('--why', required=True)
    p.add_argument('--evidence', required=True)
    p.add_argument('--result', required=True)
    p = commands.add_parser('unit', help='프로그램 작업 큐 항목 기록')
    p.add_argument('--program', required=True)
    p.add_argument('--id', required=True)
    p.add_argument('--state', choices=STATES, required=True)
    p.add_argument('--head')
    p.add_argument('--owner', required=True)
    p.add_argument('--evidence', required=True)
    p.add_argument('--depends-on', action='append', default=[])
    p = commands.add_parser('status', help='프로그램 작업 큐와 현재 SHA 검증 상태 확인')
    p.add_argument('--program', required=True)
    args = parser.parse_args(argv)
    info, root, project = scope(args.repo)
    args.branch_id = info['branch_id']
    response = dict(info, data_home=str(root), project_home=str(project), dry_run=args.dry_run)
    if args.command == 'context':
        print(encode(response), end='')
        return
    if args.command == 'init':
        target = project / 'project.json'
        if not args.dry_run:
            with lock(root, project):
                check_tree(root, target)
                if not target.exists():
                    atomic(root, target, encode(dict(info, created=now())))
    elif args.command in ['path', 'read', 'write']:
        target = artifact(project, args)
        check_tree(root, target)
        if args.command == 'read':
            if args.dry_run:
                response['action'] = 'read'
            else:
                print(target.read_text(encoding='utf-8'), end='')
                return
        elif args.command == 'write' and not args.dry_run:
            content = Path(args.file).read_text(encoding='utf-8') if args.file else sys.stdin.read()
            if not content.strip():
                raise ValueError("빈 기록은 저장하지 않습니다. 입력 생성 명령이 성공했는지 확인하세요.")
            with lock(root, project):
                check_tree(root, target)
                if target.exists() and not args.replace:
                    raise ValueError('기존 산출물이 있습니다. 갱신은 --replace로 명시하세요.')
                atomic(root, target, content)
                saved = target.read_bytes()
                if saved != content.encode("utf-8"):
                    raise ValueError("저장한 본문이 입력과 다릅니다.")
                response["bytes"] = len(saved)
                response["sha256"] = hashlib.sha256(saved).hexdigest()
    elif args.command == 'log':
        target = project / 'branches' / info['branch_id'] / 'runs' / slug(args.run) / 'decisions.jsonl'
        if not args.dry_run:
            record = {'time':now(), **{k:getattr(args,k) for k in ['phase','decision','why','evidence','result']}}
            with lock(root, project):
                check_tree(root, target)
                prior = target.read_text(encoding='utf-8') if target.exists() else ''
                atomic(root, target, prior + json.dumps(record, ensure_ascii=False) + '\n')
    else:
        target = project / 'branches' / info['branch_id'] / 'program' / slug(args.program) / 'units.json'
        check_tree(root, target)
        if args.command == 'unit' and not args.dry_run:
            if args.state in ['verified','done'] and (not args.head or not re.fullmatch(r'[a-f0-9]{40}|[a-f0-9]{64}',args.head)):
                raise ValueError('검증 완료 항목에는 정확한 전체 head SHA가 필요합니다.')
            with lock(root, project):
                check_tree(root, target)
                units = json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
                uid = slug(args.id)
                units[uid] = {'state':args.state, 'head':args.head, 'owner':args.owner,
                              'evidence':args.evidence, 'depends_on':[slug(x) for x in args.depends_on], 'updated':now()}
                atomic(root, target, encode(units))
        elif args.command == 'status' and not args.dry_run:
            units = json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
            response['units'] = units
            response['counts'] = {s:sum(u['state']==s for u in units.values()) for s in STATES}
            response['different_from_checkout'] = [uid for uid,u in units.items() if u['state'] in ['verified','done'] and u['head'] != info['head']]
    response['target'] = str(target)
    response['command'] = args.command
    print(encode(response), end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print('jstack 오류: ' + str(error), file=sys.stderr)
        sys.exit(2)
