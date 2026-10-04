---
name: setup-jstack
description: "Codex 개인 설치·사용 가능한 도구·프로젝트 실행 명령·개인 기록 경로를 점검할 때 사용한다."
---

# 개인 환경 점검

1. Python3·git·사용하려는 browser/gh 도구와 대상 프로젝트의 기존 scripts를 읽기 점검한다. 없어도 임의 설치하지 않는다.
2. 개인 state context와 dry-run init을 실행해 경로를 확인한다. 사용자에게 consequential 경로·공개·설치 선택을 한 번에 확인한다.
3. 이미 요청된 상태 초기화·개인 설치만 수행한다. Codex 모델·reasoning·sandbox·network·auth·전역 작업 rule은 바꾸지 않는다.
4. 설치는 README의 Codex marketplace 절차를 사용하고 기존 config를 보존한다. 설치 cache에서 root manifest와 스킬 목록을 확인하고 새 session 필요를 알린다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

현재 개인 경로·도구 availability·dry-run/초기화 결과·설치 상태와 미지원 환경. 모델과 auth 설정은 포함하지 않는다.
