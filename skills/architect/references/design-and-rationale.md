# 설계 후보 점검과 근거 문서

## 구조를 다시 볼 신호

각 중요한 후보를 구현 전에 아래 기준으로 점검한다. flag는 설계 수정 또는 선택을 재검토할 이유이며 자동 전면 재작성 명령은 아니다.

- 얕은 모듈. 공개 인터페이스는 큰데 숨기는 복잡도가 적다. caller가 여러 method를 조율하거나 내부 단계를 알아야 한 작업을 끝낸다. capability를 작은 공개 표면에 모으되 긴 call chain을 깊은 모듈로 착각하지 않는다.
- 정보 누출. transport·wire·storage·framework 표현을 여러 모듈이 알아 같은 정책 변경을 함께 해야 한다. 외부 표현은 경계에서 domain type으로 파싱하고 내부 표현을 공개 re-export하지 않는다.
- 시간 순서 분해. load/validate/transform/save라는 순서만으로 나눠 같은 데이터 불변식을 여러 곳이 지킨다. 실행 시점보다 지식과 ownership 경계를 기준으로 묶는다.
- 전달만 하는 method. 같은 형태의 인수를 그대로 넘기는 층이 정책·적응·별도 abstraction을 제공하는지 확인한다. 의미가 없으면 제거하거나 실제 책임을 가진 모듈로 옮긴다.
- 분산된 ownership. 같은 state를 여러 writer나 복사본이 소유한다. 한 owner가 갱신하고 나머지는 읽거나 owner에게 요청한다.
- 같은 일을 하는 여러 경로. caller가 가까운 예를 따라가며 중복 경로가 계속 늘어난다. 실제 compatibility 요구를 확인한 뒤 한 경로로 모으고 기존 caller를 옮긴다.
- import 가능한 내부 구현. 외부 caller가 internals를 쉽게 import해 사실상 public contract로 굳어진다. 기존 package/export boundary를 활용하고 필요한 경우만 제품 scope에서 접근을 제한한다.
- 수작업으로 동기화하는 목록. 같은 항목을 여러 곳에서 관리한다. 한 원본에서 derive하거나 기존 검사로 불일치를 잡는다. 팀 lint/CI를 무단 추가하지 않는다.

React에서는 state/server-data의 복사 owner, provider/hook의 감춰진 정책, Server Component 경계를 넘는 framework 객체, route마다 수동 동기화한 metadata/selector 등을 실제 source에서 확인한다.

## 개인 설계 문서의 결과 계약

한 페이지 정도의 개인 plan에 아래 내용을 실제로 채운다. placeholder 문서를 완료로 제출하지 않는다.

1. 문제. 요구와 기존 caller·type·불변식·외부 제약 때문에 설계가 어려운 이유.
2. 사용 예. type sketch보다 먼저 consumer가 import하고 호출하는 2~3개 현실적인 예와 결과. type과 usage가 다르면 usage에 맞춰 조정한다.
3. 구조. 자료 구조→signature→data flow·ownership·type으로 보장하는 불변식·validation 위치. 공개 표면이 숨기는 복잡도와 남기는 책임을 명시한다.
4. 선택 근거. 선택한 shape·이유·다른 안에서 가져온 부분·버린 부분. 서로 다른 모델 합성은 하지 않고 동일 모델 비교라는 한계를 밝힌다.
5. 수용한 tradeoff. 얻는 이점과 감수하는 제약을 쌍으로 적는다.
6. 실제 대안. 적어도 하나의 구조적으로 다른 안과 공개 복잡도·숨기는 복잡도·선택하지 않은 이유. 제약상 하나뿐이면 그 제약을 설명한다.
7. 열린 선택과 위험. 사용자에게 남은 실제 제품·보안·데이터 선택을 구체 질문으로 연결한다. 관찰로 알 수 있는 사실은 직접 확인한다.
8. 첫 구현 단위. 바로 구현할 한 단위와 검증 방법.

스케치가 틀렸다는 신호는 같은 workaround가 여러 곳에 반복되거나, caller가 내부 규칙을 알아야 하거나, 서로 다른 deviation이 같은 shape를 보일 때다. 새 constraint를 day-one 요구로 다시 설계하고 삭제를 먼저 고려한다. 하나의 작은 예외만으로 모든 구조를 버리지는 않는다.
