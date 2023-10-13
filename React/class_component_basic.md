## ▶ 클래스형 컴포넌트의 기본 사용법

### 🔹 `setState` 메서드 이해하기

- `setState`는 클래스형 컴포넌트에서 상탯값을 변경할 때 호출하는 메서드

  - `setState` 메서드로 입력된 객체는 기존 상탯값과 **병합** 됨
  - 리액트는 `setState` 메서드가 호출되면 해당 컴포넌트를 다시 렌더링함

  ```js
  class MyComponent extends React.Component {
    state = {
      count1: 0,
      count2: 0,
    };

    onClick = () => {
      const { count1 } = this.state;
      this.setState({ count1: count1 + 1 });
    };

    // ...
  }
  ```

- `setState` 메서드를 연속해서 호출하는 경우 예시

  - count 상탯값이 1만큼 증가 👉 ∵ `setState`는 비동기로 상탯값을 변경함
  - 'render' 로그는 한 번만 출력됨 👉 ∵ 리액트는 효율적으로 렌더링하기 위해 여러 개의 `setState` 메서드를 배치(batch)로 처리함

  ```js
  class MyComponent extends React.Component {
    state = {
      count: 0,
    };

    onClick = () => {
      this.setState({ count: this.state.count + 1 });
      this.setState({ count: this.state.count + 1 });
    };

    render() {
      console.log("render");
      // ...
    }
  }
  ```

- `setState` 메서드의 인수로 함수를 입력하면, 입력된 함수는 자신이 호출되기 직전의 상탯값을 매개변수로 받음

  ```js
  onClick = () => {
    this.setState((prevState) => ({
      count: prevState.count + 1;
    }));
    this.setState((prevState) => ({
      count: prevState.count + 1;
    }));
  };
  ```

- `setState` 메서드의 인수로 함수를 넘길 수 있으므로, 아래처럼 상탯값을 관리하는 로직을 컴포넌트로부터 분리할 수도 있음

  ```js
  const actions = {
    init() {
      return { count: 0 };
    },
    increment(state) {
      return { count: state.count + 1 };
    },
    decrement(state) {
      return { count: state.count - 1 };
    },
  };

  class MyComponent extends React.Component {
    state = actions.init();

    onIncrement = () => {
      this.setState(actions.increment);
    };

    onDecrement = () => {
      this.setState(actions.decrement);
    };

    // ...
  }
  ```

- `setState` 메서드의 두 번째 매개변수는 처리가 끝났을 때 호출되는 콜백 함수임

  - 콜백 함수는 상탯값 변경 후에 호출되므로, 상탯값을 기반으로 다음 작업을 처리할 때 유용

  ```js
  onClick = () => {
    this.setState({ count: 123 }, () => console.log("count is 123"));
  };
  ```

- `forceUpdate` 메서드를 사용하면 상탯값을 직접 수정할 수 있음

  - 상탯값 직접 수정 후, `forceUpdate` 메서드를 호출하면 새로운 값과 함께 화면을 다시 그림
  - 하지만, 상탯값도 속성값과 같이 불변객체로 관리하는 것이 좋음

  ```js
  onClick = () => {
    this.state.comment = "Hello";
    this.forceUpdate();
  };
  ```

### 🔹 클래스 필드를 이용해 이벤트 처리 메서드 작성하기

> 참고) [모던 자바스크립트 - 클래스 필드](https://ko.javascript.info/class#ref-714)<br>
> 참고) [개인 블로그 - 클래스 필드](https://helloworldjavascript.net/pages/270-class.html#fn-1)<br>
> 참고) [ECMAScript 2022 살펴보기 - 클래스 필드](https://yozm.wishket.com/magazine/detail/1570/)

- 과거) 이벤트 처리 메서드의 함수 바인딩 필요

  - 클래스형 컴포넌트의 이벤트 처리 메서드는 자식 컴포넌트 또는 돔 요소의 속성값으로 전달할 수 있음
  - 이벤트 처리 메서드와 `this` 객체를 바인딩하지 않으면 메서드 호출 시 엉뚱한 객체를 가리킬 수 있음
  - 따라서, 함수 바인딩을 통해 `this` 객체를 고정시킬 필요가 있음

- `constructor` 또는 `render` 메서드에서 함수 바인딩

  - `render` 메서드에서 함수를 바인딩할 경우, 렌더링할 때마다 `render` 메서드가 호출되므로 새로운 함수가 계속 생성되어 성능을 떨어뜨릴 수 있음
  - 따라서, 성능을 생각한다면 `render`보다 `constructor`에서 함수 바인딩하는 것이 좋음
  - 하지만, 최근 브라우저에서는 함수 생성이 성능에 미치는 영향이 크지 않아 큰 문제가 되진 않음

  ```js
  class MyComponent extends React.Component {
    constructor(props) {
      super(props);
      this.onClickInc = this.onClickInc.bind(this);
    }

    onClickInc(e) {
      const { count } = this.state;
      this.setState({ count: count + 1 });
    }

    onClickDec(e) {
      const { count } = this.state;
      this.setState({ count: count - 1 });
    }

    render() {
      return (
        <div>
          <button onClick={this.onClickInc} />
          <button onClick={this.onClickDec.bind(this)} />
        </div>
      );
    }
  }
  ```

- 현재) 클래스 필드(class field)가 JS 표준이 되었기 때문에, 함수 바인딩이 필요없음

  - 클래스 필드에 함수를 정의하면 prototype의 method가 아닌 instance의 method가 됨
  - 이벤트 처리 메서드를 화살표 함수로 작성하면 `this` 객체는 자동으로 바인딩 됨

  ```js
  class MyComponent extends React.Component {
    onClickInc = () => {
      const { count } = this.state;
      this.setState({ count: count + 1 });
    };

    onClickDec = () => {
      const { count } = this.state;
      this.setState({ count: count - 1 });
    };

    render() {
      return (
        <div>
          <button onClick={this.onClickInc} />
          <button onClick={this.onClickDec} />
        </div>
      );
    }
  }
  ```

#### ➕ 참고) 함수 바인딩이 필요한 이유

```js
const counter = {
  value: 0,
  increase: function () {
    this.value++;
  },
};

counter.increase();
console.log(counter.value); // 1

const incFunc1 = counter.increase;
incFunc1();
console.log(counter.value); // 1

const incFunc2 = counter.increase.bind(counter);
incFunc2();
console.log(counter.value); // 2
```

### 🔹 생명 주기 메서드에서 컨텍스트 데이터 사용하기

- 클래스형 컴포넌트의 `contextType` 정적 멤버 변수에 컨텍스트 객체를 입력하면 클래스 내부에서 컨텍스트 데이터에 접근할 수 있음

  - 단, `contextType`을 이용한 방식은 하나의 컨텍스트만 연결할 수 있다는 단점이 있음

  ```js
  const ThemeContext = React.createContext("dark");

  class MyComponent extends React.Component {
    componentDidMount() {
      const theme = this.context;
      // ...
    }

    // ...
  }

  MyComponent.contextType = ThemeContext;
  ```

- `Consumer` 컴포넌트를 이용한다면, 여러 개의 컨텍스트 데이터에 접근할 수 있음

  ```js
  const ThemeContext = React.createContext("dark");
  const UserContext = React.createContext("unknown");

  class MyComponent extends React.Component {
    componentDidMount() {
      const { theme, username } = this.props;
      // ...
    }

    // ...
  }

  export default (props) => {
    <UserContext.Consumer>
      {(username) => (
        <ThemeContext.Consumer>
          {(theme) => (
            <MyComponent {...props} username={username} theme={theme} />
          )}
        </ThemeContext.Consumer>
      )}
    </UserContext.Consumer>;
  };
  ```
