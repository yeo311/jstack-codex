# 측정 기반 반복 개선

1. 고정 metric·목표·baseline·작업 범위·budget·중단 조건을 정한다. 특정 속도 목표의 의미를 사용자 결과와 연결한다.
2. 반복마다 하나의 가설을 선택해 최소 변경→같은 조건 측정→유지/되돌림을 수행한다. 시도와 부정 결과도 개인 decisions에 기록한다.
3. 작업 누락·오류·cache/warmup·측정 노이즈를 확인한다. 의미 있는 accepted win별 검증 단위와 commit을 만든다.
4. 목표·budget·진전 중단에 도달하면 끝낸다. before/after 숫자·조건·실험 근거·기능 regression 검증을 전달한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.

## 실험 무결성

현실적인 data/history/state/concurrency workload에서 실제 증상을 재현하고 contrasting workload가 예상대로 구분되는지 먼저 확인한다. sensitivity 없는 metric은 수정한 뒤 사용한다. baseline과 기존 regression gate를 기록하고 harness가 error와 실제 work count를 출력하게 한다. benchmark-checklist를 적용한 후 harness를 고정한다.

target direction·숫자·최소 시도 수·budget은 실제 요청이나 사용자의 선택으로 정한다. lucky first win으로 전체 실험을 끝내지 않는다. 고정 harness로 before/after를 측정하고 regression gate가 green이며 개선이 noise보다 클 때만 keep한다. 그 외는 변경 전체를 되돌리고 결과를 개인 log에 남긴다. accepted fix는 실제로 바꾼 경로만 stage해 한 검증 단위로 commit한다.

plateau에서 연속 reject가 나면 source를 다시 읽고 mechanism·workload·가설 범주를 바꿔본다. cheap 미시도 가설이 남으면 성급히 완료로 하지 않고 marginal한 시도는 budget에 따라 멈춘다. predicate나 harness를 통과하려고 느슨하게 바꾸지 않는다. correctness/simplicity가 숫자보다 우선한다. 보고는 metric/target·baseline→final/percent·keep/revert 횟수·accepted fix·log·다음 가설이다.
