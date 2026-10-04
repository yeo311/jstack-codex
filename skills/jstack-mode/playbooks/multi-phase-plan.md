# 여러 단계 계획

1. 큰 요구를 사용자 결과와 관찰 가능한 완료 조건으로 풀고 독립/의존 단위·제품 경로·권한 gate를 정의한다.
2. 각 단위에 build·unit/기존 검사·live 사용자 recipe·증거 경로를 연결한다. 성능 관련 단위만 metric/probe/baseline/rule을 정의한다.
3. 개인 plans에 한국어 Markdown 또는 `scripts/check-plan.py`가 읽는 JSON plan을 저장한다. model lane 수·PR line 수를 고정하지 않는다.
4. 검증기가 positive plan을 통과시키고 evidence 없는 completed box·누락된 live proof·순환 dependency를 거부하는지 확인한다. 긴 작업에 계획과 실제 상태를 대조한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
