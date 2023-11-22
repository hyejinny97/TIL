## ▶ 페이지를 미리 렌더링하기

- 서버사이드 렌더링 시 렌더링 연산에 CPU가 많이 사용되기 때문에, 한순간에 트래픽이 몰리면 모든 요청을 처리할 수 없음
- 높은 트래픽에 대응하는 방법은 여러 가지가 있음

  - 평상시에는 서버사이드 렌더링을 하다가 서버 부하가 일정 수준을 넘어가면 클라이언트 측에서만 렌더링하게 할 수 있음
  - 데이터 의존성이 전혀 없는 페이지는 빌드 시 미리 렌더링해 놓을 수 있음
  - 데이터 의존성이 낮은 페이지는 의존성이 있는 부분만 클라이언트 측에서 렌더링하고 이외는 빌드 시 미리 서버 측에서 렌더링해 놓을 수 있음

### 🔹 화면의 일부를 클라이언트에서만 렌더링하기

- 사용자의 이름을 보여주는 UI를 'Home.js' 파일에 추가하자

  ```js
  // src/Home.js
  export default function Home({ username }) {
    return (
      <div>
        <h3>This is home page</h3>
        {username && <p>{`${username} 님 안녕하세요`}</p>}
      </div>
    );
  }
  ```

- 서버사이드 렌더링 시에는 사용자 이름 없이 렌더링하고, 클라이언트에서 마운트 이후에 사용자 이름을 API로 받아 오도록 하자

  ```js
  // src/App.js
  function fetchUsername() {
    const usernames = ["mike", "june", "jamie"];

    return new Promise((resolve) => {
      const username = usernames[Math.floor(Math.random() * 3)];
      setTimeout(() => resolve(username, 100));
    });
  }

  export default function App({ page }) {
    // ...
    const [username, setUsername] = useState(null);

    // ...
    useEffect(() => {
      fetchUsername().then((data) => setUsername(data));
    }, []);

    return (
      <Container>
        <div className="container">
          // ...
          <PageComponent username={username} />
        </div>
      </Container>
    );
  }
  ```

### 🔹 일부 페이지를 서버에서 미리 렌더링하도록 리팩터링하기

- 데이터 의존성이 낮은 일부 페이지만 미리 렌더링하도록 리팩터링하자

  - 페이지를 미리 렌더링해서 dist 폴더 밑에 저장함

  ```js
  // src/prerender.js
  import fs from "fs";
  import path from "path";
  import { renderPage, prerenderPages } from "./common";

  for (const page of prerenderPages) {
    const result = renderPage(page);

    fs.writeFileSync(path.resolve(__dirname, `../dist/${page}.html`), result);
  }
  ```

- 'src/common.js' 파일을 만들고, renderPage 함수와 prerenderPages 변수를 정의해보자

  - renderPage 함수는 '\_\_DATA_FROM_SERVER\_\_' 문자열은 변환하지 못한 채로 각 페이지의 HTML 파일을 반환해 줌
  - '\_\_DATA_FROM_SERVER\_\_' 부분은 서버에서 사용자 요청을 처리할 때 데이터를 채워 넣을 예정임

  ```js
  // src/common.js
  import fs from "fs";
  import path from "path";
  import { renderToString } from "react-dom/server";
  import { ServerStyleSheet } from "styled-components";

  const html = fs.readFileSync(
    path.resolve(__dirname, "../dist/index.html"),
    "utf8"
  );

  export const prerenderPages = ["home"];

  export function renderPage(page) {
    const sheet = new ServerStyleSheet();

    const renderString = renderToString(
      sheet.collectStyles(<App page={page} />)
    );
    const styles = sheet.getStyleTags();
    const result = html
      .replace('<div id="root"></div>', `<div id="root">${renderString}</div>`)
      .replace("__STYLE_FROM_SERVER", styles);

    return result;
  }
  ```

### 🔹 미리 렌더링한 페이지 활용하기

- 웹 서버 코드에서 미리 렌더링한 페이지를 활용하도록 'server.js' 파일을 수정하자

  - 'prerender.js' 파일이 실행될 때 미리 렌더링해 놓은 페이지를 prerenderHtml 객체에 저장함

  ```js
  // src/server.js
  // ...
  import { renderPage, prerenderPages } from "./common";

  // ...
  const prerenderHtml = {};
  for (const page of prerenderPages) {
    const pageHtml = fs.readFileSync(
      path.resolve(__dirname, `../dist/${page}.html`),
      "utf8"
    );
    prerenderHtml[page] = pageHtml;
  }

  // ...
  app.get("*", (req, res) => {
    const parseUrl = url.parse(req.url, true);
    const page = parseUrl.pathname ? parseUrl.pathname.substr(1) : "home";

    const initialData = { page };
    const pageHtml = prerenderPages.include(page)
      ? prerenderHtml[page]
      : renderPage(page);

    const result = pageHtml.replace(
      "__DATA_FROM_SERVER__",
      JSON.stringify(initialData)
    );

    res.send(result);
  });

  app.listen(3000);
  ```

### 🔹 웹팩 설정 및 결과 확인하기

- 'prerender.js' 파일을 서버에서 실행하기 위해서는 먼저 웹팩으로 빌드해야 함

  - `getConfig` 함수의 두 번째 매개변수로 name을 추가함
  - 각 name에 해당하는 파일의 번들 파일을 생성하게 됨

  ```js
  // webpack.config.js
  // ...

  function getConfig(isServer, name) {
    return {
      entry: {
        [name]: `./src/${name}`,
      },
      // ...
    };
  }

  module.exports = [
    getConfig(false, "index"),
    getConfig(true, "server"),
    getConfig(true, "prerender"),
  ];
  ```

- 웹팩 빌드 후 일부 페이지를 미리 렌더링하기 위해, 'package.json' 파일의 `build` 스크립트를 수정하자

  ```json
  {
    // ...
    "scripts": {
      "build": "webpack && node dist/prerender.bundle.js",
      "start": "node dist/server.bundle.js"
    }
  }
  ```

- 빌드 명령어를 실행하면, dist 폴더 밑에 'home.html' 파일이 생성되는 것을 확인할 수 있음
