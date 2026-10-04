# 검증 범위

## 실행한 결정적 검사

- root Agent Plugins 1.0.0 manifest를 원본 schema로 검사한다. 한국어 frontmatter/UI metadata, 상대 link, 50개 원본→47개 entrypoint, 23개 playbook을 확인한다.
- Python helper integration은 실제 임시 Git repository/worktree를 만들고 파일 hash·git status를 전후 대조한다. dry-run의 무파일 생성, 경로 이탈·symlink·repo 내부 저장 거부, branch 이름·worktree 공통 ID·동시 기록·정확 SHA 기록을 확인한다.
- JSON plan verifier는 evidence 없는 완료·fake SHA·없는 dependency·순환·누락된 live/perf 기준을 거부한다.
- PR watcher는 저장된 입력에서 draft·conflict·CI·review·unknown·queued frontier 판정을 확인한다. fixture 검사만으로 실제 GitHub PR live 상태 조회 성공을 주장하지 않는다.
- 로컬 Codex CLI 0.156.1의 실제 `plugin list` parser가 root manifest를 인식하는 것을 확인했다. 임시 Codex home에서 marketplace add→plugin add→plugin list를 실행해 enabled 0.1.0과 cache의 47개 스킬·jstack-tdd·cached helper dry-run을 확인했다. 인증을 복사하거나 전역 settings를 변경하지 않았다. `scripts/test-install.py`로 재현한다.

## 행동 평가

`tests/eval-scenarios.json`은 실제 Codex 스킬 실행을 검토할 8개 시나리오와 rubric이다. schema와 목록 검사는 model 행동 자체의 성공 검사가 아니다. 재현 전 fix·무단 인증 선택·repo 안 metadata·가짜 browser 성공·다른 모델 호출을 실패 기준으로 둔다.

가용 agent를 통한 독립 source review와 제한된 fixture의 실제 지침 적용은 별도 근거로 기록한다. 많은 실제 프로젝트·모델·browser에서 모든 미래 행동이 검증됐다는 뜻이 아니다. helper의 결정적 경계와 모델이 prose를 따르는 범위를 구분한다.

이 저장소는 Next.js 제품 앱이 아니며 전체 React/Next app browser QA·Lighthouse·실제 고객 regression을 실행했다고 주장하지 않는다. 그런 증거는 해당 프로젝트에서 기존 harness·사용자 경로와 실제 실행한 build/head로 만들어야 한다. 생성 recipe가 미실행이면 초안이다. 회사 source를 검증 fixture로 복사하지 않는다.

## 재현

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

CI는 공개 source와 generic 임시 fixture만 사용한다. 실제 개인 state·회사 프로젝트 경로·설정·비밀을 저장소에 넣지 않는다. 개인 설치 전에는 같은 패키지의 parser·script 검사와 격리 cache 설치를 확인하고 기존 settings의 무관한 값을 보존한다.

독립 source review가 기능 보존 누락과 malformed-input parser 결함을 찾아 수정했다. why/architect/benchmark/TypeScript/personal-mode 구체 references, parity/hillclimb/eval/trace 계약, interrogate의 review-only 경계를 복원했다. 이후 narrow 독립 재검토에서 해당 blockers가 해소된 것을 확인했다.

독립 지침 적용은 generic Git React fixture의 제품 파일 4개 hash와 빈 git status를 확인하고 개인 understanding·features만 helper로 저장했다. auth/저장 product 선택은 미정으로 기록하고 구현하지 않았다. browser와 앱은 미실행이며 recipe는 초안이다. 이 evidence는 제한된 실제 지침 적용이며 전체 8개 시나리오를 blind model 실험으로 통과한 결과가 아니다.
