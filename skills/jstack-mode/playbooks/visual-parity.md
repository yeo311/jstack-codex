# 화면 일치

1. 비교할 원본·새 화면·route·데이터·viewport·font·theme·browser 조건을 맞춘다. 기준 이미지는 제공되거나 실제 캡처한 것을 사용한다.
2. 같은 사용자 상태의 before/after screenshot을 개인 evidence로 저장하고 geometry·typography·spacing·color·overflow·focus를 비교한다.
3. pixel difference가 animation·font load·환경 차이인지 실제 regression인지 확인한다. 중요한 차이만 grouped fix로 제품 scope에서 고친다.
4. keyboard·responsive·interaction을 다시 실행한다. 시각 차이와 동작 차이를 따로 보고하고 screenshot을 실제 확인하지 않았다면 parity 미검증으로 남긴다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.

## Pixel-exact 계약

baseline은 변경 전 실제 component의 각 state를 같은 viewport/font/theme/data에서 캡처한 불변 specification이다. 기준이 없으면 parity 완료를 주장하지 않는다. baseline이 잘못된 것으로 보이면 사용자에게 근거를 보여주고 변경 결정을 확인하며, diff를 통과시키려고 baseline·harness·component structure를 몰래 바꾸지 않는다.

공유 primitive를 먼저 고정하고 한 component씩 migration한다. image diff의 nonzero delta는 pixel-exact 기준의 실패다. environment/animation/font 영향을 맞춘 뒤 같은 harness로 다시 확인한다. '중요하지 않은 차이'라는 판단으로 zero-diff predicate를 느슨하게 바꾸지 않는다. 사용자가 별도의 시각 허용치를 요청한 경우만 그 다른 계약을 명시한다. 결과는 component별 image diff·baseline/harness 위치·남은 차이·실제 interaction 증거다.
