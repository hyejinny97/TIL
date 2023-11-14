## ▶ 웹팩 실행하기

- 아래 명령어를 통해 웹팩 패키지를 설치할 수 있음

  - `webpack-cli`를 이용하면 CLI에서 웹팩을 실행할 수 있음

  ```bash
  $ npm install webpack webpack-cli
  ```

- 아래 명령어를 통해 웹팩을 실행할 수 있음

  - 별다른 설정 없이 웹팩을 실행하면, './src/index.js' 모듈을 입력으로 받아서 './dist/main.js' 번들 파일을 만들게 됨

  ```bash
  $ npx webpack
  ```

### 🔹 설정 파일 이용하기

- 프로젝트 루트에 `webpack.config.js` 파일을 생성하자

  - `entry` 속성: 'index.js' 파일을 입력 파일로 사용
  - `output` 속성: 'dist' 폴더 밑에 'main.js' 번들 파일을 생성
  - `mode` 속성: 'production' 모드로 설정하면, JS 코드 압축을 포함한 여러 가지 최적화 기능이 기본으로 들어가게 됨
  - `optimization` 속성: 파일 압축

  ```js
  const path = require("path");

  module.exports = {
    entry: "./src/index.js",
    output: {
      filename: "main.js",
      path: path.resolve(__dirname, "dist"),
    },
    mode: "production",
    optimization: { minimizer: [] },
  };
  ```

- 실습을 위해 util.js 파일과 index.js 파일을 생성하자

  ```js
  // src/util.js
  export function sayHello(name) {
    console.log("hello", name);
  }
  ```

  ```js
  // src/index.js
  import { sayHello } from "./util";

  function myFunc() {
    sayHello("mike");
    console.log("myFunc");
  }

  myFunc();
  ```

- 아래 명령어를 통해 웹팩을 실행하면, './dist/main.js' 번들 파일이 생성됨

  ```bash
  $ npx webpack
  ```

  ```js
  // dist/main.js
  (() => {
    // webpackBootstrap
    "use strict";
    var __webpack_exports__ = {}; // CONCATENATED MODULE: ./src/util.js

    function sayHello(name) {
      console.log("hello", name);
    } // CONCATENATED MODULE: ./src/index.js

    function myFunc() {
      sayHello("mike");
      console.log("myFunc");
    }

    myFunc();
  })();
  ```
