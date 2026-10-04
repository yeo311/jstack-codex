---
name: principle-sequence-verifiable-units
description: "작은 검증 단위로 순서를 만들고 매 단위 결과를 확인한다 관련 설계·구현·검토에서 적용할 기준."
---

# 작은 검증 단위로 순서를 만들고 매 단위 결과를 확인한다

작업을 각자 결과를 확인할 수 있는 의미 있는 작은 단위로 나누고 의존 순서대로 진행한다. 고정 line 수나 PR 수를 목표로 하지 않는다. 각 단위의 검사·증거·정확 SHA를 기록한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
