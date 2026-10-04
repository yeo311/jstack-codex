# 검토 rubric와 합성 판정

## 범위와 intent

사용자가 지정한 diff/files를 우선하고 branch 작업이면 실제 base를 확인해 full changeset과 필요한 주변 source를 읽는다. user/commit/PR에서 구현 의도를 한 문단으로 정한다. intent가 실제로 불명확하고 검토 범위를 바꾸면 질문한다. 코드 모양에서 사용자 제품 의도를 임의 확정하지 않는다.

## 관련 lens

- 정확성. 실제 caller 경로의 empty/boundary/error/state/race/stale closure, 중단 후 재실행과 idempotency, shared writer의 구조적 분리를 확인한다. null 가능성은 실제 call chain을 증명한다.
- 근본 원인. guard/retry/cast가 증상을 덮는지 주변 caller/callee/type을 읽는다. 주석으로 강제한 convention보다 ownership/type/기존 check로 막을 수 있는지 본다.
- 구조. boundary validation·자료 구조·coupling·정보 누출·불필요한 층·중복 내부 API·canonical ownership이 실제 유지보수에 주는 문제를 확인한다.
- 검증. behavior 검사·실제 integration 경로·현재 head의 실제 artifact와 live proof를 확인한다. child self-report·file mtime만으로 사실을 판정하지 않는다.
- 복잡도/품질. working code라도 간단한 구조가 큰 branch/layer/mode를 없앨 수 있는지 검토한다. 한 caller wrapper·magic fallback·cast·불필요한 설정·file size 증가의 실제 영향과 이유를 확인한다. 임의 line threshold를 새 lint로 만들지 않는다.
- 보안. input→dangerous sink/auth/data/secret/TOCTOU 경로를 실제 source에서 추적한다. 가상의 위험만으로 finding을 채우지 않는다.

모든 change에 모든 lens를 강제하지 않는다. 간단한 bug fix에 큰 architecture 감사 보고서를 붙이지 않는다. severity는 critical/warning/nit, finding은 trigger·위치·영향·근거와 필요한 경우 작은 대안을 가진다. 다른 reviewer가 보는 범위를 따라 취향을 버그로 올리지 않는다.

## Parent 합성

deduplicate한 finding마다 독립 reader 출처와 agreement/disagreement를 남긴다. parent가 실제 code와 외부 제약을 읽어 판단하며 같은 모델 agreement를 과장하지 않는다. 새 layer를 제안하기 전에 그 비용과 다음 실제 변화를 확인한다.

- 조치 필요(Act On). 실제 correctness/security/maintainability 결함으로 이 변경을 막을 이유가 있다.
- 검토할 선택(Consider). 타당하지만 지금 비용보다 가치가 큰지 사용자 선택이 남는다.
- 참고(Noted). 기술적으로 유효하나 현재 scope에서는 낮은 영향·미행동 맥락이다.
- 기각(Dismissed). 틀리거나 실제 caller/계약/제약을 놓친 의견이며 구체 이유를 적는다.

최종 결과는 intent, 동일 Codex 내부 reviewers와 실제 scope, 네 범주 finding, agreement/disagreement map이다. findings를 채우기 위한 nit을 올리지 않고 실제 correctness/security는 한 reviewer만 제기해도 신중히 확인한다. **검토 요청의 산출물은 verdict이며 자동 수정하지 않는다.** 이미 user가 fix까지 승인한 작업에서만 별도 제품 수정과 재검증을 수행한다.
