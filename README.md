# jstack-codex

React/Next.js 개발을 위한 한국어 개인 Codex 플러그인이다. Lauren Tan의 [pstack](https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills)를 바탕으로 이해·설계·구현·실제 검증·독립 검토·교훈 반영을 연결한다.

플러그인·GitHub 저장소 이름은 `jstack-codex`다. 스킬 ID `jstack-mode`/`setup-jstack`와 승인된 개인 기록 경로 `~/.local/share/jstack`는 유지한다. 일반 이름 `tdd`는 요청에 따라 `jstack-tdd`로 바꿔 구분했다.

47개 스킬과 23개 작업 절차를 보존·적응했다. 서로 다른 모델을 동시에 호출하는 경쟁·심사는 제외하고, 현재 Codex 모델을 상속하는 일반 내부 subagent 병렬 분업은 유지한다. source는 공개 배포하며 각 사용자의 프로젝트 이해·기능 지도·계획·보고서·상태는 저장소 밖 개인 위치에 둔다.

## 설치

Codex CLI의 plugin 명령을 지원하는 환경에서 실행한다. 이 프로젝트는 Mac의 Codex CLI 0.156.1에서 root manifest 인식을 확인했다. GitHub 계정이 달라도 공개 source 설치가 가능하며 설치와 runtime state는 사용자마다 분리된다. 공개 배포가 개인 기록의 공개를 뜻하지 않는다.

```sh
codex plugin marketplace add yeo311/jstack-codex --ref main
codex plugin add jstack-codex@jstack-codex-personal
codex plugin list --marketplace jstack-codex-personal --available --json
```

재현 가능한 설치는 `main` 대신 검토한 전체 commit SHA를 `--ref`로 지정한다. 설치 후 새 Codex 세션을 시작한다. 데스크톱 앱에서 해당 개인 marketplace를 확인할 수 있으며 IDE extension 지원은 보장하지 않는다. 공식 [패키징 문서](https://developers.openai.com/plugins/build/plugins)와 [설치 문서](https://learn.chatgpt.com/docs/plugins)를 참고한다.

로컬 clone을 사용하는 경우 다음과 같이 등록한다. 회사 repository에서 복사하거나 설정을 추가할 필요가 없다.

```sh
git clone https://github.com/yeo311/jstack-codex.git
codex plugin marketplace add ./jstack-codex
codex plugin add jstack-codex@jstack-codex-personal
```

`plugin.json`은 Agent Plugins 1.0.0 root manifest다. `skills/`는 자동 탐지되며 `extensions.com.openai`에 한국어 UI metadata만 둔다. `.codex-plugin` overlay·MCP·hooks·자동 package bootstrap은 없다. CLI는 설치 cache를 읽으므로 source를 수정했다면 marketplace upgrade와 재설치 흐름으로 새 파일을 확인한다. 설치는 개인 marketplace/plugin 항목을 추가하며 모델·sandbox·network·auth를 변경하지 않는다. 기존 설정은 보존한다.

삭제는 개인 등록만 제거한다. 프로젝트 기록을 자동 삭제하지 않는다.

```sh
codex plugin remove jstack-codex@jstack-codex-personal
codex plugin marketplace remove jstack-codex-personal
```

## 사용

설치된 plugin 스킬은 `jstack-codex:` namespace로 탐지된다. 아래처럼 전체 이름을 쓰거나 Codex의 스킬 선택기에서 고른다. 설치 후에는 새 세션을 시작하고, 열린 선택기에 반영되지 않으면 Codex 앱을 다시 실행한다.

```text
$jstack-codex:jstack-mode로 이 Next.js 검색 기능을 이해하고 구현·검증해줘.
$jstack-codex:how로 이 화면의 route, component, state, 데이터 흐름을 설명해줘.
$jstack-codex:architect로 폼의 서버/클라이언트 경계를 설계해줘.
$jstack-codex:create-verification-skill로 개인 기능 지도와 실제 검증 절차를 만들어줘.
$jstack-codex:recall로 현재 작업의 완료·남은 일·다음 행동을 정리해줘.
```

원본의 대부분 스킬이 명시 호출 방식이어서 `agents/openai.yaml`의 `allow_implicit_invocation: false`로 이식을 명시했다. `$jstack-codex:jstack-mode`를 호출하면 해당 작업에 필요한 스킬·원칙·절차만 읽도록 연결한다. 모든 원칙을 매 작업에서 전부 로드하지 않는다. 작은 수정은 직접 진행하고 큰 독립 조사·구현·검토는 가용 Codex 내부 agent에 분업한다. model 인수·외부 모델 API를 사용하지 않는다. 동일 모델 독립 검토는 다중 모델 다양성과 같은 보장이 아니다.

현재 설치된 스킬의 절대 위치에서 `skills/jstack-mode/scripts/`를 찾는다. clone과 cache 모두 같은 상대 구조이며 runtime helper는 Python3 표준 라이브러리와 git만 필요하다. GitHub PR watcher는 기존 `gh` 접근 권한이 있을 때 사용한다. 임의 dependency·계정·서비스를 설치하거나 인증하지 않는다.

## 개인 상태

기본은 `~/.local/share/jstack/projects/<project-id>/`다. `XDG_DATA_HOME`이 있으면 그 아래 `jstack`, Windows는 `LOCALAPPDATA/jstack`, 최우선 `JSTACK_DATA_HOME`은 절대 경로다. POSIX에서는 개인 디렉터리 0700·파일 0600을 사용한다. Windows ACL 보안은 별도 OS 권한에 의존하며 Mac/Linux 검증과 동일하게 검증했다고 주장하지 않는다.

Git common directory의 정규화 경로를 hash해서 같은 clone의 worktree는 같은 프로젝트 ID를 쓴다. 별도 clone이나 이동된 clone은 별도 ID가 된다. branch 이름은 hash로 분리하므로 slash도 안전하게 다룬다. Git이 없는 폴더는 정규화 폴더 경로로 ID를 만든다.

- 프로젝트 공유 자료는 `understanding`, `features`, `verification`에 저장한다.
- 실행별 계획·보고서·증거·판단은 `branches/<branch-id>/runs/<run-id>/`에 저장한다.
- 프로그램 queue·brief·ledger·gate는 개인 program 경로에 저장한다. 큐는 JSON으로 관리한다.
- 회사 source 전체·대화·prompt·credentials를 기본 수집하지 않는다. 필요한 근거 경로·symbol·SHA와 짧은 요약만 저장한다. 개인 state를 이 공개 plugin source에 복사하지 않는다.

helper는 root가 repo·Git dir·등록된 worktree와 겹치거나 다른 Git repo 내부이면 거부한다. 상대 경로·경로 이탈·내부 symlink도 거부한다. `--dry-run`은 mkdir도 하지 않는다. 기존 artifact는 `--replace`를 명시해야 갱신된다. project lock과 atomic replace로 동시 log/queue 기록을 보존한다. stale lock은 임의 삭제하지 않는다.

```sh
python3 skills/jstack-mode/scripts/jstack.py --repo /absolute/path/to/project context
python3 skills/jstack-mode/scripts/jstack.py --repo /absolute/path/to/project --dry-run init
python3 skills/jstack-mode/scripts/jstack.py --repo /absolute/path/to/project init
python3 skills/jstack-mode/scripts/jstack.py --repo /absolute/path/to/project path --kind features --name search.md
```

경로 예시는 사용자 환경에 맞는 확인된 절대 경로로 바꾼다. helper는 plugin metadata만 보호하는 결정적 경계이며 모델의 모든 shell 동작을 강제하는 OS sandbox는 아니다. 실제 사용자가 요청한 product source·test·README 수정은 원래 프로젝트의 정상 작업이다. 앱 build/test는 `.next`·coverage 같은 자체 산출물을 쓸 수 있다. 그런 쓰기까지 피해야 하면 개인 checkout이나 지원되는 출력 위치를 선택한다. `jstack 기록을 repo에 만들지 않는다`와 `모든 제품 실행이 무쓰기다`는 별개다.

## 검증 절차

기존 프로젝트의 package scripts와 Playwright/Cypress·browser 도구를 우선 사용한다. 기능 지도는 사용자의 진입점·하위 동작·실제 조작·pass 조건·주의점을 기록하고 한 browser writer가 조작한다. 내부 병렬 reader는 source만 읽는다. 생성 검증 문서는 개인 영역에서 읽어 실행하며 팀 repo skill 자동 등록을 하지 않는다. 실제 app을 시작·조작·증거 저장·종료까지 실행하지 않은 문서는 초안이다.

typecheck/기존 test, 실제 사용자 동작, 필요할 때 측정한 성능을 구분한다. unit green이 live UI proof를 대신하지 않는다. 성능은 관련 요구·문제가 있을 때 baseline/조건/limiter/반복 분산을 측정한다. compile만으로 browser QA나 Lighthouse 성공을 주장하지 않는다.

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

개발 검사는 manifest schema·47개 스킬·23개 절차·한국어 metadata·상대 link·50개 대응을 확인한다. helper integration tests는 임시 Git 프로젝트에서 dry-run 무쓰기, source hash와 git status, worktree ID, 경로 이탈·symlink 거부, 동시 기록, SHA 기록을 확인한다. plan/PR checker의 실패 사례도 실행한다. [행동 평가 시나리오](tests/eval-scenarios.json)는 model 평가를 위한 rubric이며 정적 시나리오 목록 검사만으로 실제 model 행동 성공을 주장하지 않는다. [검증 범위](docs/VERIFICATION.md)에 실행과 한계를 분리했다.

읽기 전용 PR watcher와 JSON 계획 검사도 제공한다.

```sh
python3 skills/jstack-mode/scripts/watch-pr.py https://github.com/OWNER/REPO/pull/NUMBER --mode check
python3 skills/jstack-mode/scripts/watch-pr.py https://github.com/OWNER/REPO/pull/NUMBER --mode drive --timeout 600
python3 skills/jstack-mode/scripts/check-plan.py /absolute/path/to/personal-plan.json
```

watcher는 PR head·check·review thread·mergeability를 읽고 READY/WAITING/BLOCKED/COMPLETE/INCONCLUSIVE를 반환한다. stack URL은 하단부터 전달한다. frontier 이동은 ADVANCE event이며 queued merge-ready는 WAITING/merge-queue로 종료한다. 조회 중 head가 변하면 미확인으로 종료한다. merge·comment·push·CI retrigger는 하지 않는다. `READY`는 관찰한 forge 상태이며 독립 코드 검토·live proof·사용자 merge 권한의 대체가 아니다.

## pstack와 달라진 점

기능 보존은 원본 tool 문법·모델 역할·프로젝트 local metadata를 그대로 복사한다는 뜻이 아니다. Codex 가용 도구와 사용자가 정한 저장·권한 경계에 맞춰 결과를 보존했다. Bun/commander bootstrap, Cursor transcript 경로·전역 모델 rule, 다른 모델 panel, Cursor cloud-only 지시, Graphite 필수 조건을 제거했다. 프로그램 상태 runtime은 atomic Python/JSON helper로 바꾸고 git/gh를 기본 경로로 삼았다. Origin adapter와 Cursor watcher의 정확한 CLI flag 전부를 이식했다고 주장하지 않는다. state queue·현재 SHA·live/CI 근거·merge-ready 전달의 기능을 한국어 절차와 watcher로 제공한다.

모든 PR은 기본 초안이다. push/PR/comment/merge/deploy/메시지·설정 변경은 해당 요청에 대한 권한이 필요하다. 원본의 자율 실행 지침이나 내부 reviewer 통과를 외부 변경 권한으로 물려받지 않는다. 이미 승인된 권한은 반복 확인하지 않는다. owner gate와 중단 상태는 보존한다.

React/Next.js에서는 router·버전·server/client 직렬화·cache/revalidation·hydration·권한·accessibility·responsive·비동기 lifetime을 실제 source에서 확인한다. `useEffect`나 주석을 일괄 금지하지 않는다. 기존 구조를 우선하고 구조·type·기존 check로 반복 오류를 줄인다. 팀 lint/CI는 plugin 설치만으로 추가하지 않는다.

## 원본 50개 항목 결과

| 원본 | 결과 | jstack 대응과 이유 |
| --- | --- | --- |
| `architect` | 유지·Codex 적응 | [`architect`](skills/architect/SKILL.md). 구현 전 자료형·인터페이스·모듈 경계를 설계하고 근거를 비교한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `arena` | 제외 | 다른 모델 후보의 동시 경쟁·합성을 제거했다. 설계 대안 비교는 architect의 작은 sketch와 일반 Codex 분업으로 유지한다. |
| `automate-me` | 유지·Codex 적응 | [`automate-me`](skills/automate-me/SKILL.md). 반복되는 개인 선호를 작업 스킬로 만든다. 역할별 단계·근거·출력 계약을 보존했다. |
| `benchmark-checklist` | 유지·Codex 적응 | [`benchmark-checklist`](skills/benchmark-checklist/SKILL.md). 측정 조건·병목·오류·반복 가능성을 확인한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `blast-radius` | 유지·Codex 적응 | [`blast-radius`](skills/blast-radius/SKILL.md). 변경 밖의 영향 경로와 회귀 위험을 실행 증거로 확인한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `bro` | 유지·Codex 적응 | [`bro`](skills/bro/SKILL.md). 직전 설명을 쉬운 말로 풀어쓴다. 역할별 단계·근거·출력 계약을 보존했다. |
| `correct` | 유지·Codex 적응 | [`correct`](skills/correct/SKILL.md). 반복 오류를 구조·자료형·검사로 예방한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `create-verification-skill` | 개인 검증으로 재작성 | [`create-verification-skill`](skills/create-verification-skill/SKILL.md). 실제 앱을 조작하는 검증 절차와 기능 지도를 생성한다. 생성 metadata는 개인 state에 두고 실제 실행·제품 regression을 구분한다. |
| `figure-it-out` | 유지·Codex 적응 | [`figure-it-out`](skills/figure-it-out/SKILL.md). 맞는 작업 절차가 없을 때 관찰 가능한 완료 조건과 단계별 실험을 설계한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `how` | 유지·Codex 적응 | [`how`](skills/how/SKILL.md). 코드의 실행 흐름·소유 경계·위치를 이해한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `interrogate` | 동일 모델 검토로 재작성 | [`interrogate`](skills/interrogate/SKILL.md). 검토-only의 자동 수정 금지·rubric·합성 네 범주·agreement map을 유지하고 다른 모델 panel은 제거했다. |
| `maintain-verification-skill` | 개인 검증으로 재작성 | [`maintain-verification-skill`](skills/maintain-verification-skill/SKILL.md). 기능별 소스 조사와 실제 조작으로 검증 지도 차이를 고친다. 생성 metadata는 개인 state에 두고 실제 실행·제품 regression을 구분한다. |
| `make-bot-ui` | 제외 | 사용자 선택. Cursor Grok webhook·Tailscale bot UI를 포함하지 않는다. |
| `no-comments` | 문맥에 맞는 주석 검토 | [`no-comments`](skills/no-comments/SKILL.md). 불필요한 주석 제거와 제약 code화는 유지하고 필요한 이유·license·directive를 보존한다. |
| `poteto-mode` | jstack-mode로 재작성 | [`jstack-mode`](skills/jstack-mode/SKILL.md). 23개 절차와 필요한 원칙을 React/Next.js/Codex·개인 상태로 연결한다. |
| `principle-attack-the-premise` | 유지·한국어화 | [`principle-attack-the-premise`](skills/principle-attack-the-premise/SKILL.md). 반복 실패를 만드는 공통 전제를 다시 확인한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-boundary-discipline` | 유지·한국어화 | [`principle-boundary-discipline`](skills/principle-boundary-discipline/SKILL.md). 외부 입력을 경계에서 검증하고 내부 로직을 단순화한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-build-the-lever` | 유지·한국어화 | [`principle-build-the-lever`](skills/principle-build-the-lever/SKILL.md). 반복 작업이나 증명을 재실행 가능한 도구로 만든다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-encode-lessons-in-structure` | 유지·한국어화 | [`principle-encode-lessons-in-structure`](skills/principle-encode-lessons-in-structure/SKILL.md). 반복 지침을 자료형·검사·스크립트로 표현한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-exhaust-the-design-space` | 유지·한국어화 | [`principle-exhaust-the-design-space`](skills/principle-exhaust-the-design-space/SKILL.md). 새로운 설계는 구조가 다른 소수의 대안을 비교한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-experience-first` | 유지·한국어화 | [`principle-experience-first`](skills/principle-experience-first/SKILL.md). 사용자 경험에 맞춰 기능 범위와 품질을 선택한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-explain-the-number` | 유지·한국어화 | [`principle-explain-the-number`](skills/principle-explain-the-number/SKILL.md). 측정값이 무엇을 측정했는지 설명하고 병목을 확인한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-fix-root-causes` | 유지·한국어화 | [`principle-fix-root-causes`](skills/principle-fix-root-causes/SKILL.md). 재현 후 증상이 아닌 원인을 고친다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-foundational-thinking` | 유지·한국어화 | [`principle-foundational-thinking`](skills/principle-foundational-thinking/SKILL.md). 자료 구조와 상태 소유권을 먼저 정한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-guard-the-context-window` | 유지·한국어화 | [`principle-guard-the-context-window`](skills/principle-guard-the-context-window/SKILL.md). 큰 결과는 필요한 근거와 요약만 전달한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-laziness-protocol` | 유지·한국어화 | [`principle-laziness-protocol`](skills/principle-laziness-protocol/SKILL.md). 작은 변경과 삭제를 먼저 고려한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-make-operations-idempotent` | 유지·한국어화 | [`principle-make-operations-idempotent`](skills/principle-make-operations-idempotent/SKILL.md). 반복 실행과 중단 후 재실행이 같은 결과로 수렴하게 한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-migrate-callers-then-delete-legacy-apis` | 유지·한국어화 | [`principle-migrate-callers-then-delete-legacy-apis`](skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md). 사용처를 옮긴 뒤 오래된 내부 API를 삭제한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-minimize-reader-load` | 유지·한국어화 | [`principle-minimize-reader-load`](skills/principle-minimize-reader-load/SKILL.md). 호출 층과 숨은 상태를 줄여 코드를 읽기 쉽게 한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-model-the-domain` | 유지·한국어화 | [`principle-model-the-domain`](skills/principle-model-the-domain/SKILL.md). 업무 규칙을 명확한 자료 구조·상태 모델로 표현한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-never-block-on-the-human` | 유지·한국어화 | [`principle-never-block-on-the-human`](skills/principle-never-block-on-the-human/SKILL.md). 이미 승인된 가역적 작업은 진행하되 실제 결정권은 존중한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-outcome-oriented-execution` | 유지·한국어화 | [`principle-outcome-oriented-execution`](skills/principle-outcome-oriented-execution/SKILL.md). 목표 구조에 맞춰 단계와 검증을 설계한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-prove-it-works` | 유지·한국어화 | [`principle-prove-it-works`](skills/principle-prove-it-works/SKILL.md). 완료 전에 실제 결과물과 사용자 경로로 확인한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-redesign-from-first-principles` | 유지·한국어화 | [`principle-redesign-from-first-principles`](skills/principle-redesign-from-first-principles/SKILL.md). 새 요구를 처음부터 있던 제약처럼 설계에 반영한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-separate-before-serializing-shared-state` | 유지·한국어화 | [`principle-separate-before-serializing-shared-state`](skills/principle-separate-before-serializing-shared-state/SKILL.md). 공유 쓰기를 줄이고 각 작업의 소유권을 분리한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-sequence-verifiable-units` | 유지·한국어화 | [`principle-sequence-verifiable-units`](skills/principle-sequence-verifiable-units/SKILL.md). 작은 검증 단위로 순서를 만들고 매 단위 결과를 확인한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-subtract-before-you-add` | 유지·한국어화 | [`principle-subtract-before-you-add`](skills/principle-subtract-before-you-add/SKILL.md). 불필요한 코드·검사를 정리한 뒤 필요한 것을 추가한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-test-behavior-not-implementation` | 유지·한국어화 | [`principle-test-behavior-not-implementation`](skills/principle-test-behavior-not-implementation/SKILL.md). 구현 형태 대신 사용자가 관찰하는 동작을 검사한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `principle-type-system-discipline` | 유지·한국어화 | [`principle-type-system-discipline`](skills/principle-type-system-discipline/SKILL.md). 불가능한 상태를 막는 자료형과 외부 입력 검증을 사용한다. React/Next.js·개인 경계에 맞춰 적용한다. |
| `recall` | 유지·Codex 적응 | [`recall`](skills/recall/SKILL.md). 현재 작업 맥락과 남은 일을 근거로 복원한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `reflect` | 유지·Codex 적응 | [`reflect`](skills/reflect/SKILL.md). 최근 작업의 교훈을 기존 스킬 변경에 연결한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `setup-pstack` | setup-jstack로 재작성 | [`setup-jstack`](skills/setup-jstack/SKILL.md). 모델 역할 설정 대신 개인 상태·도구·설치를 점검한다. 전역 model rule은 제거했다. |
| `show-me-your-work` | 유지·Codex 적응 | [`show-me-your-work`](skills/show-me-your-work/SKILL.md). 중요한 판단·이유·근거·결과를 재검토 가능한 기록으로 남긴다. 역할별 단계·근거·출력 계약을 보존했다. |
| `swarm` | 진입점 제외 | 다중 모델 fanout 진입점을 제거했다. coverage 분업·독립 검증·queue는 jstack-mode와 프로그램 절차에 유지한다. |
| `tdd` | jstack-tdd로 이름 변경 | [`jstack-tdd`](skills/jstack-tdd/SKILL.md). 필요한 회귀 시나리오에서 실패 검사 후 최소 변경으로 고친다. 역할별 단계·근거·출력 계약을 보존했다. |
| `teach` | 유지·Codex 적응 | [`teach`](skills/teach/SKILL.md). 실행 구조와 설계 이유를 연결해 사람이 이해할 수 있게 설명한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `technical-writing` | 유지·Codex 적응 | [`technical-writing`](skills/technical-writing/SKILL.md). 독자와 목적에 맞춰 문서·설계안·PR 설명을 작성한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `typescript-best-practices` | 유지·Codex 적응 | [`typescript-best-practices`](skills/typescript-best-practices/SKILL.md). TypeScript 자료형·추론·예외 처리 규칙을 적용한다. 역할별 단계·근거·출력 계약을 보존했다. |
| `unslop` | 한국어 문체로 재작성 | [`unslop`](skills/unslop/SKILL.md). 영어 금지어 기반 강제 지침 대신 의미·조건·근거를 보존하는 한국어 문체 기준을 사용한다. |
| `why` | 유지·Codex 적응 | [`why`](skills/why/SKILL.md). Git·문서·이슈 등 근거에서 설계 선택의 이유를 확인한다. 역할별 단계·근거·출력 계약을 보존했다. |

## 원본 23개 절차 결과

| 절차 | 결과와 변경 이유 |
| --- | --- |
| [`authoring-a-skill`](skills/jstack-mode/playbooks/authoring-a-skill.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`autonomous-run`](skills/jstack-mode/playbooks/autonomous-run.md) | 일반 Codex 내부 parallel owner/queue·pilot·drain·재개·중단·현재 SHA 검증을 유지했다. Cursor cloud·다중 모델·무조건 merge·고정 tick은 제거했다. |
| [`autopilot-full`](skills/jstack-mode/playbooks/autopilot-full.md) | 일반 Codex 내부 parallel owner/queue·pilot·drain·재개·중단·현재 SHA 검증을 유지했다. Cursor cloud·다중 모델·무조건 merge·고정 tick은 제거했다. |
| [`autopilot-stack`](skills/jstack-mode/playbooks/autopilot-stack.md) | 일반 Codex 내부 parallel owner/queue·pilot·drain·재개·중단·현재 SHA 검증을 유지했다. Cursor cloud·다중 모델·무조건 merge·고정 tick은 제거했다. |
| [`babysit`](skills/jstack-mode/playbooks/babysit.md) | git/gh·현재 head·frontier·draft PR·검증과 사용자 권한을 유지했다. 외부 verdict/comment 자동 게시·Origin 전용 adapter는 제외했다. |
| [`bug-fix`](skills/jstack-mode/playbooks/bug-fix.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`eval`](skills/jstack-mode/playbooks/eval.md) | 같은 모델의 행동 rubric·실제 artifact·검증기 negative 검사를 유지하고 다른 모델 후보 panel은 제거했다. |
| [`feature`](skills/jstack-mode/playbooks/feature.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`hillclimb`](skills/jstack-mode/playbooks/hillclimb.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`investigation`](skills/jstack-mode/playbooks/investigation.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`multi-phase-plan`](skills/jstack-mode/playbooks/multi-phase-plan.md) | 개인 plan·단위별 검사/live/조건부 perf·근거를 유지하고 고정 10lane/영어 문체 checker를 JSON verifier로 대체했다. |
| [`opening-a-pr`](skills/jstack-mode/playbooks/opening-a-pr.md) | git/gh·현재 head·frontier·draft PR·검증과 사용자 권한을 유지했다. 외부 verdict/comment 자동 게시·Origin 전용 adapter는 제외했다. |
| [`orchestrate`](skills/jstack-mode/playbooks/orchestrate.md) | 일반 Codex 내부 parallel owner/queue·pilot·drain·재개·중단·현재 SHA 검증을 유지했다. Cursor cloud·다중 모델·무조건 merge·고정 tick은 제거했다. |
| [`pause-safely`](skills/jstack-mode/playbooks/pause-safely.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`perf-issue`](skills/jstack-mode/playbooks/perf-issue.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`prototype`](skills/jstack-mode/playbooks/prototype.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`refactoring`](skills/jstack-mode/playbooks/refactoring.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`runtime-forensics`](skills/jstack-mode/playbooks/runtime-forensics.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`session-pickup`](skills/jstack-mode/playbooks/session-pickup.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`shipping`](skills/jstack-mode/playbooks/shipping.md) | git/gh·현재 head·frontier·draft PR·검증과 사용자 권한을 유지했다. 외부 verdict/comment 자동 게시·Origin 전용 adapter는 제외했다. |
| [`trace-forensics`](skills/jstack-mode/playbooks/trace-forensics.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`visual-parity`](skills/jstack-mode/playbooks/visual-parity.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |
| [`worktree-cleanup`](skills/jstack-mode/playbooks/worktree-cleanup.md) | 기능·trigger·단계·실제 검증 결과를 한국어로 적응했다. |

## Lauren Tan의 의도와 이번 선택

참고 영상 3개의 전체 자동 캡션을 조사해 아래 방향을 확인했다. 영상 화면 전체를 직접 시청하거나 timestamp별 장면을 검증한 결과로 표현하지 않는다. 캡션에는 ASR 오류가 있을 수 있어 본문은 짧은 요약만 남겼다. 전체 transcript를 재배포하지 않는다.

- [첫 번째 참고 영상](https://www.youtube.com/watch?v=zkmvCDSxqdc). 목표는 많은 PR 수 자체보다 반복되는 수동 수정의 원인을 검증 가능한 환경으로 줄이는 데 있다. 실행 가능한 검증 CLI와 기능 지도는 각각 앱을 조작하는 방법과 사용자 진입점을 아는 역할을 맡는다. 기능·코드 품질·측정 성능은 다른 축이며 예방은 구조/types와 기존 static check를 먼저 고려한다.
- [워크숍 영상](https://www.youtube.com/watch?v=jLKQp4SgGr0). 읽기 전 진단을 피하는 how와 실제 조사 증거, 스킬 자체의 행동 평가와 verifier 검증, 작은 의미 있는 reversible unit, 로컬 실행을 보고 신뢰한 뒤 automation을 넓히는 방향을 강조한다. 무제한 token 방식과 프로젝트별 effect/주석 규칙을 모두에게 강제하지 않으며 개인 적응을 권한다.
- [세 번째 참고 영상](https://www.youtube.com/watch?v=MN9dGgmLyso). 결정적인 작업은 CLI/script로, 판단은 짧은 skill로 나누고 실제 앱 조작·trace·snapshot과 반복 교훈 기반 개인 workflow를 연결하는 방향이다. 이 영상은 [자동 캡션 공개 mirror](https://prepublish.ai/youtube-transcript/MN9dGgmLyso)도 참고했다.

이에 따라 jstack는 실제 이해→재현→수정→사용자 경로 검증→검토→교훈 사이클과 feature map/eval을 보존했다. 다른 모델 동시 실행 제거, 한국어, React/Next.js 특화, 개인 기록, bot UI 제외는 이 사용자가 선택한 jstack 요구다. 동일 모델 분업이 원본의 다중 모델 diversity를 대체한다고 주장하지 않는다.

원본은 pstack 0.15.9, 고정 commit `e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a`, MIT `Copyright (c) 2026 Lauren Tan`이다. 원본 copyright/permission은 [LICENSE](LICENSE), 출처와 변경 설명은 [NOTICE.md](NOTICE.md), 개별 원본 hash는 [inventory](research/upstream-inventory.json)에 기록했다.
