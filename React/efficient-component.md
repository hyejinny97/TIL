## ▶ 가독성과 생산성을 고려한 컴포넌트 코드 작성법

### 🔹 추천하는 컴포넌트 파일 작성법

- 컴포넌트 파일 작성 순서

  - 파일 최상단에 속성값 타입을 정의
  - 컴포넌트 함수의 매개변수는 destructuring object로 정의하는게 좋음
  - 컴포넌트 외부의 변수와 함수는 파일의 가장 밑에 정의
  - 상수의 이름은 대문자로 작성

- 서로 연관된 코드를 한 곳으로 모으기

  - `useState`끼리, `useEffect`끼리 코드를 모아두는 것보다 연관된 코드끼리 한 곳으로 모으는게 좋음

- 컴포넌트 코드가 복잡하다고 느껴지면, 각 기능을 custom hook으로 분리하는 것도 좋음
  - 기능을 custom hook으로 분리하면 같은 기능을 다른 곳에서도 사용하기 좋음

### 🔹 속성값 타입 정의하기 - `prop-types`

- `prop-types`: 속성값의 타입 정보를 정의할 때 사용하는 리액트 공식 패키지
- 동적 타입 언어인 js를 사용할 경우, 규모가 큰 프로그램에서 생산성이 떨어지는 문제가 있음

  - 따라서, 가능하면 정적 타입 언어를 사용하는 것이 좋음
  - 정적 타입 언어를 사용하지 못했다면, 차선책으로 `prop-types`를 사용해 코드의 가독성을 높일 수 있음

- `prop-types` 사용 시 장점

  - 컴포넌트의 속성값에 잘못된 타입을 입력하면 콘솔에 에러 메시지를 출력해 줌
  - 타입 정의 자체가 훌륭한 문서가 되기 때문에, 컴포넌트의 로직을 이해하지 않아도 속성값의 타입 정보를 한눈에 파악할 수 있음

- `prop-types`로 정의할 수 있는 타입

  - 리액트 요소

    ```js
    MyComponent.propTypes = {
      menu: PropTypes.element,
    };
    ```

  - 컴포넌트가 반환할 수 있는 모든 것 (number, string, array, element 등)

    ```js
    MyComponent.propTypes = {
      description: PropTypes.node,
    };
    ```

  - 특정 class로 생성된 모든 객체

    ```js
    MyComponent.propTypes = {
      message: PropTypes.instanceOf(Message),
    };
    ```

  - 배열에 포함된 값 중에서 하나를 만족

    ```js
    MyComponent.propTypes = {
      name: PropTypes.oneOf(["john", "mike"]),
    };
    ```

  - 배열에 포함된 타입 중에서 하나를 만족

    ```js
    MyComponent.propTypes = {
      name: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    };
    ```

  - 특정 타입만 포함하는 배열

    ```js
    MyComponent.propTypes = {
      name: PropTypes.arrayOf(PropTypes.number),
    };
    ```

  - 객체의 속성값 타입을 정의

    ```js
    MyComponent.propTypes = {
      name: PropTypes.shape({
        color: PropTypes.string,
        weight: PropTypes.number,
      }),
    };
    ```

  - 객체에서 모든 속성값의 타입이 같은 경우

    ```js
    MyComponent.propTypes = {
      name: PropTypes.objectOf(PropTypes.number),
    };
    ```

  - 타입 정의 함수를 이용해 웬만한 타입 정보 표현 가능

    ```js
    MyComponent.propTypes = {
      age: function (props, propName, componentName) {
        const value = props[propName];

        if (value < 10 || value > 20) {
          return new Error(
            `Invalid prop ${propName} supplied to ${componentNode}.
            It must be 10 <= value <= 20.
            `
          );
        }
      },
    };
    ```

### 🔹 가독성을 높이는 조건부 렌더링 방법

- 조건부 렌더링 (conditional rendering): 컴포넌트 함수 내부에서 특정 값에 따라 선택적으로 렌더링하는 것
- 상황에 따라 삼항 연산자를 사용하는 것보다 `&&` 연산자를 사용한 조건부 렌더링이 가독성이 높음
- `&&` 연산자를 이용한 조건부 렌더링

  - 렌더링할 리액트 요소를 `&&` 연산자의 끝에 작성하고, 앞쪽에는 해당 조건을 작성하는 방식으로 조건부 렌더링 구현 가능

  ```js
  function Greeting({ isLogin, name, cash }) {
    return (
      <div>
        저희 사이트에 방문해 주셔서 감사합니다.
        {isLogin && (
          <div>
            <p>{name}님 안녕하세요.</p>
            <p>현재 보유하신 금액은 {cash}원입니다.</p>
          </div>
        )}
      </div>
    );
  }
  ```

#### ➕ 참고) `&&` 연산자, `||` 연산자

- `&&` 연산자: 첫 거짓 (false) 값 또는 마지막 값을 반환
- `||` 연산자: 첫 참 (true) 값 또는 마지막 값을 반환

#### ➕ 참고) `&&` 연산자 사용 시 주의할 점

- `null`, `undefined`뿐만 아니라 `0`, `''` (empty string)도 falsy value임

  - 의도적으로 `0`을 거짓으로 처리하고 싶다면 앞에 `!!`을 입력하면 됨
  - 또는 명확하게 `undefined`, `null`이 아닌 경우라고 표현해야 함

  ```js
  // && 연산자를 잘못 사용한 예
  <div>
    {cash && <p>{cash}원 보유 중</p>}
    {memo && <p>{200 - memo.length}자 입력 가능</p>}
  </div>
  ```

  ```js
  // && 연산자를 잘 사용한 예
  <div>
    {!!cash && <p>{cash}원 보유 중</p>}
    {cash != null && <p>{cash}원 보유 중</p>}
  </div>
  ```

### 🔹 관심사 분리를 위한 프레젠테이션/컨테이너 컴포넌트 구분하기

> 참고) [Presentational 컴포넌트와 Container 컴포넌트](https://redux.vlpt.us/1-2-presentational-and-container-components.html)

- UI 처리, API 호출, DB 관리 등의 코드가 같은 곳에 있으면 복잡하기 때문에 이들을 서로 관심사가 다르다고 보고 분리해서 관리하는 것이 좋음
- 컴포넌트를 Presentational 컴포넌트와 Container 컴포넌트로 구분하고 폴더도 이에 따라 별도로 관리하는 것이 좋음
- Presentational 컴포넌트의 특징
  - 비즈니스 로직이 없음
  - 상탯값이 없음 (UI 효과를 위한 상탯값은 제외)
