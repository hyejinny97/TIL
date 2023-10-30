# ✔ 리덕스의 주요 개념 이해하기

- 리덕스에서 상탯값이 변경되는 과정

  - 아래에소 뷰는 리액트의 컴포넌트라고 할 수 있음

  ```plaintext
  액션 → 미들웨어 → 리듀서 → 스토어
    ↑___________뷰____________↲
  ```

## ▶ 액션 (Action)

- 액션(Action)은 `type` 속성값을 가진 자바스크립트 객체임
- 액션 객체를 `dispatch` 메서드에 넣어서 호출하면 리덕스는 상탯값을 변경하게 됨

  - 각 액션은 고유한 `type` 속성값을 사용해야 함
  - `type` 이름의 충돌을 피하기 위해, 접두사를 붙이는 방법이 많이 사용됨

  ```js
  store.dispatch({ type: "todo/ADD", title: "영화 보기", priority: "high" });
  ```

- 액션에서 특정 속성값이 항상 존재하도록 강제하기 위해 '액션 생성자 함수'를 사용할 수 있음

  - 액션 생성자 함수를 필요한 인수와 함께 호출하면 항상 같은 구조의 액션 객체가 만들어짐

  ```js
  function addTodo({ title, priority }) {
    return { type: "todo/ADD", title, priority };
  }

  store.dispatch(addTodo({ title: "영화 보기", priority: "high" }));
  ```

- `type` 속성값은 상수 변수로 만드는 게 좋음

  - ∵ 리듀서에서 액션 객체를 구분할 때도 사용되기 때문

  ```js
  const ADD = "todo/ADD";

  function addTodo({ title, priority }) {
    return { type: ADD, title, priority };
  }
  ```

- 액션 생성자 함수에서는 API 호출 들 부수 효과를 발생시켜도 괜찮음

## ▶ 미들웨어 (Middleware)

- 미들웨어(Middleware)는 리듀서가 액션을 처리하기 전에 실행되는 함수임

  - 미들웨어를 설정하지 않았다면, 발생한 액션은 곧바로 리듀서로 보내짐

- 미들웨어 사용 목적

  - 예1) 디버깅 목적으로 상탯값 변경 시 로그 출력을 위해 사용
  - 예2) 리듀서에서 발생한 예외를 서버로 전송하기 위해 사용

- 미들웨어는 함수 세 개가 중첩된 구조임

  - 미들웨어는 스토어와 액션 객체를 기반으로 작업 수행
  - `next` 함수를 호출하면 다른 미들웨어 함수가 호출되면서 최종적으로 리듀서 함수가 호출됨

  ```js
  const myMiddleware = (store) => (next) => (action) => next(action);
  ```

- 미들웨어 설정 및 실행 순서

  - 실행 순서: middleware1 → middleware2 → store의 dispatch → reducer

  ```js
  import { createStore, applyMiddleware } from "redux";

  const middleware1 = (store) => (next) => (action) => {
    console.log("middleware1 start");
    const result = next(action);
    console.log("middleware1 end");
    return result;
  };

  const middleware2 = (store) => (next) => (action) => {
    console.log("middleware2 start");
    const result = next(action);
    console.log("middleware2 end");
    return result;
  };

  const myReducer = (state, action) => {
    console.log("reducer");
    return state;
  };

  const store = createStore(
    myReducer,
    applyMiddleware(middleware1, middleware2)
  );

  store.dispatch({ type: "someAction" });
  ```

  ```plaintext
  middleware1 start
  middleware2 start
  reducer
  middleware2 end
  middleware1 end
  ```

### 🔹 미들웨어 활용 예

- 액션이 발생할 때마다 이전 상탯값과 이후 상탯값을 로그로 출력해주는 미들웨어

  ```js
  const printLog = (store) => (next) => (action) => {
    console.log(`prev state = ${store.getState()}`);
    const result = next(action);
    console.log(`next state = ${store.getState()}`);
    return result;
  };
  ```

- 리듀서에서 예외가 발생하면 자동으로 서버에 에러 정보를 전송하는 미들웨어

  - 이때, 리듀서뿐만 아니라 하위의 미들웨어 코드에서 발생하는 예외도 `catch` 문으로 들어오게 됨

  ```js
  const reportCrash = (store) => (next) => (action) => {
    try {
      return next(action);
    } catch (err) {
      // 서버로 예외 정보 전송
    }
  };
  ```

- 원하는 경우 액션 처리를 일정 시간 동안 연기할 수 있는 미들웨어

  ```js
  const delayAction = (store) => (next) => (action) => {
    const delay = action.meta && action.meta.delay;
    if (!delay) {
      return next(action);
    }
    const timeoutId = setTimeout(() => next(action), delay);
    return function cancel() {
      clearTimeout(timeoutId);
    };
  };
  ```

  ```js
  const cancel = store.dispatch({
    type: "SomeAction",
    meta: { delay: 1000 },
  });
  // ...
  cancel();
  ```

- 특정 액션이 발생하면 로컬 스토리지에 값을 저장하는 미들웨어

  ```js
  const saveToLocalStorage = (store) => (next) => (action) => {
    if (action.type === "SET_NAME") {
      localStorage.setItem("name", action.name);
    }
    return next(action);
  };
  ```
