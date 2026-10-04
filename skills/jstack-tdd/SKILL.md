---
name: jstack-tdd
description: "필요한 회귀 시나리오에서 실패 검사 후 최소 변경으로 고친다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 필요한 회귀 검사

1. 사용자가 TDD/회귀 검사를 요청했거나 싸고 명확한 local test target이 있는 bug에서 적용한다.
2. 기존 test 환경과 소비자 경로를 사용해 현재 오류에서 실패하는 검사를 실행한다. 테스트가 왜 실패하는지 확인한다.
3. 원인을 고치는 최소 변경 후 같은 검사가 통과하는지 확인한다. 구현을 그대로 따라 쓰는 검사와 무조건 통과하는 assertion을 피한다.
4. 실제 앱 사용자 경로도 필요한 범위에서 확인하고 실행하지 못한 검사를 구분한다. 명확한 test path가 없으면 억지 harness 추가 대신 재현 증거를 남긴다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

수정 전 실패·최소 변경·수정 후 성공·실제 사용자 경로 검증 수준과 실행하지 못한 검사.
