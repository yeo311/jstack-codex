---
name: principle-fix-root-causes
description: "재현 후 증상이 아닌 원인을 고친다 관련 설계·구현·검토에서 적용할 기준."
---

# 재현 후 증상이 아닌 원인을 고친다

실제 사용자 경로에서 오류를 재현하고 상태·data·lifetime을 따라 원인을 찾는다. nil guard나 retry로 증상만 숨기지 않는다. 기존 검사나 관찰 가능한 재현으로 고친 이유를 확인한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
