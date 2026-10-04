---
name: typescript-best-practices
description: "TypeScript 자료형·추론·예외 처리 규칙을 적용한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# TypeScript 작업

1. 실제 TypeScript 설정과 React/Next.js 사용 방식을 확인한다. authoritative schema에서 type을 도출한다.
2. discriminated union과 적절한 자료 구조로 불가능한 state 조합을 막고 unknown 외부 입력은 경계에서 파싱한다.
3. 추론을 살리고 any·근거 없는 cast·non-null assertion으로 컴파일러를 속이지 않는다. 브랜드 타입은 의미상 혼동 위험이 실제로 있을 때만 쓴다.
4. component props와 async 반환형을 명확히 하고 exhaustiveness·error 경계를 확인한다. 요청된 동작에 필요한 기존 typecheck와 사용자 흐름을 검증한다.

## 상세 기준

[schema/guard·narrowing·satisfies·derived type·object args·telemetry의 구체 기준을 적용한다.](references/patterns.md)

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

변경한 type/state boundary와 이유, 실제 typecheck·behavior 결과, 남은 타입/호환 제약.
