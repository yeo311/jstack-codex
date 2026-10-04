---
name: how
description: "코드의 실행 흐름·소유 경계·위치를 이해한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 프로젝트 이해

1. 질문 범위를 해석하고 관련 entrypoint부터 실제 실행 흐름을 읽는다. 파일 이름만 나열하지 않는다.
2. 작은 질문은 직접 조사한다. 큰 subsystem은 독립 route·state·data·UI slice를 같은 Codex 내부 read-only agent로 나눌 수 있다.
3. route/layout/component/hook/server 경계의 입력·출력·소유권·조건을 실제 파일과 symbol로 연결한다.
4. 개요·핵심 개념·흐름·파일 위치·주의점을 필요한 만큼 한국어로 설명한다. 개인 understanding에 확인한 SHA와 근거를 남기고 추측을 구분한다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

개요·핵심 개념·실행 흐름·파일 소유 경계·주의점, 실제 조사한 경로/symbol/SHA와 개인 understanding 경로.

여러 component 사이의 data/호출 흐름이 글만으로 어려우면 필요한 작은 Mermaid 그림을 포함한다. 서로 다른 source reader 결과가 겹치거나 충돌하면 parent가 실제 code에서 확인해 하나의 흐름으로 합친다.
