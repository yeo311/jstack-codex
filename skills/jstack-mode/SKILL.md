---
name: jstack-mode
description: "React/Next.js 프로젝트를 이해·설계·구현·검증하고 개인 상태와 일반 Codex 병렬 분업으로 진행할 때 사용한다."
---

# jstack 작업 모드

React/Next.js 작업에서 이해→설계→구현→실제 검증→검토→교훈 반영을 연결한다. 작은 수정은 짧게 처리하고 큰 작업은 재개 가능한 검증 단위로 나눈다.

## 시작

1. 적용되는 프로젝트 지침과 기존 변경을 확인하고 [개인 상태](references/state.md), [프런트엔드](references/frontend.md), [권한](references/permissions.md)을 읽는다. 상태가 필요한 작업은 helper context와 dry-run으로 저장 경계를 확인한다.
2. 관련 code를 조사해 사용자 entrypoint와 자료 흐름을 이해한다. 큰 질문은 `how`, 중요한 선택은 `architect`/`why`로 이어간다. 실제 product 선택이 필요한 질문을 구체적으로 제시한다.
3. 아래 표에서 맞는 절차만 읽는다. 같은 Codex 내부 분업은 [병렬 기준](references/parallel.md)을 따른다. 서로 다른 모델의 동시 경쟁·심사나 외부 모델 API를 사용하지 않는다.
4. 요청된 제품 수정과 개인 metadata를 구분한다. 관련 기존 검사와 실제 사용자 경로를 검증하고 [한국어 설명](references/writing.md)으로 결과·근거·남은 일을 전달한다.

## 작업 선택

| 요청 | 읽을 절차 |
| --- | --- |
| 읽기 조사 | [investigation](playbooks/investigation.md) |
| 기능·bug·refactor | [feature](playbooks/feature.md), [bug-fix](playbooks/bug-fix.md), [refactoring](playbooks/refactoring.md) 중 하나 |
| prototype·화면 일치 | [prototype](playbooks/prototype.md), [visual-parity](playbooks/visual-parity.md) |
| 성능·장기 개선 | [perf-issue](playbooks/perf-issue.md), [hillclimb](playbooks/hillclimb.md) |
| live·captured trace 진단 | [runtime-forensics](playbooks/runtime-forensics.md), [trace-forensics](playbooks/trace-forensics.md) |
| 스킬 작성·행동 평가 | [authoring-a-skill](playbooks/authoring-a-skill.md), [eval](playbooks/eval.md) |
| PR 작성·상태 점검·승인된 landing | [opening-a-pr](playbooks/opening-a-pr.md), [babysit](playbooks/babysit.md), [shipping](playbooks/shipping.md) |
| 장기·프로그램·여러 PR | [autonomous-run](playbooks/autonomous-run.md), [orchestrate](playbooks/orchestrate.md), [autopilot-full](playbooks/autopilot-full.md), [autopilot-stack](playbooks/autopilot-stack.md) |
| 계획·중단·재개·정리 | [multi-phase-plan](playbooks/multi-phase-plan.md), [pause-safely](playbooks/pause-safely.md), [session-pickup](playbooks/session-pickup.md), [worktree-cleanup](playbooks/worktree-cleanup.md) |

일치하는 절차가 없거나 범위가 큰 bespoke 작업은 `figure-it-out`을 사용한다. 실제 기능 지도는 `create-verification-skill`로 만들고 `maintain-verification-skill`로 확인한다. 필요한 원칙은 대응하는 `principle-*` 스킬만 읽으며 모든 원칙을 매번 전체 로드하지 않는다.

## 내부 분업과 기록

독립 소스 조사·독립 component 구현·검증 관점을 일반 Codex subagent로 분리할 수 있다. model 인수를 넣지 않고 현재 설정을 상속한다. 한 browser writer와 file/branch별 한 writer를 유지한다. 큐 상태는 helper unit/status, 중요한 판단은 helper log로 개인 state에 저장한다. 부모는 child의 실제 diff·evidence를 확인한다. 지침·보고서·상태를 팀 repo 안에 생성하지 않는다.
