---
name: maintain-verification-skill
description: "기능별 소스 조사와 실제 조작으로 검증 지도 차이를 고친다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 기능 지도 유지

1. 해당 프로젝트의 개인 verification·features를 찾고 없으면 생성 스킬로 안내한다. 대상이 여럿이면 실제 작업 범위를 확인한다.
2. 각 기능의 현재 source와 지도 차이를 독립 read-only 내부 agent로 조사할 수 있다.
3. 한 browser writer가 각 핵심 진입 경로를 실제로 조작한다. UI·side effect·error 상태와 증거를 함께 확인한다.
4. 이 실행에서는 개인 검증 문서와 지도만 고친다. 제품 regression은 보고하고 범위를 별도로 확인한다. 실제 회귀를 문서 수정으로 정상화하지 않는다.
5. 실행 실패·도구 부재와 문서 drift를 구분해 reports에 남기고 유지 cadence는 사용자 요청 때만 설정한다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

기능별 current source·live 결과·문서 drift·제품 regression·수정한 개인 지도 경로와 미검증 범위.
