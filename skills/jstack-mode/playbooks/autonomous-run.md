# 장기 자율 작업

1. 완료 predicate·scope·budget·user gate·중단 조건을 정한다. 이미 승인된 가역 단계는 진행한다.
2. 개인 plan과 decisions를 시작하고 단위별 investigate→build→verify→review loop를 실행한다. 독립 작업만 bounded 내부 Codex agent로 분업한다.
3. 매 단위에서 실제 evidence와 정확 SHA를 확인한다. long wait 동안 사용자 질문에 답하고 명시 stop은 모든 writer에 전달한다.
4. 외부 쓰기·merge·deploy는 사용자 권한 범위에 한정한다. 다시 깨우기/schedule은 요청과 가용 도구가 있을 때만 만든다.
5. 최종 predicate를 실제 artifact에서 확인하고 완료·미확인·blocker·재개 위치를 개인 reports에 기록한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
