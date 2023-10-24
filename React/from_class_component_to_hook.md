# ✔ 클래스형 컴포넌트를 훅으로 변환하기

- 리액트 버전 16.8에서는 `getSnapshotBeforeUpdate`, `getDerivedStateFromError`, `componentDidCatch` 메서드를 제외한 클래스형 컴포넌트의 모든 기능을 함수형 컴포넌트에서도 사용할 수 있음

- `componentDidMount` 메서드, `componentWillUnmount` 메서드 👉 `useEffect` 훅 또는 `useLayoutEffect` 훅

- 클래스 멤버 변수 👉 `useRef` 훅

## ▶ `constructor` 메서드

- 클래스형 컴포넌트의 `constructor` 메서드는 주로 속성값으로부터 초기 상탯값을 계산하려는 용도로 사용되거나, `componentDidMount`보다 좀 더 빠르게 작업을 처리하는 용도로 사용됨

- `constructor` 메서드를 훅으로 구현

  - 컴포넌트 최초 호출 시에만 callApi 함수를 호출하기 위해 `useRef` 훅을 이용

  ```js
  // 클래스형 컴포넌트
  class Profile extends React.Component {
    constructor(props) {
      super(props);

      this.state = {
        name: `${props.firstName} ${props.lastName}`,
      };

      callApi();
    }
  }
  ```

  ```js
  // 함수형 컴포넌트
  function Profile({ firstName, lastName }) {
    const [name, setName] = useState(`${props.firstName} ${props.lastName}`);
    const isFirstRef = useRef(true);

    if (isFirstRef.current) {
      callApi();
      isFirstRef.current = false;
    }
    // ...
  }
  ```

## ▶ `componentDidUpdate` 메서드

- 클래스형 컴포넌트에서 최초 렌더링 이후에는 `componentDidUpdate` 메서드가 호출됨

  - `useEffect` 훅은 최초 렌더링 직후에도 호출되므로, 이를 피하기 위해 `useRef` 훅을 이용할 수 있음

- `componentDidUpdate` 메서드는 매개변수로 이전 상탯값과 이전 속성값을 전달함

  - 함수형 컴포넌트에서는 이전 값이 필요하다면 `useRef` 값으로 직접 관리해야 함
  - 아래 usePrevious 훅은 매개변수로 현재 값을 받고, 이전 값을 반환함

  ```js
  function usePrevious(value) {
    const valueRef = useRef();

    useEffect(() => {
      valueRef.current = value;
    }, [value]);

    return valueRef.current;
  }
  ```

- `componentDidUpdate` 메서드를 훅으로 구현

  - 마운트 여부를 `useRef` 훅으로 관리

  ```js
  // 클래스형 컴포넌트
  class Profile extends React.Component {
    state = { name: this.props.name };

    componentDidUpdate(prevProps) {
      const { userId, name } = this.props;

      if (prevProps.userId !== userId) {
        this.setState({ name });
      }
    }
    // ...
  }
  ```

  ```js
  // 함수형 컴포넌트
  function Profile({ userId, name }) {
    const [name, setName] = useState(name);
    const prevUserId = usePrevious(userId);
    const isMountedRef = useRef(false);

    if (isMountedRef.current) {
      if (prevUserId !== userId) setName(name);
    } else {
      isMountedRef.current = true;
    }
    // ...
  }
  ```

- 업데이트 시점에 함수를 호출해 주는 커스텀 훅

  ```js
  function useOnUpdate(func) {
    const isMountedRef = useRef(false);

    useEffect(() => {
      if (isMountedRef.current) {
        func();
      } else {
        isMountedRef.current = true;
      }
    });
  }
  ```

## ▶ `getDerivedStateFromProps` 메서드

- `getDerivedStateFromProps` 정적 메서드는 속성값 변경에 따라 상탯값도 변경할 때 사용됨
- `getDerivedStateFromProps` 정적 메서드를 훅으로 구현

  - 리액트는 렌더 함수에서 상탯값을 변경하면 변경된 상탯값으로 렌더 함수를 다시 호출함
  - 주의) 렌더 함수가 무한대로 호출되는 것을 주의해야 함

  ```js
  // 클래스형 컴포넌트
  class SpeedIndicator extends React.Component {
    state = { isFaster: false, prevSpeed: 0 };

    static getDerivedStateFromProps(props, state) {
      if (props.speed !== prevSpeed) {
        return {
          isFaster: props.speed > prevSpeed,
          prevSpeed: props.speed,
        };
      }
      return null;
    }
  }
  ```

  ```js
  // 함수형 컴포넌트
  function SpeedIndicator({ speed }) {
    const [isFaster, setIsFaster] = useState(false);
    const [prevSpeed, setPrevSpeed] = useRef(0);

    if (speed !== prevSpeed) {
      setIsFaster(speed > prevSpeed);
      setPrevSpeed(speed);
    }
    // ...
  }
  ```

## ▶ `forceUpdate` 메서드

- `forceUpdate` 메서드를 훅으로 구현

  ```js
  // 함수형 컴포넌트
  function MyComponent() {
    const [_, forceUpdate] = useReducer((s) => s + 1, 0);

    function onClick() {
      forceUpdate();
    }
  }
  ```
