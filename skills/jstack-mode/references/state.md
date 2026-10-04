# 개인 상태와 제품 수정의 경계

jstack가 만든 이해 지도, 기능 지도, 계획, 검증 절차, 보고서, 판단 기록, 실행 상태는 개인 디렉터리에 둔다. 프로젝트 내부의 `.cursor`, `.agents`, `.codex`, `.plans`, `.audit`에 생성하지 않는다. 실제 사용자가 요청한 제품 소스·테스트 수정은 해당 작업 범위에서 별도로 수행한다. 플러그인 metadata 격리가 제품 수정 권한을 줄이거나 늘리지 않는다.

helper는 이 스킬 패키지의 `scripts/jstack.py`다. 현재 읽은 `jstack-mode/SKILL.md`의 절대 경로에서 패키지 경로를 찾는다. 설치 cache나 clone 어느 곳에서도 같은 상대 구조다. shell 명령에서 `<helper>`와 `<repo>`는 실제 확인한 절대 경로로 바꾼 뒤 안전하게 인수로 전달한다. 표기를 그대로 실행하지 않는다.

```sh
python3 <helper> --repo <repo> context
python3 <helper> --repo <repo> --dry-run init
python3 <helper> --repo <repo> init
python3 <helper> --repo <repo> path --kind features --name search.md
python3 <helper> --repo <repo> write --kind understanding --name overview.md
python3 <helper> --repo <repo> read --kind understanding --name overview.md
```

`write`는 표준 입력을 저장한다. 이미 있는 파일은 실패한다. 읽고 갱신 범위를 정한 경우에만 `--replace`를 쓴다. `path`는 경로를 알려줄 뿐 디렉터리를 만들지 않는다. 증거를 저장할 상위 디렉터리가 필요하면 `write`로 해당 kind의 작은 index 파일을 먼저 만든다. runtime state는 공개 plugin Git tree에 넣지 않는다. 대량 소스를 복사하지 말고 필요한 경로·symbol·commit·근거 요약을 기록한다. 사용자 prompt나 비밀값은 기본 기록 대상이 아니다.

기본 위치는 `~/.local/share/jstack`, Windows는 `LOCALAPPDATA/jstack`다. `XDG_DATA_HOME/jstack`을 존중하며 `JSTACK_DATA_HOME`은 최우선 절대 경로 override다. repo·Git dir·등록된 worktree와 겹치는 root, 다른 Git 저장소 내부 root, 상대 경로, 내부 symlink를 거부한다. Git common dir hash는 같은 clone의 worktree를 묶고 별도 clone은 별도 ID로 만든다. `branches/<branch-hash>/runs/<run-id>/`는 분기·실행 상태를 나눈다. 공유 지도는 project별이고 기록·프로그램 상태는 branch별이다.

```sh
python3 <helper> --repo <repo> write --kind plans --name plan.md --run run-001
python3 <helper> --repo <repo> log --run run-001 --phase design --decision '선택' --why '이유' --evidence '실제 경로와 SHA' --result '결과'
python3 <helper> --repo <repo> unit --program frontend --id search --state running --owner agent-1 --evidence 'brief 경로'
python3 <helper> --repo <repo> status --program frontend
```

기록과 큐 갱신은 project 잠금과 atomic replace를 사용한다. 검증 완료 상태에는 전체 head SHA가 필요하다. `different_from_checkout`는 현재 checkout과 다른 SHA 목록이며, 다른 branch 작업의 판정을 자동 무효화하는 뜻이 아니다. unit head와 실제 PR head를 직접 비교한다. stale lock은 자동 삭제하지 않는다. 소유 프로세스·작업을 확인한 뒤 사용자가 재실행한다. path guard는 플러그인 소유 helper의 경계이며 모든 모델 shell 명령을 OS 수준에서 제한하는 보안 sandbox는 아니다.

앱 실행·기존 테스트는 `.next`, coverage 등 자체 산출물을 만들 수 있다. evidence 경로를 개인 root로 지정하고 기존 build의 쓰기 위치를 설명한다. 소스 checkout까지 무쓰기가 필요하면 허용된 개인 worktree 또는 출력 경로를 선택한다. helper가 이를 자동 보장한다고 말하지 않는다.
