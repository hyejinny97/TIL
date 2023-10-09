## ▶ 렌더링 속도를 올리기 위한 성능 최적화 방법

- 속성값이나 상탯값이 변경되면 리액트가 자동으로 컴포넌트 함수를 실행해서 화면을 다시 그림
- 리액트에서 최초 렌더링 이후 데이터 변경 시 진행되는 렌더링 단계

  1. 이전 렌더링 결과를 재사용할지 판단함

     - 속성값이나 상탯값의 이전 이후 값을 비교해, 동일하다면 이후 단계를 생략함
     - 클래스형 컴포넌트인 경우, `shouldComponentUpdate` 메서드를 이용해 비교/판단
     - 함수형 컴포넌트인 경우, `React.memo`를 이용해 비교/판단

  2. 컴포넌트 함수를 호출함

  3. 가상 돔끼리 비교해 변경되 부분만 실제 돔에 반영함

### 🔹 `React.memo`로 렌더링 결과 재사용하기

- `React.memo(컴포넌트, 속성값 비교 함수)`

  - `React.memo`로 감싸지 않은 컴포넌트인 경우, 속성값이 변경되지 않아도 부모 컴포넌트가 렌더링될 때마다 자식 컴포넌트도 렌더링됨
  - `React.memo`로 감싼 컴포넌트인 경우, 부모 컴포넌트가 렌더링될 때마다 **속성값 비교 함수**가 호출됨

- 속성값 비교 함수는 이전/이후 속성값을 매개변수로 받아, `true`와 `false`를 반환함

  - `true`를 반환하면, 컴포넌트 함수의 실행(2단계)과 가상 돔의 계산(3단계) 단계를 생략하고 이전 렌더링 결과를 재사용함
  - `false`를 반환하면, 컴포넌트 함수를 실행함

  ```js
  function MyComponent(props) {
    // ...
  }

  function isEqual(prevProps, nextProps) {
    // true 또는 false를 반환
  }

  React.memo(MyComponent, isEqual);
  ```

- 속성값 비교 함수를 입력하지 않으면 얕은(shallow) 비교를 수행하는 기본 함수가 사용됨
- 속성값을 불변 객체로 관리했다면 이전/이후 값의 단순 비교만으로 변경되었는지 알 수 있으므로 렌더링 성능에 큰 도움이 됨

#### ➕ 참고) 리액트에서 속성값의 변경 여부를 계산하는 알고리즘

- `React.memo`에 속성값 비교 함수를 입력하지 않으면, 리액트에서 기본으로 제공하는 함수가 사용됨
- 리액트는 속성값 변경 여부를 판단하기 위해 속성값에 직접 연결된 모든 속성을 단순 비교(1 depth만 비교)함 👉 얕은(shallow) 비교

- 주의) 최상위 객체의 참조값으로 비교하지 않음

  - 이유) 부모 컴포넌트가 렌더링할 때마다 객체의 내부 속성값이 변경되지 않아도 새로운 속성값이 생성되어 최상위 객체의 참조값이 항상 변경되기 때문임

### 🔹 속성값과 상탯값을 불변 변수로 관리하는 법

- 자식 컴포넌트의 속성값으로 입력되는 '함수'의 값이 변하지 않도록 관리하기

  - 문제점

    - 부모 컴포넌트가 재렌더링될 때마다 함수가 새로 생성되는 경우, 자식 컴포넌트에서 `React.memo`를 사용했어도 속성값이 변경되었으므로 렌더링 됨

  - 해결 방법

    - 1️⃣ `useState`, `useReducer`의 상탯값 변경 함수는 변하지 않으므로 이를 이용
    - 2️⃣ 이벤트 처리 함수에서 상탯값 변경 외에 다른 처리도 필요하다면 `useCallback`를 사용

  ```js
  // 문제 상황
  function Parent() {
    const [selectedFruit, setSelectedFruit] = useState("apple");

    return (
      <div>
        <SelectFruit
          selected={selectedFruit}
          onChange={(fruit) => setSelectedFruit(fruit)}
        />
      </div>
    );
  }
  ```

  ```js
  // 해결 1) useState의 상탯값 변경 함수를 사용
  function Parent() {
    const [selectedFruit, setSelectedFruit] = useState("apple");

    return (
      <div>
        <SelectFruit selected={selectedFruit} onChange={setSelectedFruit} />
      </div>
    );
  }
  ```

  ```js
  // 해결 2) useCallback을 사용
  function Parent() {
    const [selectedFruit, setSelectedFruit] = useState("apple");
    const onChangeFruit = useCallback((fruit) => {
      setSelectedFruit(fruit);
      sendLog({ type: "fruit change", value: fruit });
    }, []);

    return (
      <div>
        <SelectFruit selected={selectedFruit} onChange={onChangeFruit} />
      </div>
    );
  }
  ```

- 자식 컴포넌트의 속성값으로 입력되는 '객체'의 값이 변하지 않도록 관리하기

  - 문제점

    - 부모 컴포넌트 내에서 객체를 정의해서 자식 컴포넌트의 속성값으로 입력하면, 자식 컴포넌트에서 `React.memo`를 사용했어도 속성값이 변경되었으므로 렌더링 됨

  - 해결 방법
    - 1️⃣ 부모 컴포넌트 내부가 아닌 외부에서 상수 변수로 관리하면 됨
    - 2️⃣ 속성값이나 상탯값을 이용해서 계산해야 된다면, `useMemo`를 이용하자

  ```js
  // 문제 상황
  function SelectFruit({ selectedFruit, onChange }) {
    const options = [
      { name: "apple", price: 500 },
      { name: "banana", price: 1000 },
      { name: "orange", price: 1500 },
    ];

    return (
      <div>
        <Select
          options={options}
          selected={selectedFruit}
          onChange={onChange}
        />
      </div>
    );
  }
  ```

  ```js
  // 해결 1) 외부에서 상수 변수로 관리
  function SelectFruit({ selectedFruit, onChange }) {
    return (
      <div>
        <Select options={FRUITS} selected={selectedFruit} onChange={onChange} />
      </div>
    );
  }

  const FRUITS = [
    { name: "apple", price: 500 },
    { name: "banana", price: 1000 },
    { name: "orange", price: 1500 },
  ];
  ```

  ```js
  // 해결 2) useMemo를 이용
  function SelectFruit({ selectedFruit, onChange }) {
    const [maxPrice, setMaxPrice] = useState(1000);

    const fruits = useMemo(
      () => FRUITS.filter((fruit) => fruit.price <= maxPrice),
      maxPrice
    );

    return (
      <div>
        <Select options={FRUITS} selected={selectedFruit} onChange={onChange} />
      </div>
    );
  }
  ```

#### ➕ 참고) 상탯값을 불변 객체로 관리하기

- 속성값이나 상탯값이 변경되면 반드시 객체도 새로 생성해야 함
- 부모 컴포넌트에서 새로운 객체를 생성하지 않고 기존 객체를 수정한 채로 자식 컴포넌트의 속성값으로 전달하면, 자식 컴포넌트가 `React.memo`를 이용한 경우 속성값이 변하지 않았으므로 렌더링 되지 않음

### 🔹 가상 돔에서의 성능 최적화

- 요소의 '타입'을 변경하면, 리액트는 해당 요소의 모든 자식 요소를 삭제하고 다시 추가함

  - 자식 요소의 내용이 변경되지 않아도 실제 돔에서 삭제되고 다시 추가되므로 매우 비효율적임
  - 자식 컴포넌트가 삭제된 후 다시 추가되므로 자식 컴포넌트의 상탯값은 초기화 됨
  - 자식 요소가 많은 부모 요소의 타입을 변경하면 화면이 끊기는 느낌이 들 수 있음

  ```js
  function App() {
    const [flag, setFlag] = useState(true);

    useEffect(() => {
      setTimeout(() => setFlag((prev) => !prev), 1000);
    });

    if (flag) {
      return (
        <div>
          <Counter />
          <p>사과</p>
          <p>바나나</p>
        </div>
      );
    } else {
      return (
        <span>
          <Counter />
          <p>사과</p>
          <p>바나나</p>
        </span>
      );
    }
  }
  ```

- 요소의 '속성값'만 변경하면, 리액트는 해당 속성만 실제 돔에 반영함

  - 아래 예시의 경우, color 속성은 그대로 두고 backgroundColor 속성만 실제 돔에 반영됨

  ```js
  function App() {
    return (
      <div
        className={flag ? "yes" : "no"}
        style={{ color: "black", backgroundColor: flag ? "green" : "red" }}
      >
        <Counter />
        <p>사과</p>
        <p>바나나</p>
      </div>
    );
  }
  ```

- 요소를 '추가'하거나 '삭제'하는 경우

  - 일단 리액트는 효율적 연산을 위해 순서(order) 정보를 이용해 이전 가상 돔과 현재 가상돔을 비교한 후 변경된 요소만 실제 돔에 반영함
    - '끝' 부분에 요소를 추가/삭제하는 경우, 해당 요소만 실제 돔에 추가/삭제되고 기존 요소는 변경되지 않음
    - '중간' 부분에 요소를 추가/삭제하는 경우, 그 뒤 요소들은 전부 변경됨
  - `key` 속성값을 입력하면 리액트는 같은 키를 가지는 요소끼리만 비교해서 변경점을 찾게 됨
    - 즉, `key` 속성값은 리액트가 렌더링을 효율적으로 할 수 있도록 추가 정보를 제공함
    - 주의) 배열 '중간'에 원소를 추가/삭제할 경우, `key` 속성값으로 순서(order) 정보를 입력하는 것은 바람직하지 않음

  ```js
  function App() {
    if (flag) {
      return (
        <div>
          <p key="apple">사과</p>
          <p key="banana">바나나</p>
        </div>
      );
    } else {
      return (
        <span>
          <p key="apple">사과</p>
          <p key="pineapple">파인애플</p>
          <p key="banana">바나나</p>
        </span>
      );
    }
  }
  ```
