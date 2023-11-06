# ✔ reselect 패키지로 선택자 함수 만들기

- reselect 패키지는 원본 데이터를 다양한 형태로 가공해서 사용할 수 있도록 도와줌
- 특히, 리덕스의 데이터를 리액트 컴포넌트에서 필요한 데이터로 가공하는 용도로 많이 사용됨

## ▶ reselect 패키지 없이 구현해보기

- 이전에 구현한 친구 목록에 연령 제한 옵션과 개수 제한 옵션을 설정할 수 있도록 추가해보자
- 옵션을 선택할 수 있는 기능을 가진 컴포넌트를 만들어 보자

  ```js
  function NumberSelect({ value, options, postfix, onChange }) {
    return (
      <div>
        <select
          onChange={(e) => {
            const value = e.currentTarget.value;
            onChange(value);
          }}
          value={value}
        >
          {options.map((option) => {
            return (
              <option key={option} value={option}>
                {option}
              </option>
            );
          })}
        </select>
        {postfix}
      </div>
    );
  }
  ```

### 🔹 친구 목록의 리덕스 코드 리팩터링하기

- 이전 친구 목록의 리덕스 코드 리팩터링해보자

  ```js
  // friend/state.js
  const {
    add,
    remove,
    edit,
    reducer: friendsReducer,
  } = createItemsLogic("friends");

  // 액션
  const SET_AGE_LIMIT = "friend/SET_AGE_LIMIT";
  const SET_SHOW_LIMIT = "friend/SET_SHOW_LIMIT";

  // 액션 생성자 함수
  // ...
  const setAgeLimit = (ageLimit) => ({ type: SET_AGE_LIMIT, ageLimit });
  const setShowLimit = (showLimit) => ({ type: SET_SHOW_LIMIT, showLimit });

  // 초기 상탯값
  const INITIAL_STATE = { ageLimit: MAX_AGE_LIMIT, showLimit: MAX_SHOW_LIMIT };

  // 리듀서 함수
  const reducer = createReducer(INITIAL_STATE, {
    [SET_AGE_LIMIT]: (state, action) => (state.ageLimit = action.ageLimit),
    [SET_SHOW_LIMIT]: (state, action) => (state.showLimit = action.showLimit),
  });

  // 두 리듀서 함수 합치기
  const reducers = [reducer, friendReducer];
  export default mergeReducers(reducers);
  ```

### 🔹 FriendMain 컴포넌트 리팩토링하기

- 이전 FriendMain 컴포넌트 리팩토링해보자

  ```js
  function FriendMain() {
    const [ageLimit, showLimit, friendsWithAgeLimit, friendsWithAgeShowLimit] =
      useSelector((state) => {
        const { friends, ageLimit, showLimit } = state.friend;
        const friendsWithAgeLimit = friends.filter(
          (friend) => friend.age <= ageLimit
        );

        return [
          ageLimit,
          showLimit,
          friendsWithAgeLimit,
          friendsWithAgeLimit.slice(0, showLimit),
        ];
      }, shallowEqual);

    // ...

    return (
      <div>
        <NumberSelect
          onChange={(v) => dispatch(setAgeLimit(v))}
          value={ageLimit}
          options={AGE_LIMIT_OPTIONS}
          postfix="세 이하만 보기"
        />
        <FriendList friends={friendsWithAgeLimit} />
        <NumberSelect
          onChange={(v) => dispatch(setShowLimit(v))}
          value={showLimit}
          options={SHOW_LIMIT_OPTIONS}
          postfix="명 이하만 보기"
        />
        <FriendList friends={friendsWithAgeShowLimit} />
      </div>
    );
  }

  const AGE_LIMIT_OPTIONS = [15, 20, 25, MAX_AGE_LIMIT];
  const SHOW_LIMIT_OPTIONS = [2, 4, 6, SHOW_AGE_LIMIT];
  ```

- 위 코드에서의 문제점: 리덕스의 액션이 처리될 때마다 새로운 목록을 만드는 연산이 수행됨

  - 친구 목록이 변경되지 않았을 때도 새로운 목록을 만드는 연산이 수행됨
  - 친구 목록의 크기가 크면 클수록 불필요한 연산도 증가함

## ▶ reselect 패키지 사용하기

- 아래 명령어를 통해 reselect 패키지 설치 가능함

  ```bash
  $ npm install reselect
  ```

- reselect 패키지를 사용해 선택자 함수를 작성할 수 있음

### 🔹 친구 목록 데이터의 선택자 함수 만들기

- reselect의 `createSelector`를 사용해 선택자 함수를 만들 수 있음

  - 매개변수
    - 첫 번째: 두 번째 매개변수로 전달될 인수를 정의하며, 배열의 각 함수가 반환하는 값이 순서대로 전달됨
    - 두 번째: 배열의 함수들이 반환한 값을 입력받아서 처리하는 함수
  - 반환값
    - 선택자 함수를 반환함

  ```js
  // friend/selector.js
  import { createSelector } from "reselect";

  const getFriends = (state) => state.friend.friends;
  const getAgeLimit = (state) => state.friend.ageLimit;
  const getShowLimit = (state) => state.friend.showLimit;

  export const getFriendsWithAgeLimit = createSelector(
    [getFriends, getAgeLimit],
    (friends, ageLimit) => friends.filter((friend) => friend.age <= ageLimit)
  );

  export const getFriendsWithAgeShowLimit = createSelector(
    [getFriendsWithAgeLimit, getShowLimit],
    (friendsWithAgeLimit, showLimit) => friendsWithAgeLimit.slice(0, showLimit)
  );
  ```

- reselect 패키지는 메모이제이션 기능이 있음

  - 따라서, 연산에 사용되는 데이터가 변경된 경우에만 연산을 수행하고, 변경되지 않았다면 이전 결과값을 재사용함
  - 즉, getFriendsWithAgeLimit 함수는 friends, ageLimit이 변경될 때만 연산하고, getFriendsWithAgeShowLimit 함수는 friends, ageLimit, showLimit이 변경될 때만 연산됨

- reselect를 사용해 선택자 함수를 정의했을 때의 장점

  - 1️⃣ 여러 컴포넌트에서 선택자 함수를 쉽게 재사용할 수 있음
  - 2️⃣ 데이터를 가공하는 코드가 컴포넌트 파일에서 분리되기 때문에, 컴포넌트 파일에는 UI 코드에 집중할 수 있음

### 🔹 선택자 함수 사용하기

- reselect 패키지로 만든 위 선택자 함수를 FriendMain 컴포넌트에서 활용해보자

  ```js
  function FriendMain() {
    const [ageLimit, showLimit, friendsWithAgeLimit, friendsWithAgeShowLimit] =
      useSelector((state) => {
        return [
          getAgeLimit(state),
          getShowLimit(state),
          getFriendsWithAgeLimit(state),
          getFriendsWithAgeShowLimit(state),
        ];
      }, shallowEqual);
  }
  ```

## ▶ reselect에서 컴포넌트의 속성값 이용하기

- 선택자 함수는 state 외에도 props를 입력으로 받을 수 있음
- 선택자 함수에서 속성값을 이용하면, 컴포넌트의 각 인스턴스에 특화된 값을 반환할 수 있음
- ageLimit props를 받는 FriendMain 컴포넌트를 구현해보자

  ```js
  // index.js
  // ...
  ReactDOM.render(
    <Provider store={store}>
      <div>
        <FriendMain ageLimit={30} />
        <FriendMain ageLimit={15} />
      </div>
    </Provider>,
    rootElement
  );
  ```

  ```js
  function FriendMain({ ageLimit }) {
    const friendWithAgeLimit = useSelector((state) =>
      getFriendsWithAgeLimit(state, ageLimit)
    );
    // ...
  }
  ```

  ```js
  // friend/selector.js
  // ...
  export const getAgeLimit = (_, ageLimit) => ageLimit;
  ```

- 위 코드의 문제점: reselect에서 제공하는 메모이제이션 기능이 제대로 동작하지 않음

  - ∵ 두 개의 FriendMain 컴포넌트 인스턴스가 서로 다른 연령 제한 속성값을 가지고 있기 때문에, 두 인스턴스는 '같은' 선택자 함수를 다른 속성값으로 호출하게 됨
  - 따라서, 선택자 함수는 이전의 결과값을 재사용하지 못하고 매번 반복해서 연산을 수행하게 됨

## ▶ 컴포넌트 인스턴스별로 독립된 메모이제이션 적용하기

- 컴포넌트 인스턴스별로 독립된 메모이제이션 기능을 제공하기 위해서는 선택자 함수도 여러 인스턴스로 만들어져야 함

  ```js
  // friend/selector.js
  // ...
  export const makeGetFriendsWithAgeLimit = () => {
    return createSelector([getFriends, getAgeLimit], (friends, ageLimit) =>
      friends.filter((friend) => friend.age <= ageLimit)
    );
  };
  ```

- `useMemo` 훅을 이용해서 getFriendWithAgeLimit 함수의 참조값이 변경되지 않게 하자

  - 결과적으로, 각 컴포넌트 인스턴스는 각자의 getFriendWithAgeLimit 함수를 가질 수 있음

  ```js
  function FriendMain({ ageLimit }) {
    const getFriendWithAgeLimit = useMemo(makeGetFriendsWithAgeLimit, []);
    const friendWithAgeLimit = useSelector((state) =>
      getFriendsWithAgeLimit(state, ageLimit)
    );
    // ...
  }
  ```
