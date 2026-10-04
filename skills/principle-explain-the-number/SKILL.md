---
name: principle-explain-the-number
description: "측정값이 무엇을 측정했는지 설명하고 병목을 확인한다 관련 설계·구현·검토에서 적용할 기준."
---

# 측정값이 무엇을 측정했는지 설명하고 병목을 확인한다

속도·latency·bundle·throughput 숫자를 믿기 전에 측정 대상과 limiter를 확인한다. warmup/cache/errors/누락 작업을 배제하고 반복 분산·사용자 관련성을 설명한다.

[프런트엔드 기준](../jstack-mode/references/frontend.md)과 [개인 상태 경계](../jstack-mode/references/state.md)를 해당 작업에서 적용한다. 확인한 결과와 남은 한계를 한국어로 설명한다.
