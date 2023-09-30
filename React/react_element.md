## ▶ 리액트 요소와 가상 돔

- 리액트 요소(element)는 리액트가 UI를 표현하는 수단
- 리액트는 렌더링 성능을 위해 가상 돔을 활용
  - 이전 가상 돔과 이후 가상 돔을 비교해서 변경된 부분만 실제 돔에 반영함

### 🔹 리액트 요소

- JSX 문법으로 작성된 코드 → createElement() 함수로 변경 → 리액트 요소를 반환
- 코드 예시

  ```js
  // JSX 코드
  const element = (
    <a key="key1" href="http://google.com" style={{ width: 100 }}>
      click here
    </a>
  );
  ```

  ```js
  // createElement()
  const element = React.createElement(
    "a",
    {
      key: "key1",
      href: "http://google.com",
      style: {
        width: 100,
      },
    },
    "click here"
  );
  ```

  ```js
  // 리액트 요소
  const element = {
    type: "a",
    key: "key1",
    ref: null,
    props: {
      href: "http://google.com",
      style: {
        width: 100,
      },
      children: "click here",
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
    type: "h1",
    props: {
      children: ["제 나이는 ", 25, "세입니다."],
    },
    // 생략
  };
  ```

- 리액트 요소는 불변 객체이기 때문에 속성값을 변경할 수 없음

  ```js
  const element = <a href="http://google.com">click here</a>;
  element.type = "h1"; // 에러 발생
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
