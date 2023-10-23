# ✔ 컴포넌트의 공통 기능 관리하기

## ▶ 고차 컴포넌트를 이용한 공통 기능 관리

- 고차 컴포넌트: 컴포넌트를 입력으로 받아서 컴포넌트를 출력해 주는 함수
- 고차 컴포넌트를 이용해서 코드 중복을 없앨 수 있음

### 🔹 마운트 시 서버로 이벤트를 보내는 고차 컴포넌트

- 고차 컴포넌트에 `componentDidMount` 생명 주기 메서드를 만들고 그 안에 서버에 이벤트를 보냄

  ```js
  function withMountEvent(InputComponent, componentName) {
    return class OutputComponent extends React.Component {
      componentDidMount() {
        sendMountEvent(componentName)
      }

      render() {
        return <InputComponent {...this.props}>
      }
    }
  }
  ```

  ```js
  function MyComponent() {
    // ...
  }

  export default withMountEvent(MyComponent, "MyComponent");
  ```

### 🔹 마운트 여부를 알려 주는 고차 컴포넌트

- 고차 컴포넌트는 출력되는 컴포넌트의 속성값으로 추가 정보를 제공할 수 있음

  - `react-redux`의 `connect` 함수가 대표적인 예

  ```js
  function withHasMounted(InputComponent) {
    return class OutputComponent extends React.Component {
      state = {
        hasMounted: false,
      };

      componentDidMount() {
        this.setState({ hasMounted: true });
      }

      render() {
        const { hadMounted } = this.state;
        return <InputComponent {...this.props} hasMounted={hasMounted} />;
      }
    };
  }
  ```

### 🔹 로그인 여부에 따라 다르게 보여 주는 고차 컴포넌트

- 로그인한 사용자에게만 화면을 보여 주는 기능

  - 아래처럼, 고차 컴포넌트 내부에서 속성값 일부를 사용하고 입력된 컴포넌트로 나머지 속성값만 내려 줄 수 있음

  ```js
  function withOnlyLogin(InputComponent) {
    return function ({ isLogin, ...rest }) {
      if (isLogin) {
        return <InputComponent {...rest} />;
      } else {
        return <p>권한이 없습니다.</p>;
      }
    };
  }
  ```

### 🔹 클래스 상속을 이용한 고차 컴포넌트

- 입력된 컴포넌트를 상속받아서 새로운 컴포넌트를 생성할 수 있음

  ```js
  function withSomething(InputComponent) {
    return class OutputComponent extends InputComponent {
      // ...
    };
  }
  ```

- 상속되어 생성된 컴포넌트는 입력된 컴포넌트의 멤버 변수와 메서드에 접근할 수 있음

  - 즉, 입력된 컴포넌트로 만들어진 인스턴스의 속성값, 상탯값, 생명 주기 메서드, 기타 멤버 변수 및 메서드에 접근 가능함

  ```js
  function withDebug(InputComponent) {
    return class OutputComponent extends InputComponent {
      render() {
        return (
          <div>
            <p>props: {JSON.stringify(this.props)}</p>
            <p>state: {JSON.stringify(this.state)}</p>
            {super.render()}
          </div>
        );
      }
    };
  }
  ```

  ```js
  function withDiv(InputComponent) {
    return class OutputComponent extends InputComponent {
      render() {
        const rendered = super.render();
        if (rendered && rendered.type !== "div") {
          return React.createElement("div", null, rendered);
        }
        return rendered;
      }
    };
  }
  ```

### 🔹 여러 개의 고차 컴포넌트 사용하기

> 참고: [recompose 패키지의 getDisplayName 함수](https://velog.io/@kwonh/React-%EA%B3%B5%ED%86%B5%EA%B8%B0%EB%8A%A5%EB%B6%84%EB%A6%AC1-%EA%B3%A0%EC%B0%A8%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8Higher-Order-Components)

- 고차 컴포넌트 여러 개를 동시에 사용하는 것도 가능함

  ```js
  withDebug(withDiv(MyComponent));
  ```

- `recompose` 패키지에서 제공하는 `getDisplayName` 함수를 사용해, 고차 컴포넌트의 displayName을 설정해 주면 리액트 개발자 도구에서 디버깅을 편리하게 할 수 있음

  ```js
  import getDisplayName from "recompose/getDisplayName";

  function withSomething(InputComponent) {
    class OutputComponent extends React.Component {
      // ...
    }

    OutputComponent.displayName = `withSomething(${getDisplayName(
      InputComponent
    )})`;

    return OutputComponent;
  }
  ```

### 🔹 고차 컴포넌트를 사용할 때 유의점

- 고차 컴포넌트를 사용하는 순간, 입력되는 컴포넌트의 정적 메서드는 출력되는 컴포넌트에 전달되지 않음

  - 해결법) `hoist-non-react-statics` 패키지를 이용하면, 입력되는 컴포넌트의 모든 정적 메서드를 출력되는 컴포넌트로 연결시켜줄 수 있음

  ```js
  import hoistNonReactStatic from "hoist-non-react-statics";

  function withSomething(InputComponent) {
    class OutputComponent extends React.Component {
      // ...
    }

    hoistNonReactStatic(OutputComponent, InputComponent);
    return OutputComponent;
  }
  ```

### 🔹 고차 컴포넌트의 단점

1. 고차 컴포넌트를 사용하면 속성값이 암묵적으로 넘어옴

   - ex) `react-redux`의 `connect` 고차 컴포넌트를 사용하면 사용자가 명시한 속성값 외에도 `dispatch`라는 함수가 암묵적으로 넘어옴

2. 서로 다른 고차 컴포넌트가 똑같은 속성값 이름을 사용할 때 충돌하는 문제 발생

   - 그 결과, 마지막으로 호출된 고차 컴포넌트의 속성값으로 덮어 씌워짐

3. 의례적인 절차(ceremony)가 필요함

   - 고차 컴포넌트를 만들 때 항상 함수로 감싸 줘야 함
   - displayName을 설정해 줘야 함
   - 정적 메서드를 전달하기 위한 코드 필요

## ▶ 렌더 속성값을 이용한 공통 기능 관리

- 렌더 속성값(render props): 코드 재사용을 위해 함수 타입의 속성값을 이용하는 패턴

### 🔹 마운트 시 서버로 이벤트를 보내는 렌더 속성값

- 함수를 사용한 children 속성값을 render 메서드의 반환값으로 사용

  ```js
  class MountEvent extends React.Component {
    componentDidMount() {
      const { name } = this.props;
      sendMountEvent(name);
    }

    render() {
      const { children } = this.props;
      return children();
    }
  }
  ```

  ```js
  function MyComponent() {
    return (
      <MountEvent name="MyComponent">{() => <div>{/* ... */}</div>}</MountEvent>
    );
  }
  ```

- children 속성값 대신 다른 속성값 이름을 사용해도 무방함

  ```js
  function MyComponent() {
    return (
      <MountEvent name="MyComponent" render={() => <div>{/* ... */}</div>} />
    );
  }
  ```

### 🔹 서버로 요청을 보내는 렌더 속성값

- 데이터가 아직 도착하지 않았다면, 렌더 함수에서 로딩 애니메이션이나 null을 반환하도록 구현

  ```js
  class DataFetcher extends React.Component {
    state = {
      data: null,
    };

    componentDidMount() {
      const { url, parseData } = this.props;
      axios(url).then((response) => {
        const data = parseData(response.data);
        this.setState({ data });
      });
    }

    render() {
      const { children } = this.props;
      const { data } = this.state;

      if (data === null) {
        return <p>데이터 로딩 중...</p>;
      } else {
        return children({ data });
      }
    }
  }
  ```

  ```js
  function MyComponent() {
    return (
      <DataFetcher url="https://..." parseData={parseRepoData}>
        (({data}) =>{" "}
        {
          <div>
            <p>{`name: ${data.name}`}</p>
            <p>{`name: ${data.stars}`}</p>
            <p>{`name: ${data.openIssues}`}</p>
          </div>
        }
        )
      </DataFetcher>
    );
  }

  function parseRepoData(data) {
    return {
      name: data.name,
      stars: data.stargazer_count,
      openIssues: data.open_issues,
    };
  }
  ```

### 🔹 마우스의 위치 정보를 알려 주는 렌더 속성값

- `onMouseMove` 이벤트를 이용해서 특정 돔 요소 위에서 마우스가 움직일 때마다 마우스의 위치값을 알려 주는 렌더 속성값

  ```js
  class MouseTracer extends React.Component {
    state = {
      x: null,
      y: null,
    };

    onMouseMove = (e) => {
      this.setState({
        x: e.clientX,
        y: e.clientY,
      });
    };

    render() {
      const { children } = this.props;
      const { x, y } = this.state;
      return <div onMouseMove={this.onMouseMove}>{children({ x, y })}</div>;
    }
  }
  ```

  ```js
  function MyComponent() {
    return (
      <MouseTracer>{({ x, y }) => <p>{`(x, y): (${x}, ${y})`}</p>}</MouseTracer>
    );
  }
  ```

### 🔹 렌더 속성값 함수의 매개변수를 속성값으로 전달하기

- 위에서 살펴본 렌더 속성값은 렌더 함수에서 정의한 함수의 매개변수를 통해서만 정보를 받을 수 있었음
- 하지만, Wrapper 컴포넌트를 이용하면 렌더 속성값 함수의 매개변수를 컴포넌트의 속성값으로 전달해 줄 수 있음

  ```js
  class MountInfo extends React.Component {
    state = {
      hasMounted: false,
    };

    componentDidMount() {
      this.setState({
        hasMounted: true,
      });
    }

    render() {
      const { children } = this.props;
      const { hasMounted } = this.state;
      return children({ hasMounted });
    }
  }
  ```

  ```js
  class MyComponent extends React.Component {
    componentDidUpdate() {
      const { hasMounted } = this.props;
      console.log(`hasMounted: ${hasMounted}`);
    }

    render() {
      const { hasMounted } = this.props;
      return <p>{`hasMounted: ${hasMounted}`}</p>;
    }
  }
  ```

  ```js
  function MyComponentWrapper(props) {
    return (
      <MountInfo>
        {({ hasMounted }) => <MyComponent {...props} hasMounted={hasMounted} />}
      </MountInfo>
    );
  }
  ```

### 🔹 고차 컴포넌트 vs 렌더 속성값

- 렌더 속성값의 장점

  1. wrapper 컴포넌트를 사용하는 경우를 제외하고, 속성값 이름 충돌 문제가 존재하지 않음

- 렌더 속성값의 단점

  1. 렌더 함수가 호출될 때마다 새로운 함수를 만들기 때문에 성능에 부정적인 영향을 줌
  2. 사용하는 쪽의 렌더 함수가 복잡한 특징을 지님

- 고차 컴포넌트와 렌더 속성값 중 어느 쪽이 더 우월하다고 보기는 힘들며, 거의 모든 경우에 있어서 고차 컴포넌트를 렌더 속성값으로 또는 그 반대로 변환할 수 있음
