# 스킬 작성

1. 개선할 실제 행동·trigger·출력·권한·evidence를 정하고 기존 skill이 담당하는 범위를 읽는다.
2. 사용자 scope의 개인 스킬 또는 명시 요청한 plugin source에 작성한다. 팀 repo의 숨김 metadata를 만들지 않는다.
3. UTF-8 YAML name/description과 필요한 한국어 body를 쓰고 상세 참고·결정적 helper는 필요한 경우에만 분리한다.
4. 실제 parser·상대 link·script 실행·관련 행동 fixture를 확인한다. metadata lint와 agent behavior eval을 구분해 보고한다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
