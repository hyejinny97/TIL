# ✔ 리덕스의 주요 개념 이해하기

- 리덕스에서 상탯값이 변경되는 과정

  - 아래에소 뷰는 리액트의 컴포넌트라고 할 수 있음
  - 스토어의 `dispatch` 메소드로 액션 발생 <br />
    → 미들웨어 함수 실행 <br />
    → 리듀서 실행으로 상탯값 변경 <br />
    → 스토어에 등록된 모든 이벤트 처리 함수가 실행됨

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

## ▶ 리듀서 (Reducer)

- 리듀서(Reducer)는 액션이 발생했을 때 새로운 상탯값을 만드는 함수임

  ```js
  (state, action) => nextState;
  ```

- 상탯값은 불변 객체로 관리해야 하므로, 리듀서 함수는 상탯값을 수정할 때마다 새로운 객체를 생성함

  - 문제점) 아래처럼 전개 연산자를 사용하더라도 수정하려는 값이 상탯값의 깊은 곳에 있다면 수정이 쉽지 않음
  - 해결책) 자바스크립트에서 불변 객체를 관리해주는 `immer` 패키지 사용

  ```js
  function reducer(state = INITIAL_STATE, action) {
    switch (action.type) {
      case ADD:
        return {
          ...state,
          todos: [
            ...state.todos,
            { id: getNewId(), title: action.title, priority: action.priority },
          ],
        };
      case REMOVE_ALL:
        return {
          ...state,
          todos: [],
        };
      default:
        return state;
    }
  }
  ```

### 🔹 `immer`를 사용해 리듀서 작성하기

- `immer` 패키지에서의 `produce` 함수

  - 매개변수
    - 첫 번째: 변경하고자 하는 객체
    - 두 번째: 첫 번째 매개변수로 입력된 객체를 수정하는 함수
  - 반환값
    - 새로운 객체를 반환

  ```js
  import produce from "immer";

  const person = { name: "mike", age: 23 };
  const newPerson = produce(person, (draft) => (draft.age = 23));
  ```

- `immer`를 사용해 리듀서 함수 작성

  - `immer`를 사용했기 때문에, 배열의 push 메서드를 사용해도 기존 상탯값은 직접 수정되지 않고 새로운 객체가 생성됨

  ```js
  function reducer(state = INITIAL_STATE, action) {
    return produce(state, (draft) => {
      switch (action.type) {
        case ADD:
          draft.todos.push(action.todo);
          break;
        case REMOVE_ALL:
          draft.todos = [];
          break;
        default:
          break;
      }
    });
  }
  ```

### 🔹 리듀서 작성 시 주의할 점 - 데이터 참조

- 리덕스의 상탯값은 불변 객체이기 때문에 언제든지 객체의 참조값이 변경될 수 있음

  - 따라서, 객체를 참조할 때는 객체의 참조값이 아니라 고유한 ID 값을 이용하는 것이 좋음

  ```js
  // 잘못된 예
  function reducer(state = INITIAL_STATE, action) {
    return produce(state, (draft) => {
      switch (action.type) {
        case SET_SELECTED_PERSON: // 특정 사람을 참조
          draft.selectedPerson = draft.peopleList.find(
            (item) => item.id === action.id
          );
          break;
        // ...
      }
    });
  }
  ```

  ```js
  // 올바른 예
  function reducer(state = INITIAL_STATE, action) {
    return produce(state, (draft) => {
      switch (action.type) {
        case SET_SELECTED_PERSON: // 특정 사람의 고유한 ID 값을 참조
          draft.selectedPerson = action.id;
          break;
        // ...
      }
    });
  }
  ```

### 🔹 리듀서 작성 시 주의할 점 - 순수 함수

- 리듀서 함수는 순수 함수이어야 함

  - 같은 인수로 호출하면 같은 값을 반환해야 함
  - API 호출과 같은 부수 효과가 발생해서는 안됨

  ```js
  // 잘못된 예
  function reducer(state = INITIAL_STATE, action) {
    return produce(state, (draft) => {
      switch (action.type) {
        // 랜덤 함수에 의해 같은 인수지만 다른 값 반환
        case SAY_HELLO:
          const random = Math.floor(Math.random() * 10 + 1);
          draft.msg = `안녕하세요. ${action.name}님의 행운의 숫자는 ${random}입니다.`;
          break;
        // 부수 효과를 발생함
        case INCREMENT:
          callApi({ url: "./sendActionLog", data: action });
          draft.value += 1;
          break;
        // ...
      }
    });
  }
  ```

### 🔹 `createReducer` 함수로 리듀서 작성하기

- `createReducer` 함수를 이용하면 `switch` 문보다 더 간결하게 리듀서 함수를 작성할 수 있음

  - 매개변수
    - 첫 번째: 초기 상탯값
    - 두 번째: 액션 처리 함수를 담고 있는 객체
  - 반환값
    - 리듀서 함수를 반환

  ```js
  const reducer = createReducer(INITIAL_STATE, {
    [ADD]: (state, action) => state.todos.push(action.todo),
    [REMOVE_ALL]: (state) => (state.todos = []),
  });
  ```

- `createReducer` 함수의 내부 코드

  ```js
  function createReducer(initialState, handlerMap) {
    return function (state = initialState, action) {
      return produce(state, (draft) => {
        const handler = handlerMap[action.type];
        if (handler) {
          handler(draft, action);
        }
      });
    };
  }
  ```

## ▶ 스토어 (Store)

- 스토어(store)는 리덕스의 상탯갑을 가지는 객체임
- 외부에서 상탯값 변경 여부를 알기 위해서는 스토어에 이벤트 처리 함수를 등록하면 됨

  - `subscribe` 메서드를 이용해서 이벤트 처리 함수를 등록할 수 있음
  - 스토어에 등록된 이벤트 처리 함수는 액션이 처리될 때마다 호출됨

  ```js
  const reducer = createReducer(INITIAL_STATE, {
    [INCREMENT]: (state) => (state.value += 1),
  });

  const store = createStore(reducer);

  let pevState;
  store.subscribe(() => {
    const state = store.getState();
    if (state === prevState) {
      console.log("상탯값이 같음");
    } else {
      console.log("상탯값이 변경됨");
    }
    prevState = state;
  });

  store.dispatch({ type: INCREMENT });
  ```
