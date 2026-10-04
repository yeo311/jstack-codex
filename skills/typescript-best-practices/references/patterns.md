# TypeScript 구체 기준

`principle-type-system-discipline`를 먼저 적용한다. 같은 코드베이스의 이름·schema·logger·export convention을 존중한다.

- discriminated union. optional-field bag/여러 boolean 대신 공통 `kind`/`type`/`tag` literal로 실제 variant만 표현한다. 새 variant는 `never` exhaustiveness 검사에서 드러나게 한다.
- 의미상 primitive. ID·시간·currency 혼동이 실제 위험일 때 기존 brand convention을 사용하고 boundary에서 검증한다. 내부에서는 그 type을 신뢰한다. branding을 모든 값에 강제하지 않는다.
- 구성 가능한 상태. `[T, ...T[]]`, `[T,T][]` 같은 표현이 caller의 assertion을 제거하는지 본다. plain `T[]`의 연산이 total이면 그대로 둔다. duration을 number로 둔 것만으로 음수 값까지 타입으로 불가능해졌다고 주장하지 않는다.
- `unknown` 경계. JSON/RPC/IPC/environment/file/database 입력은 외부 값이다. schema·narrowing 전에는 내부 domain type이라고 주장하지 않는다.
- schema 우선. property별 guard 전에 기존 runtime schema를 찾고 inference로 type을 derive한다. schema/interface/guard를 세 벌로 손동기화하지 않는다. 한 guard를 위해 새 dependency를 무단 추가하지 않는다. 예상된 validation 실패는 기존 safeParse 등 정상 branch로 처리한다.
- guard의 진실성. `isX`/`hasX`는 주장하는 모든 필수 값·type을 실제 검사해야 한다. 이름만 안전해 보이는 lying guard는 cast보다 오류를 숨기기 쉽다.
- narrowing 순서. discriminant switch → `in` → `typeof`/`instanceof` → 실제 검증하는 guard → 검증된 근거가 있는 최후의 cast. `as`/`!`가 필요한 이유가 missing discriminant·wide source·untyped boundary인지 먼저 고친다.
- `satisfies`. literal을 보존하면서 shape를 검사할 수 있으면 `as` 대신 사용한다. runtime external validation의 대체는 아니다.
- type 도출. OpenAPI/GraphQL/proto/database schema에서 나온 type을 우선하고 `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof`로 derive한다.
- 객체 인수. 같은 primitive 순서를 바꾸기 쉬운 API는 named object 인수를 고려한다. per-frame/parser/tokenizer hot path의 allocation은 실제 측정 제약을 확인한다.
- 경계·지속 상태. persist JSON은 version·parse 실패를 처리하고 기존 protocol의 forward compatibility 정책을 따른다. 내부 call chain에서 같은 값을 반복 파싱하지 않는다.
- 실제 검사·진단. 기존 framework test를 쓰고 가능한 실제 코드 경로를 실행한다. production logger가 있으면 request/entity ID와 structured context로 문제를 추적한다. 사용자 데이터·비밀값을 telemetry에 추가하지 않는다. 무작정 `console.log`를 새 convention으로 넣지 않는다.

```ts
type RequestState<T> =
  | { kind: "idle" }
  | { kind: "loading" }
  | { kind: "ready"; data: T }
  | { kind: "error"; message: string };

const options = { theme: "dark", columns: 3 } satisfies {
  theme: "dark" | "light";
  columns: number;
};
```

React props·server/client 직렬화·effect cleanup·cache와 hydration은 실제 Next/React 버전·router 기준을 함께 확인한다. 예시 type을 실제 runtime 검증 코드라고 오해하지 않는다.
