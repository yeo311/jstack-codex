---
name: principle-separate-before-serializing-shared-state
description: "공유 쓰기를 줄이고 각 작업의 소유권을 분리한다 관련 설계·구현·검토에서 적용할 기준."
---

# 공유 쓰기를 줄이고 각 작업의 소유권을 분리한다

writer가 공유할 필요가 없는 파일·branch·worktree·browser/data를 분리한다. 필요한 공유 metadata만 한 lock/atomic 경계로 갱신한다. 같은 사용자 browser session을 여러 agent가 동시에 조작하지 않는다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
