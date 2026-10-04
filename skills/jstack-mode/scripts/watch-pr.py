#!/usr/bin/env python3
"""GitHub PR을 읽기 점검하며 merge·comment·push하지 않는다."""
import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone


def classify(pr, threads, queued=False):
    if not isinstance(pr,dict): return {'verdict':'INCONCLUSIVE','reason':'PR 응답 형식 오류'}
    required=('state','isDraft','headRefOid','mergeable','mergeStateStatus','statusCheckRollup','reviewDecision')
    if any(key not in pr for key in required):
        return {'verdict':'INCONCLUSIVE','reason':'PR 응답의 필수 필드 누락'}
    allowed={'state':('OPEN','CLOSED','MERGED'),'mergeable':('MERGEABLE','CONFLICTING','UNKNOWN'),
             'mergeStateStatus':('CLEAN','UNKNOWN','BEHIND','BLOCKED','UNSTABLE','DIRTY','DRAFT','HAS_HOOKS'),
             'reviewDecision':('','APPROVED','REVIEW_REQUIRED','CHANGES_REQUESTED')}
    if any(pr[key] not in values for key,values in allowed.items()):
        return {'verdict':'INCONCLUSIVE','reason':'알 수 없는 forge enum'}
    if not isinstance(pr['isDraft'],bool) or not re.fullmatch(r'[a-f0-9]{40}|[a-f0-9]{64}',str(pr['headRefOid'])):
        return {'verdict':'INCONCLUSIVE','reason':'잘못된 draft 형식 또는 head SHA'}
    if not isinstance(threads,list) or any(not isinstance(t,dict) or not isinstance(t.get('isResolved'),bool)
                                          or not isinstance(t.get('isOutdated'),bool) for t in threads):
        return {'verdict':'INCONCLUSIVE','reason':'review thread 형식 오류'}
    base={'head':pr['headRefOid'],'number':pr.get('number'),'url':pr.get('url')}
    if pr['state']=='MERGED': return dict(base,verdict='COMPLETE',reason='이미 merge됨')
    if pr['state']=='CLOSED': return dict(base,verdict='BLOCKED',reason='merge 없이 닫힘')
    if pr['isDraft']: return dict(base,verdict='BLOCKED',reason='초안 PR의 사용자 검토 gate')
    if pr['mergeable']=='CONFLICTING': return dict(base,verdict='BLOCKED',reason='충돌')
    if pr['reviewDecision']=='CHANGES_REQUESTED': return dict(base,verdict='BLOCKED',reason='변경 요청 review')
    if any(not t.get('isResolved',False) and not t.get('isOutdated',False) for t in threads):
        return dict(base,verdict='BLOCKED',reason='미해결 review thread')
    checks=pr['statusCheckRollup']
    if not isinstance(checks,list) or any(not isinstance(c,dict) for c in checks): return dict(base,verdict='INCONCLUSIVE',reason='check 목록 형식 오류')
    failed=[]; pending=[]
    for check in checks:
        if any(check.get(key) is not None and not isinstance(check.get(key),str) for key in ['conclusion','state','status']):
            return dict(base,verdict='INCONCLUSIVE',reason='check field 형식 오류')
        conclusion=(check.get('conclusion') or check.get('state') or '').upper()
        status=(check.get('status') or '').upper()
        name=check.get('name') or check.get('context') or 'check'
        if conclusion in ('FAILURE','ERROR','CANCELLED','TIMED_OUT','ACTION_REQUIRED','STARTUP_FAILURE','STALE'):
            failed.append(name)
        elif conclusion not in ('SUCCESS','NEUTRAL','SKIPPED') or status in ('QUEUED','IN_PROGRESS','PENDING'):
            pending.append(name)
    if failed: return dict(base,verdict='BLOCKED',reason='실패한 check',checks=failed)
    if pending: return dict(base,verdict='WAITING',reason='진행 중인 check',checks=pending)
    if pr['reviewDecision']=='REVIEW_REQUIRED': return dict(base,verdict='WAITING',reason='owner review 대기')
    if pr['mergeable']=='UNKNOWN' or pr['mergeStateStatus'] in ('UNKNOWN','BEHIND','BLOCKED','UNSTABLE','DIRTY','DRAFT','HAS_HOOKS'):
        return dict(base,verdict='WAITING',reason='forge merge 조건 대기',merge_state=pr['mergeStateStatus'])
    if pr['mergeStateStatus'] not in ('CLEAN',):
        return dict(base,verdict='INCONCLUSIVE',reason='알 수 없는 forge merge 상태',merge_state=pr['mergeStateStatus'])
    return dict(base,verdict='WAITING' if queued else 'READY',reason='merge-queue' if queued else '현재 head의 check·review·mergeability 확인',checks_observed=len(checks))


def gh(*args):
    result=subprocess.run(['gh',*args],text=True,capture_output=True,timeout=45,check=False)
    if result.returncode: raise ValueError('gh 읽기 요청 실패. 연결·repo 접근 권한을 확인하세요.')
    return json.loads(result.stdout)


def read_pr(url):
    match=re.fullmatch(r'https://github\.com/([^/]+)/([^/]+)/pull/(\d+)',url)
    if not match: raise ValueError('정확한 github.com PR URL을 지정하세요.')
    owner,repo,number=match.groups()
    pr=gh('pr','view',url,'--json','number,url,state,isDraft,headRefOid,baseRefOid,mergeable,mergeStateStatus,statusCheckRollup,reviewDecision')
    threads=[]; cursor=None
    query='query($owner:String!,$repo:String!,$number:Int!,$after:String){repository(owner:$owner,name:$repo){pullRequest(number:$number){headRefOid reviewThreads(first:100,after:$after){nodes{isResolved isOutdated}pageInfo{hasNextPage endCursor}}}}}'
    while True:
        args=['api','graphql','-f','query='+query,'-f','owner='+owner,'-f','repo='+repo,'-F','number='+number]
        if cursor: args+=['-f','after='+cursor]
        response=gh(*args)
        if response.get('errors'): raise ValueError('review thread 조회를 확인하지 못했습니다.')
        record=response['data']['repository']['pullRequest']
        if record['headRefOid'] != pr['headRefOid']: raise ValueError('조회 중 PR head 변경. 새 SHA에서 재시도하세요.')
        page=record['reviewThreads']
        threads+=page['nodes']
        if not page['pageInfo']['hasNextPage']: break
        cursor=page['pageInfo']['endCursor']
        if not cursor: raise ValueError('review thread pagination을 확인하지 못했습니다.')
    return pr,threads


def main():
    p=argparse.ArgumentParser(description='읽기 전용 PR 상태 확인. merge 권한을 부여하지 않습니다.')
    p.add_argument('urls',nargs='+')
    p.add_argument('--mode',choices=['check','drive'],default='check')
    p.add_argument('--queued',action='store_true')
    p.add_argument('--interval',type=int,default=30)
    p.add_argument('--timeout',type=int,default=600)
    args=p.parse_args()
    if args.interval<5 or args.interval>60 or args.timeout<0: raise ValueError('interval은 5~60초, timeout은 0 이상이어야 합니다.')
    start=time.monotonic(); previous=None
    while True:
        frontier=None; all_done=True
        for url in args.urls:
            pr,threads=read_pr(url)
            result=classify(pr,threads,args.queued)
            if result['verdict']!='COMPLETE':
                frontier=result; all_done=False; break
        result={'verdict':'COMPLETE','reason':'모든 PR merge 확인'} if all_done else frontier
        if previous and previous!=result.get('number') and not all_done:
            print(json.dumps(dict(result,event='ADVANCE',time=datetime.now(timezone.utc).isoformat()),ensure_ascii=False),flush=True)
        previous=result.get('number')
        print(json.dumps(dict(result,time=datetime.now(timezone.utc).isoformat()),ensure_ascii=False),flush=True)
        if args.mode=='check' or result['verdict'] in ('READY','COMPLETE','BLOCKED','INCONCLUSIVE') or result['reason']=='merge-queue': return
        if time.monotonic()-start>=args.timeout:
            print(json.dumps({'verdict':'WAITING','reason':'관찰 시간 한도. 개인 기록에서 재개하세요.'},ensure_ascii=False),flush=True); return
        time.sleep(min(args.interval,max(0,args.timeout-(time.monotonic()-start))))


if __name__=='__main__':
    try: main()
    except (ValueError,KeyError,OSError,subprocess.TimeoutExpired) as error:
        print(json.dumps({'verdict':'INCONCLUSIVE','reason':str(error)},ensure_ascii=False)); sys.exit(2)
