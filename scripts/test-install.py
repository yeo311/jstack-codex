#!/usr/bin/env python3
"""공식 Codex isolated home에서 설치·cache·스킬 탐지를 확인한다."""
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory(prefix='jstack-install-') as test_directory:
        test_codex_home=Path(test_directory)/'codex'
        test_codex_home.mkdir(mode=0o700)
        environment=dict(os.environ)
        environment['CODEX_HOME']=str(test_codex_home)
        def run(*args):
            result=subprocess.run(['codex',*args],env=environment,cwd=ROOT,text=True,capture_output=True,timeout=60)
            if result.returncode:
                raise RuntimeError(result.stderr)
            return json.loads(result.stdout)
        added=run('plugin','marketplace','add',str(ROOT),'--json')
        installed=run('plugin','add','jstack-codex@jstack-codex-personal','--json')
        listed=run('plugin','list','--marketplace','jstack-codex-personal','--available','--json')
        assert len(listed['installed'])==1,listed
        item=listed['installed'][0]
        assert item['name']=='jstack-codex' and item['version']=='0.1.0' and item['enabled'] is True,item
        manifests=list(test_codex_home.rglob('plugin.json'))
        package_roots=[p.parent for p in manifests if json.loads(p.read_text()).get('name')=='jstack-codex' and (p.parent/'skills').exists()]
        assert package_roots,'설치 cache 없음'
        cached=package_roots[0]
        skills=sorted(p.parent.name for p in (cached/'skills').glob('*/SKILL.md'))
        assert len(skills)==47 and 'jstack-tdd' in skills and 'tdd' not in skills,skills
        helper=cached/'skills/jstack-mode/scripts/jstack.py'
        private_root=Path(test_directory)/'state'
        environment['JSTACK_DATA_HOME']=str(private_root)
        result=subprocess.run(['python3',str(helper),'--repo',str(ROOT),'--dry-run','init'],env=environment,text=True,capture_output=True,timeout=30)
        assert result.returncode==0,result.stderr
        assert not private_root.exists()
        print(json.dumps({'isolated_install':'통과','enabled':item['enabled'],'version':item['version'],'cached_skills':len(skills),
                          'cached_helper_dry_run':'통과','global_config_modified':False,
                          'scope':'공식 CODEX_HOME을 child process의 임시 사용자 home으로 지정. 인증 복사·전역 설정 변경 없음.'},ensure_ascii=False))


if __name__=='__main__': main()
