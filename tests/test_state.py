import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/jstack-mode/scripts/jstack.py'


class StateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.repo = self.base / 'team-project'
        self.repo.mkdir()
        self.git('init', '-b', 'main')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('config', 'user.name', 'Fixture')
        (self.repo / 'package.json').write_text('{"private":true,"scripts":{"test":"existing"}}\n')
        (self.repo / 'app').mkdir()
        (self.repo / 'app/page.tsx').write_text('export default function Page() { return <main>fixture</main> }\n')
        self.git('add', '.')
        self.git('commit', '-m', 'fixture')
        self.data = self.base / 'personal-state'
        self.env = dict(os.environ, JSTACK_DATA_HOME=str(self.data))
        self.before = self.snapshot()

    def tearDown(self):
        self.assertEqual(self.snapshot(), self.before)
        self.assertEqual(self.git('status', '--porcelain'), '')
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git','-C',str(self.repo),*args],text=True,stderr=subprocess.DEVNULL).strip()

    def snapshot(self):
        return {str(p.relative_to(self.repo)):hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.repo.rglob('*') if p.is_file() and '.git' not in p.relative_to(self.repo).parts}

    def invoke(self,*args,repo=None,env=None,content='',ok=True):
        result = subprocess.run([sys.executable,str(SCRIPT),'--repo',str(repo or self.repo),*args],
                                env=env or self.env,input=content,text=True,capture_output=True)
        if ok:
            self.assertEqual(result.returncode,0,result.stderr)
            return json.loads(result.stdout) if result.stdout.startswith('{') else result.stdout
        self.assertNotEqual(result.returncode,0,result.stdout)
        return result

    def test_dry_run_has_zero_files(self):
        for args in [('init',),('write','--kind','features','--name','search.md'),
                     ('log','--run','r1','--phase','start','--decision','검사','--why','확인','--evidence','fixture','--result','계획'),
                     ('unit','--program','p1','--id','u1','--state','running','--owner','a','--evidence','fixture')]:
            self.invoke('--dry-run',*args)
        self.assertFalse(self.data.exists())

    def test_idempotent_init_and_preserved_artifact(self):
        first = self.invoke('init')
        target = Path(first['target'])
        original = target.read_bytes()
        self.invoke('init')
        self.assertEqual(target.read_bytes(),original)
        written=self.invoke('write','--kind','understanding','--name','overview.md',content='프로젝트 이해\n')
        self.assertEqual(Path(written['target']).read_text(),'프로젝트 이해\n')
        self.invoke('write','--kind','understanding','--name','overview.md',content='덮어쓰기',ok=False)
        self.assertEqual(Path(written['target']).stat().st_mode & 0o777,0o600)
        self.assertEqual(self.data.stat().st_mode & 0o777,0o700)

    def test_failed_input_producer_cannot_create_or_erase_artifact(self):
        for content in ['', ' \n\t']:
            self.invoke('write','--kind','plans','--name','plan.md','--run','r1',content=content,ok=False)
            self.assertFalse(self.data.exists())
        written=self.invoke('write','--kind','plans','--name','plan.md','--run','r1',content='열린 결정: 인증 제공자\n')
        self.invoke('write','--kind','plans','--name','plan.md','--run','r1','--replace',content='',ok=False)
        self.assertEqual(Path(written['target']).read_text(),'열린 결정: 인증 제공자\n')

    def test_file_input_preserves_literal_text_and_verifies_saved_bytes(self):
        source=self.base/'draft.md'
        content='설계 초안: `Server` / $literal / $(literal)\n열린 질문: 인증 선택?\n'
        source.write_text(content)
        written=self.invoke('write','--kind','plans','--name','draft.md','--run','r1','--file',str(source))
        self.assertEqual(Path(written['target']).read_text(),content)
        self.assertEqual(written['bytes'],len(content.encode('utf-8')))
        self.assertEqual(written['sha256'],hashlib.sha256(content.encode('utf-8')).hexdigest())
        self.invoke('write','--kind','plans','--name','missing.md','--file',str(self.base/'missing'),ok=False)
        source.write_text(' \n')
        self.invoke('write','--kind','plans','--name','draft.md','--run','r1','--replace','--file',str(source),ok=False)
        self.assertEqual(Path(written['target']).read_text(),content)

    def test_repo_roots_and_git_indirection(self):
        worktree = self.base / 'feature-copy'
        self.git('worktree','add','-b','feature/search',str(worktree))
        original=self.invoke('context')
        other=self.invoke('context',repo=worktree)
        self.assertEqual(original['project_id'],other['project_id'])
        self.assertNotEqual(original['branch_id'],other['branch_id'])
        self.assertNotIn('/',other['branch_id'])
        for root in [self.repo/'metadata',worktree/'metadata',self.repo/'.git/metadata',self.base]:
            self.invoke('init',env=dict(self.env,JSTACK_DATA_HOME=str(root)),ok=False)
        self.assertFalse((self.repo/'metadata').exists())
        self.assertFalse((worktree/'metadata').exists())

    def test_relative_xdg_and_home_default(self):
        self.invoke('init',env=dict(self.env,JSTACK_DATA_HOME='relative'),ok=False)
        env=dict(self.env); env.pop('JSTACK_DATA_HOME'); env['XDG_DATA_HOME']=str(self.base/'xdg')
        value=self.invoke('context',env=env)
        self.assertEqual(value['data_home'],str((self.base/'xdg/jstack').resolve()))
        env['XDG_DATA_HOME']='relative'; self.invoke('init',env=env,ok=False)
        env.pop('XDG_DATA_HOME'); value=self.invoke('context',env=env)
        self.assertTrue(value['data_home'].endswith('/.local/share/jstack'))

    def test_symlink_and_traversal(self):
        ctx=self.invoke('init')
        project=Path(ctx['project_home'])
        (project/'features').symlink_to(self.repo,target_is_directory=True)
        self.invoke('write','--kind','features','--name','package.json',content='bad',ok=False)
        self.invoke('path','--kind','plans','--name','../escape.md',ok=False)
        link=self.base/'state-link'; link.symlink_to(self.data,target_is_directory=True)
        self.invoke('init',env=dict(self.env,JSTACK_DATA_HOME=str(link)),ok=False)
        self.invoke('write','--kind','plans','--name','run.md','--run','../bad',ok=False)

    def test_no_bulk_source_copy(self):
        value=self.invoke('init')
        self.assertEqual(sorted(p.name for p in Path(value['project_home']).iterdir()),['project.json'])
        self.assertNotIn('fixture</main>',Path(value['target']).read_text())

    def test_concurrent_logs_and_queue_updates_are_not_lost(self):
        def log(index):
            return self.invoke('log','--run','r1','--phase','unit','--decision',str(index),
                               '--why','검사','--evidence','fixture','--result','완료')
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            rows=list(pool.map(log,range(24)))
        records=[json.loads(line) for line in Path(rows[0]['target']).read_text().splitlines()]
        self.assertEqual({r['decision'] for r in records},{str(i) for i in range(24)})
        def unit(index):
            return self.invoke('unit','--program','p1','--id',f'u{index}','--state','running',
                               '--owner',f'agent-{index}','--evidence','fixture')
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(unit,range(24)))
        status=self.invoke('status','--program','p1')
        self.assertEqual(len(status['units']),24)
        self.assertEqual(status['counts']['running'],24)

    def test_exact_sha_required_for_verified(self):
        args=('unit','--program','p1','--id','u1','--state','verified','--owner','agent','--evidence','fixture')
        self.invoke(*args,ok=False)
        self.invoke(*args,'--head','abc',ok=False)
        self.invoke(*args,'--head',self.git('rev-parse','HEAD'))
        self.assertEqual(self.invoke('status','--program','p1')['counts']['verified'],1)

    def test_non_git_folder_identity_and_data_in_other_git_refused(self):
        folder=self.base/'no-git'; folder.mkdir()
        self.assertEqual(self.invoke('context',repo=folder)['branch'],'no-git')
        self.invoke('init',repo=folder,env=dict(self.env,JSTACK_DATA_HOME=str(self.repo/'other-state')),ok=False)


if __name__ == '__main__':
    unittest.main()
