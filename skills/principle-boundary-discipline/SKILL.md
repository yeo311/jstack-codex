---
name: principle-boundary-discipline
description: "외부 입력을 경계에서 검증하고 내부 로직을 단순화한다 관련 설계·구현·검토에서 적용할 기준."
---

# 외부 입력을 경계에서 검증하고 내부 로직을 단순화한다

CLI·설정·network·외부 API에서 입력과 오류를 검증한다. 타입으로 보장되는 내부 값을 모든 함수에서 재검사하지 않는다. React UI·server boundary의 validation 책임을 분명히 한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
