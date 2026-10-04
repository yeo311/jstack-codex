---
name: blast-radius
description: "변경 밖의 영향 경로와 회귀 위험을 실행 증거로 확인한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 변경 영향 확인

1. diff의 export·component·hook·schema·route·style token을 사용처와 데이터 경계까지 추적한다.
2. 영향받는 화면·권한·cache·navigation·hydration과 기존 소비자를 적는다. 읽기 분업은 독립 scope로 한다.
3. 변경이 안전한 핵심 가정을 한 문장으로 쓰고 실제 앱·기존 검사로 그 가정을 확인한다.
4. 직접 영향과 관찰하지 못한 위험을 구분해 reports에 남긴다. 별도 요청이 없는 무관한 cleanup은 추가하지 않는다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

영향받는 entrypoint/caller·깨질 수 있는 조건·실행해 증명한 핵심 가정·남은 미확인 영향.
