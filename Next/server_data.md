## ▶ 서버 데이터를 클라이언트로 전달하기

- 서버사이드 렌더링 시 서버에서 생성한 데이터를 클라이언트로 전달해보자

  - 이전 코드까지는 항상 Home 컴포넌트가 렌더링됐음
  - 이제는 url에 따라 해당 컴포넌트가 렌더링되게 수정하자

### 🔹 HTML에 서버 데이터 넣기

- HTML에 서버 데이터를 넣기 위해 'template/index.html' 파일을 수정해보자

  - 서버는 '**DATA_FROM_SERVER**' 부분에 필요한 데이터를 채워서 전달하게 됨
  - 클라이언트는 'window.**INITIAL_DATA**'를 통해 서버의 데이터를 받을 수 있음

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>test-ssr</title>
      <script type="text/javascript">
        window.__INITIAL_DATA__ = __DATA_FROM_SERVER__;
      </script>
    </head>
    <body>
      <div id="root"></div>
    </body>
  </html>
  ```

- 'server.js' 파일을 수정해, 서버의 데이터를 HTML에 삽입해보자

  - url 모듈: 문자열로 된 주솟값을 구조체로 변환

  ```js
  // src/server.js
  // ...
  import * as url from "url";

  // ...
  app.get("*", (req, res) => {
    const parseUrl = url.parse(req.url, true);
    const page = parseUrl.pathname ? parseUrl.pathname.substr(1) : "home";

    const renderString = renderToString(<App page={page} />);
    const initialData = { page };
    const result = html
      .replace('<div id="root"></div>', `<div id="root">${renderString}</div>`)
      .replace("__DATA_FROM_SERVER__", JSON.stringify(initialData));
  });
  ```

### 🔹 클라이언트에서 데이터 사용하기

- 'src/index.js' 파일을 수정해, 클라이언트에서 서버의 데이터를 받아 사용해보자

  ```js
  // src/index.js
  // ...
  const initialData = window.__INITIAL_DATA__;

  ReactDom.hydrate(
    <App page={initialData.page} />,
    document.getElementById("root")
  );
  ```

- 리덕스를 사용하는 프로젝트의 경우, 리덕스의 상탯값을 'window.**INITIAL_STATE**'로 전달해 사용할 수 있음
