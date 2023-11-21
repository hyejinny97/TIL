## ▶ 스타일 적용하기

- 'CSS 파일'을 사용할 경우, HTML 파일에 연결하면 서버사이드 렌더링 시 특별히 고민할 것이 없음
- 'css-module'이나 'css-in-js' 방식을 사용할 경우, 서버사이드 렌더링 시 추가 작업을 해야함

  - 두 방식 모두 JS 코드가 실행되면서 스타일 코드가 DOM에 삽입되는 방식임
  - 서버에는 DOM이 없으므로 별도의 작업을 하지 않으면 서버사이드 렌더링 시 스타일 정보가 HTML에 포함되지 않음

### 🔹 `styled-components`로 스타일 적용해 보기

- 우선, `styled-components` 패키지를 설치해보자

  ```bash
  $ npm install styled-components
  ```

- `styled-components`를 사용해 'App.js' 파일을 수정하자

  ```js
  // src/App.js
  import styled from "styled-components";

  const Container = styled.div`
    background-color: #aaaaaa;
    border: 1px solid blue;
  `;

  export default function App({ page }) {
    // ...
    return <Container>// ...</Container>;
  }
  ```

- 서버사이드 렌더링에서 `styled-components`을 사용한 경우

  - 문제점) 서버로부터 전달된 HTML을 살펴보면 스타일 코드가 없는 것을 확인할 수 있는데, 이로 인해 스타일이 적용되지 않은 화면이 잠시 보이고 클라이언트에서 JS가 실행한 후에야 스타일이 적용됨
  - 따라서, 서버사이드 렌더링 과정에서 스타일을 추출하여 HTML에 삽입해주는 작업이 필요함

### 🔹 서버사이드 렌더링에 스타일 적용하기

- HTML에 스타일 코드를 넣기 위해 'template/index.html' 파일을 수정해보자

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <!-- ... -->
      __STYLE_FROM_SERVER__
    </head>
    <body>
      <div id="root"></div>
    </body>
  </html>
  ```

- 'server.js' 파일을 수정해, 스타일 코드를 HTML에 삽입해보자

  - `ServerStyleSheet`: 스타일을 추출하는 데 사용될 객체
  - `collectStyles` 메서드에 리액트 요소를 입력하면, 스타일 정보를 수집하기 위한 코드가 리액트 요소에 삽입됨
  - `getStyleTags` 메서드를 호출하면 스타일 정보가 추출됨

  ```js
  // src/server.js
  // ...
  import { ServerStyleSheet } from "styled-components";

  // ...
  app.get("*", (req, res) => {
    // ...
    const sheet = new ServerStyleSheet();

    const renderString = renderToString(
      sheet.collectStyles(<App page={page} />)
    );
    const styles = sheet.getStyleTags();
    const initialData = { page };
    const result = html
      .replace('<div id="root"></div>', `<div id="root">${renderString}</div>`)
      .replace("__DATA_FROM_SERVER__", JSON.stringify(initialData))
      .replace("__STYLE_FROM_SERVER__", styles);
  });
  ```

- 결과) 서버로부터 전달되는 HTML 형태

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <script type="application/javascript">
        window.__INITIAL_DATA__ = { page: "about" };
      </script>
      <style data-styled="true" data-styled-versions="5.0.1">
        .jgHfmw {
          background-color: #aaaaaa;
          border: 1px solid blue;
        }
        data-styled.g1[id="sc-AxjAm"] {
          content: "jgHfmw";
        }
      </style>
    </head>
    <body>
      <div id="root">
        <div class="sc-AxjAm jpHfmw">
          <!-- ... -->
        </div>
      </div>
    </body>
  </html>
  ```

- 이로 인해, 스타일 정보가 HTML에 포함되어 전달되므로 사용자는 JS가 실행되지 않더라도 빠르게 스타일이 적용됨 화면을 볼 수 있음
