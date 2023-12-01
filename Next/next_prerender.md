## ▶ 페이지 미리 렌더링하기

### 🔹 자동으로 미리 렌더링하기

- 넥스트에서 빌드 시 `getInitialProps` 함수가 없는 페이지는 자동으로 미리 렌더링됨

  - 따라서, `getInitialProps` 함수는 꼭 필요한 경우에만 작성하는 것이 좋음
  - 주의) `_app.js` 파일에서 `getInitialProps` 함수를 정의하면 모든 페이지가 미리 렌더링 되지 않음

- 빌드 후 `.next/server/static` 폴더를 확인해 보면, 'page1'은 미리 렌더링된 HTML 파일로 만들어지고 'page2'는 JS 파일로 만들어지는 것을 확인할 수 있음

### 🔹 `next export`로 미리 렌더링하기

- 넥스트에서는 `next export` 명령어를 통해 '전체' 페이지를 미리 렌더링할 수 있음

  ```bash
  $ npx next build && npx next export
  ```

- 이 명령어를 실행하면 프로젝트 루트에 다음과 같은 'out' 폴더가 생성됨

  - `_next` 폴더: 프로젝트 루트의 '.next' 폴더에 있는 번들 파일
  - 'out' 폴더만 있으면 서버에서 넥스트를 실행하지 않고도 정적 페이지를 서비스할 수 있음

  ```plain
  out
    ↳ 404.html
    ↳ page1.html
    ↳ page2.html
    ↳ _next
    ↳ static
          ↳ icon.png
  ```

- 단순히 정적 파일을 서비스하도록 'server.js' 파일을 수정해보자

  ```js
  // server.js
  const express = require("express");

  const server = express();
  server.use(express.static("out"));

  server.listen(3000, (err) => {
    if (err) throw err;
  });
  ```

- 서버를 실행한 후, 브라우저에서 'http://localhost:3000/page2.html?text=hello'로 접속해보자

  - 미리 렌더링된 정적 파일이기 때문에, 쿼리 파라미터가 적용되지 않음
  - 넥스트에서는 쿼리 파라미터도 미리 설정할 수 있는 `exportPathMap` 옵션을 제공해줌

### 🔹 넥스트의 `exportPathMap` 옵션 사용하기

- 넥스트의 `exportPathMap` 옵션을 이용하면 쿼리 파라미터를 활용해서 정적 페이지를 만들 수 있음

- `next.config.js` 파일을 수정해보자

  - `next export` 명령어를 실행할 때 `exportPathMap` 옵션이 사용됨

  ```js
  // next.config.js
  module.exports = {
    // ...
    exportPathMap: function () {
      return {
        "/page1": { page: "/page1" },
        "/page2-hello": { page: "/page2", query: { text: "hello" } },
        "/page2-world": { page: "/page2", query: { text: "world" } },
      };
    },
  };
  ```

- 서버를 실행해보자

  - 'http://localhost:3000/page2-hello'로 접속하면 화면에 'text: hello'가 출력됨
  - 하지만, 'http://localhost:3000/page2'로 접속하는 경우 이에 대한 정적 파일을 미리 만들어 놓지 않았기 때문에 페이지를 찾지 못함
  - 해결책) 동적 페이지와 정적 페이지를 동시에 서비스하면 됨

  ```bash
  $ npx next build && npx next export
  $ node server.js
  ```

### 🔹 동적 페이지와 정적 페이지를 동시에 서비스하기

- 동적 페이지를 서비스하기 위해 넥스트를 실행하면서, 미리 렌더링한 페이지도 같이 서비스할 수 있도록 구현해보자

  - 'out' 폴더에 있는 미리 렌더링된 HTML 파일을 읽어서 prerenderCache에 저장함
  - `next export` 명령어는 배포 모드에서만 사용하므로, out 폴더의 내용을 읽는 작업은 배포 모드에서만 함

  ```js
  // server.js
  // ...
  const fs = require("fs");

  const prerenderList = [
    { name: "page1", path: "/page1" },
    { name: "page2-hello", path: "/page2?text=hello" },
    { name: "page2-world", path: "/page2?text=world" },
  ];

  const prerenderCache = {};
  if (!dev) {
    for (const info of prerenderList) {
      const { name, path } = info;
      const html = fs.readFileSync(`./out/${name}.html`, "utf8");

      prerenderCache[path] = html;
    }
  }

  async function renderAndCache(req, res) {
    const parsedUrl = url.parse(req.url, true);
    const cacheKey = parsedUrl.path;

    if (ssrCache.has(cacheKey)) {
      res.send(ssrCache.get(cacheKey));
      return;
    }

    if (prerenderCache.hasOwnProperty(cacheKey)) {
      res.send(prerenderCache[cacheKey]);
      return;
    }

    // ...
  }
  ```

- 아래 명령어를 통해 배포 모드로 빌드 후 실행해보자

  ```bash
  $ npx next build && npx next export
  $ NODE_ENV=production node server.js
  ```
