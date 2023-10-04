## ▶ ref 속성값으로 자식 요소에 접근하기

- ref 속성값을 이용하면 자식 요소 (**돔 요소** 또는 **컴포넌트**)에 직접 접근 가능

### 🔹 ref 속성값 이해하기

- `useRef` hook은 ref 객체를 반환
- 접근하고 하는 자식 요소의 ref 속성값에 ref 객체를 입력
- ref 객체의 `current` 속성을 이용하면 자식 요소에 접근할 수 있음
- 주의) 접근하고자 하는 자식 요소가 생성되어야 ref 객체로 접근 가능

  - `useEffect` hook 내부의 callback 함수는 컴포넌트 렌더링 결과가 돔에 반영된 후 호출되므로 ref 객체로 접근 가능

  ```js
  function TextInput() {
    const inputRef = useRef();

    useEffect(() => {
      inputRef.current.focus();
    }, []);

    return (
      <div>
        <input type="text" ref={inputRef} />
        <button>저장</button>
      </div>
    );
  }
  ```

### 🔹 ref 속성값 활용하기

- 클래스형 컴포넌트에서 ref 속성값 사용하기

  - `ref.current`는 해당 컴포넌트의 인스턴스를 가리킴
  - 따라서, `ref.current`로 해당 클래스의 메서드를 호출할 수 있음

- 함수형 컴포넌트에서 ref 속성값 사용하기

  - 인스턴스로 만들어지지 않지만, `useImperativeHandle` hook을 사용하면 함수형 컴포넌트에서도 변수와 함수를 외부로 노출시킬 수 있음
  - 함수형 컴포넌트에 ref 속성값을 사용하면, 리액트가 내부적으로 처리하기 때문에 손자 요소에 연결할 수 없음
  - 대신, ref가 아닌 다른 이름으로 ref 객체를 입력받아서 내부의 리액트 요소로 연결할 수는 있음
  - 단, 이 방법은 컴포넌트 내부 구조를 외부에서 알아야 하므로 좋지는 않음

  ```js
  function TextInput({ inputRef }) {
    return (
      <div>
        <input type="text" inputRef={inputRef} />
        <button>저장</button>
      </div>
    );
  }
  ```

  ```js
  function Form() {
    const inputRef = useRef();

    useEffect(() => {
      inputRef.current.focus();
    }, []);

    return (
      <div>
        <TextInput inputRef={inputRef} />
      </div>
    );
  }
  ```

- `forwardRef` 함수로 ref 속성값을 직접 처리하기

  - forwardRef 함수를 이용하면 부모 컴포넌트에서 넘어온 ref 속성값을 직접 처리 가능
  - 이를 통해, 함수형 컴포넌트에서 ref 이름을 사용해 ref 객체를 넘겨줄 수 있음

  ```js
  const TextInput = React.forwardRef((props, ref) => {
    return (
      <div>
        <input type="text" ref={ref} />
        <button>저장</button>
      </div>
    );
  });
  ```

  ```js
  function Form() {
    // ...
    return (
      <div>
        <TextInput ref={inputRef} />
      </div>
    );
  }
  ```

- ref 속성값으로 함수 사용하기

  - ref 속성값으로 함수를 입력하면, **해당 요소가 생성되거나 제거될 때마다 호출**됨
  - 요소가 생성될 때는 해당 요소를 참조하는 변수가 넘어오고, 삭제될 때는 null 값이 넘어옴
  - 주의) 리액트는 ref 속성값으로 새로운 함수가 들어오면 이전 함수에 null 인수를 넣어서 호출하고, 새로운 함수에는 요소의 참조값을 넣어서 호출함
  - 해결책) 따라서, 컴포넌트가 렌더링할 때마다 ref 속성값으로 들어온 함수가 호출되게 하고 싶지 않다면 ref 속성값으로 **고정된 함수**를 입력해야 함

  ```js
  function Form() {
    const [text, setText] = useState(INITIAL_TEXT);
    const [showText, setShowText] = useState(true);

    const setInitialText = useCallback(
      (ref) => ref && setText(INITIAL_TEXT),
      []
    );

    return (
      <div>
        {showText && (
          <input
            type="text"
            ref={setInitialText}
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        )}
        <button onClick={() => setShowText(!showText)}>보이기/가리기</button>
      </div>
    );
  }
  ```

### 🔹 ref 속성값 사용 시 주의할 점

- 조건부 렌더링을 하는 경우, 컴포넌트가 생성된 이후라 하더라도 ref 객체의 `current` 속성이 없을 수 있기 때문에 주의해야 함

  - 따라서, 조건부 렌더링이 사용된 요소의 ref 객체는 `current` 속성을 검사하는 코드가 필요

  ```js
  function Form() {
    const inputRef = useRef();
    const [showText, setShowText] = useState(true);

    return (
      <div>
        {showText && <input type="text" ref={inputRef} />}
        <button onClick={() => setShowText(!showText)}>보이기/가리기</button>
        <button onClick={() => inputRef.current && inputRef.current.focus()}>
          텍스트로 이동
        </button>
      </div>
    );
  }
  ```
