---
name: principle-minimize-reader-load
description: "호출 층과 숨은 상태를 줄여 코드를 읽기 쉽게 한다 관련 설계·구현·검토에서 적용할 기준."
---

# 호출 층과 숨은 상태를 줄여 코드를 읽기 쉽게 한다

질문과 답 사이의 layer·숨은 mutable state를 줄인다. 한 caller wrapper를 무조건 삭제하기보다 역할을 확인하고 code ownership이 읽는 곳에서 명확하게 드러나게 만든다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
