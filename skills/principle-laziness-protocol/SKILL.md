---
name: principle-laziness-protocol
description: "작은 변경과 삭제를 먼저 고려한다 관련 설계·구현·검토에서 적용할 기준."
---

# 작은 변경과 삭제를 먼저 고려한다

목표를 푸는 최소 변경을 선택하고 삭제·기존 abstraction 재사용을 먼저 고려한다. 한 번의 호출을 위해 여러 층을 만들거나 범위 밖 cleanup을 섞지 않는다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
