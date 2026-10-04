---
name: show-me-your-work
description: "중요한 판단·이유·근거·결과를 재검토 가능한 기록으로 남긴다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 판단 기록

1. 장기·무인·여러 단계 작업에서 개인 run-id와 decisions 기록을 시작한다. 모든 사소한 action을 중계하지 않는다.
2. 중요 선택마다 phase·decision·why·실제 evidence·result를 helper log로 추가한다. 다른 agent 기록은 합의된 run-id와 단일 atomic 기록 경계를 쓴다.
3. 잘못된 판단은 기존 기록 삭제 대신 후속 정정 기록으로 남긴다. 기록의 경로와 SHA가 실제 증거를 가리키는지 확인한다.
4. 필요하면 같은 Codex 모델의 독립 reviewer가 누락된 근거·건너뛴 검증·범위 확대를 확인한다. 동일 모델 검토임을 밝히고 실제 확인한 주의점을 reports에 적는다.
5. 개인 기록은 팀 repo·PR body·공개 plugin에 자동 게시하지 않는다. 승인된 보고에도 필요한 결론만 최소한으로 전달한다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

개인 decisions.jsonl 경로, 주요 선택과 근거, 정정 기록, 독립 검토의 실제 주의점. 원본의 cross-model reviewer 기능은 제거됐다고 구분한다.
