# 기능 구현

1. 사용자의 새 동작과 loading/empty/error/success, 진입 route·권한·data 요구를 확인한다. scope를 바꾸는 제품 선택은 질문한다.
2. 기존 실행 흐름을 how로 읽고 state shape와 component/server 경계를 설계한다. 중요 선택은 architect에서 작은 대안과 실제 prototype을 비교한다.
3. 완료 조건·기존 검사·실제 사용자 조작·증거 경로를 개인 plan에 기록한다. 독립 component/source/test는 같은 Codex 내부 agent에 제한된 scope로 분업한다.
4. 한 파일 writer를 유지해 요청된 제품 코드를 구현한다. 새로운 framework·테스트 설정은 필요와 요청 범위를 확인한다.
5. 관련 typecheck/lint/test/build를 실행하고 실제 앱에서 핵심 경로·오류·keyboard/반응형을 확인한다. 성능 요구가 있을 때만 적절한 측정을 추가한다.
6. 실제 artifact와 diff를 검토하고 확인한 commit·검사·live 증거·한계를 reports로 전달한다. 수행하지 않은 UI proof를 완료로 쓰지 않는다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
