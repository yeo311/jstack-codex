---
name: principle-build-the-lever
description: "반복 작업이나 증명을 재실행 가능한 도구로 만든다 관련 설계·구현·검토에서 적용할 기준."
---

# 반복 작업이나 증명을 재실행 가능한 도구로 만든다

반복되는 변환·측정·검증에는 재실행 가능한 작은 도구를 쓴다. 이미 있는 script를 재사용하고 도구 개발 비용보다 작은 일에 새 framework를 만들지 않는다. 개인 artifact 생성 도구는 repo 밖으로만 쓴다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
