# 구조 변경

1. 유지해야 하는 사용자 동작·외부 API·style·data 흐름을 기존 검사와 live baseline으로 고정한다.
2. 기존 shape가 왜 복잡한지 읽고 제거할 branch·중복·invalid state를 명시한다. 단순 코드에 새로운 계층을 추가하지 않는다.
3. 작은 단위로 caller를 옮긴 뒤 legacy 내부 API를 정리한다. public compatibility 요구는 별도 계약으로 보존한다.
4. 기계적인 독립 경로는 Codex 내부 agent에 분업할 수 있다. rename의 string·문서·selector·dynamic import 사용처도 실제로 검색한다.
5. 매 단위 baseline을 확인하고 사용자 동작이 유지되는지 검증한다. 결과와 의도적인 차이를 기록한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
