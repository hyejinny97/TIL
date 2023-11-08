# ✔ 리덕스 사가를 이용한 비동기 액션 처리

- 비동기 액션을 위해 사용되는 패키지들

  | 패키지명           | 선택 기준                                                                       | 특징                                                                  |
  | ------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
  | `redux-thunk`      | - 여러 개의 비동기 코드가 중첩되지 않음 <br/>- 비동기 코드의 로직이 간단함<br/> | - 가장 간단하게 시작 가능                                             |
  | `redux-observable` | - 비동기 코드가 많이 사용됨                                                     | - RxJS 패키지를 기반으로 만들어짐<br/>- 따라서, 진입 장벽이 가장 높음 |
  | `redux-saga`       | - 비동기 코드가 많이 사용됨                                                     | - 제너레이터를 적극적으로 활용함<br/>- 테스트 코드 작성이 쉬움        |

- `redux-saga`는 ES6 제너레이터를 기반으로 만들어짐
- `redux-saga`에서는 모든 부수 효과가 JS 객체로 표현됨

  - 따라서, API 통신을 위한 설정을 하지 않고도 테스트 코드를 쉽게 작성할 수 있음

## ▶ 리덕스 사가 시작하기

- `redux-saga`를 이용해서 타임라인에 좋아요 기능을 추가해 보자

  - 좋아요 버튼을 누르면 서버로 이벤트가 전송되고, 클라이언트에서는 좋아요 숫자가 증가되도록 구현

### 🔹 리덕스 코드 리팩토링하기

- 기존 타임라인 리덕스 코드를 수정해보자

  ```js
  // timeline/index.js
  // ...

  // 액션 타입
  export const types = {
    REQUEST_LIKE: "timeline/REQUEST_LIKE",
    ADD_LIKE: "timeline/ADD_LIKE",
    SET_LOADING: "timeline/SET_LOADING",
  };

  // 액션 생성자 함수
  export const actions = {
    // ...
    requestLike: (timeline) => ({ type: types.REQUEST_LIKE, timeline }),
    addLike: (timelineId, value) => ({
      type: types.ADD_LIKE,
      timelineId,
      value,
    }),
    setLoading: (isLoading) => ({ type: types.SET_LOADING, isLoading }),
  };

  // 초기 상탯값
  const INITIAL_STATE = { isLoading: false };

  // 리듀서 함수
  const reducer = createReducer(INITIAL_STATE, {
    [types.ADD_LIKE]: (state, action) => {
      const timeline = state.timelines.find(
        (item) => item.id === action.timelineId
      );

      if (timeline) {
        timeline.likes += action.value;
      }
    },
    [types.SET_LOADING]: (state, action) =>
      (state.isLoading = action.isLoading),
  });

  // ...
  ```

### 🔹 리액트 컴포넌트에 좋아요 기능 추가하기

- TimelineList 컴포넌트를 수정해보자

  ```js
  function TimelineList({timelines, onLike}) {
    return (
      <ul>
        {timelines.map({id, desc, likes} => {
          return (
            <li key={id}>
              {desc}
              <button data-id={id} onClick={onLike}>{`좋아요(${likes})`}</button>
            </li>
          )
        })}
      </ul>
    )
  }
  ```

- TimelineMain 컴포넌트를 수정해보자

  ```js
  function TimelineMain() {
    const dispatch = useDispatch();
    const timelines = useSelector((state) => state.timeline.timelines);
    const isLoading = useSelector((state) => state.timeline.isLoading);

    function onLike(e) {
      const id = e.target.dataset.id;
      const timeline = timelines.find((item) => item.id === id);
      dispatch(actions.requestLike(timeline));
    }

    return (
      <div>
        <TimelineList timelines={timelines} onLike={onLike} />
        {!!isLoading && <p>전송 중...</p>}
      </div>
    );
  }
  ```

### 🔹 좋아요 이벤트를 처리하는 사가 함수 작성하기

- `redux-saga`에서는 API 통신하기, 리덕스 액션 발생시키기 등의 부수 효과를 허용함

  - `redux-saga`에서 제공하는 `call`, `put`, `take` 등의 '부수 효과 함수'를 사용해서 처리 가능
  - 사가 함수: 부수 효과 함수를 이용해 하나의 완성된 로직을 담고 있는 함수

- 좋아요 이벤트를 처리하는 '사가 함수'를 작성해보자

  - 아래 fetchData 함수는 REQUEST_LIKE 액션을 처리하는 제너레이터 함수, 즉 사가 함수임
  - `take` 함수: 인수로 전달된 액션 타입을 기다리다가, 해당 액션이 발생하면 실행되어 액션 객체를 반환함
  - `put` 함수: 새로운 액션을 발생시킴 (= `store.dispatch` 메서드를 호출하는 효과)
  - `call` 함수: 입력된 함수를 대신 호출해 줌

    - 입력된 함수가 프로미스를 반환하면 settled 상태가 될 때까지 기다림
    - 서버로부터 응답이 올 때까지 기다림

  ```js
  // timeline/state/saga.js
  import { all, call, put, take, fork } from "redux-saga/effects";

  export function* fetchData(action) {
    while (true) {
      const { timeline } = yield take(types.REQUEST_LIKE);
      yield put(actions.setLoading(true));
      yield put(actions.addLike(timeline.id, 1));
      yield call(callApiLike);
      yield put(action.setLoading(false));
    }
  }
  ```

- 여러 개의 사가 함수를 모아, 나중에 사가 미들웨어에 입력되어야 함

  - 아래를 통해 사가 함수를 추가할 수 있음

  ```js
  yield all([fork(f1), fork(f2)])
  ```

  ```js
  export default function* watcher() {
    yield all([fork(fetchData)]);
  }
  ```

### 🔹 리덕스에 사가 미들웨어 추가하기

- 기존 store를 수정해보자

  ```js
  import createSagaMiddleware from "redux-saga";
  import timelineSaga from "../timeline/state/saga";
  // ...

  const sagaMiddleware = createSagaMiddleware();
  const store = createStore(reducer, applyMiddleware(sagaMiddleware));

  sagaMiddleware.run(timelineSaga);
  ```

#### ➕ 참고) 리덕스 사가의 부수 효과 함수

- `take`, `put`, `call` 등 부수 효과 함수는 JS 객체를 반환함

  ```js
  const a = take(types.REQUEST_LIKE);
  const b = put(actions.setLoading(true));
  const c = call(callApiLike);

  console.log({ a, b, c });
  /*
  a = {
    TAKE: {
      pattern: 'timeline/REQUEST_LIKE',
    }
  }
  
  b = {
    PUT: {
      channel: null,
      action: {
        type: 'timeline/SET_LOADING',
        isLoading: true,
      }
    }
  }
  
  c = {
    CALL: {
      context: null,
      fn: callApiLike,
      args: [],
    }
  }
  */
  ```

- 이렇게 반환된 객체는 사가 미들웨어에 전달됨
- 사가 미들웨어는 부수 효과 객체가 설명하는 일을 하고, 그 결과와 함께 실행 흐름을 우리가 작성한 함수로 넘기게 됨

## ▶ 여러 개의 액션이 협업하는 사가 함수

- 두 개 이상의 액션을 조합해서 하나의 완성된 사가 함수를 작성할 수 있음

  ```js
  function* loginFlow() {
    while (true) {
      const { id, password } = yield take(types.LOGIN);
      const userInfo = yield call(callApiLogin, id, password);
      yield put(types.SET_USER_INFO, userInfo);

      yield take(types.LOGOUT);
      yield call(callApiLogout, id);
      yield put(types.SET_USER_INFO, null);
    }
  }
  ```

## ▶ 사가 함수의 예외 처리

- 타임라인 코드에 예외 처리 기능을 추가해보자

### 🔹 리액트 컴포넌트에 에러 정보 추가하기

- 예외 발생 시 사용자가 에러 정보를 확인할 수 있게 하자

  ```js
  function TimelineMain() {
    // ...
    const error = useSelector((state) => state.timeline.error);
    // ...

    return (
      <div>
        // ...
        {!!error && <p>에러 발생: {error}</p>}
      </div>
    );
  }
  ```

### 🔹 리덕스 코드 리팩토링하기

- 에러 정보를 리덕스에 저장해보자

  ```js
  // timeline/index.js
  // ...

  // 액션 타입
  export const types = {
    // ...
    SET_ERROR: "timeline/SET_ERROR",
  };

  // 액션 생성자 함수
  export const actions = {
    // ...
    setError: (error) => ({ type: SET_ERROR, error }),
  };

  // 초기 상탯값
  const INITIAL_STATE = { isLoading: false, error: "" };

  // 리듀서 함수
  const reducer = createReducer(INITIAL_STATE, {
    // ...
    [types.SET_ERROR]: (state, action) => (state.error = action.error),
  });

  // ...
  ```

### 🔹 사가 함수에 에러 처리 코드 작성하기

- try ~ catch 문을 사용해 사가 함수에 에러 처리 코드를 작성해보자

  ```js
  // timeline/state/saga.js
  import { all, call, put, take, fork } from "redux-saga/effects";

  export function* fetchData(action) {
    while (true) {
      const { timeline } = yield take(types.REQUEST_LIKE);
      yield put(actions.setLoading(true));
      yield put(actions.addLike(timeline.id, 1));

      yield put(actions.setError(""));
      try {
        yield call(callApiLike);
      } catch (error) {
        yield put(actions.setError(error));
        yield put(actions.addLike(timeline.id, -1));
      }
      yield put(action.setLoading(false));
    }
  }
  ```

## ▶ 리덕스 사가로 디바운스 구현하기

- 디바운스 (debounce): 짧은 기간에 같은 이벤트가 반복해서 발생되어 같은 함수가 연속해서 호출될 때 첫 번째 또는 마지막 호출만 실행하는 기능
- 연속해서 문자열을 입력하다가 일정 시간 동안 입력이 없을 때 리덕스의 상탯값을 변경하는 기능을 구현해 보자

### 🔹 리덕스 코드 수정하기

- 기존 타임라인 리덕스 코드를 수정해보자

  ```js
  // timeline/index.js
  // ...

  // 액션 타입
  export const types = {
    // ...
    SET_TEXT: "timeline/SET_TEXT",
    TRY_SET_TEXT: "timeline/TRY_SET_TEXT",
  };

  // 액션 생성자 함수
  export const actions = {
    // ...
    setText: (text) => ({ type: types.SET_TEXT, text }),
    trySetText: (text) => ({ type: types.TRY_SET_TEXT, text }),
  };

  // 초기 상탯값
  const INITIAL_STATE = { isLoading: false, error: "", text: "" };

  // 리듀서 함수
  const reducer = createReducer(INITIAL_STATE, {
    [types.SET_TEXT]: (state, action) => (state.text = action.text),
  });

  // ...
  ```

### 🔹 리액트 컴포넌트 수정하기

- 문자열 입력창 기능을 추가하자

  ```js
  function TimelineMain() {
    // ...
    const text = useSelector((state) => state.timeline.text);
    const [currentText, setCurrentText] = useState("");

    function onChangeText(e) {
      const text = e.target.value;
      dispatch(actions.trySetText(text));
      setCurrentText(text);
    }
    // ...

    return (
      <div>
        // ...
        <input type="text" value={currentText} onChange={onChangeText} />
        {!!text && <p>{text}</p>}
      </div>
    );
  }
  ```

### 🔹 사가 함수 작성 및 수정하기

- debounce 부수 효과 함수를 사용하는 코드를 추가해보자

  - 아래에서는, TRY_SET_TEXT 액션이 발생하고 0.5초동안 재발생하지 않으면 trySetText 사가 함수가 실행되게 됨

  ```js
  import { debounce } from "redux-saga/effects";

  // ...
  export function* trySetText(action) {
    const { text } = action;
    yield put(actions.setText(text));
  }

  export default function* watcher() {
    yield all([fork(fetchData), debounce(500, types.TRY_SET_TEXT, trySetText)]);
  }
  ```

## ▶ 사가 함수 테스트하기

- 일반적으로 API 통신과 같은 비동기 코드를 테스트하려면 mock 객체를 생성해야 함
- 하지만, `redux-saga`에서는 mock 객체가 필요 없음

  - ∵ 부수 효과 함수를 호출한 결과가 JS 객체이기 때문

- `redux-saga`는 테스트 코드 작성을 지원하기 위해 아래의 패키지를 제공함

  ```bash
  $ npm install @redux-saga/testing-utils
  ```

- `saga.test.js` 파일을 만들고, 예외가 발생하는 경우와 발생하지 않는 경우를 각각 테스트해 보자

  - `cloneableGenerator` 함수를 이용하면 '복사가 가능한 제너레이터 객체'를 만들 수 있음

  ```js
  import { call, put, take } from "redux-saga/effects";
  import { cloneableGenerator } from "@redux-saga/testing-utils";

  describe("fetchData", () => {
    // 테스트에 사용될 데이터
    const timeline = { id: 1 };
    const action = actions.requestLike(timeline);

    // 복사가 가능한 제너레이터 객체
    const gen = cloneableGenerator(fetchData)();

    // 순차적으로 테스트
    expect(gen.next().value).toEqual(take(types.REQUEST_LIKE));
    expect(get.next(action).value).toEqual(put(actions.setLoading(true)));
    expect(gen.next().value).toEqual(put(actions.addLike(timeline.id, 1)));
    expect(gen.next(action).value).toEqual(put(actions.setError("")));
    expect(gen.next().value).toEqual(call(callApiLike));

    // API 통신 성공/실패 테스트
    it("on fail callApiLike", () => {
      const gen2 = gen.clone();
      const errorMsg = "error";
      expect(gen2.throw(errorMsg).value).toEqual(
        put(actions.setError(errorMsg))
      );
      expect(gen2.next().value).toEqual(put(actions.addLike(timeline.id, -1)));
    });

    it("on success callApiLike", () => {
      const gen2 = gen.clone();
      expect(gen2.next(Promise.resolve()).value).toEqual(
        put(actions.setLoading(false))
      );
      expect(gen2.next().value).toEqual(take(types.REQUEST_LIKE));
    });
  });
  ```
