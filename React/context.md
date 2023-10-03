## ▶ Context API로 데이터 전달하기

- 상위 컴포넌트에서 하위 컴포넌트로 데이터를 전달할 때 속성값(props)을 이용
- 하위 컴포넌트가 상위 컴포넌트에서 멀리 떨어져 있다면, 중간 컴포넌트들이 기계적으로 속성값을 전달해야 함
- Context API를 사용하면, 상위 컴포넌트에서 하위 컴포넌트로 직접 데이터 전달 가능

### 🔹 Context API 이해하기

> 실습: [콘텍스트 API를 사용한 코드 실습](https://codesandbox.io/s/3-38-kontegseuteu-apireul-sayonghan-kodeu-silseub-po6e01?file=/src/App.js)

- `React.createContext()` 함수를 호출하면 콘텍스트 객체가 생성됨

  ```js
  React.createContext(기본값);
  ```

- 상위 컴포넌트에서는 `Provider` 컴포넌트를 이용해서 데이터를 전달
- 하위 컴포넌트에서는 `Consumer` 컴포넌트를 이용해서 데이터를 사용
- Consumer 컴포넌트는 데이터를 찾기 위해 상위로 올라가면서 가장 가까운 Provider 컴포넌트를 찾아 데이터를 받음

  - 만약, 최상위에 도달할 때까지 Provider 컴포넌트를 찾지 못한다면 기본값을 사용하게 됨

  ```js
  const UserContext = React.createContext("");

  function App() {
    return (
      <div>
        <UserContext.Provider value="mike">
          <Profile />
        </UserContext.Provider>
      </div>
    );
  }

  function Profile() {
    return (
      <div>
        <Greeting />
      </div>
    );
  }

  function Greeting() {
    return (
      <UserContext.Consumer>
        {(username) => <p>{username}</p>}
      </UserContext.Consumer>
    );
  }
  ```

- Provider 컴포넌트의 속성값이 변경되면 하위의 모든 Consumer 컴포넌트는 다시 렌더링됨

  - 이때, **중간 컴포넌트의 렌더링 여부와 상관없이** Consumer 컴포넌트는 다시 렌더링됨

  ```js
  const UserContext = React.createContext('');

  function App() {
    return (
      <div>
        <UserContext.Provider value="mike">
          <Profile />
        </UserContext.Provider>
      </div>
    );
  }

  function Profile = React.memo(() => {
    return (
      <div>
        <Greeting />
      </div>
    );
  });

  function Greeting() {
    return (
      <UserContext.Consumer>
        {username => <p>{username}</p>}
      </UserContext.Consumer>
    );
  }
  ```

  - Profile 컴포넌트는 `React.memo`로 만들어졌고 속성값이 없기 때문에, 최초 한 번만 렌더링 됨
  - Profile 컴포넌트의 렌더링 여부와 상관없이, Provider 컴포넌트의 속성값이 변경되면 Greeting 컴포넌트의 Consumer는 다시 렌더링 됨

### 🔹 Context API 활용하기

> 실습: [Provider, Consumer 컴포넌트를 중첩해서 사용한 예](https://codesandbox.io/s/3-40-provider-consumer-keomponeonteureul-jungceobhaeseo-sayonghan-ye-vg6n5q?file=/src/App.js)
> 실습: [하위 컴포넌트에서 콘텍스트 데이터 수정하기](https://codesandbox.io/s/3-42-hawi-keomponeonteueseo-kontegseuteu-deiteo-sujeonghagi-f73n59?file=/src/App.js)

- 여러 콘텍스트의 Provider, Consumer 컴포넌트를 중첩해서 사용할 수도 있음

  ```js
  const UserContext = React.createContext("");
  const ThemeContext = React.createContext("dark");

  function App() {
    return (
      <div>
        <ThemeContext.Provider value="light">
          <UserContext.Provider value="mike">
            <Profile />
          </UserContext.Provider>
        </ThemeContext.Provider>
      </div>
    );
  }

  function Profile() {
    return (
      <div>
        <Greeting />
      </div>
    );
  }

  function Greeting() {
    return (
      <ThemeContext.Consumer>
        {(theme) => (
          <UserContext.Consumer>
            {(username) => (
              <p style={{ color: theme === "dark" ? "gray" : "green" }}>
                {username}
              </p>
            )}
          </UserContext.Consumer>
        )}
      </ThemeContext.Consumer>
    );
  }
  ```

- 상위 컴포넌트에서 상태값 변경 함수를 전달하면, 하위 컴포넌트에서도 콘텍스트 데이터를 수정할 수 있음

  ```js
  const UserContext = React.createContext({ username: "", helloCount: 0 });
  const SetUserContext = React.createContext(() => {});

  function App() {
    const [user, setUser] = useState({ username: "mike", helloCount: 0 });
    return (
      <div>
        <SetUserContext.Provider value={setUser}>
          <UserContext.Provider value={user}>
            <Profile />
          </UserContext.Provider>
        </SetUserContext.Provider>
      </div>
    );
  }

  function Profile() {
    return (
      <div>
        <Greeting />
      </div>
    );
  }

  function Greeting() {
    return (
      <SetUserContext.Consumer>
        {(setUser) => (
          <UserContext.Consumer>
            {({ username, helloCount }) => (
              <React.Fragment>
                <p>{username}</p>
                <p>{`인사 횟수: ${helloCount}`}</p>
                <button
                  onClick={() =>
                    setUser({ username, helloCount: helloCount + 1 })
                  }
                >
                  인사하기
                </button>
              </React.Fragment>
            )}
          </UserContext.Consumer>
        )}
      </SetUserContext.Consumer>
    );
  }
  ```

### 🔹 Context API 사용할 시 주의할 점

- 콘텍스트 데이터로 객체를 사용할 때, 주의하지 않으면 렌더링할 때마다 새로운 객체를 전달해서 불필요한 렌더링이 발생함

  ```js
  // 불필요한 렌더링 발생하는 코드
  const UserContext = React.createContext({ username: "" });

  function App() {
    const [username, setUsername] = useState("");
    return (
      <div>
        <UserContext.Provider value={{ username }}>
          <Profile />
        </UserContext.Provider>
      </div>
    );
  }
  ```

  - 컴포넌트가 렌더링될 때마다 새로운 객체가 생성되므로, username 값이 변경되지 않아도 컴포넌트가 렌더링될 때마다 하위의 Consumer 컴포넌트도 다시 렌더링 됨

  ```js
  // 불필요한 렌더링 발생하지 않는 코드
  const UserContext = React.createContext({ username: "" });

  function App() {
    const [username, setUsername] = useState({ username: "" });
    return (
      <div>
        <UserContext.Provider value={user}>
          <Profile />
        </UserContext.Provider>
      </div>
    );
  }
  ```

- Consumer 컴포넌트와 Provider 컴포넌트를 적절한 위치에 사용하지 않아서, Consumer 컴포넌트가 상위 컴포넌트에서 Provider 컴포넌트를 찾지 못하는 경우 발생

  ```js
  const UserContext = React.createContext("");

  function App() {
    return (
      <div>
        <UserContext.Provider value="mike"></UserContext.Provider>
        <Profile />
      </div>
    );
  }
  ```
