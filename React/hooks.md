## ▶ React 내장 Hook 살펴보기

### 🔹 Consumer 컴포넌트 없이 context 사용하기 - `useContext`

- `useContext`를 이용하면 Consumer 컴포넌트를 사용하지 않고도 부모 컴포넌트로부터 전달된 Context 데이터를 사용할 수 있음

  - Consumer 컴포넌트 사용 시 단점: Consumer 컴포넌트 안쪽에서만 context 데이터에 접근할 수 있고 JSX 부분이 복잡해짐

  ```js
  const UserContext = React.createContext();
  const user = { name: "mike", age: 23 };

  function Parent() {
    return (
      <UserContext.Provider value={user}>
        <Child />
      </UserContext.Provider>
    );
  }
  ```

  ```js
  function Child() {
    const user = useContext(UserContext);
    // ...
  }
  ```

### 🔹 렌더링과 무관한 값 저장하기 - `useRef`

- `useRef`를 사용하면 자식 요소에 접근할 수 있음
- 이외에, 컴포넌트 내부에서 생성되는 값 중 렌더링과 무관한 값을 저장할 때 사용

  ```js
  function Profile() {
    const [age, setAge] = useState(20)
    const prevAgeRef = useRef(20)

    useEffect(() => {
      prevAgeRef.current = age;
    }, [age])

    const prevAge = prevAgeRef.current;
    const text = age === prevAge ? 'same': age > prevAge ? 'older' : 'younger';

    return (
      <div>
        <p>
          {`age ${age}` is ${text}` than age ${prevAge}}
        </p>
        <button
          onClick={() => {
            const age = Math.floor(Math.random() * 50 + 1);
            setAge(age);
          }}
        >
          나이 변경
        </button>
      </div>
    )
  }
  ```

### 🔹 메모이제이션 - `useMemo`, `useCallback`

- 이전 값을 기억해서 성능을 최적화하는 용도
- `useMemo(함수, 의존성 배열)`는 함수의 반환값을 재활용하는 용도로 사용됨

  - 첫번째 매개변수인 함수가 반환한 값을 기억
  - 의존성 배열의 값이 변경되지 않으면 이전에 반환된 값을 재사용
  - 의존성 배열의 값이 변경되었으면 첫번째 매개변수인 함수를 실행하고 반환값을 기억

  ```js
  function MyComponent({ v1, v2 }) {
    const value = useMemo(() => runExpensiveJob(v1, v2), [v1, v2]);
    // ...
  }
  ```

- `useCallback(함수, 의존성 배열)`은 함수를 재활용하는 용도로 사용됨

  - 리액트의 렌더링 성능을 위해 제공되는 훅
  - 컴포넌트가 렌더링될 때마다 새로운 함수를 생성해서 자식 컴포넌트의 속성값으로 입력되는 경우가 많음
    - 사실, 브라우저에서 함수 생성이 성능에 미치는 영향은 작음
    - 대신, 자식 컴포넌트의 속성값이 매번 변경되기 때문에 자식 컴포넌트에서 `React.memo`를 사용해도 불필요한 렌더링이 발생하는 문제가 있음
  - `useCallback`을 사용하면 의존성 배열의 값이 변경되지 않는 한 이전 함수를 재사용하므로 불필요한 렌더링을 막을 수 있음

  ```js
  function Profile() {
    const [name, setName] = useState("");
    const onSave = useCallback(() => saveToServer(name), [name]);

    return (
      <div>
        <p>{`my name is ${name}`}</p>
        <UserEdit onSave={onSave} setName={setName} />
      </div>
    );
  }
  ```

### 🔹 컴포넌트의 상탯값을 Redux처럼 관리하기 - `useReducer`

- `useReducer(reducer 함수, 초기 상탯값)`은 `[상탯값, dispatch 함수]`를 반환함

  ```js
  const INITIAL_STATE = { name: "", age: 0 };

  function reducer(state, action) {
    switch (action.type) {
      case "setName":
        return { ...state, name: action.name };
      case "setAge":
        return { ...state, age: action.age };
    }
  }

  function Profile() {
    const [state, dispatch] = useReducer(reducer, INITIAL_STATE);

    return (
      <div>
        <p>{`my name is ${name}`}</p>
        <input
          type="text"
          value={state.name}
          onChange={(e) =>
            dispatch({ type: "setName", name: e.currentTarget.value })
          }
        />
      </div>
    );
  }
  ```

- `useReducer`와 Context API를 사용하면 상위 컴포넌트에서 트리의 깊은 곳으로 이벤트 처리 함수를 쉽게 전달할 수 있음

  - `useReducer`의 dispatch 함수는 값이 변하지 않는 특징이 있어서, Context의 Consumer 컴포넌트가 불필요하게 자주 렌더링되진 않음

  ```js
  const ProfileDispatch = React.createContext(null);

  // ...

  function Profile() {
    const [state, dispatch] = useReducer(reducer, INITIAL_STATE);

    return (
      <div>
        <p>{`my name is ${name}`}</p>
        <ProfileDispatch.Provider value={dispatch}>
          <SomeComponent />
        </ProfileDispatch.Provider>
      </div>
    );
  }
  ```

### 🔹 부모 컴포넌트에서 접근 가능한 함수 구현하기 - `useImperativeHandle`

- 부모 컴포넌트는 ref 객체를 통해 클래스형 컴포넌트인 자식 컴포넌트의 메서드를 호출할 수 있음
- 함수형 컴포넌트에서도 `useImperativeHandle`을 사용하면 마치 자식 컴포넌트에 메서드가 있는 것처럼 만들 수 있음

  ```js
  function Profile(props, ref) {
    const [name, setName] = useState("");
    const [age, setAge] = useState(0);

    useImperativeHandle(ref, () => {
      addAge: value => setAge(age + value),
      getNameLength: () => name.length
    });

    return (
      <div>
        <p>{`my name is ${name}`}</p>
      </div>
    );
  }

  export default forwardRef(Profile)
  ```

  ```js
  function Parent() {
    const profileRef = useRef();

    const onClick = () => {
      if (profileRef.current) {
        console.log(profileRef.current.getNameLength());
        profileRef.current.addAge(5);
      }
    };

    return (
      <div>
        <Profile ref={profileRef} />
        <button onClick={onClick}>add age 5</button>
      </div>
    );
  }
  ```

- 하지만, 이 방식은 자식 컴포넌트의 내부 구현에 의존성이 생기므로 지양하는 것이 좋음

### 🔹 기타 React Hooks - `useLayoutEffect`, `useDebugValue`

- `useLayoutEffect`은 `useEffect`와 유사

  - `useEffect`의 callback function은 렌더링 결과가 돔에 반영된 후 **비동기**로 호출됨
  - 반면, `useLayoutEffect`의 callback function은 렌더링 결과가 돔에 반영된 직후 **동기**로 호출됨

- `useDebugValue`를 사용하면 custom hook의 내부 상태를 관찰할 수 있기 때문에 디버깅에 도움이 됨

  - `useDebugValue`으로 입력한 값은 리액트 개발자 도구에서 확인할 수 있음

  ```js
  function useToggle(initialValue) {
    const [value, setValue] = useState(initialValue);
    const onToggle = () => setValue(!value);

    useDebugValue(value ? "on" : "off");

    return [value, onToggle];
  }
  ```
