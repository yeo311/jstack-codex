# 독립 작업 큐 진행

1. 서로 독립적인 제품 작업과 각 owner·branch·완료 조건·사용자가 허용한 외부 행동을 정한다. merge 권한이 없으면 merge-ready 전달로 끝낸다.
2. owner마다 조사·구현·초안 PR·self-proof·CI·review를 맡길 수 있다. 첫 검증 단위가 끝나면 승인된 branch push를 수행하고 개인 decisions/children 상태를 기록한다.
3. 독립 owners는 같은 Codex 모델을 상속해 병렬 진행한다. file overlap·같은 browser/data·의존성이 있는 부분만 순서를 정한다.
4. code-ready head마다 독립 reviewer와 실제 사용자 경로로 verdict를 만든다. 부모가 결과를 확인하고 결함을 묶어 전달한다. 새 patch는 새 검증 범위를 정한다.
5. 실제 current trunk·mergeability·현재 head CI를 확인하고 사용자가 허용한 owner만 merge한다. root의 내부 verdict 자체는 권한이 아니다.
6. 정기 tick은 user schedule 요청과 가용 도구가 있을 때만 설정한다. 현재 실행에서는 child 상태와 실제 side effect를 관찰해 stalled 일을 정리하고 explicit stop은 즉시 모든 writer에 전달한다.
7. 각 unit의 owner·PR·head·verified evidence·merged 여부·남은 gate를 보고한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
