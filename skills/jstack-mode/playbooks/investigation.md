# 읽기 조사

1. 질문의 범위와 답을 지지할 근거를 정한다. 관련 source를 읽기 전에 원인이나 해결책을 확정하지 않는다.
2. entrypoint부터 실제 흐름을 추적한다. 구조는 how, 결정 이유는 why에서 확인한다. 독립 source slice는 같은 Codex 내부 reader에 분업한다.
3. 필요한 관찰·read-only 실험을 실행한다. 읽기 조사 요청에서 product code를 수정하지 않는다.
4. 관찰·추론·미확인을 구분하고 근거 경로·symbol·SHA를 개인 understanding/reports에 남긴다. 답변은 핵심 흐름과 남은 불확실성이다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
