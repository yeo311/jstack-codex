---
name: principle-model-the-domain
description: "업무 규칙을 명확한 자료 구조·상태 모델로 표현한다 관련 설계·구현·검토에서 적용할 기준."
---

# 업무 규칙을 명확한 자료 구조·상태 모델로 표현한다

여러 boolean·조건문으로 반복하는 업무 규칙은 union·상태 전이·table·registry 등 알맞은 구조로 표현한다. 단순한 local 코드는 불필요한 모델 계층 없이 둔다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
