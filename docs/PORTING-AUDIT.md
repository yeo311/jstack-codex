# 0.1.3 이식 잔재 감사 기록

이 문서는 수정 전 증상·출처·변경 이유를 남기는 검증 이력이다. 여기 인용한 원본 도구와 경로는 현재 실행 지시가 아니다. 현재 동작은 README 설치·사용 절과 skills의 Codex 지침을 따른다.

## 수정 전 문자열 검색

기준 커밋 `414f7d11955dd1f7a434f667378f0dcd2e070b23`의 추적 파일 149개를 `cursor` 대소문자 무시 literal로 검색했다. 10개 파일, 30개 매칭행, 36회 등장했다. 실행 설명 5행, 출처·이식 이력 20행, 정상 GitHub GraphQL 페이지 처리 5행으로 분류했다.

| 수정 전 실행 파일 | 확인한 문제와 수정 |
| --- | --- |
| `skills/setup-jstack/SKILL.md:3` | “Cursor 전역 모델 역할 규칙과 reasoning 예산을 설정한다”가 본문의 설정 변경 금지와 충돌했다. description·UI를 실제 Codex 개인 설치·도구·실행 명령·기록 경로 점검으로 맞췄다. |
| `skills/recall/SKILL.md:25` | 원본 transcript 경로 비교를 실제 제공되는 thread/history 조회와 개인 기록·Git 상태 fallback으로 바꿨다. 없는 세션 경로를 추측하지 않는다. |
| `skills/automate-me/references/personal-mode.md:3` | 원본 설정 디렉터리 비교를 개인 초안·확인된 Codex 설치 위치와 팀 저장소 밖 경계로 바꿨다. |
| `skills/jstack-mode/references/state.md:3` | 원본 디렉터리 나열을 helper가 확인한 개인 data root에만 기록하는 경계로 명확히 했다. 정상 요청된 제품 수정은 유지한다. |
| `skills/jstack-mode/playbooks/orchestrate.md:4` | 원본 cloud/store 비교를 현재 Codex 내부 분업과 git/gh의 branch·PR 상태 대조로 바꿨다. |

문자열에 잡히지 않는 비교 문맥도 검토했다. stack 절차는 git/gh의 실제 branch/base/PR 확인으로, 권한 기준은 현재 사용자 scope와 인증·네트워크 변경 범위로, 주석 기준은 실제 프로젝트 지침과 주석 역할로 적었다. 고정 lane 수나 원본 프로젝트 이름을 현재 동작의 전제로 삼지 않는다. 현재 모델을 상속하는 내부 subagent 분업은 유지한다.

## 보존한 기록과 API

원본 MIT 귀속·출처 URL·README 원본 비교표·research snapshot은 보존했다. 정상 GitHub GraphQL `endCursor` field도 유지했다. 페이지 변수는 `pagination_after`로 명확히 이름을 붙였고 API 동작은 유지했다. 감사 정책과 실패 사례에 나타나는 원본 단어는 재발 검사 자료다.

## 재발 검사와 범위

`scripts/audit_runtime.py`는 135개 실행 surface(스킬·절차·참고·UI·helper·manifest·README 실행부·설치 script)를 검사한다. README의 명시된 원본 이력 절과 원본 출처 link를 구분하고, 정상 API field는 read_pr의 실제 query/응답 index의 AST 문자열 범위에만 적용한다. import나 새 도구 호출은 정상 pagination 예외로 숨기지 않는다.

원본 setup description의 skill/UI 재유입, 플랫폼 이름 없는 전용 도구, 역사 영역 다음 설치 절, 정상 페이지 코드에 신규 import·호출·같은 행 import가 들어오는 실패 사례를 검사한다. 이 5개 회귀검사와 기존 22개 검사가 통과했다. manifest·47개 스킬·23개 절차·개인 상태 불변 검사는 유지했다.

독립 검토는 실행 파일의 의미적 잔재와 기능 보존을 확인했다. 같은 검토가 감사 예외의 import 숨김을 발견해 수정하고 다시 확인했다. 이 결과는 정적 검사와 제한된 의미 감사다. 금지 어휘 검사만으로 모든 미래 지시나 모델 판단을 보장하지 않으며, 원본 역사 절에 새 실행 지시를 넣는 문제는 계속 의미적으로 검토해야 한다. 0.1.3에서 전체 모델 행동·실제 앱·브라우저·Lighthouse를 새로 실행했다고 주장하지 않는다. 이전의 제한된 model smoke 결과는 VERIFICATION 문서에서 구분한다.
