# 실행 상태 진단

1. leak·idle CPU·glitch 등 증상을 해당 화면에서 관찰하고 환경과 발생 조건을 고정한다.
2. 가용 profiler·heap·request·event instrumentation에서 hot path·retainer·반복 callback을 찾는다. 큰 artifact parsing은 독립 내부 reader에 맡길 수 있다.
3. 가설을 최소 read-only 실험으로 반증한다. 측정 오버헤드나 instrumentation이 만든 증상도 확인한다.
4. 진단 근거와 불확실성을 보고한다. 이 절차의 요청이 진단이면 product 수정은 별도 요청 없이 수행하지 않는다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
