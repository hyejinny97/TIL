## ▶ 로더 사용하기

- 로더(loader): 모듈을 입력으로 받아서 원하는 형태로 변환한 후 새로운 모듈을 출력해 주는 함수

  - JS 파일, CSS 파일, 이미지 파일, CSV 파일 들 모든 파일은 모듈이 될 수 있음

### 🔹 자바스크립트 파일 처리하기

- `babel-loader`: JS 파일을 처리

  ```bash
  $ npm install babel-loader
  ```

- `babel-loader`는 바벨의 설정 파일 `babel.config.js`을 이용해 JS 파일을 처리함

- JSX 문법으로 작성된 리액트 코드를 처리하기 위해 아래와 같은 패키지를 설치하고, `babel.config.js` 파일을 생성하자

  ```bash
  $ npm install @babel/core @babel/preset-react
  ```

  ```js
  // react 컴포넌트
  function App() {
    return (
      <div className="container">
        <h3 className="title">webpack example</h3>
      </div>
    );
  }
  ```

  ```js
  // babel.config.js
  const presets = ["@babel/preset-react"];

  module.exports = { presets };
  ```

- 프로젝트 루트에 `webpack.config.js` 파일을 생성한 후, `babel-loader`를 설정해주자

  - js 확장자를 갖는 모듈은 `babel-loader`가 처리하도록 설정

  ```js
  // webpack.config.js
  const path = require("path");

  module.exports = {
    entry: "./src/index.js",
    output: {
      filename: "main.js",
      path: path.resolve(__dirname, "dist"),
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: 'babel-loader',
        },
      ],
    }
    mode: "production",
  };
  ```

- 아래 명령어를 통해 웹팩을 실행하면, './dist/main.js' 번들 파일이 생성됨

  ```bash
  $ npx webpack
  ```

- dist 폴더 밑에 'index.html' 파일을 생성하고 실행하여 잘 동작하는지 확인해보자

  ```html
  <!-- dist/index.html -->
  <html>
    <body>
      <div id="root"></div>
      <script src="./main.js"></script>
    </body>
  </html>
  ```

### 🔹 CSS 파일 처리하기

- `css-loader`: CSS 파일을 처리
- `style-loader`: 스타일을 실제 적용

  ```bash
  $ npm install css-loader style-loader
  ```

- 'App.css' 파일을 만들고, index.js에서 사용해보자

  ```css
  .container {
    border: 1px solid blue;
  }

  .title {
    color: red;
  }
  ```

  ```js
  // src/index.js
  import Style from "./App.css";
  // ...
  ```

- `webpack.config.js` 파일에 `css-loader`와 `style-loader`를 설정해주자

  - css 확장자를 갖는 모듈은 `css-loader`와 `style-loader`가 처리하게 됨
  - 로더를 배열로 입력하면 오른쪽 로더부터 실행됨
  - `css-loader`는 css-module 기능을 제공해주거나, `@import`나 `url()` 등의 처리를 도와줌
  - `style-loader`는 `css-loader`가 생성한 CSS 데이터를 `style` 태그로 만들어서, 번들 파일이 브라우저에서 실행될 때 HTML head에 삽입함

  ```js
  // webpack.config.js
  const path = require("path");

  module.exports = {
    // ...
    module: {
      rules: [
        // ...
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        }
      ],
    }
    mode: "production",
  };
  ```

### 🔹 기타 파일 처리하기

- `file-loader`: PNG 모듈을 처리
- `raw-loader`: TXT 모듈을 처리
- JSON 모듈은 웹팩에서 기본적으로 처리해 줌

  ```bash
  $ npm install file-loader raw-loader
  ```

- 'icon.png', 'data.txt', 'data.json' 파일을 만들고, index.js에서 사용해보자

  ```js
  // src/index.js
  import Icon from "./icon.png";
  import Text from "./data.txt";
  import Json from "./data.json";
  // ...
  ```

- `webpack.config.js` 파일에 `file-loader`와 `raw-loader`를 설정해주자

  - `file-loader`는 모듈의 내용을 그대로 복사해서 dist 폴더 밑에 복사본을 만들고, 모듈을 사용하는 쪽에는 해당 모듈의 경로를 넘겨줌
  - `raw-loader`는 모듈의 내용을 그대로 JS 코드로 가져옴

  ```js
  // webpack.config.js
  const path = require("path");

  module.exports = {
    // ...
    module: {
      rules: [
        // ...
        {
          test: /\.(png|jpg|gif)$/,
          use: 'file-loader',
        },
        {
          test: /\.txt$/,
          use: 'raw-loader',
        },
      ],
    }
    mode: "production",
  };
  ```

### 🔹 이미지 파일 요청 횟수 줄이기

- 이미지 파일을 번들 파일에 포함시키면 브라우저의 파일 요청 횟수를 줄일 수 있음

  - 단, 큰 이미지 파일을 번들 파일에 포함시키면 JS가 늦게 실행되므로, 작은 이미지 파일만 포함시키는게 좋음

- `url-loader`: 크기가 작은 이미지 파일을 번들 파일에 포함시킴

  ```bash
  $ npm install url-loader
  ```

- `webpack.config.js` 파일에 `url-loader`를 설정해주자

  - `url-loader`는 파일 크기가 `limit` 설정값보다 작은 경우 번들 파일에 파일의 내용을 포함시킴 (파일의 경로가 아닌, 데이터를 입력함)
  - 만약, 파일의 크기가 `limit` 설정값보다 큰 경우, 다른 로더가 처리할 수 있도록 `fallback` 옵션을 제공함
  - `fallback` 옵션을 입력하지 않으면, 기본적으로 `file-loader`가 처리하게 됨

  ```js
  // webpack.config.js
  const path = require("path");

  module.exports = {
    // ...
    module: {
      rules: [
        // ...
        {
          test: /\.(png|jpg|gif)$/,
          use: [
            {
              loader: 'url-loader',
              options: {
                limit: 8192,
              }
            }
          ]
        },
      ],
    }
    mode: "production",
  };
  ```
