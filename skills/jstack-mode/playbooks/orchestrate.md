# 프로그램 운영

1. 한 세션 단일 작업을 넘어서는 program인지 확인하고 전체 predicate·unit 수·의존성·budget·standing scope·권한 gate를 개인 plan에 정의한다.
2. 개인 program 영역에 brief·overview·ledger·frontier·gate 근거를 둔다. helper unit/status가 원자적 JSON queue를 관리한다. 현재 세션에서 제공되는 Codex 내부 분업 도구로 작업을 맡기고, branch·PR 상태는 git/gh에서 읽어 개인 큐와 대조한다.
3. brief는 goal/scope/금지 경로/context/acceptance/verify/timebox/report/standing orders를 구체화한다. 한 writer per file/branch/worktree, 한 browser driver를 지정한다.
4. 첫 unit을 pilot로 investigate→implement→live proof→review까지 끝내 contract를 확인한다. pilot 결과·작업 독립성·도구 가용성·budget에 맞춰 이후 동시 작업 수를 정한다.
5. rolling window로 독립 owners를 시작하고 completion을 queue event로 기록한다. dependency 결과를 다음 brief에 전달하고 모든 child를 terminal state로 정리한다. 가용 도구가 제한되면 순차로 같은 queue를 진행한다.
6. drain 때 unit state·head·owner·evidence를 갱신하고 ledger/frontier와 실제 gh 상태를 대조한다. 잠깐의 완료 통지가 현재 critical section을 불필요하게 중단시키지 않는다.
7. landing은 명시 권한과 현재 SHA verdict가 있는 unit만 수행한다. 검증 안 된 아래 unit을 건너 stack을 합치지 않는다. root는 code/merge 소유를 실제 scope에 맞춰 분리한다.
8. 최종 queue·미완료 child·정확 SHA proof·gates를 reconcile하고 기록을 보존한다. scheduler/메시지/자동 merge는 program을 시작했다는 이유만으로 만들지 않는다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
