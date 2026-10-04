# 스킬 행동 평가

1. 새 스킬이 바꿔야 하는 행동을 literal rubric으로 정한다. 예시 source·초기 상태·완료 조건·실패 조건을 고정한다.
2. 작은 fixture에서 기존/새 안내 또는 구조를 같은 Codex 모델과 같은 조건으로 비교한다. 다른 모델 후보 동시 실행은 하지 않는다.
3. 평가 label을 익명화하고 독립 same-model reader가 rubric을 확인할 수 있다. self-report 대신 실제 파일 읽기·검사·artifact·경로를 확인한다.
4. 검증기가 일부러 잘못된 결과를 거부하는지도 실행한다. 재현 없이 fix, compile만으로 UI 완료, repo 내부 metadata 같은 negative 사례를 포함한다.
5. 정적 fixture lint·helper integration·실제 model/browser 실행 여부를 따로 기록한다. model 실행이 없으면 behavioral success를 주장하지 않는다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.

## Blind 계약

3~6개 구체 rubric은 judge만 보고 candidate에게 보여주지 않는다. candidate는 일반 사용자가 쓴 것 같은 goal prompt와 project-shaped context만 받는다. candidate가 보는 path/file/prompt에 eval/test/judge/experiment/rubric/score/compare/benchmark/candidate/arena 같은 실험 정체성을 드러내는 표지를 넣지 않는다. organic 제품 test script 자체가 있는 경우 그 정상 프로젝트 맥락은 유지하되 evaluation label을 덧씌우지 않는다.

다른 candidate의 존재, variant 이름, 적용 skill/principle/file을 나열하라는 chain-eliciting 요청은 숨긴다. judge는 sanitized output label과 같은 rubric/scale로 두 variant를 한 번에 본다. 동일 Codex 모델로 평가하며 다른 모델을 동시에 호출하지 않는다.

실제 tool/file evidence와 artifact shape를 보고 chain-following을 평가한다. 관련 record가 제공되지 않으면 모른다고 표시하며 unrelated chat를 조회하지 않는다. parent가 모든 output을 읽고 judge와의 disagreement를 해소해 rubric·per-output 결과·한계·promotion 판단을 보고한다. `tests/eval-scenarios.json`은 judge 준비 자료이므로 candidate에게 파일 전체를 주지 않는다.
