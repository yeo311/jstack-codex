---
name: principle-redesign-from-first-principles
description: "새 요구를 처음부터 있던 제약처럼 설계에 반영한다 관련 설계·구현·검토에서 적용할 기준."
---

# 새 요구를 처음부터 있던 제약처럼 설계에 반영한다

새 요구가 반복 workaround를 만들면 기존 구조를 절대 기준으로 삼지 않는다. 그 제약이 처음부터 있었다면 어떤 ownership과 type이 맞는지 다시 설계하고 더 작은 구조를 선택한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
