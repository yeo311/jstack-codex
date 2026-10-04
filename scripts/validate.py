#!/usr/bin/env python3
"""manifest·스킬 metadata·참고 경로·전체 대응을 정적 검사한다."""
import json
from pathlib import Path
import re
import sys
import yaml
import jsonschema

ROOT=Path(__file__).resolve().parents[1]


def main():
    manifest=json.loads((ROOT/'plugin.json').read_text())
    schema=json.loads((ROOT/'schemas/plugin.schema.json').read_text())
    jsonschema.Draft202012Validator(schema).validate(manifest)
    marketplace=json.loads((ROOT/'.agents/plugins/marketplace.json').read_text())
    assert marketplace['plugins'][0]['source']=={'source':'local','path':'./'}
    assert manifest['name']=='jstack-codex' and marketplace['name']=='jstack-codex-personal'
    skills={}
    for path in sorted((ROOT/'skills').glob('*/SKILL.md')):
        text=path.read_text(encoding='utf-8')
        assert text.startswith('---\n'),path
        _,front,body=text.split('---',2)
        meta=yaml.safe_load(front)
        name=meta['name']; description=meta['description']
        assert re.fullmatch(r'[a-z0-9-]+',name) and name==path.parent.name,path
        assert 0<len(description)<=1024 and re.search('[가-힣]',description),path
        assert body.strip() and re.search('[가-힣]',body),path
        assert not any(k in meta for k in ['disable-model-invocation','paths','mode','reminder']),path
        ui=yaml.safe_load((path.parent/'agents/openai.yaml').read_text())
        assert 25<=len(ui['interface']['short_description'])<=64,path
        assert '$'+manifest['name']+':'+name in ui['interface']['default_prompt'],path
        assert ui['policy']['allow_implicit_invocation'] is False,path
        skills[name]=path
    assert len(skills)==47,len(skills)
    assert not set(['arena','swarm','make-bot-ui','poteto-mode','setup-pstack','tdd']) & skills.keys()
    for path in (ROOT/'skills').rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            if re.match(r'[a-z]+:|#|/',link): continue
            target=(path.parent/link.split('#')[0]).resolve()
            assert ROOT in target.parents and target.exists(),(path,link)
    scenarios=json.loads((ROOT/'tests/eval-scenarios.json').read_text())
    for case in scenarios:
        assert case['skill'] in skills,case
        if 'playbook' in case: assert (ROOT/'skills/jstack-mode/playbooks'/(case['playbook']+'.md')).exists(),case
        assert len(case['checks'])>=3,case
    inventory=json.loads((ROOT/'research/upstream-inventory.json').read_text())
    assert len(inventory['skills'])==50
    expected={ {'poteto-mode':'jstack-mode','setup-pstack':'setup-jstack','tdd':'jstack-tdd'}.get(x['upstream'],x['upstream'])
              for x in inventory['skills'] if x['upstream'] not in ['arena','swarm','make-bot-ui'] }
    assert expected==set(skills)
    assert len(list((ROOT/'skills/jstack-mode/playbooks').glob('*.md')))==23
    assert 'Copyright (c) 2026 Lauren Tan' in (ROOT/'LICENSE').read_text()
    print(json.dumps({'manifest':'통과','skills':len(skills),'playbooks':23,'eval_scenarios':len(scenarios),
                      'scope':'schema·metadata·links·역할 대응의 정적 검사. model 행동·실제 browser QA는 별도.'},ensure_ascii=False))


if __name__=='__main__': main()
