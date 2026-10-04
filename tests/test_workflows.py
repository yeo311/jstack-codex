import copy
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'skills/jstack-mode/scripts'/f'{name}.py')
    value=importlib.util.module_from_spec(spec); spec.loader.exec_module(value); return value

PLAN=module('check-plan'); WATCH=module('watch-pr')


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.plan={'goal':'검색','done_when':'검색한 결과와 오류 상태를 관찰','units':[{'id':'search','outcome':'검색 결과',
                   'files':['app/page.tsx'],'verify':['기존 test'],'live':'실제 검색 조작','depends_on':[]}]}

    def test_positive_and_evidence_free_complete_rejected(self):
        self.assertEqual(PLAN.validate(self.plan),[])
        self.plan['units'][0]['status']='done'
        self.assertTrue(any('evidence.live' in e for e in PLAN.validate(self.plan)))

    def test_measured_perf_is_conditional(self):
        self.plan['units'][0]['performance_relevant']=True
        self.assertTrue(any('perf.baseline' in e for e in PLAN.validate(self.plan)))
        self.plan['units'][0]['perf']={'metric':'LCP','probe':'기존 browser trace','baseline':'3회 2000ms','rule':'같은 조건 10% 개선'}
        self.assertEqual(PLAN.validate(self.plan),[])

    def test_missing_and_cyclic_dependencies_rejected(self):
        self.plan['units'][0]['depends_on']=['search']
        self.assertTrue(any('순환' in e for e in PLAN.validate(self.plan)))
        self.plan['units'][0]['depends_on']=['missing']
        self.assertTrue(any('없는' in e for e in PLAN.validate(self.plan)))

    def test_fake_head_and_missing_live_recipe_rejected(self):
        unit=self.plan['units'][0];unit['status']='verified';unit['evidence']={'head':'abc','unit':'test.out','live':'screenshot.png'}
        self.assertTrue(any('전체 SHA' in e for e in PLAN.validate(self.plan)))
        unit['evidence']['head']='a'*40;unit.pop('live')
        self.assertTrue(any('live가 필요' in e for e in PLAN.validate(self.plan)))


    def test_boolean_recipes_and_evidence_refused(self):
        unit=self.plan['units'][0]
        for field in ('outcome','files','verify','live'):
            unit[field]=True
        self.assertGreaterEqual(len(PLAN.validate(self.plan)),4)
        unit.update(outcome='결과',files=['app/page.tsx'],verify=['test'],live='조작',status='done',
                    evidence={'head':'a'*40,'unit':True,'live':True})
        self.assertTrue(any('evidence.live' in e for e in PLAN.validate(self.plan)))


class WatchTests(unittest.TestCase):
    def setUp(self):
        self.pr={'state':'OPEN','isDraft':False,'headRefOid':'a'*40,'number':1,'url':'https://github.com/example/fixture/pull/1',
                 'mergeable':'MERGEABLE','mergeStateStatus':'CLEAN','reviewDecision':'APPROVED',
                 'statusCheckRollup':[{'name':'CI','status':'COMPLETED','conclusion':'SUCCESS'}]}

    def verdict(self,threads=None,queued=False): return WATCH.classify(self.pr,threads or [],queued)

    def test_ready_and_queued_stop(self):
        self.assertEqual(self.verdict()['verdict'],'READY')
        self.assertEqual(self.verdict(queued=True)['reason'],'merge-queue')

    def test_merged_and_closed(self):
        self.pr['state']='MERGED';self.assertEqual(self.verdict()['verdict'],'COMPLETE')
        self.pr['state']='CLOSED';self.assertEqual(self.verdict()['verdict'],'BLOCKED')

    def test_draft_conflict_and_review_blockers(self):
        for field,value in [('isDraft',True),('mergeable','CONFLICTING'),('reviewDecision','CHANGES_REQUESTED')]:
            with self.subTest(field=field):
                pr=copy.deepcopy(self.pr);pr[field]=value
                self.assertEqual(WATCH.classify(pr,[])['verdict'],'BLOCKED')
        self.assertEqual(self.verdict([{'isResolved':False,'isOutdated':False}])['verdict'],'BLOCKED')
        self.assertEqual(self.verdict([{'isResolved':True,'isOutdated':False}])['verdict'],'READY')

    def test_pending_failure_and_unknown_fail_closed(self):
        for check,expected in [({'status':'IN_PROGRESS','conclusion':''},'WAITING'),({'conclusion':'FAILURE'},'BLOCKED'),
                               ({'state':'PENDING'},'WAITING'),({'conclusion':'FUTURE_STATE'},'WAITING')]:
            self.pr['statusCheckRollup']=[check];self.assertEqual(self.verdict()['verdict'],expected)
        self.pr['statusCheckRollup']=[];self.pr['mergeStateStatus']='FUTURE_STATE'
        self.assertEqual(self.verdict()['verdict'],'INCONCLUSIVE')

    def test_unknown_or_missing_forge_state_not_ready(self):
        self.pr['mergeable']='UNKNOWN';self.assertEqual(self.verdict()['verdict'],'WAITING')
        self.pr.pop('headRefOid');self.assertEqual(self.verdict()['verdict'],'INCONCLUSIVE')


    def test_malformed_responses_refused(self):
        for field in ['state','mergeable','reviewDecision']:
            pr=copy.deepcopy(self.pr);pr[field]='FUTURE_STATE'
            self.assertEqual(WATCH.classify(pr,[])['verdict'],'INCONCLUSIVE')
        for field,value in [('headRefOid','fake'),('isDraft','false'),('statusCheckRollup',[None]),('statusCheckRollup',[{'conclusion':True}])]:
            pr=copy.deepcopy(self.pr);pr[field]=value
            self.assertEqual(WATCH.classify(pr,[])['verdict'],'INCONCLUSIVE')
        self.assertEqual(WATCH.classify(self.pr,[None])['verdict'],'INCONCLUSIVE')


if __name__=='__main__': unittest.main()
