---
name: figure-it-out
description: "맞는 작업 절차가 없을 때 관찰 가능한 완료 조건과 단계별 실험을 설계한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 맞춤 작업 절차

1. 관찰 가능한 완료 조건·범위·위험·blocker를 먼저 적고 큰 작업의 실제 선택을 확인한다.
2. 모르는 위험부터 검증하는 작은 단위를 설계한다. 각 단위의 입력·제품 수정 범위·검사·증거를 개인 plans에 둔다.
3. 독립 작업만 일반 Codex 내부 agent에 분업하고 한 경로 writer를 겹치게 하지 않는다.
4. 매 단위에서 가설→최소 변경→실제 측정→유지 또는 되돌림을 수행한다. 결과는 VERIFIED/NOT VERIFIED/INCONCLUSIVE로 기록한다.
5. 전체 사용자 결과를 마지막에 확인하고 판단 기록·검증·남은 일을 reports로 전달한다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

설계한 단계·선택한 검증 수준과 이유·단위별 evidence·판단 기록 경로·완료 predicate와 남은 blocker.
