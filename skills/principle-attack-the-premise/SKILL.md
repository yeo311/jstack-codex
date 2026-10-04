---
name: principle-attack-the-premise
description: "반복 실패를 만드는 공통 전제를 다시 확인한다 관련 설계·구현·검토에서 적용할 기준."
---

# 반복 실패를 만드는 공통 전제를 다시 확인한다

같은 전제의 해결책이 두 번 이상 같은 기준에서 실패하면 다시 patch하지 말고 실제 actor·상태·분배를 확인한다. 공통 전제를 바꾸는 작은 실험을 선택하고 결과를 근거로 기록한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
