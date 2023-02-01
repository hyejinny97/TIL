# ✔ React 기초



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
    const domNode = document.getElementById('modal');
    return ReactDOM.createPortal(
        <p>안녕하세요</p>, 
        domNode
      );
   }
   ```

8. 조건부 렌더링
   
   ```js
   function MyComponent({ title }) {
      return title.length > 0 && <p>{title}</p>
   }
   ```
   
   - title 속성값의 길이가 0 이면, false를 반환해서 아무것도 렌더링되지 않음
   - title 속성값의 길이가 1 이상이면, p요소가 반환됨




## ▶ 리액트 요소와 가상 돔

- 리액트 요소(element)는 리액트가 UI를 표현하는 수단
- 리액트는 렌더링 성능을 위해 가상 돔을 활용
  - 이전 가상 돔과 이후 가상 돔을 비교해서 변경된 부분만 실제 돔에 반영함

### 🔹 리액트 요소

- JSX 문법으로 작성된 코드 → createElement() 함수로 변경 → 리액트 요소를 반환
- 코드 예시
  
  ```js
  // JSX 코드
  const element = <a key="key1" href="http://google.com" style={{ width: 100 }}>click here</a>;
  ```

  ```js
  // createElement()
  const element = React.createElement('a', { 
      key: "key1", 
      href: 'http://google.com', 
      style: { 
        width: 100,
      }
    }, 'click here');
  ```

  ```js
  // 리액트 요소 
  const element = {
    type: 'a',
    key: 'key1',
    ref: null,
    props: {
      href: 'http://google.com',
      style: { 
        width: 100,
      },
      children: 'click here',
    },
    // 생략
  };
  ```

  - type 속성값
    - 문자열인 경우, HTML 태그를 의미함
    - 함수인 경우, 컴포넌트를 의미함
  - JSX 코드에서 `key`나 `ref` 속성값은 그대로 리액트 요소에서 `key`나 `ref` 속성값으로 들어감
  - JSX 코드에서 `key`, `ref`를 제외한 속성값은 리액트 요소에서 `props` 속성값으로 들어감

- JSX 코드에서 표현식이 들어가면, 리액트 요소에서는 표현식이 여러 개로 분할되어서 들어감
  
  ```js
  // JSX 코드
  const element = <h1>제 나이는 {20 + 5} 세입니다.</h1>;
  ```

  ```js
  // 리액트 요소 
  const element = {
    type: 'h1',
    props: {
      children: ['제 나이는 ', 25, '세입니다.'],
    },
    // 생략
  };
  ```

- 리액트 요소는 불변 객체이기 때문에 속성값을 변경할 수 없음
  
  ```js
  const element = <a href="http://google.com">click here</a>;
  element.type = 'h1';   // 에러 발생
  ```

- 리액트는 전달된 리액트 요소를 이전의 리액트 요소와 비교해서 변경된 부분만 실제 돔에 반영함

### 🔹 리액트 요소가 돔 요소로 만들어지는 과정

> 실습: [실제 돔으로 만드는 과정을 보여줄 예제 코드](https://codesandbox.io/s/3-17-silje-domeuro-mandeuneun-gwajeongeul-boyeo-jul-yeje-kodeu-silseub-9lnyxc?file=/src/App.js)

- 하나의 화면을 표현하기 위해 여러 개의 리액트 요소가 트리 구조로 구성되고, 이러한 리액트 요소 트리를 가상 돔이라고 함
- 리액트는 렌더링할 때마다 가상 돔을 만들고, 이전의 가상 돔과 현재의 가상 돔을 비교해서 변경된 부분만 실제 돔을 반영함
- 리액트에서 UI 데이터 변경에 의한 화면 업데이트는 1) 렌더 단계(render phase), 2) 커밋 단계(commit phase)를 거침
  - 렌더: 실제 돔에 반영할 변경 사항을 파악하는 단계
  - 커밋: 파악된 변경 사항을 실제 돔에 반영하는 단계
- 렌더 단계는 아래의 두 함수에 의해 시작됨
  - ReactDOM.render() 함수
  - 상태값 변경 함수

  ```js
  // App.js
  import React, { useState } from "react";

  function App() {
    return (
      <Todo
        title="리액트 공부하기"
        desc="실전 리액트 프로그래밍을 열심히 읽는다"
      />
    );
  }

  function Todo({ title, desc }) {
    const [priority, setPriority] = useState("high");
    const onClick = function () {
      setPriority(priority === "high" ? "low" : "high");
    };

    return (
      <div>
        <Title title={title}></Title>
        <p>{desc}</p>
        <p>{priority === "high" ? "우선순위 높음" : "우선순위 낮음"}</p>
        <button onClick={onClick}>우선순위 변경</button>
      </div>
    );
  }

  function Title({ title }) {
    return <p style={{ color: "blue" }}>{title}</p>;
  }

  React.memo(Title);

  export default App;
  ```

  - '우선순위 변경' 버튼을 누르면 `<p>우선순위 높음</p>` 부분만 변경됨
  - 따라서, 실제 돔에서도 해당 p 태그의 문자열만 수정됨