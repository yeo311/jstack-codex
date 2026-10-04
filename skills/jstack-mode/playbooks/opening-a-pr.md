# 초안 PR 작성

1. 사용자가 push/PR 생성을 요청한 owner·repo·branch·scope를 확인하고 실제 authenticated 계정과 remote를 읽는다.
2. 관련 프로젝트 pre-review 검사와 diff·비밀·생성 artifact를 확인한다. 개인 state·회사 source를 plugin repo에 섞지 않는다.
3. 요청된 branch를 push하고 초안 PR을 만든다. body는 문제→바뀐 동작→관련 validation·제약 중심이며 multiline body-file 또는 structured 인수를 사용한다.
4. 생성 URL·정확 head를 읽고 제공되는 artifact attachment 도구가 있으면 연결한다. PR 생성이 merge·comment·deploy 권한은 아니다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.
