# 캡처된 trace 진단

1. 제공된 cpuprofile·trace·heap snapshot의 format·버전·캡처 환경을 확인하고 맞는 도구로 읽는다.
2. 핵심 hot path·retainer·idle 반복을 작은 근거로 줄인다. 큰 artifact는 same-model 내부 reader로 나눌 수 있다.
3. 실제 source·symbol·시간 구간에 연결하고 observed fact·가능 원인·추가로 필요한 관찰을 구분한다.
4. 진단 결과와 evidence pointer를 개인 report로 남긴다. 캡처만으로 재현·fix·성능 개선까지 실행했다고 말하지 않는다.

[개인 상태](../references/state.md), [프런트엔드](../references/frontend.md), [권한](../references/permissions.md)을 적용한다. 병렬 실행은 [일반 Codex 분업](../references/parallel.md)으로 제한하고 결과·정확 SHA·실행한 검증·남은 blocker를 한국어로 전달한다.

## 캡처 진단의 확신

제공된 capture는 고정 데이터다. source artifact를 바꾸지 않고 query 가능한 표/구조(SQL 또는 적절한 parser)로 필요한 event·allocation·retainer를 줄인다. retainer→GC root·hot path→실제 symbol의 mapping이 해결되지 않았으면 원인을 확정한 진단이 아니다.

paired before/after capture나 재현 증거가 없으면 가장 강한 가설과 대안·반증에 필요한 관찰로 보고한다. 타당한 설명이 있다는 이유로 causality를 단정하지 않는다. source 변경이나 새 profiling capture는 현재 진단 요청의 scope와 환경 가용성을 확인한다.
