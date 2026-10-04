---
name: principle-make-operations-idempotent
description: "반복 실행과 중단 후 재실행이 같은 결과로 수렴하게 한다 관련 설계·구현·검토에서 적용할 기준."
---

# 반복 실행과 중단 후 재실행이 같은 결과로 수렴하게 한다

중단·재시도·중복 호출을 고려해 같은 최종 상태로 수렴하게 만든다. 데이터나 외부 쓰기는 실패 범위와 재시도 경계를 먼저 확인한다. helper init은 기존 상태를 덮어쓰지 않는다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
