---
name: interrogate
description: "현재 Codex 모델을 상속하는 독립 관점에서 설계·변경을 검토한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 독립 관점 검토

1. 변경의 요구·diff·정확 head·핵심 검증 증거를 확인한다.
2. consumer 동작, state/비동기 lifetime, data/auth 경계 등 실제로 다른 관점에 현재 Codex 모델을 상속하는 내부 agent를 배치할 수 있다. 다른 모델 호출·panel 경쟁은 하지 않는다.
3. 각 finding은 재현 가능한 trigger·영향·파일 위치·근거를 갖춘다. 취향과 미관찰 가정은 버그와 구분한다.
4. 부모가 근거를 읽고 합성 verdict를 전달한다. 검토만 요청했다면 자동 수정하지 않는다. 이미 수정 권한이 있을 때만 실제 결함을 묶어 수정·재검증한다. 동일 모델의 agreement를 독립 모델 다양성이라고 설명하지 않는다.

## 검토 계약

[검토 rubric와 합성 판정](references/review.md)을 읽고 Act On/Consider/Noted/Dismissed·agreement map을 적용한다. 검토만 요청한 경우 결과는 verdict이며 자동 수정하지 않는다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

관점별 finding과 trigger/위치/영향/근거, 실제 확인한 fix/dismiss/ask 판단, current head의 verdict와 동일 모델 검토 한계.
