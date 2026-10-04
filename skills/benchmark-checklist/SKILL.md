---
name: benchmark-checklist
description: "측정 조건·병목·오류·반복 가능성을 확인한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 측정 검토

1. 변경 전후의 동일한 화면·데이터·build mode·장치·network 조건과 metric을 명시한다.
2. 처리한 일의 수, 오류, warmup·cache·rate limit·timeout을 확인한다. 빨라진 것처럼 보이는 누락 작업을 배제한다.
3. 실제 limiter와 측정 지점을 찾는다. React profiler·browser trace·bundle 분석 중 필요한 기존 도구만 사용한다.
4. 반복 측정의 분산을 보고 baseline과 효과를 함께 제시한다. 사용자 체감과 다른 proxy metric이면 그렇게 설명한다.

## 상세 기준

[성능 비교 판정 전 구체 일곱 기준·profiling 분리·튜닝·상한·A/B 반복·미확인 조건을 적용한다.](references/measurement.md)

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

metric·처리한 일·limiter·환경/제한·오류·반복 분산·사용자 관련성·실제 측정 수행 여부.
