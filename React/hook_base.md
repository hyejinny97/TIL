## ▶ 리액트 훅 기초

- 훅(hook): 함수형 컴포넌트에 기능을 추가할 때 사용하는 함수
- 비교적 최근(React v-16.8)에 추가된 기능
- 클래스형 컴포넌트보다는 훅을 사용한 함수형 컴포넌트로 작성하는 것을 지향함!

### 🔹 상태값 추가하기 - `useState()`

> 참고: [React 18 의 새 기능 자동 배칭(Automatic Batching)](https://nukw0n-dev.tistory.com/33)<br>
> 참고: [[React] useState batching, 비동기, 동기처리](https://choi-records.tistory.com/entry/React-useState-batching-%EB%B9%84%EB%8F%99%EA%B8%B0-%EB%8F%99%EA%B8%B0%EC%B2%98%EB%A6%AC)<br>
> 실습: [상태값 변경 함수를 연속해서 호출하는 코드](https://codesandbox.io/s/3-22-sangtaegabs-byeongyeong-hamsureul-yeonsoghaeseo-hoculhaneun-kodeu-silseub-r8s9g1?file=/src/App.js)<br>
> 실습: [상태값 변경 함수의 인자로 함수를 사용한 코드](https://codesandbox.io/s/3-23-sangtaegabs-byeongyeong-hamsuyi-insuro-hamsureul-sayonghan-kodeu-silseub-hsxg0i?file=/src/App.js)<br>
> 실습: [하나의 useState 훅으로 여러 상태값 관리하기](https://codesandbox.io/s/3-25-hanayi-usestate-hugeuro-yeoreo-sangtaegabs-gwanrihagi-silseub-kkdye1?file=/src/App.js)

- useState 훅을 이용하면 컴포넌트에 상태값을 추가할 수 있음
  - useState 훅이 반환하는 배열 = [상태값, 상태값 변경 함수]
- 상태값 변경 함수는 비동기로 동작하고, 여러 개의 상태값 변경 요청을 배치(batch)로 처리함

  ```js
  function MyComponent() {
    const [count, setCount] = useState({ value: 0 });
    function onClick() {
      setCount({ value: count.value + 1 });
      setCount({ value: count.value + 1 });
    }
    console.log("render called");

    return (
      <div>
        <h2>{count.value}</h2>
        <button onClick={onClick}>증가</button>
      </div>
    );
  }
  ```

  - 기대한 결과
    - 증가 버튼 한 번 클릭할 때마다 value가 2씩 증가
    - 'render called' 로그가 두 번 출력됨
  - 실제 결과
    - 증가 버튼 한 번 클릭할 때마다 value가 1씩 증가 👉 이유: 상태값 변경 함수는 비동기로 진행되기 때문
    - 'render called' 로그가 한 번 출력됨 👉 이유: 리액트는 상태값 변경을 배치로 처리하기 때문

- 상태값 변경 함수의 인자로 함수를 입력할 수 있음

  - 상태값 변경 함수로 입력된 함수는 자신이 호출되기 직전의 상태값을 인자로 받음

  ```js
  function MyComponent() {
    const [count, setCount] = useState(0);
    function onClick() {
      setCount((prev) => prev + 1);
      setCount((prev) => prev + 1);
    }

    return (
      <div>
        <h2>{count}</h2>
        <button onClick={onClick}>증가</button>
      </div>
    );
  }
  ```

  - 위 코드에서 첫번째 setCount() 함수 호출 시 변경된 상태값이 두번째 setCount() 함수의 인자로 들어옴
  - 따라서, 증가 버튼 한 번 클릭할 때마다 value가 2씩 증가함

- 하나의 useState 훅으로 여러 상태값 관리 가능

  - 클래스형 컴포넌트/함수형 컴포넌트의 상태값 변경 함수는 조금 다르게 동작함
  - 클래스형 컴포넌트의 setState 메서드: 기존 상태값과 새로 입력된 값을 병합
  - 함수형 컴포넌트의 useState 훅: 이전 상태값을 덮어씀

  ```js
  function Profile() {
    const [state, setState] = useState({ name: "", age: 0 });
    return (
      <div>
        <p>{state.name}</p>
        <p>{state.age}</p>
        <input
          type="text"
          value={state.name}
          onChange={(e) => setState({ ...state, name: e.target.value })}
        />
        <input
          type="text"
          value={state.age}
          onChange={(e) => setState({ ...state, age: e.target.value })}
        />
      </div>
    );
  }
  ```

  - 사실, 상태값을 하나의 객체로 관리할 때는 `useState` 훅보단 `useReducer` 훅을 사용하는 것이 좋음

#### ➕ 참고) 상태값 변경이 배치로 처리되지 않는 경우

- 리액트 내부에서 관리하는(리액트 요소에 등록된) 이벤트 처리 함수에 대해서만 상태값 변경을 배치로 처리함
- 리액트 외부에서 관리되는(리액트 요소에 등록되지 않은) 이벤트 처리 함수는 상태값 변경이 배치로 처리되지 않음
  - `ReactDOM.unstable_batchedUpdates()` 함수를 이용하면 상태값 변경 함수는 모두 배치로 처리됨
  - 위 함수는 사실 안정화된 API가 아니므로 사용하지 않는 것이 좋음

### 🔹 부수 효과 처리하기 - `useEffect`

> 실습: [useEffect 훅의 사용 예](https://codesandbox.io/s/3-28-useeffect-hugyi-sayong-ye-silseub-45i65q?file=/src/App.js)<br>
> 실습: [useEffect 훅을 이용해서 이벤트처리함수 등록/해제하기]()

- 부수 효과: 함수 실행 시, 함수 외부의 상태를 변경하는 연산
  - 예) API 호출하기, 이벤트 처리 함수 등록하고 해제하기
- 모든 부수 효과는 useEffect 훅에서 처리하는 것이 좋음
- useEffect 훅에 입력하는 함수를 부수 효과 함수라고 함

  - 부수 효과 함수는 1) 렌더링 결과가 실제 돔에 반영된 후 호출되고, 2) 컴포넌트가 사라지기 직전에 마지막으로 호출됨

  ```js
  function MyComponent() {
    const [count, setCount] = useState(0);
    useEffect(() => {
      document.title = `업데이트 횟수: ${count}`;
    });

    return <button onClick={() => setCount(count + 1)}>증가</button>;
  }
  ```

- useEffect 훅에서 API 호출하는 코드 예시

  - 부수 효과 함수는 렌더링할 때마다 호출되기 때문에 API 통신을 불필요하게 많이 하게 됨
  - 이를 방지하기 위해 useEffect 훅 두번째 인자로 배열을 입력하면, 배열의 값이 변경되는 경우에만 함수가 호출됨 (의존성 배열)

  ```js
  function Profile({ userId }) {
    const [user, setUser] = useState(null);
    useEffect(() => {
      getUserApi(userId).then((data) => setUser(data));
    }, [userId]);

    return (
      <div>
        {!user && <p>사용자 정보를 가져오는 중...</p>}
        {user && (
          <>
            <p>{user.name}</p>
            <p>{user.age}</p>
          </>
        )}
      </div>
    );
  }
  ```

  - 위의 경우, userId가 변경되는 경우에만 부수 효과 함수가 호출됨

- useEffect 훅에서 이벤트 처리 함수를 등록하고 해제하는 코드 예시

  - 부수 효과 함수는 함수를 반환할 수 있음
  - 반환된 함수는 1) 부수 효과 함수가 호출되기 직전에 호출되고, 2) 컴포넌트가 사라지기 직전에 마지막으로 호출됨
  - 의존성 배열로 빈 배열을 입력하면 1) 컴포넌트가 생성될 때만 부수 효과 함수가 호출되고, 2) 컴포넌트가 사라질 때만 반환된 함수가 호출됨

  ```js
  function WidthPrinter() {
    const [width, setWidth] = useState(window.innerWidth);
    useEffect(() => {
      const onResize = () => setWidth(window.innerWidth);
      window.addEventListener("resize", onResize);
      return () => window.removeEventListener("resize", onResize);
    }, []);

    return <div>{width}</div>;
  }
  ```

### 🔹 훅 직접 만들기

- 리액트가 제공하는 훅을 이용해서 custom 훅을 만들 수 있음
- custom 훅을 이용해서 또 다른 custom 훅을 만들 수도 있음
- custom 훅의 이름도 내장 훅처럼 `use`로 시작하는 것이 좋음
- custom 훅을 사용하면 내부 구현을 숨기면서 사용 편의성을 높일 수 있음

- 코드 예시) useUser 커스텀 훅

  ```js
  function useUser(userId) {
    const [user, setUser] = useState(null);
    useEffect(() => {
      getUserApi(userId).then((data) => setUser(data));
    }, [userId]);

    return user;
  }

  function Profile({ userId }) {
    const user = useUser(userId);

    return (
      <div>
        {!user && <p>사용자 정보를 가져오는 중...</p>}
        {user && (
          <>
            <p>{user.name}</p>
            <p>{user.age}</p>
          </>
        )}
      </div>
    );
  }
  ```

- 코드 예시) useWindowWidth 커스텀 훅

  ```js
  function useWindowWidth() {
    const [width, setWidth] = useState(window.innerWidth);
    useEffect(() => {
      const onResize = () => setWidth(window.innerWidth);
      window.addEventListener("resize", onResize);
      return () => window.removeEventListener("resize", onResize);
    }, []);

    return width;
  }

  function WidthPrinter() {
    const width = useWindowWidth();

    return <div>{width}</div>;
  }
  ```

- 코드 예시) useMounted 커스텀 훅

  - mount: 컴포넌트의 첫 번째 렌더링 결과가 실제 돔에 반영된 상태
  - 아래 useMounted 훅은 컴포넌트의 마운트 여부를 알려줌

  ```js
  function useMounted() {
    const [mounted, setMounted] = useState(false);
    useEffect(() => setMounted(true), []);

    return mounted;
  }
  ```

### 🔹 훅 사용 시, 지켜야 할 규칙

1. 훅은 함수형 컴포넌트 또는 커스텀 훅 안에서만 호출되어야 함
2. 하나의 컴포넌트에서 훅을 호출하는 순서는 항상 같아야 함

   - 이유: 리액트는 훅이 사용된 순서를 저장하고, 배열에 저장된 순서를 기반으로 훅을 관리하기 때문
   - 아래와 같은 사례들로 훅을 호출하면 순서가 보장되지 않아 규칙2를 위반하게 됨
   - 조건에 따라 훅을 호출하는 경우

     ```js
     function MyComponent() {
       const [value, setValue] = useState(0);
       if (value === 0) {
         const [v1, setV1] = useState(0);
       } else {
         const [v2, setV2] = useState(0);
       }
       // 생략
     }
     ```

   - 반복문 안에서 훅을 호출하는 경우

     ```js
     function MyComponent() {
       const [value, setValue] = useState(0);
       for (let i = 0; i < value; i++) {
         const [num, setNum] = useState(0);
       }
       // 생략
     }
     ```

   - 함수가 언제 호출될지 알 수 없는 경우

     ```js
     function MyComponent() {
       const [value, setValue] = useState(0);
       function func1() {
         const [num, setNum] = useState(0);
       }
       // 생략
     }
     ```
