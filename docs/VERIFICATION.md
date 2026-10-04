# 검증 범위

## 실행한 결정적 검사

- root Agent Plugins 1.0.0 manifest를 원본 schema로 검사한다. 한국어 frontmatter/UI metadata, 상대 link, 50개 원본→47개 entrypoint, 23개 playbook을 확인한다.
- Python helper integration은 실제 임시 Git repository/worktree를 만들고 파일 hash·git status를 전후 대조한다. dry-run의 무파일 생성, 경로 이탈·symlink·repo 내부 저장 거부, branch 이름·worktree 공통 ID·동시 기록·정확 SHA 기록을 확인한다.
- JSON plan verifier는 evidence 없는 완료·fake SHA·없는 dependency·순환·누락된 live/perf 기준을 거부한다.
- PR watcher는 저장된 입력에서 draft·conflict·CI·review·unknown·queued frontier 판정을 확인한다. fixture 검사만으로 실제 GitHub PR live 상태 조회 성공을 주장하지 않는다.
- 로컬 Codex CLI 0.156.1의 실제 `plugin list` parser가 root manifest를 인식하는 것을 확인했다. 임시 Codex home에서 marketplace add→plugin add→plugin list를 실행해 manifest와 일치하는 enabled 버전과 cache의 47개 스킬·jstack-tdd·cached helper dry-run을 확인했다. 인증을 복사하거나 전역 settings를 변경하지 않았다. `scripts/test-install.py`로 재현한다.

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

## 연결된 Mac의 실제 설치 검사

공개 커밋을 고정한 개인 marketplace 설치 후 모든 tracked 파일과 cache의 SHA-256을 비교했다. 기존 config는 개인 installation-backups에 백업하고 jstack marketplace/plugin 이외 TOML 값이 보존됐는지 확인했다. 실제 Codex app-server `skills/list`는 활성화된 47개 스킬을 `jstack-codex:how` 같은 namespace 이름으로 반환했다. 이를 반영해 호출 예제와 UI 기본 prompt를 전체 이름으로 맞췄다.

임시 React fixture에서 실제 `$how` 모델 실행도 시도했으나 기존 CLI 설정의 `gpt-6.1-sol`을 기존 ChatGPT CLI 인증에서 지원하지 않는다는 400 응답으로 model turn 전에 중단됐다. 인증·모델·security 설정을 바꿔 우회하지 않았다. 제품 파일 4개의 hash와 빈 git status는 보존됐고 개인 state는 생성되지 않았다. 이 시도는 model 행동 통과 근거가 아니다. 8개 scenario는 정적 rubric이며 actual model 행동·live React browser·Lighthouse의 end-to-end 통과를 주장하지 않는다.

공식 `model/list`가 제공한 `gpt-6-luna` low를 명령에만 임시 지정해 실제 namespace 스킬 두 개를 실행했다. `how`는 코드·SHA를 조사해 내용 있는 understanding을 개인 root에 저장하고 소스 4개 hash·빈 git status를 보존했다. `architect`는 소스를 보존했지만 셸 입력 실패로 빈 plan이 남은 뒤 저장을 요약해 해당 behavior는 통과로 판정하지 않았다. 이 실패를 근거로 helper의 빈 입력·빈 replace 거부와 architect의 본문 재읽기·최종 답변의 직접 결정 질문 계약을 추가했다. 기본 모델·계정·보안 config는 변경하지 않았다. 같은 generic fixture 구조로 수정된 architect를 targeted 재검사했다. 4683 bytes의 내용 있는 개인 plan을 저장했고 helper read가 성공했다. 응답 bytes/hash와 파일을 대조했으며 대안 2개·열린 결정·첫 단위를 확인했다. 최종 답변에서도 로그인 제공자·저장소·병합·오프라인 정책을 직접 물었고 선택은 채택하지 않았다. 제품 4개 파일 hash와 빈 git status는 보존됐으며 browser/build 성공을 주장하지 않았다. 수정 전 실패와 수정 후 제한된 재검사 결과를 구분한다.

현재 결정적 회귀검사는 22개다. 빈 stdin·공백·없는 입력 파일은 산출물을 생성하지 않고, 빈 `--replace`가 기존 기록을 지우지 않는지 검사한다. `--file` 입력의 backtick·달러 문자가 그대로 저장되고 UTF-8 bytes/hash가 실제 파일과 일치하는지도 확인한다. 두 성공 행동 사례(how와 수정 후 architect)는 제한된 실제 model smoke이며, 8개 rubric 전체나 실제 앱/browser/Lighthouse 통과 근거는 아니다.
