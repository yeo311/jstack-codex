# 성능 문제

1. 사용자의 느린 경로와 metric·조건·오류 여부를 정하고 기존 build에서 baseline을 반복 측정한다.
2. profiler/trace/network/bundle로 실제 limiter를 찾고 benchmark-checklist를 읽는다. 숫자를 보고 원인을 바로 추측하지 않는다.
3. 한 가설의 최소 변경을 적용하고 같은 일을 같은 조건에서 다시 측정한다. 기능 누락과 오류 증가를 배제한다.
4. 실제 사용자 결과·관련 regression 검사를 확인한다. measured effect·분산·조건·남은 limiter를 reports로 전달한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
