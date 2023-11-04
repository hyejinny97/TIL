# ✔ 리액트 상탯값을 리덕스로 관리하기

## ▶ react-redux 패키지 없이 직접 구현하기

### 🔹 타임라인 화면 만들기

- 타임라인 배열을 받아 화면에 그리는 프레젠테이션 컴포넌트를 만들자

  ```js
  function TimelineList({ timelines }) {
    return (
      <ul>
        {timelines.map((timeline) => (
          <li key={timeline.id}>{timeline.desc}</li>
        ))}
      </ul>
    );
  }
  ```

- 리덕스의 상탯값에 접근하는 컨테이너 컴포넌트를 만들자

  - 액션이 처리될 때마다 화면을 다시 그리기 위해 `subscribe` 메서드를 사용함

    - 리덕스 상태가 변경되면 무조건 컴포넌트를 렌더링하기 위해 forceUpdate 함수를 사용함

  - 컴포넌트가 언마운트될 때 `subscribe` 메서드에 등록한 이벤트 처리 함수를 해제함

  ```js
  import { getNextTimeline } from "../../common/mockData";
  import { addTimeline } from "../state";

  function TimelineMain() {
    const [, forceUpdate] = useReducer((v) => v + 1, 0);

    useEffect(() => {
      const unsubscribe = store.subscribe(() => forceUpdate());
      return () => unsubscribe();
    }, []);

    function onAdd() {
      const timeline = getNextTimeline();
      store.dispatch(addTimeline(timeline));
    }

    const timelines = store.getState().timeline.timelines;

    return (
      <div>
        <button onClick={onAdd}>타임라인 추가</button>
        <TimelineList timelines={timelines} />
      </div>
    );
  }
  ```

### 🔹 친구 목록 화면 만들기

- 친구 목록 배열을 받아 화면에 그리는 프레젠테이션 컴포넌트를 만들자

  ```js
  function FriendList({ friends }) {
    return (
      <ul>
        {friends.map((friend) => (
          <li key={friend.id}>{friend.desc}</li>
        ))}
      </ul>
    );
  }
  ```

- 리덕스의 상탯값에 접근하는 컨테이너 컴포넌트를 만들자

  ```js
  import { getNextFriend } from "../../common/mockData";
  import { addFriend } from "../state";

  function FriendMain() {
    const [, forceUpdate] = useReducer((v) => v + 1, 0);

    useEffect(() => {
      const unsubscribe = store.subscribe(() => forceUpdate());
      return () => unsubscribe();
    }, []);

    function onAdd() {
      const friend = getNextFriend();
      store.dispatch(addFriend(friend));
    }

    const friends = store.getState().friend.friends;

    return (
      <div>
        <button onClick={onAdd}>친구 추가</button>
        <FriendList friends={friends} />
      </div>
    );
  }
  ```

### 🔹 FriendMain 컴포넌트 개선하기

- 위 코드에서는 타임라인 추가 버튼을 눌러도 FriendMain 컴포넌트 함수가 호출되는 문제가 있음
- 따라서, 불필요하게 컴포넌트 함수가 호출되지 않도록 하려면 상탯값 변경 여부를 검사해야 함

  - 상탯값이 변경된 경우에만 forceUpdate 함수를 호출하도록 수정

  ```js
  function FriendMain() {
    // ...
    useEffect(() => {
      let prevFriends = store.getState().friend.friends;

      const unsubscribe = store.subscribe(() => {
        const friends = store.getState().friend.friends;
        if (prevFriends !== friends) {
          forceUpdate();
        }
        prevFriend = friends;
      });

      return () => unsubscribe();
    }, []);
    // ...
  }
  ```

## ▶ react-redux 패키지 사용하기

- 아래 명령어를 통해 `react-redux` 패키지를 설치하자

  ```bash
  $ npm install react-redux
  ```

### 🔹 Provider 컴포넌트 사용하기

- Provider 컴포넌트를 리액트의 최상위 컴포넌트로 정의하자
- Provider 컴포넌트 하위에 있는 컴포넌트는 리덕스의 상탯값이 변경되면 자동으로 컴포넌트 함수가 호출됨

  - 스토어 객체를 Provider 컴포넌트의 속성값으로 넣음
  - Provider 컴포넌트는 전달받은 스토어 객체의 `subscribe` 메서드를 호출해 액션 처리가 끝날 때마다 알림을 받음
  - 그 다음, Context API를 사용해서 리덕스의 상탯값을 하위 컴포넌트로 전달함

  ```js
  import { Provider } from "react-redux";

  ReactDOM.render(
    <Provider store={store}>
      <App />
    </Provider>,
    document.getElementById("root")
  );
  ```

### 🔹 FriendMain 컴포넌트 리팩터링하기

- `useSelector` 훅을 사용해 컴포넌트가 리덕스 상탯값 변경에 반응하게 됨

  - 첫번째 매개변수: selector function (선택자 함수)
  - 반환값: selector function의 반환값
  - `useSelector` 훅은 리덕스의 상탯값이 변경되면, 이전 반환값과 새로운 반환값을 비교해 두 값이 다른 경우에만 컴포넌트를 다시 렌더링함

- `useDispatch` 훅을 사용해 액션을 발생시키게 됨

  - 반환값: dispatch 함수를 반환

- `react-redux`를 사용해 FriendMain 컴포넌트를 수정해보자

  ```js
  // ...
  import { useSelector, useDispatch } from "react-redux";

  function FriendMain() {
    const friends = useSelector((state) => state.friend.friends);
    const dispatch = useDispatch();

    function onAdd() {
      const friend = getNextFriend();
      dispatch(addFriend(friend));
    }

    return (
      <div>
        <button onClick={onAdd}>친구 추가</button>
        <FriendList friends={friends} />
      </div>
    );
  }
  ```

### 🔹 useSelector 훅으로 여러 상탯값 반환하기

- `useSelector` 훅으로 여러 상탯값을 가져오려면 selector function이 객체를 반환해야 함
- 이때, 객체 리터럴 문법을 이용하면 실제 상탯값이 바뀌지 않아도 매번 새로운 객체가 반환되는 문제가 있음

  - 해결책1) `useSelector` 훅을 필요한 상탯값 개수만큼 사용함
  - 해결책2) `reselect`와 같은 라이브러리의 메모이제이션을 이용함
  - 해결책3) `useSelector` 훅의 두 번째 매개변수를 활용함

- `useSelector` 훅의 두 번째 매개변수는 컴포넌트 렌더링 여부를 판단하는 역할을 함

  - 두 번째 매개변수를 입력하지 않으면, 참조값만 비교하는 단순 비교 함수가 사용됨
  - 따라서, selector function이 객체 리터럴을 반환하면 컴포넌트가 불필요하게 자주 렌더링되는 문제가 발생함
  - 해결책) 두 번째 매개변수에 `redux-react`의 `shallowEqual` 함수를 입력하면, 배열의 각 원소가 변경됐는지 검사하게 됨

  ```js
  import { shallowEqual } from "react-redux";

  function MyComponent() {
    const [value1, value2] = useSelector(
      (state) => [state.value1, state.value2],
      shallowEqual
    );
  }
  ```
