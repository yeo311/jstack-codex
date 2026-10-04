---
name: why
description: "Git·문서·이슈 등 근거에서 설계 선택의 이유를 확인한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 선택 이유 조사

1. 질문의 동작·시점·변경 범위를 `how`와 현재 source에서 먼저 확인한다.
2. 관련 git log/blame/diff·README·테스트를 조사하고 사용자 요청 범위의 접근 가능한 이슈·문서를 필요할 때만 확인한다.
3. 독립 evidence 범주는 같은 Codex 모델의 read-only 내부 agent에 분업할 수 있다. 모든 외부 connector를 무조건 호출하지 않는다.
4. 관찰된 결정·합리적 추론·모르는 이유를 구분하고 직접 supporting 출처와 함께 한국어로 설명한다. 개인 understanding에 최소 요약만 저장한다.

## 조사 계약

[근거 범주와 확신 수준](references/investigation.md)을 읽고 코드 anchor·일곱 범주 coverage/null·방어 코드 incident·다섯 확신 수준·경쟁 가설을 적용한다. 변경 전에는 Preserve/Change/Avoid/Risk를 도출한다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

확인한 결정 이유와 직접 출처, 자료 사이 충돌, 추론과 미확인 이유, 현재 코드에 주는 제약.
