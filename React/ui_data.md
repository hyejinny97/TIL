## ▶ 상태값과 속성값으로 관리하는 UI 데이터

- 리액트는 UI 데이터가 변경되면 화면을 자동으로 갱신해 주는 역할을 함
- UI 데이터는 상태값과 속성값으로 관리해야 함
  - 상태값: 컴포넌트 내부에서 관리되는 데이터
  - 속성값: 부모 컴포넌트로부터 전달받는 데이터
- 만약, UI 데이터가 상태값과 속성값으로 관리되지 않으면 UI 데이터가 변경돼도 화면이 갱신되지 않을 수 있음

### 🔹 컴포넌트의 상태값 (state)

> 실습: [컴포넌트의 상태값을 사용하는 코드](https://codesandbox.io/s/3-1-2-keomponeonteuyi-sogseonggabsgwa-sangtaegabs-silseub-x8j99f)

- 컴포넌트의 상태값을 추가할 때 `useState` 훅을 이용

  - argument: 초깃값
  - 반환값: `[상태값, 상태값 변경 함수]` 배열

- 코드 예시

  ```js
  // App.js
  import { useState } from "react";

  export default function App() {
    const [color, setColor] = useState("red");
    const onClick = function () {
      setColor("blue");
    };

    return (
      <button style={{ backgroundColor: color }} onClick={onClick}>
        좋아요
      </button>
    );
  }
  ```

  - setColor 함수가 호출되면 상태값을 변경하고, 해당 컴포넌트를 다시 렌더링함

- 같은 컴포넌트를 여러 번 사용 가능한데, 이때 각 컴포넌트는 상태값을 위한 자신만의 메모리 공간이 있어서 상태값이 따로 관리됨
- 상태값은 불변 변수가 아니므로 직접 수정이 가능

  - 하지만, 다음과 같은 경우는 상태값을 수정해도 화면이 갱신되지 않음
  - 리액트는 상태값 변경 유무를 이전 참조값과의 비교로 판단하는데, count 객체의 참조값은 그대로이므로 변경 사항이 없다고 판단했기 때문임
  - 따라서, 상태값을 불변 변수로 관리하는 것이 좋음

  ```js
  function MyComponent() {
    const [count, setCount] = useState({ value: 0 });
    function onClick() {
      count.value = 2;
      setCount(count);
    }
    // 생략
  }
  ```

### 🔹 컴포넌트의 속성값 (props)

> 실습: [속성값을 이용한 코드](https://codesandbox.io/s/3-5-6-sogseonggabseul-iyonghan-kodeu-silseub-4bz8ii?file=/src/Todo.js)

- 코드 예시

  ```js
  // Todo.js
  import { useState } from "react";
  import Title from "./Title";

  export default function Todo() {
    const [count, setCount] = useState(0);
    const onClick = function () {
      setCount(count + 1);
    };

    return (
      <div>
        <Title count={`현재 카운트: ${count}`}></Title>
        <button onClick={onClick}>증가</button>
      </div>
    );
  }
  ```

  ```js
  // Title.js
  export default function Title(props) {
    return <h1>{props.count}</h1>;
  }
  ```

  - Title 컴포넌트는 Todo 컴포넌트로부터 count라는 속성값을 받음
  - 부모 컴포넌트인 Todo가 렌더링될 때마다, Title 컴포넌트가 같이 렌더링되고 title 속성값의 변경 사항이 바로 화면에 반영됨

- `React.memo()` 함수를 사용하면, 부모 컴포넌트가 렌더링될 때마다 자식 컴포넌트가 같이 렌더링되지 않고 속성값이 변경될 때만 렌더링됨

  ```js
  // Title.js
  function Title(props) {
    return <h1>{props.count}</h1>;
  }

  export default React.memo(Title);
  ```

- 속성값은 불변(Immutable) 변수이기 때문에, 값을 변경하려고 시도하면 에러가 발생함

### 🔹 컴포넌트 함수의 반환값

1. 컴포넌트, HTML에 정의된 거의 모든 태그

   ```js
   return <MyComponent title="안녕하세요" />;
   ```

   ```js
   return <p>안녕하세요</p>;
   ```

2. 문자열, 숫자

   ```js
   return "안녕하세요";
   ```

   ```js
   return 124;
   ```

3. 배열

   - 단, 이떄 각 리액트 요소는 `key` 속성값을 가지고 있어야 함

   ```js
   return [<p key="a">안녕하세요</p>, <p key="b">반갑습니다</p>];
   ```

4. React Fragment

   - React Fragment를 사용하면 배열을 사용하지 않고도 여러 개의 요소를 표현할 수 있음
   - 이떄 각 리액트 요소에는 `key` 속성값을 부여하지 않아도 됨

   ```js
   return (
     <React.Fragment>
       <p>안녕하세요</p>
       <p>반갑습니다</p>
     </React.Fragment>
   );
   ```

5. React Fragment의 축약 형태

   - 바벨을 이용하면 React Fragment를 축약해서 작성 가능

   ```js
   return (
     <>
       <p>안녕하세요</p>
       <p>반갑습니다</p>
     </>
   );
   ```

6. null, boolean

   - null이나 boolean을 반환하면 아무것도 렌더링되지 않음

   ```js
   return null;
   ```

   ```js
   return false;
   ```

7. React Portal

   - React Portal을 사용하면 컴포넌트의 현재 위치와는 상관없이 특정 돔 요소에 렌더링 가능

   ```js
   return ReactDOM.createPortal(<p>안녕하세요</p>, domNode);
   ```

   ```js
   function Modal() {
     const domNode = document.getElementById("modal");
     return ReactDOM.createPortal(<p>안녕하세요</p>, domNode);
   }
   ```

8. 조건부 렌더링

   ```js
   function MyComponent({ title }) {
     return title.length > 0 && <p>{title}</p>;
   }
   ```

   - title 속성값의 길이가 0 이면, false를 반환해서 아무것도 렌더링되지 않음
   - title 속성값의 길이가 1 이상이면, p요소가 반환됨
