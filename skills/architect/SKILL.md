---
name: architect
description: "구현 전 자료형·인터페이스·모듈 경계를 설계하고 근거를 비교한다. 해당 요청의 React/Next.js 작업에서 사용한다."
---

# 프런트엔드 설계

1. 관련 route·component·state·서버 경계를 `how`로 추적한다. ownership을 바꿀 때 `why`에서 기존 이유도 확인한다.
2. 호출하는 쪽의 사용 예부터 작성하고 자료형·prop·signature·모듈 경계를 도출한다. 설계 sketch는 개인 plans에 보관한다.
3. 새롭고 중요한 설계에는 구조가 다른 두 가지 안을 간단히 비교한다. 같은 Codex 내부 reader를 독립 관점에 쓸 수 있다. 이미 정해진 기계적 변경은 대안을 억지로 만들지 않는다.
4. 사용자 요구를 각 안의 수용 기준·복잡도·장단점에 대입한다. 실험으로 결정되는 사실은 실행해 확인하고 제품 선택은 사용자에게 구체적으로 묻는다. 아직 답하지 않은 인증·저장·권한 정책을 임의로 선택하지 않는다. 최종 답변에도 결정에 필요한 질문을 직접 적고, 질문을 plan 파일 링크 뒤에만 숨기지 않는다.
5. 정한 구조에 맞춰 요청된 제품 코드를 구현한다. 같은 우회가 여러 곳에서 나타나면 sketch를 다시 설계하고 실제 사용자 경로를 검증한다.

## 설계 점검

중요한 후보를 선택하기 전에 [구조 위험과 근거 문서](references/design-and-rationale.md)를 읽고 각 후보를 점검한다. usage-first rationale·대안·tradeoff·open choice·첫 구현 단위가 결과 계약이다.

## 공통 경계

[개인 상태](../jstack-mode/references/state.md)와 [프런트엔드](../jstack-mode/references/frontend.md), [권한](../jstack-mode/references/permissions.md)을 따른다. 분업이 필요할 때만 [일반 Codex 병렬 기준](../jstack-mode/references/parallel.md)을 읽는다. 설명은 [한국어 문체](../jstack-mode/references/writing.md)를 따른다.

## 결과

선택한 사용 예·자료형·모듈 지도, 대안별 tradeoff, 구현 중 바뀐 가정, 실제 검증 결과를 개인 plans/reports에 남긴다. 저장한 plan의 본문을 helper로 다시 읽어 대안·장단점·열린 질문·첫 단위가 실제로 있는지 확인한다. 빈 파일이나 입력 생성 실패는 plan 저장 성공으로 보고하지 않는다.
