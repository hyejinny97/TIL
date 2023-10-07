## ▶ useEffect 훅 활용법

### 🔹 의존성 배열 관리하는 법

- 의존성 배열이 변경되었을 때 `useEffect` 훅의 두번째 매개변수인 부수 효과 함수가 실행됨

  - 부수 효과 함수를 수정할 때, 새로운 상탯값을 사용했다면 의존성 배열에 추가해야 함
  - `eslint`의 exhaustive-deps 규칙에 의해 잘못 사용된 의존성 배열을 알 수 있음

- 부수 효과 함수에서 API 호출하는 경우

  ```js
  function Profile({ userId }) {
    const [user, setUser] = useState();

    useEffect(() => {
      fetchUser(userId).then((data) => setUser(data));
    }, [userId]);

    // ...
  }
  ```

- `useEffect` 훅에서 `async` `await` 함수 사용하기

  - 부수 효과 함수의 반환값은 항상 함수 타입이어야 함
  - 부수 효과 함수가 반환한 함수는 부수 효과 함수가 호출되기 직전과 컴포넘트가 사라지기 직전에 호출됨
  - `async` `await` 함수는 promise 객체를 반환하므로, 부수 효과 함수를 `async` `await` 함수로 만들면 에러가 발생함
  - 따라서, 부수 효과 함수 내에서 `async` `await` 함수를 만들어서 호출해야 함

  ```js
  useEffect(() => {
    async function fetchAndSetUser() {
      const data = await fetchUser(userId);
      setUser(data);
    }

    fetchUserAndSetUser();
  }, [userId]);
  ```

- fetchUserAndSetUser 함수 재사용하기

  - `useEffect` 훅 안에 있는 fetchUserAndSetUser 함수를 훅 밖으로 빼보자
  - 컴포넌트가 렌더링될 때마다 fetchUserAndSetUser 함수가 갱신되어 `useEffect` 훅에 의해 호출되지 않도록 `useCallback` 훅을 사용하자
  - 아래처럼 `useCallback` 훅을 사용하면 userId가 변경될 때만 fetchUserAndSetUser 함수가 갱신됨

  ```js
  function Profile({ userId }) {
    const [user, setUser] = useState();
    const fetchAndSetUser = useCallback(
      async function (needDetail) {
        const data = await fetchUser(userId, needDetail);
        setUser(data);
      },
      [userId]
    );

    useEffect(() => {
      fetchAndSetUser(false)
    }, [fetchAndSetUser])

    return (
      <div>
        <h1>{user.name}</h1>
        <button onClick={() => fetchAndSetUser(true)}>더보기</button>
        <UserDetail user={user}>
      </div>
    )
  }
  ```

#### ➕ 참고) 의존성 배열을 잘못 관리하면 생기는 일

- 의존성 배열에 입력해야 할 값을 입력하지 않으면 오래된 값을 참조하는 문제가 발생함
- 컴포넌트 함수가 실행될 때마다 부수 효과 함수가 생성되고, 함수는 생성될 당시의 변수를 참조함

  - 같은 val2 변수라고 하더라도 컴포넌트 함수가 실행될 때마다 새로운 메모리 공간을 가짐
  - 따라서, 부수 효과 함수는 함수가 생성된 시점의 val2를 참조하므로, 예전에 생성된 부수 효과 함수는 예전 val2를 참조하게 됨

  ```js
  // 의존성 배열을 잘못 관리한 경우 (∵ val2를 배열에 넣지 않음)
  function MyComponent() {
    const [val1, setVal1] = useState(0);
    const [val2, setVal2] = useState(0);

    useEffect(() => {
      const id = setInterval(() => console.log(val1, val2), 1000);
      return () => clearInterval(id);
    }, [val1]);

    return (
      <div>
        <button onClick={() => setVal1(val1 + 1)}>val1 증가</button>
        <button onClick={() => setVal2(val2 + 1)}>val2 증가</button>
      </div>
    );
  }
  ```

### 🔹 의존성 배열을 없애는 법

- `useEffect` 훅에서 가능하다면 의존성 배열을 사용하지 않는 것이 좋음
  - 의존성 배열을 입력하지 않으면 부수 효과 함수에서 사용된 모든 변수는 가장 최신화된 값을 참조하게 됨
- 부수 효과 내에서 분기 처리하기

  - 의존성 배열을 입력하지 않는 대신 부수 효과 함수 내에서 if 문으로 실행 시점 조절할 수 있음

  ```js
  function Profile({ userId }) {
    const [user, setUser] = useState();
    const fetchAndSetUser = useCallback(/*...*/,
      [userId]
    );

    useEffect(() => {
      if (!user || user.id !== userId) {
        fetchAndSetUser(false)
      }
    })

    // ...
  }
  ```

- `useState`의 상탯값 변경 함수에 '함수' 입력하기

  - 상탯값 변경 함수에 '함수'를 입력하면, 이전 상탯값을 매개변수로 받을 수 있음
  - 따라서, 의존성 배열에서 상탯값을 제거할 수 있음

  ```js
  // 의존성 배열에 상탯값을 추가한 경우
  function MyComponent() {
    const [count, setCount] = useState(0);

    useEffect(() => {
      function onClick() {
        setCount(count + 1);
      }

      window.addEventListener("click", onClick);
      return () => window.removeEventListener("click", onClick);
    }, [count]);

    // ...
  }
  ```

  ```js
  // useState의 상탯값 변경 함수에 함수를 입력한 경우
  function MyComponent() {
    const [count, setCount] = useState(0);

    useEffect(() => {
      function onClick() {
        setCount((prev) => prev + 1);
      }

      window.addEventListener("click", onClick);
      return () => window.removeEventListener("click", onClick);
    });

    // ...
  }
  ```

- `useReducer` 활용하기

  - 여러 상탯값을 참조해야 하는 경우에 `useReducer` 훅을 사용하면 의존성 배열을 제거할 수 있음

  ```js
  // 의존성 배열에 여러 개의 상탯값을 추가한 경우
  function Timer({ initialTotalSeconds }) {
    const [hour, setHour] = useState(Math.floor(initialTotalSeconds / 3600));
    const [minute, setMinute] = useState(
      Math.floor((initialTotalSeconds % 3600) / 60)
    );
    const [second, setSecond] = useState(initialTotalSeconds % 60);

    useEffect(() => {
      const id = setInterval(() => {
        if (second) {
          setSecond(second - 1);
        } else if (minute) {
          setMinute(minute - 1);
          setSecond(59);
        } else if (hour) {
          setHour(hour - 1);
          setMinute(59);
          setSecond(59);
        }
      }, 1000);

      return () => clearInterval(id);
    }, [hour, minute, second]);

    // ...
  }
  ```

  ```js
  // useReducer 훅을 사용해 여러 상탯값을 변경하는 경우
  function Timer({ initialTotalSeconds }) {
    const [state, dispatch] = useReducer(reducer, {
      hour: Math.floor(initialTotalSeconds / 3600),
      minute: Math.floor((initialTotalSeconds % 3600) / 60),
      second: initialTotalSeconds % 60,
    });

    useEffect(() => {
      const id = setInterval(dispatch, 1000);

      return () => clearInterval(id);
    });

    // ...
  }

  function reducer(state) {
    const { hour, minute, second } = state;

    if (second) {
      return { ...state, second: second - 1 };
    } else if (minute) {
      return { ...state, minute: minute - 1, second: 59 };
    } else if (hour) {
      return { ...state, hour: hour - 1, minute: 59, second: 59 };
    } else {
      return state;
    }
  }
  ```

- `useRef` 활용하기

  - 속성값이 렌더링 결과에 영향을 주는 값이 아니라면 `useRef` 훅을 이용해서 의존성 배열을 제거할 수 있음

  ```js
  // 의존성 배열에 자주 변경되는 속성값을 추가한 경우
  function MyComponent({ onClick }) {
    useEffect(() => {
      window.addEventListener("click", () => {
        onClick();
      });
      // ...
    }, [onClick]);

    // ...
  }
  ```

  ```js
  // useRef 훅을 사용해 개선한 경우
  function MyComponent({ onClick }) {
    const onClickRef = useRef();

    useEffect(() => {
      onClickRef.current = onClick;
    });

    useEffect(() => {
      window.addEventListener("click", () => {
        onClickRef.current();
      });
      // ...
    });

    // ...
  }
  ```
