# ✔ 리액트에 타입 적용하기

## ▶ 리액트 컴포넌트에서 타입 정의하기

- 타입을 정의할 때 리액트는 `@types/react`와 `@types/react-dom` 패키지를 이용함
- 이벤트 객체의 타입 정의

  - 리액트에서 발생하는 대부분의 이벤트 객체는 아래의 타입으로 정의할 수 있음

  ```ts
  type EventObject<T = HTMLElement> = React.SyntheticEvent<T>;
  ```

- 이벤트 처리 함수의 타입 정의

  - 리액트에서 발생하는 대부분의 이벤트 처리 함수는 아래의 타입으로 정의할 수 있음

  ```ts
  type EventFunc<T = HTMLElement> = (e: EventObject<T>) => void;
  ```

### 🔹 함수형 컴포넌트의 타입 정의하기

- 속성값(props)의 타입 정보는 문서의 역할을 하므로 파일의 최상단에 정의하는 것이 좋음

  ```ts
  interface Props {
    name: string;
    age?: number;
  }

  // 함수형 컴포넌트의 타입 정의 예시 1
  export default function MyComponent({ name, age = 23 }: Props) {
    // ...
  }

  // 함수형 컴포넌트의 타입 정의 예시 2
  const MyComponent: React.FunctionComponent<Props> = function ({
    name,
    age = 23,
  }) {
    // ...
  };
  ```

### 🔹 클래스형 컴포넌트의 타입 정의하기

- 파일 최상단에 속성값(props) 타입 정보 → defaultProps → 상탯값(state) 타입 정보순으로 컴포넌트보다 먼저 정의하는 것이 좋음

  - 리액트에서 돔 요소에 입력하는 스타일 객체의 타입은 `React.CSSProperties`를 사용함
  - 속성값과 상탯값의 타입을 `React.Component`의 제너릭으로 입력함

    - `React.Component`의 두번째 제너릭으로 입력한 State 타입은 setState 메서드의 타입 정의에 사용됨

  - 모든 이벤트 객체에 currentTarget 속성이 있기 때문에 위에서 정의한 EventObject 타입만으로도 충분함
  - 버튼 이벤트 객체에만 존재하는 속성을 이용하려면 정확한 타입을 입력해야 함

  ```ts
  interface Props {
    containerStyle: React.CSSProperties;
    theme: string;
  }

  const defaultProps = {
    theme: "dark",
  };

  interface State {
    name: string;
    age?: number;
  }

  class MyComponent extends React.Component<Props, State> {
    state: State = {
      name: "mike",
    };

    static defaultProps = defaultProps;
    pRef = createRef<HTMLParagraphElement>();

    onClick1 = (e: EventObject) => {
      console.log(e.currentTarget.dataset.food);
    };

    onClick2 = (e: React.MouseEvent<HTMLButtonElement>) => {
      console.log(e.clientX, e.clientY);
    };

    render() {
      const { containerStyle, theme } = this.props;
      const { name, age } = this.state;

      return (
        <div style={containerStyle}>
          <p pRef={this.pRef}>{name}</p>
          <button data-food="soup" onClick={this.onClick1}>
            버튼1
          </button>
          <button onClick={this.onClick2}>버튼2</button>
        </div>
      );
    }
  }
  ```

## ▶ 리덕스에서 타입 정의하기

- 타입을 정의할 때 리덕스는 `@types/react-redux` 패키지와 리덕스에 내장된 타입 정보를 이용함

### 🔹 `useReducer` 훅 사용하기

- `useReducer`의 제너릭으로 두 개의 타입이 들어감

  - 첫번째: 리덕스 상탯값에 대한 타입
  - 두번째: `useReducer` 훅의 매개변수로 입력된 함수의 반환값에 대한 타입

  ```ts
  import { ReduxState, actions } from "@store";

  interface Props {
    birthday: string;
  }

  export default function Person({ birthday }: Person) {
    const name = useSelector<ReduxState, string>((state) => state.person.name);
    const age = useSelector<ReduxState, number>((state) => state.person.age);

    const dispatch = useDispatch();
    function onClick() {
      dispatch(actions.setName("mike"));
      dispatch(actions.setAge(23));
    }

    // ...
  }
  ```

- ReduxState 타입이 미리 입력된 훅을 만들어서 사용하면 편하게 입력할 수 있음

  ```ts
  // useTypedSelector 훅
  import { TypedUseSelectorHook } from 'react-redux'

  export default const useTypedSelector: TypedUseSelectorHook<ReduxState> = useSelector;
  ```

  ```ts
  export default function Person({ birthday }: Person) {
    const name = useTypedSelector((state) => state.person.name);
    const age = useTypedSelector((state) => state.person.age);

    // ...
  }
  ```

### 🔹 `createAction` 함수와 `createReducer` 함수 정의하기

- action 객체의 타입 정의하기

  ```ts
  interface TypedAction<T extends string> {
    type: T;
  }

  interface TypedPayloadAction<T extends string, P> extends TypedAction<T> {
    payload: P;
  }
  ```

- action creator 함수의 타입 정의하기

  - payload 데이터 유무를 구별하기 위해 함수 오버로드를 이용

  ```ts
  export function createAction<T extends string>(type: T): TypedAction<T>;
  export function createAction<T extends string, P>(
    type: T,
    payload: P
  ): TypedPayloadAction<T, P>;
  export function createAction(type, payload?) {
    return payload !== undefined ? { type, payload } : { type };
  }
  ```

- reducer를 생성하는 함수의 타입 정의하기

  - S: 상탯값의 타입
  - T: action 타입
  - A: 모든 action 객체의 유니온 타입

  ```ts
  import produce from "immer";

  export function createReducer<S, T extends string, A extends TypedAction<T>>(
    initialState: S,
    handlerMap: {
      [key in T]: (
        state: Draft<S>,
        action: Extract<A, TypedActon<key>>
      ) => void;
    }
  ) {
    return function (
      state: S = initialState,
      action: Extract<A, TypedAction<T>>
    ) {
      return produce(state, (draft) => {
        const handler = handlerMap[action.type];
        if (handler) {
          handler(draft, action);
        }
      });
    };
  }
  ```

### 🔹 `createAction` 함수 사용하기

- 위에서 정의한 `createAction` 함수를 이용해서 action creator 함수를 만들자

  - enum으로 action 타입을 정의

  ```ts
  export enum ActionType {
    SetName = "person_setName",
    SetAge = "person_setAge",
  }

  export const actions = {
    setName: (name: string) => createAction(ActionType.SetName, { name }),
    setAge: (age: number) => createAction(ActionType.SetAge, { age }),
  };
  ```

### 🔹 `createReducer` 함수 사용하기

- 위에서 정의한 `createReducer` 함수를 이용해서 reducer를 만들자

  - 아래에서 타입스크립트는 `action.payload`가 SetName 액션 객체의 데이터라는 것을 알고 있음
  - 따라서, name이 아닌 다른 데이터르르 사용하려고 하면 타입 에러가 발생함

  ```ts
  export interface StatePerson {
    name: string;
    age: number;
  }

  const INITIAL_STATE = {
    name: "empty",
    age: 0,
  };

  type Action = ReturnType<(typeof actions)[keyof typeof actions]>;
  export default createReducers<StatePerson, ActionType, Action>(
    INITIAL_STATE,
    {
      [ActionType.SetName]: (state, action) =>
        (state.name = action.payload.name),
      [ActionType.SetAge]: (state, action) => (state.age = action.payload.age),
    }
  );
  ```

### 🔹 store를 만들어 컴포넌트에 공유

- person reducer와 product reducer를 합쳐 store를 만들자

  ```ts
  export interface ReduxState {
    person: StatePerson;
    product: StateProduct;
  }

  const reducer = combineReducers<ReduxState>({
    person,
    product,
  });

  export const store = createStore(reducer);
  ```

- react-redux의 `Provider`를 통해 store를 컴포넌트에 공유

  ```ts
  import {Provider} from 'react-redux'

  function App {
    return (
      <Provider store={store}>
        <div>
          <Person birthday='2015-04-15' />
          <Product />
        </div>
      </Provider>
    )
  }
  ```
