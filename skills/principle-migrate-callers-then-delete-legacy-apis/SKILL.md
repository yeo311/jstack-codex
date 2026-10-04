---
name: principle-migrate-callers-then-delete-legacy-apis
description: "사용처를 옮긴 뒤 오래된 내부 API를 삭제한다 관련 설계·구현·검토에서 적용할 기준."
---

# 사용처를 옮긴 뒤 오래된 내부 API를 삭제한다

새 내부 API를 도입하면 현재 caller를 추적해 계획된 단위에서 옮기고 legacy API를 삭제한다. 실제 compatibility 요구가 있으면 사용자 계약을 지키고 temporary 병행의 제거 기준을 기록한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
