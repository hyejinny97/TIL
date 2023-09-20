## ▶ Single Page Application(SPA) 만들기

- 리액트 애플리케이션의 페이지 전환은 SPA 방식으로 개발하는 것이 정석임
- SPA: 초기 요청 시에만 서버에서 첫 페이지를 처리하고, 이후의 라우팅은 클라이언트에서 처리하는 웹 애플리케이션

### 🔹 브라우저 히스토리 API

- 브라우저에는 히스토리에 state을 저장하는 stack이 존재
- 브라우저 히스토리 API로 SPA를 구현하려면 아래 두 가지 기능이 필요함

  - JS에서 브라우저로 **페이지 전환** 요청을 보내야 함 (서버로 요청 x) 👉 `pushState`, `replaceState` 함수
  - 브라우저의 **뒤로 가기**에 의한 페이지 전환 요청을 JS에서 처리해야 함 (서버로 요청 x) 👉 `popState` 이벤트

- `pushState` 함수: 브라우저의 히스토리 스택에 state를 쌓음

  ```js
  window.history.pushState(state, unused, url);
  ```

- `replaceState` 함수: 현재 브라우저의 히스토리 스택에서 가장 최신의 state를 대체함

  ```js
  window.history.replaceState(stateObj, unused, url);
  ```

- `popstate` 이벤트

  - 사용자의 세션 기록 탐색으로 인해 현재 활성화된 기록 항목이 바뀔 때 발생
  - `pushState()`, `replaceState()`는 popstate 이벤트를 발생시키지 않음
  - 브라우저의 뒤로 가기 버튼 등에 의해서 발생됨

  ```js
  window.onpopstate = (e) => {
    console.log(e.state);
  };
  ```

### 🔹 react-router-dom 사용하기

- react-router-dom 패키지도 내부적으로 브라우저 히스토리 API를 사용함
- react-router-dom 설치 명령어

  ```bash
  $ npm install react-router-dom
  ```

- react-router-dom을 사용하기 위해서 전체 컴포넌트를 `BrowserRouter` 컴포넌트로 감싸줘야 함

  ```jsx
  <BrowserRouter>
    <App />
  </BrowserRouter>
  ```

- 페이지를 전환할 때는 `Link` 컴포넌트를 사용해야 함

  - `to` 속성값: 이동할 주소

  ```jsx
  <Link to='/'>홈</Link>
  <Link to='/photo'>사진</Link>
  ```

- `Route` 컴포넌트를 이용해서 각 페이지를 정의

  - 현재 주소가 `path` 속성값으로 시작하면 `component` 속성값이 가리키는 컴포넌트를 렌더링함
  - `exact` 속성값을 입력하면, 그 값이 완전히 일치해야 해당 컴포넌트가 렌더링됨

  ```jsx
  <Route exact path='/' component={Home} />
  <Route path='/photo' component={Photo} />
  ```

- `Route`를 통해 렌더링되는 컴포넌트는 `match` 속성값을 사용할 수 있음

  - `match.url`: `Route` 컴포넌트의 `path` 속성값과 같은 값을 가져옴
  - `match.params.{파라미터 이름}`: `/photo/:photoId`와 같은 `path` 속성값에서 콜론을 사용한 동적 파라미터 값을 가져올 수 있음

  ```js
  function Photos({ match }) {
    return (
      <div>
        <Link to={`${match.url}/dog`}>강아지 사진</Link>
        <Link to={`${match.url}/cat`}>고양이 사진</Link>
        <Route path={`${match.url}/:photoName`} component={Photo} />
      </div>
    );
  }
  ```

  ```js
  function Photo({ match }) {
    return <p>`${match.params.photoName} 사진을 선택하였습니다.`</p>;
  }
  ```
