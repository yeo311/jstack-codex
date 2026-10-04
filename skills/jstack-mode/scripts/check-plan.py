#!/usr/bin/env python3
"""개인 JSON 계획에서 검증 가능한 단위와 증거를 검사한다."""
import argparse
import json
import re
from pathlib import Path
import sys


def text(value):
    return isinstance(value,str) and bool(value.strip())


def texts(value):
    return isinstance(value,list) and bool(value) and all(text(x) for x in value)


def validate(plan):
    errors=[]
    if not isinstance(plan,dict):
        return ['계획은 JSON object여야 합니다.']
    for key in ('goal','done_when'):
        if not isinstance(plan.get(key),str) or not plan[key].strip():
            errors.append(f'{key}가 필요합니다.')
    units=plan.get('units')
    if not isinstance(units,list) or not units:
        return errors+['units는 비어 있지 않은 목록이어야 합니다.']
    ids=set()
    graph={}
    for i,unit in enumerate(units):
        if not isinstance(unit,dict):
            errors.append(f'unit {i}는 object여야 합니다.'); continue
        uid=unit.get('id')
        if not isinstance(uid,str) or not uid or uid in ids:
            errors.append(f'unit {i} 식별자가 없거나 중복입니다.'); continue
        ids.add(uid)
        for field in ('outcome','live'):
            if not text(unit.get(field)): errors.append(f'{uid}: 문자열 {field}가 필요합니다.')
        for field in ('files','verify'):
            if not texts(unit.get(field)): errors.append(f'{uid}: 문자열 목록 {field}가 필요합니다.')
        deps=unit.get('depends_on',[])
        if not isinstance(deps,list) or not all(isinstance(x,str) for x in deps):
            errors.append(f'{uid}: depends_on은 문자열 목록이어야 합니다.'); deps=[]
        graph[uid]=deps
        if 'performance_relevant' in unit and not isinstance(unit['performance_relevant'],bool):
            errors.append(f'{uid}: performance_relevant는 boolean이어야 합니다.')
        if unit.get('status','pending') not in ('pending','running','needs-verification','verified','blocked','done','abandoned'):
            errors.append(f'{uid}: 알 수 없는 상태입니다.')
        if unit.get('performance_relevant'):
            perf=unit.get('perf',{})
            for field in ('metric','probe','baseline','rule'):
                if not isinstance(perf,dict) or not text(perf.get(field)): errors.append(f'{uid}: perf.{field}가 필요합니다.')
        if unit.get('status') in ('verified','done'):
            evidence=unit.get('evidence',{})
            for field in ('head','unit','live'):
                if not isinstance(evidence,dict) or not text(evidence.get(field)): errors.append(f'{uid}: 완료에 evidence.{field}가 필요합니다.')
            if isinstance(evidence,dict) and not re.fullmatch(r'[a-f0-9]{40}|[a-f0-9]{64}',str(evidence.get('head',''))):
                errors.append(f'{uid}: evidence.head는 전체 SHA여야 합니다.')
    visited=set(); active=set()
    def visit(uid):
        if uid in active: errors.append(f'{uid}: 의존성이 순환합니다.'); return
        if uid in visited: return
        active.add(uid)
        for dep in graph[uid]:
            if dep not in graph: errors.append(f'{uid}: 없는 의존 단위 {dep}')
            else: visit(dep)
        active.remove(uid); visited.add(uid)
    for uid in graph: visit(uid)
    return errors


def main():
    p=argparse.ArgumentParser(description='개인 JSON plan의 검증 구조 검사')
    p.add_argument('plan',type=Path)
    args=p.parse_args()
    errors=validate(json.loads(args.plan.read_text(encoding='utf-8')))
    print(json.dumps({'valid':not errors,'errors':errors},ensure_ascii=False,indent=2))
    return 1 if errors else 0


if __name__=='__main__':
    try: sys.exit(main())
    except (OSError,ValueError) as error:
        print('계획 검사 오류: '+str(error),file=sys.stderr); sys.exit(2)
