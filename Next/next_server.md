## ▶ 웹 서버 직접 띄우기

- 이전까지는 넥스트에 내장된 웹 서버를 사용했음
- 내장된 웹 서버를 사용하지 않고 웹 서버를 직접 띄우면 좀 더 많은 일을 할 수 있음

  - ex) 서버사이드 렌더링 결과를 캐싱할 수 있음

- `express`를 사용해서 직접 웹 서버를 띄워 보자

  ```bash
  $ npm install express
  ```

- 프로젝트 루트에 'server.js' 파일을 만들자

  - 넥스트를 실행하기 위해 필요한 객체와 함수를 생성함
  - `express` 웹 서버에서 처리할 url 패턴을 등록함

  ```js
  // server.js
  const express = require("express");
  const next = require("next");

  const port = 3000;
  const dev = process.env.NODE_ENV !== "production";
  const app = next({ dev });
  const handle = app.getRequestHandler();

  app.prepare().then(() => {
    const server = express();

    server.get("/page/:id", (req, res) => {
      res.redirect(`/page${req.params.id}`);
    });
    server.get("*", (req, res) => {
      return handle(req, res);
    });

    server.listen(port, (err) => {
      if (err) throw err;
    });
  });
  ```

- 아래 명령어를 통해 직접 만든 웹 서버를 띄워보자

  - 브라우저에서 'http://localhost:3000/page/1'로 접속해도 잘 동작하는 것을 확인할 수 있음

  ```bash
  $ node server.js
  ```

- 배포 모드로 실행하는 경우, 먼저 빌드해야 함

  ```bash
  $ npx next build
  $ NODE_ENV=production node server.js
  ```
