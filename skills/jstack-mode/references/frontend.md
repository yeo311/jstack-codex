# React와 Next.js 작업 기준

먼저 `package.json`, lockfile, 적용되는 `AGENTS.md`, router 구조, 관련 화면과 기존 테스트를 읽는다. React/Next 버전과 App Router/Pages Router를 실제 코드에서 확인한다. 없는 package script, route, selector, API를 추측해 명령에 넣지 않는다.

사용자 진입점부터 route → layout → component → state → data/서버 경계까지 흐름을 짧게 추적한다. Server Component가 기본인 프로젝트에서는 상호작용이 필요한 가장 작은 경계만 Client Component로 둔다. 직렬화되지 않는 props, browser API의 서버 사용, hydration 차이, 권한을 우회하는 client-only 검증을 살핀다. Pages Router 프로젝트에 App Router 구조를 강제로 도입하지 않는다.

UI 상태는 loading·empty·error·success와 사용자 조작의 전이를 명확히 표현한다. 파생값은 계산이나 적절한 memoization으로 표현하고 외부 시스템 동기화에 필요한 effect는 유지한다. `useEffect`를 일괄 금지하거나 렌더 중 side effect를 실행하지 않는다. 서버 데이터와 화면 상태의 중복 소유, stale closure, 취소·cleanup, race, 재검증·캐시 경계를 실제 사용 흐름에서 확인한다.

CSS와 UI는 기존 design system과 component 패턴을 따른다. keyboard·focus·label·aria·터치 영역·반응형·긴 한글 문장과 오류 상태를 확인한다. 로딩 경험, 레이아웃 이동, 이미지·font·bundle·불필요한 요청은 관찰한 문제가 있을 때 측정한다. 프로젝트별 컨벤션이 우선이며 새로운 library, lint, CI는 단순히 plugin을 쓴다는 이유로 추가하지 않는다.

검증은 기존 typecheck/lint/관련 test/build 중 변경에 맞는 검사와 실제 브라우저 사용자 경로를 조합한다. Playwright/Cypress가 있으면 재사용하고 evidence 출력 경로를 개인 state로 지정한다. 브라우저 도구가 있으면 읽은 접근성 정보나 DOM에서 selector를 확인한다. 도구가 없다면 실행한 수준과 실제 조작 미검증을 구분한다. mock 검사가 실제 app proof를 대신한다고 말하지 않는다.
