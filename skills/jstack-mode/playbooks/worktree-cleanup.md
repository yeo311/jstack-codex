# worktree 정리

1. 이번 작업이 만들었거나 사용자가 정리를 요청한 worktree만 목록과 실제 경로·branch·dirty 상태로 확인한다.
2. 미커밋·untracked·ignored 결과와 evidence를 확인해 필요한 것을 개인 state 또는 요청된 제품 branch에 보존한다.
3. 관리형 worktree는 해당 환경의 archive 도구를 우선 사용한다. 일반 git worktree는 dirty 상태나 연결된 진행 작업을 확인하고 명확한 정리 scope에서만 제거한다.
4. 회사 repo·기존 사용자 worktree·memories·실행 증거를 자동 삭제하지 않는다. 남은 blocker와 보존 위치를 보고한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
