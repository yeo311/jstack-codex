# 고정 원본과 조사 결과

이 문서는 고정 커밋의 원본 의존성과 이식 판단을 남기는 역사적 조사 기록이다. 현재 실행은 README의 설치·사용 절과 skills의 Codex 지침을 따른다.
원본은 [cursor/plugins의 pstack](https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack), 커밋 `e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a`, 버전 0.15.9다. 50개 스킬과 23개 절차를 조사했다. [원본 inventory](upstream-inventory.json)에 각 스킬 원본 SHA256을 보존했다.

MIT 저작권 `Copyright (c) 2026 Lauren Tan`과 허가·무보증 고지를 [원본 LICENSE](UPSTREAM-LICENSE.txt) 및 프로젝트 LICENSE에 유지했다. 원본 로고·브랜드를 복제하지 않고 적응 사실을 NOTICE에 밝혔다.

| 원본 구성 | 의존성 | 최종 처리 |
| --- | --- | --- |
| 스킬·모델 역할 | Cursor Task/AskQuestion/create-skill, 외부 모델 slug, 전역 rules | Codex 도구를 확인하고 일반 내부 분업은 현재 모델 상속. 모델 역할·다중 모델 동시 panel 제외. |
| workflow helpers | Bun, commander 14.0.0, TypeScript, bun-types, node API | 추가 설치 없는 Python3 stdlib helper. cache bootstrap·캐시 쓰기 제외. |
| orchestration·watcher | git/gh, 일부 Graphite/Origin, Cursor cloud agent와 runtime store | 개인 JSON queue·정확 SHA·독립 검증·pilot/drain/restart를 유지. git/gh 기본. 다른 runtime 문법을 전부 이식했다고 주장하지 않음. |
| 검증·맥락 | browser control/Playwright/Cypress/PTY/HTTP, Cursor transcripts, project-local verification/map | 기존 React/Next harness·가용 browser 우선. 지도·계획·기록은 개인 위치. 없는 Cursor 경로를 Codex에 적용하지 않음. |
| bot UI | Cursor Grok webhook·Tailscale·sudo | 사용자 선택으로 make-bot-ui 제외. |

최종 plugin/repo 이름은 `jstack-codex`, 개인 state 기본은 `~/.local/share/jstack`다. 원본 50개와 절차 23개의 항목별 결과·이유·지원 차이는 [README](../README.md)에 기록했다. `arena`, `swarm`, `make-bot-ui` entrypoint를 제외하고 47개 스킬을 제공한다. `poteto-mode`→`jstack-mode`, `setup-pstack`→`setup-jstack`, `tdd`→`jstack-tdd`로 변경했다. 서로 다른 모델 동시 호출만 제외하며 일반 Codex 내부 병렬과 독립 검토는 유지한다.

[공식 패키징 문서](https://developers.openai.com/plugins/build/plugins)의 root Agent Plugins 1.0.0 schema와 설치 CLI 0.156.1 parser를 확인했다. root plugin.json 단독으로 개인 marketplace에서 인식·격리 설치·cache 47개 스킬을 확인했다. OpenAI-specific interface는 com.openai에만 두며 중복 compatibility overlay는 없다. schema의 내려받은 사본은 schemas/plugin.schema.json이다. runtime helper에는 MCP·모델API·추가 package가 없다.

원본의 중요한 세부 기준이 축약되지 않도록 독립 검토에서 why의 coverage/확신, architect의 구조/rationale, benchmark/TypeScript/personal-mode, visual-parity/hillclimb/eval/trace, review-only 계약을 다시 비교하고 한국어 reference로 복원했다. 결정적 helper tests·정적 검사·실제 model/browser 증거의 범위는 [검증 문서](../docs/VERIFICATION.md)에서 구분한다.
