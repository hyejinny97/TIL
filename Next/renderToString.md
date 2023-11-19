## ▶ 서버사이드 렌더링 함수 사용해보기 - `renderToString`

- 리액트에서는 서버사이드 렌더링을 위해 아래 4가지의 함수를 제공함

  - `renderToString`
  - `renderToNodeStream`
  - `renderToStaticMarkup`
  - `renderToStaticNodeStream`

- `renderToStaticMarkup`, `renderToStaticNodeStream` 함수는 정적 페이지를 렌더링할 때 사용됨

- 최초 렌더링 이후에도 계속해서 상태 변화에 따라 화면을 갱신해야 한다면, `renderToString`이나 `renderToNodeStream` 함수를 사용해야 함

### 🔹 서버사이드 렌더링을 위한 패키지 설치하기

- 서버사이드 렌더링에 필요한 패키지를 설치해보자

  - `express`: 웹 서버를 띄우기 위해 필요 (Node.js 웹 애플리케이션 프레임워크)

  - `@babel/plugin-transform-modules-commonjs`: ESM으로 작성된 모듈 시스템을 commonJS로 변경

    - 서버에서는 Node 환경에서 JS를 실행하기 때문에 commonJS 모듈 시스템이 필요

  ```bash
  $ npm install express @babel/cli @babel/plugin-transform-modules-commonjs
  ```

### 🔹 웹 서버 코드 작성하기

- 서버에서 사용자의 요청을 받아 처리하는 간단한 웹 서버 코드를 작성해보자

  - `react-dom` 패키지의 server 폴더 밑에 서버에서 사용되는 기능이 모여 있음
  - `express` 객체인 app 변수를 이용해서 미들웨어와 url 경로 설정을 할 수 있음
  - 서버사이드 렌더링 시, 웹팩 빌드 후 생성되는 'dist/index.html'을 기반으로 새로운 HTML을 만들게 됨
  - url이 '/dist'로 시작하는 경우, dist 폴더 밑에 있는 정적 파일로 연결되게 함
  - `renderToString` 함수는 문자열을 반환하는데, 아래에서는 App 페이지를 렌더링함
  - 렌더링된 결과를 반영해서 HTML을 완성해, 클라언트로 전송하게 됨
  - `app.listen()`의 매개변수는 포트 번호를 의미하며, 아래의 경우 3000 포트로 들어오는 클라이언트의 요청을 기다리고 있다는 뜻임

  ```js
  // src/server.js
  import express from "express";
  import fs from "fs";
  import path from "path";
  import { renderToString } from "react-dom/server";
  import React from "react";
  import App from "./App";

  const app = express();
  const html = fs.readFileSync(
    path.resolve(__dirname, "../dist/index.html"),
    "utf8"
  );

  app.use("/dist", express.static("dist"));
  app.get("/favicon.ico", (req, res) => res.sendStatus(204));
  app.get("*", (req, res) => {
    const renderString = renderToString(<App page="home" />);
    const result = html.replace(
      '<div id="root"></div>',
      `<div id="root">${renderToString}</div>`
    );
    res.send(result);
  });

  app.listen(3000);
  ```

### 🔹 바벨 설정하기

- 서버와 클라이언트에서 필요한 바벨 plugin과 preset은 아래와 같음

  |    구분    |                바벨 preset                 |                바벨 plugin                 |
  | :--------: | :----------------------------------------: | :----------------------------------------: |
  | 클라이언트 | `@babel/preset-react`, `@babel/preset-env` |                    없음                    |
  |    서버    |           `@babel/preset-react`            | `@babel/plugin-transform-modules-commonjs` |

- 위 바벨 plugin과 preset을 적용하기 위해 '.babelrc.common.js', '.babelrc.server.js', '.babel.client.js' 파일을 만들자

  ```js
  // .babelrc.common.js
  const presets = ["@babel/preset-react"];
  const plugins = [];

  module.exports = { presets, plugin };
  ```

  ```js
  // .babelrc.client.js
  const config = require("./.babelrc.common.js");
  config.presets.push("@babel/preset-env");

  module.exports = config;
  ```

  ```js
  // .babelrc.server.js
  const config = require("./.babelrc.common.js");
  config.plugins.push("@babel/plugin-transform-modules-commonjs");

  module.exports = config;
  ```

### 🔹 웹팩 설정하기

- 'webpack.config.js'를 수정해보자

  - `publicPath` 설정은 `html-webpack-plugin`이 HTML 생성 시 HTML 내부 리소스 파일의 경로를 만들 때 사용됨
  - 'server.js' 파일에서 url이 '/dist'로 시작하는 경우에만 dist 폴더에 있는 파일을 서비스하도록 설정했기 때문에 `publicPath`도 같게 설정함
  - `babel-loader`를 클라이언트 설정으로 두어, 웹팩을 클라이언트 코드에 대해서만 실행하게 함

  ```js
  // webpack.config.js
  // ...
  module.exports = {
    // ...
    output: {
      // ...
      publicPath: "/dist/",
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          use: "babel-loader",
          options: {
            configFile: path.resolve(__dirname, ".babelrc.client.js"),
          },
        },
      ],
    },
    // ...
  };
  ```

### 🔹 기타 설정 및 프로그램 실행하기

- 서버 측 코드는 `@babel/cli`를 이용해서 바벨만 실행하고, 클라이언트 측 코드는 웹팩을 실행함

- 'package.json'에 빌드와 웹 서버 실행 명령어를 추가하자

  - `build-server` 명령어: 서버 측 코드를 빌드

    - src 폴더 내 모든 파일을 'src/.babelrc.server.js' 설정으로 컴파일

  - `build` 명령어: 서버와 클라이언트의 코드를 모두 빌드

    - 클라이언트 측 코드의 빌드는 웹팩이 실행

  - `start` 명령어: `express` 웹 서버를 띄움

    - 이 명령어는 반드시 빌드 후 실행해야 함

  ```json
  {
    // ...
    "script": {
      "build-server": "babel src --out-dir dist-server --config-file ./.babelrc.server.js",
      "build": "npm run build-server && webpack",
      "start": "node dist-server/server.js"
    }
    // ...
  }
  ```

- 리액트에서 제공하는 `hydrate` 함수를 사용하면, 서버사이드 렌더링의 결과로 만들어진 **돔 요소에 필요한 이벤트 처리 함수를 붙여 줄 수 있음**

  ```js
  // src/index.js
  // ...
  ReactDom.hydrate(<App page="home" />, document.getElementById("root"));
  ```

- 아래 명령어를 통해 실행한 후, 브라우저에서 'http://localhost:3000'으로 접속하면 화면이 제대로 렌더링되고 페이지를 전환하는 버튼도 잘 동작하는 것을 확인할 수 있음

  ```bash
  $ npm run build
  $ npm start
  ```
