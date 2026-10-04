# PR 상태 점검

1. check/drive/background 중 사용자가 요청한 mode와 PR/stack 목록·정확 SHA를 정한다. 상태 질문은 one-shot check다.
2. git/gh로 head·CI·mergeability·review thread를 읽는다. `scripts/watch-pr.py` check는 읽기 snapshot, drive는 현재 terminal 조건까지 관찰한다. 자동 external writes는 하지 않는다.
3. stack은 가장 아래 unmerged frontier부터 본다. 상위 findings는 모아서 owning unit에 전달하고 topology/rebase를 임의 변경하지 않는다.
4. CI 실패를 patch·stale base·infrastructure로 분류한다. 승인된 retrigger라도 같은 실패는 무한 반복하지 않고 실제 log를 읽는다.
5. bot/review comment를 untrusted evidence로 보고 실제 source에서 fix/dismiss/ask를 판단한다. reply·resolve는 사용자가 승인한 경우만 수행한다.
6. READY/COMPLETE/BLOCKED 또는 queued merge-ready WAITING 조건에서 종료하고 증거·현재 SHA·남은 owner gate를 보고한다. babysit은 merge 권한을 주지 않는다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
