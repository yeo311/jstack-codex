---
name: principle-never-block-on-the-human
description: "이미 승인된 가역적 작업은 진행하되 실제 결정권은 존중한다 관련 설계·구현·검토에서 적용할 기준."
---

# 이미 승인된 가역적 작업은 진행하되 실제 결정권은 존중한다

이미 승인된 읽기·가역 작업·정상 제품 수정을 진행하고 구체 결과로 보고한다. 권한이 없는 외부 변경이나 사용자의 consequential 선택은 필요한 근거를 준비한 뒤 확인한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
