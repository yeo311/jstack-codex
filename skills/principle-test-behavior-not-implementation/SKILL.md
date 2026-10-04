---
name: principle-test-behavior-not-implementation
description: "구현 형태 대신 사용자가 관찰하는 동작을 검사한다 관련 설계·구현·검토에서 적용할 기준."
---

# 구현 형태 대신 사용자가 관찰하는 동작을 검사한다

사용자가 호출하는 경로에서 관찰 가능한 literal 결과를 검사한다. import한 코드가 undefined를 반환해도 통과하는 assertion은 고친다. implementation shape를 그대로 따라 쓰는 검사를 만들지 않는다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
