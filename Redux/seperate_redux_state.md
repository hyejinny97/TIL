# ✔ 데이터 종류별로 상탯값 나누기

- 리덕스에서 제공하는 `combineReducer` 함수를 이용하면 리듀서 함수를 여러 개로 분리할 수 있음

## ▶ 상탯값 나누기 예제를 위한 사전 작업

- 페이스북의 타임라인과 친구 목록을 구현해 보자

### 🔹 `createReducer` 함수 구현

- 일단, `createReducer` 함수를 구현해서 차후 이를 통해 리듀서 함수를 만들자

  ```js
  // common/createReducer.js
  import produce from "immer";

  export default function createReducer(initialState, handlerMap) {
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

### 🔹 친구 목록을 위한 리덕스 코드 작성하기

- 친구 목록 데이터를 배열로 관리하고, 추가/삭제/수정 액션을 만들자

  ```js
  // friend/state.js
  // 액션
  const ADD = "friend/ADD";
  const REMOVE = "friend/REMOVE";
  const EDIT = "friend/EDIT";

  // 액션 생성자 함수
  export const addFriend = (friend) => ({ type: ADD, friend });
  export const removeFriend = (friend) => ({ type: REMOVE, friend });
  export const editFriend = (friend) => ({ type: EDIT, friend });

  // 초기 상탯값
  const INITIAL_STATE = { friends: [] };

  // 리듀서 함수
  export default const reducer = createReducer(INITIAL_STATE, {
    [ADD]: (state, action) => state.friends.push(action.friend),
    [REMOVE]: (state, action) =>
      (state.friends = state.friends.filter(
        (friend) => friend.id !== action.friend.id
      )),
    [EDIT]: (state, action) => {
      const idx = state.friend.findIndex(
        (friend) => friend.id === action.friend.id
      );
      if (idx >= 0) {
        state.friends[idx] = action.friend;
      }
    },
  });
  ```

### 🔹 타임라인을 위한 리덕스 코드 작성하기

- 게시물 데이터를 배열로 관리하고, 추가/삭제/수정과 다음 페이지 이동 액션을 만들자

  ```js
  // timeline/state.js
  // 액션
  const ADD = "timeline/ADD";
  const REMOVE = "timeline/REMOVE";
  const EDIT = "timeline/EDIT";
  const INCREASE_NEXT_PAGE = 'timeline/INCREASE_NEXT_PAGE'

  // 액션 생성자 함수
  export const addTimeline = (timeline) => ({ type: ADD, timeline });
  export const removeTimeline = (timeline) => ({ type: REMOVE, timeline });
  export const editTimeline = (timeline) => ({ type: EDIT, timeline });
  export const increaseNextPage = () => ({ type: INCREASE_NEXT_PAGE });

  // 초기 상탯값
  const INITIAL_STATE = { timelines: [], nextPage: 0 };

  // 리듀서 함수
  export default const reducer = createReducer(INITIAL_STATE, {
    [ADD]: (state, action) => state.timelines.push(action.timeline),
    [REMOVE]: (state, action) =>
      (state.timelines = state.timelines.filter(
        (timeline) => timeline.id !== action.timeline.id
      )),
    [EDIT]: (state, action) => {
      const idx = state.timeline.findIndex(
        (timeline) => timeline.id === action.timeline.id
      );
      if (idx >= 0) {
        state.timelines[idx] = action.timeline;
      }
    },
    [INCREASE_NEXT_PAGE]: (state, action) => (state.nextPage += 1)
  });
  ```

### 🔹 여러 리듀서를 하나로 합치기

- 리덕스에서 제공하는 `combineReducers` 함수를 이용하면 여러 개의 리듀서를 하나로 합칠 수 있음

  - 즉, `combineReducers` 함수를 이용하면 리듀서별로 상탯값을 관리할 수 있음

  ```js
  // index.js
  import { createStore, combineReducers } from "redux";

  const reducer = combineReducers({
    timeline: timelineReducer,
    friend: friendReducer,
  });

  const store = createStore(reducer);

  store.dispatch(addTimeline({ id: 1, desc: "코딩은 즐거워" }));
  ```

#### ➕ 참고) 덕스(ducks) 패턴

- 리덕스 공식 문서에서는 액션 타입, 액션 생성자 함수, 리듀서 함수를 각각의 파일로 만들어서 설명함

  - 하지만, 이 방법은 간단한 액션을 추가하려고 해도 세 개 이상의 파일을 열어서 수정해야한다는 수고스러움이 있음
  - 대신, 덕스 패턴으로 리덕스 코드를 작성하는 것이 효율적임

- 덕스 패턴 특징

  - 1️⃣ 연관된 액션 타입, 액션 생성자 함수, 리듀서 함수를 하나의 파일로 작성함
  - 2️⃣ 리듀서 함수는 export default 키워드로 내보냄
  - 3️⃣ 액션 생성자 함수는 export 키워드로 내보냄
  - 4️⃣ 액션 타입은 접두사와 액션 이름을 조합해서 만듦

- 덕스 패턴에 의해 특정 파일의 코드가 많아지면, 굳이 하나의 파일을 고집할 필요 없이 리듀서 코드롸 액션 코드를 별도의 파일로 분리하는 것이 좋음

## ▶ 리듀서에서 공통 기능 분리하기

- 위 친구 목록 코드와 타임 라인 코드에는 서로 중복된 코드가 많음

  - 액션 타입, 액션 생성자 함수
  - 초기 상탯값
  - 리듀서 함수

### 🔹 중복 코드를 함수화하기

- 위 친구 목록 코드와 타임 라인 코드에서 중복되는 코드를 별도의 파일로 분리해보자

  - 입력 받은 이름을 이용해서 액션, 액션 생성자 함수, 리듀서를 만듦
  - 액션 생성자 함수와 리듀서를 반환함

  ```js
  // common/createItemsLogic.js
  export default function createItemsLogic(name) {
    // 액션
    const ADD = `${name}/ADD`;
    const REMOVE = `${name}/REMOVE`;
    const EDIT = `${name}/EDIT`;

    // 액션 생성자 함수
    const add = (item) => ({ type: ADD, item });
    const remove = (item) => ({ type: REMOVE, item });
    const edit = (item) => ({ type: EDIT, item });

    // 초기 상탯값
    const INITIAL_STATE = { [name]: [] };

    // 리듀서 함수
    const reducer = createReducer(INITIAL_STATE, {
      [ADD]: (state, action) => state[name].push(action.item),
      [REMOVE]: (state, action) => {
        const idx = state.item.findIndex((item) => item.id === action.item.id);
        state[name].splice(idx, 1);
      },
      [EDIT]: (state, action) => {
        const idx = state.item.findIndex((item) => item.id === action.item.id);
        if (idx >= 0) {
          state[name][idx] = action.item;
        }
      },
    });

    return { add, remove, edit, reducer };
  }
  ```

#### ➕ 참고) 값에 의한 호출과 참조에 의한 호출

- `createItemsLogic` 함수에서 REMOVE 액션을 처리하는 코드는 filter 메서드를 이용하는 방법에서 splice 메서드를 이용하는 방법으로 변경됐음

  - ∵ 아래처럼, filter 메서드를 이용하면 순간적으로 매개변수의 값만 변경될 뿐, 원하는 대로 state 값이 변하지 않음

  ```js
  [REMOVE]: (state, action) =>
  (state.timelines = state.timelines.filter(
    (timeline) => timeline.id !== action.timeline.id
  )),
  ```

### 🔹 기존 코드 리팩토링하기

- 친구 목록 코드 리팩토링하기

  ```js
  // friend/state.js
  const { add, remove, edit, reducer } = createItemsLogic("friends");

  // 액션 생성자 함수
  export const addFriend = add;
  export const removeFriend = remove;
  export const editFriend = edit;

  // 리듀서 함수
  export default reducer;
  ```

- 타임라인 코드 리팩토링하기

  ```js
  // timeline/state.js
  const {
    add,
    remove,
    edit,
    reducer: timelinesReducer,
  } = createItemsLogic("timelines");

  const INCREASE_NEXT_PAGE = "timeline/INCREASE_NEXT_PAGE";

  // 액션 생성자 함수
  export const addTimeline = add;
  export const removeTimeline = remove;
  export const editTimeline = edit;
  export const increaseNextPage = () => ({ type: INCREASE_NEXT_PAGE });

  // 초기 상태값
  const INITIAL_STATE = { nextPage: 0 };

  // 리듀서 함수
  const reducer = createReducer(INITIAL_STATE, {
    [INCREASE_NEXT_PAGE]: (state, action) => (state.nextPage += 1),
  });
  const reducers = [reducer, timelineReducer];
  export default mergeReducers(reducers);
  ```

### 🔹 여러 리듀서를 합치는 `mergeReducers` 함수

- 리덕스에서 제공하는 `combineReducers` 함수를 이용하면 상탯값의 깊이가 불필요하게 깊어짐
- 따라서, 여러 개의 리듀서 함수를 입력받아 합쳐 하나의 리듀서를 반환하는 `mergeReducers` 함수를 만들어 사용하자

  - 초기 상탯값을 계산할 때는 모든 리듀서 함수의 결괏값을 합침
  - 초기화 단계가 아니라면, 입력된 모든 리듀서를 호출해 다음 상탯값을 반환함

  ```js
  // common/mergeReducers.js
  export default function mergeReducers(reducers) {
    return function (state, action) {
      if (!state) {
        return reducers.reduce(
          (acc, r) => ({ ...acc, ...r(state, action) }, {})
        );
      } else {
        let nextState = state;
        for (const r of reducers) {
          nextState = r(nextState, action);
        }
        return nextState;
      }
    };
  }
  ```
