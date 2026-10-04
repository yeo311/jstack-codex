---
name: principle-type-system-discipline
description: "불가능한 상태를 막는 자료형과 외부 입력 검증을 사용한다 관련 설계·구현·검토에서 적용할 기준."
---

# 불가능한 상태를 막는 자료형과 외부 입력 검증을 사용한다

불가능한 상태·semantic primitive 혼동·외부 입력을 타입과 boundary parsing으로 막는다. authoritative schema에서 type을 도출하고 union을 exhaust한다. any/cast로 보장을 꾸미거나 branding을 불필요하게 늘리지 않는다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
