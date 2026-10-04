# 승인된 landing

1. 사용자가 해당 repo/PR의 merge·land를 명시 요청했는지 확인한다. 배포는 별도의 실행이며 merge 요청에서 자동 확장하지 않는다.
2. 각 PR의 정확 head/base·diff·기존 check·실제 사용자 경로를 독립 같은 모델 reviewer로 검증할 수 있다. 결과는 개인 ledger/report에 둔다. 외부 verdict 게시 권한은 따로 확인한다.
3. stack은 아래부터 연속으로 verified된 범위만 landing 후보로 삼는다. 위 PR green을 아래 결함의 대체 증거로 쓰지 않는다.
4. head/base가 바뀌면 이전 evidence가 그대로 유효한지 실제 patch와 build를 확인한다. live server 증거는 실행한 build/head가 같아야 한다. 필요한 lane만 재실행하고 CI/mergeability는 현재 head에서 다시 확인한다.
5. 현재 trunk와 conflicts·중요 경로 overlap을 확인하고 승인된 최하단 PR만 처리한다. shared branch force-push·descendant auto-merge는 요청된 권한 없이 하지 않는다.
6. forge에서 실제 merged SHA·상태를 읽어 완료를 확인하고 다음 frontier·blocked PR을 보고한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
