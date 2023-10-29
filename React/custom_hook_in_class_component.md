# ✔ 기존 클래스형 컴포넌트를 고려한 커스텀 훅 작성법

- 커스텀 훅을 감싸는 래퍼(wrapper) 컴포넌트를 만들면 클래스형 컴포넌트에서도 커스텀 훅의 로직을 재사용할 수 있음

## ▶ 커스텀 훅의 반환값이 없는 경우

### 🔹 디바운스 기능을 제공하는 `useDebounce` 훅

- 특정 ms 시간동안 deps가 변경되지 않으면 callback 함수를 호출하는 커스텀 훅 구현

  ```js
  function useDebounce({ ms, callback, deps }) {
    useEffect(() => {
      const id = setTimeout(callback, ms);
      return () => clearTimeout(id);
    }, deps);
  }
  ```

- 함수형 컴포넌트에서 `useDebounce` 훅의 사용

  ```js
  function Profile() {
    const [name, setName] = useState("");
    const [nameTemp, setNameTemp] = useState("");

    useDebounce({
      ms: 1000,
      callback: () => setName(nameTemp),
      deps: [nameTemp],
    });

    return (
      <div>
        <p>{name}</p>
        <input
          type="text"
          value={nameTemp}
          onChange={(e) => setNameTemp(e.currentTarget.value)}
        />
      </div>
    );
  }
  ```

### 🔹 클래스형 컴포넌트에서 `useDebounce` 훅 사용

- `useDebounce` 훅의 래퍼(wrapper) 컴포넌트

  ```js
  function Debounce({ children, ...props }) {
    useDebounce(props);
    return children;
  }
  ```

- 클래스형 컴포넌트에서 `Debounce` 컴포넌트 사용

  ```js
  class Profile extends React.Component {
    state = { name: "", nameTemp: "" };

    render() {
      const { name, nameTemp } = this.state;

      return (
        <Debounce
          ms={1000}
          callback={() => this.setState({ name: nameTemp })}
          deps={[nameTemp]}
        >
          <div>
            <p>{name}</p>
            <input
              type="text"
              value={nameTemp}
              onChange={(e) =>
                this.setState({ nameTemp: e.currentTarget.value })
              }
            />
          </div>
        </Debounce>
      );
    }
  }
  ```

## ▶ 커스텀 훅의 반환값이 있는 경우

### 🔹 마운트 상태를 관리하는 `useMounted` 훅 구현

- `useMounted` 훅의 기능을 제공하기 위한 고차 컴포넌트

  - 고차 컴포넌트는 새로 생성하는 컴포넌트의 속성값으로 정보를 전달할 수 있음

  ```js
  function withMounted(Component) {
    return function (props) {
      const mounted = useMounted();
      return <Component {...props} mounted={mounted} />;
    };
  }
  ```

- `useMounted` 훅의 기능을 제공하기 위한 렌더 속성값

  - 렌더 속성값에서는 children 속성값이 함수이므로, 매개변수로 정보를 전달할 수 있음

  ```js
  function Mounted({ children }) {
    const mounted = useMounted();
    return children(mounted);
  }
  ```

### 🔹 클래스형 컴포넌트에서 `useMounted` 훅 사용

- 클래스형 컴포넌트에서 `withMounted` 고차 컴포넌트를 사용하기

  ```js
  class MyComponent extends React.Component {
    render() {
      const { mounted } = this.props;
      return <p>{mounted ? "yes" : "no"}</p>;
    }
  }

  export default withMounted(MyComponent);
  ```
