# 오류 수정

1. 보고된 오류를 같은 route·데이터·사용자 조작으로 먼저 재현한다. 환경·기대·실제 결과를 개인 evidence에 기록한다. 환경을 직접 사용할 수 없으면 blocker와 필요한 정보만 묻는다.
2. 증상을 만드는 component/state/effect/data 경계를 source에서 추적하고 root cause를 가설로 적는다.
3. 싸고 명확한 회귀 test target이 있으면 수정 전 실패를 실행한다. local test가 없으면 실제 재현 recipe와 관찰 결과를 남긴다.
4. 원인을 고치는 최소 제품 변경을 수행한다. 독립 reader가 source 또는 영향 범위를 확인할 수 있지만 같은 browser instance는 공유 조작하지 않는다.
5. 같은 재현을 다시 실행하고 관련 기존 검사·다른 caller·동일 패턴을 확인한다. 실제 원인과 before/after 근거를 reports에 남긴다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
