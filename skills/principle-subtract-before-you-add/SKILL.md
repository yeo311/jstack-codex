---
name: principle-subtract-before-you-add
description: "불필요한 코드·검사를 정리한 뒤 필요한 것을 추가한다 관련 설계·구현·검토에서 적용할 기준."
---

# 불필요한 코드·검사를 정리한 뒤 필요한 것을 추가한다

dead code·중복 validation·stub reference를 요청 범위에서 정리한 뒤 새 요구를 구현한다. 실제 사용처와 계약을 읽고 필요한 것을 미리 삭제하지 않는다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
