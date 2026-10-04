---
name: recall
description: "현재 작업 맥락과 남은 일을 근거로 복원한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 작업 맥락 복원

1. 사용자가 지정한 프로젝트의 현재 branch/head/status와 개인 understanding·plans·reports·program 기록을 읽는다.
2. 활성 thread나 사용자가 요청한 관련 기록만 조사한다. unrelated chat·회사 데이터·memories를 광범위하게 수집하지 않는다.
3. 기록의 SHA와 현재 source를 비교하고 이미 끝난 일·진행 중·blocker·다음 행동을 구분한다.
4. 짧은 현재 상태를 한국어로 전달한다. 이전 보고의 self-report를 실제 완료 근거로 대체하지 않는다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

현재 branch/head·검증된 완료·진행 중·blocker·다음 행동과 각 상태의 supporting 근거.

## 맥락 범위와 결과 형식

특정 prior session 하나의 재개는 session-pickup, 선호를 영구 스킬로 만드는 작업은 automate-me로 구분한다. 사용자가 완전한 state capsule을 주면 새 기록 수집을 생략한다. 그 외는 topic·workspace·기간을 고정하고 '최근' 기본은 7일로 명시한다. 사용자의 '전체' 요청을 말없이 최근 몇 건으로 줄이지 않는다.

가용 Codex thread/history 도구나 사용자가 지정한 기록만 조회한다. 실제 수정 시각으로 관련 후보를 정하고 topic을 먼저 찾은 뒤 해당 구간만 읽는다. 현재 chat와 noise/agent/eval 대화는 제외한다. 실제로 무엇을 실행했는지가 중요하면 요약만으로 판단하지 않고 관련 full record를 확인한다. 없는 Cursor transcript 경로를 Codex에 적용하지 않는다.

named feature/bug/subsystem은 why의 관련 shared-record 범주에서 현재 상태·되돌린 fix·반복 사용자 증상을 확인하고 null/접근 불가를 기록한다. pure 활동 회고는 개인 기록과 live 상태만으로 끝낼 수 있다. 주변 feature는 이 작업을 막을 때만 포함한다.

결과는 5개 이내 핵심 capsule, thread별 상태(merge됨/열린PR/진행branch/검증미커밋/revert/미시작), 반복 문제 5개 이내, 가장 유용한 다음 행동 하나다. 실제 PR·branch·SHA와 근거를 붙이고 공개 output의 private 맥락은 최소화한다.
