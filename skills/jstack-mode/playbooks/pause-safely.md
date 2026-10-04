# 안전한 중단

1. 사용자 stop을 모든 관련 writer에 전달하고 추가 mutation을 중지한다. 가용 내부 interrupt 도구를 사용한다.
2. current branch/head/변경·running process·lock owner·마지막 verified unit·남은 gate를 개인 report와 program 상태에 기록한다.
3. 이번 작업에서 시작한 process만 정리하고 기존 사용자 server·worktree·증거는 보존한다. 미완료가 완료로 기록되지 않게 한다.
4. 재개할 brief·검사·state path를 전달한다. stop 상태에서 자동 wake/schedule을 임의 설정하지 않는다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
