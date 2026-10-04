---
name: create-verification-skill
description: "실제 앱을 조작하는 검증 절차와 기능 지도를 생성한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 검증 절차 생성

1. 코드에서 시작 명령·실제 route·selectors·auth·데이터·기존 Playwright/Cypress를 확인한다. 모르는 product call만 사용자에게 묻는다.
2. 개인 verification 영역의 `verify-<app>.md`에 시작, 준비 상태 점검, 실제 조작, 관찰 기준, 증거 위치, 종료 절차를 쓴다. 필요하면 개인 SKILL.md 형태의 파일로 보관하되 자동 등록됐다고 주장하지 않는다.
3. 개인 features에 기능 index와 우선 3~5개 핵심 기능을 적는다. 각 기능에 하위 동작, 사용자의 진입 경로, 실제 조작 recipe, pass 조건, 주의점을 넣는다.
4. 기존 harness가 없으면 가용 browser 도구를 사용하는 recipe를 만들고 도구·dependency의 미지원 부분을 표시한다. 팀 repo test/설정 추가는 별도 제품 요구 범위에서만 한다.
5. 시작→준비 점검→기능 한 개의 실제 조작→증거 저장→종료를 실행한다. 시작한 process만 종료하고 증거가 남는지 확인한다. 미실행 절차는 초안으로 표시한다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

개인 검증 문서, 기능 index와 기능별 사용자 recipe, 실제 실행한 기능의 action/result 증거, 종료 후 남은 증거 경로. 미실행 절차는 초안으로 구분한다.
