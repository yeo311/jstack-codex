# 검증된 PR stack 구성

1. queue의 의존 순서·root/base·owner·branch·topology writer와 review-before-land gate를 정의한다. 본 절차는 merge하거나 auto-merge를 설정하지 않는다.
2. owners는 같은 Codex 내부 분업으로 독립 build를 수행하고 requested push/초안 PR·self-proof·CI·review까지 진행한다.
3. 각 round의 정확 head와 build/live 증거를 독립 reviewer가 확인한다. verified unit만 intended parent 뒤에 추가한다.
4. 한 topology owner가 승인된 branch/base 작업을 수행한다. git/gh가 기본이며 Graphite/Origin을 요구하지 않는다. shared branch history를 임의 rewrite하지 않는다.
5. base/rebase/head가 바뀌면 patch·build와 lane validity를 확인하고 현재 head CI/mergeability를 다시 검사한다. 바뀐 결과를 아래부터 정리한다.
6. 사용자가 검토하고 land할 수 있는 chain 링크·순서·verdict·현재 SHA·open gates를 전달한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
