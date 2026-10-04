# 개인 mode 만들기와 갱신

1. 개인 skill 위치와 사용자가 지정한 기존 mode를 찾는다. 초안은 개인 jstack 영역에 두고 실제 설치 위치는 사용자가 지정한 개인 Codex 스킬 또는 플러그인 경로에서 확인한다. 기존 하위 범주도 살피고 팀 프로젝트 안에 개인 mode를 만들지 않는다. 기존 matching mode가 있으면 update가 기본이고 이미 '갱신'을 요청했다면 다시 묻지 않는다. 새로 시작해 기존 내용을 버릴 필요가 있을 때만 구체 차이를 확인한다.
2. 갱신은 마지막 수정 이후 관련 근거와 사용자 변경 요청만 본다. 기존 내용을 전면 재생성하지 않고 모순된 section만 수정한다. 정말 새 규칙만 추가한다. 새 mode는 관련 scope의 최근 2~4주 범위를 지정할 수 있고 기록이 없으면 현재 사용자 입력으로 시작한다.
3. response·autonomy·이해 방식·분업·검증·코드/문체·git/PR·스킬 습관의 반복 패턴을 조사한다. 독립 slice는 같은 Codex 내부 reader로 나눌 수 있다. 여러 slice/대화에서 반복된 신호는 강한 근거, 한 번뿐인 상충 신호는 약한 근거다. 대화 원문이나 회사 source를 개인 공개 plugin에 대량으로 옮기지 않는다.
4. 관찰만으로 알 수 없는 선호는 짧은 한국어 선택 질문으로 모으고 사용자의 기존 답을 재사용한다. 20개 질문이나 고정된 질문 수를 강제하지 않는다. 새 mode는 중요 범주, update는 바뀐/빠진 범주를 묻는다.
5. 실제로 비기본 규칙이 있는 section만 남긴다. 다른 스킬은 reference로 연결하고 내용을 복제하지 않는다. `<handle>-mode` description은 handle/명시 skill invocation/그 스타일 요청으로 좁힌다. 일반 '코딩/리뷰' trigger로 모든 작업을 끌어오지 않는다. 명시 호출 policy를 기본으로 보존하되 사용자가 매 turn 적용을 요청하면 그 변경을 확인한다.
6. 자연스러운 한국어 초안을 보여주고 사용자 calibration으로 맞춘다. working style의 주관적 만족을 임의 수치 benchmark로 성공 판정하지 않는다. description이 실제 잘못 routing할 때만 trigger 평가를 추가한다.
7. 개인 설치나 plugin 수정은 요청된 scope에서만 하고 기존 category·identity를 보존한다. product/task-specific workflow 하나는 일반 스킬이며 개인 working-style mode로 확대하지 않는다. 사용자 memories나 팀 config를 자동 변경하지 않는다.
