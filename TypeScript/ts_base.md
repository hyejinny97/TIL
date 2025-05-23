# ✔ 타입스크립트 기초

- 자바스크립트에 정적 타입을 추가해주는 언어 및 도구

  - `TypeScript`
  - `Elm`
  - `ReasonML`
  - `Flow`

## ▶ 동적 타입 언어 vs 정적 타입 언어

- 동적 타입 언어 vs 정적 타입 언어

  |                     |      동적 타입 언어      |      정적 타입 언어      |
  | :-----------------: | :----------------------: | :----------------------: |
  |      진입 장벽      |           낮음           |           높음           |
  |       생산성        | 코드의 양이 적을 때 높음 | 코드의 양이 많을 때 높음 |
  | 타입 오류 발견 타임 |          런타임          |       컴파일 타임        |

- 정적 타입 언어가 생산성이 높은 이유

  - 함수를 호출하기 위해 함수 이름를 입력하면, 매개변수 종류와 반환값의 타입을 알 수 있음
  - 객체 이름을 입력하면, 속성값 목록을 확인할 수 있음
  - 철자가 틀리거나 타입이 맞지 않으면 IDE가 즉시 알려줌
  - 컴파일 타임에 에러가 발생하므로, 코드를 실행해 보기도 전에 타입 에러를 확인할 수 있음

- 자바스크립트는 '동적 타입 언어'이므로, 변수의 타입이 **런타임**에 결정됨
- 타입스크립트는 '정적 타입 언어'이므로, 변수의 타입이 **컴파일 타임**에 결정됨

## ▶ 타입스크립트의 장점

- MS에서 개발하고 있고 꾸준히 업데이트 버전이 나오고 있음
- 다른 경쟁 언어에 비해 큰 생태계를 가지고 있음
- MS에서 개발하고 있는 IDE인 vsCode와 같이 사용할 경우, 다양한 기능을 사용할 수 있음

  - vsCode는 특별한 설정 없이도 타입스크립트 파일의 타입 검사를 자동으로 실행함
  - 타입스크립트 코드를 위한 다양한 리팩터링 기능을 지원함

- 타입을 명시적으로 입력하지 않아도 자동으로 타입을 인식하는 기능이 있음

  - 타입 추론(Type Inference)
  - 타입 추론 덕분에 기존 자바스크립트를 크게 변경하지 않고도 타입스크립트를 비교적 쉽게 적용할 수 있음
