---
name: correct
description: "반복 오류를 구조·자료형·검사로 예방한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 반복 오류 예방

1. 사용자가 지적한 오류를 실제 코드와 재현에서 확인한다. 개인 decisions에 원인과 근거를 기록한다.
2. 우선 ownership·state 구조·자료형으로 오류를 막는 작은 변경을 찾는다. 필요한 기존 lint·test를 재사용한다.
3. 새 lint/CI나 공통 규칙이 제품 범위를 넓히면 구체 제안으로 확인한다. plugin metadata를 팀 repo에 만들지 않는다.
4. 실제 과거 오류에서 새 검사나 구조가 실패를 잡는지 확인한다. 문서만 더 쓰는 것으로 예방했다고 주장하지 않는다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

반복 오류와 root cause·선택한 구조적 방지책·실제 오류를 잡는 검사 또는 재현·제품 범위 밖 제안.
