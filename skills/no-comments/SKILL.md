---
name: no-comments
description: "불필요한 주석을 지우고 필요한 제약을 코드로 표현한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 주석 검토

1. 관련 코드와 주석의 실제 역할을 읽는다. 독립 reader가 필요하면 같은 Codex 모델을 상속한다.
2. 코드 동작을 되풀이하는 설명·오래된 설명·우회를 정당화하는 주석을 찾고 각각 근거를 확인한다.
3. 자료형·이름·작은 함수·기존 검사로 표현하는 것이 더 명확할 때 요청 범위에서 수정한다.
4. 외부 제약·비직관적 이유·license·tool directive는 남긴다. blanket 주석 금지를 새 규칙으로 추가하지 않는다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

삭제/유지/코드화한 주석의 이유, 보존한 license/directive/외부 제약과 관련 검사.
