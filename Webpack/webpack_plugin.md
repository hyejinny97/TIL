## ▶ 플러그인 사용하기

- 로더는 특정 모듈에 대한 처리만 담당하지만, 플러그인은 웹팩이 실행되는 전체 과정에 개입할 수 있음

- 프로젝트 루트에 `webpack.config.js` 파일을 생성하고, JS 파일을 처리하기 위해서 `babel-loader`를 설정하자

  - chunkhash를 사용하면 파일의 내용이 수정될 때마다 파일 이름이 변경되도록 할 수 있음
  - `babel.config.js` 파일로 바벨을 설정할 수도 있지만, 아래처럼 `babel-loader`에서 직접 바벨 설정을 할 수도 있음

  ```js
  // webpack.config.js
  const path = require("path");

  module.exports = {
    entry: "./src/index.js",
    output: {
      filename: "[name].[chunkhash].js",
      path: path.resolve(__dirname, "dist"),
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-react'],
            }
          }
        }
      ],
    }
    mode: "production",
  };
  ```

### 🔹 `html-webpack-plugin`

- `html-webpack-plugin`: 웹팩이 실행될 때마다 './dist/index.html'이 자동으로 생성되게 함
- `clean-webpack-plugin`: 웹팩이 실행될 때마다 dist 폴더를 정리해줌

  ```bash
  $ npm install clean-webpack-plugin html-webpack-plugin
  ```

- `webpack.config.js` 파일에 플러그인 설정을 추가하자

  - `html-webpack-plugin`에서 `template` 옵션을 통해 우리가 원하는 형태를 기반으로 './dist/index.html'이 생성되도록 할 수 있음

  ```js
  // webpack.config.js
  const path = require("path");
  const { CleanWebpackPlugin } = require("clean-webpack-plugin");
  const HtmlWebpackPlugin = require("html-webpack-plugin");

  module.exports = {
    // ...
    plugins = [
      new CleanWebpackPlugin(),
      new HtmlWebpackPlugin({
        template: './template/index.html',
      })
    ]
  };
  ```

- './template/index.html' 파일을 만들어서 기타 필요한 태그를 추가하면, `html-webpack-plugin`이 생성하는 새로운 HTML 파일에 같이 포함됨

  ```html
  <!-- template/index.html -->
  <html>
    <head>
      <title>웹펙 플러그인 예제</title>
    </head>
    <body>
      <div id="root"></div>
    </body>
  </html>
  ```

- 웹팩을 실행하면 './dist/index.html' 파일이 생성되고, './template/index.html' 파일의 내용을 반영하게 됨

  ```html
  <!-- dist/index.html -->
  <html>
    <head>
      <title>웹펙 플러그인 예제</title>
    </head>
    <body>
      <div id="root"></div>
      <script
        type="text/javascript"
        src="main.8d77122044eebd82d355.js"
      ></script>
    </body>
  </html>
  ```

### 🔹 `DefinePlugin`

- `DefinePlugin`: 모듈 내부에 있는 특정 문자열을 대체해줌

  - 웹팩에 내장된 플러그인으로, 별도로 설치할 필요가 없음

- 먼저 `DefinePlugin`으로 대체할 문자열을 'src/index.js' 파일에 추가해보자

  ```js
  // src/index.js
  // ...
  <div>
    <p>{`앱 버전은 ${APP_VERSION}입니다.`}</p>
    <p>{`10 * 10 = ${TEN * TEN}`}</p>
  </div>
  ```

- `webpack.config.js` 파일에 플러그인 설정을 추가하자

  - `DefinePlugin`은 웹팩 모듈에 포함되어 있음

  ```js
  // webpack.config.js
  // ...
  const webpack = require('webpack')

  module.exports = {
    // ...
    plugins = [
      // ...
      new webpack.DefinePlugin({
        APP_VERSION: '"1.2.3"',
        TEN: '10',
      })
    ]
  };
  ```

### 🔹 `ProvidePlugin`

- JSX 문법을 사용하는 파일을 작성한다면, 바벨이 JSX를 React.createElement 코드로 변환해주기 때문에 반드시 리액트 모듈이 필요함

  - 하지만, 모든 컴포넌트 파일마다 리액트 모듈을 import 키워드를 사용해서 가져오는 것은 귀찮은 일임

- `ProvidePlugin`: 미리 설정한 모듈을 자동으로 등록해줌

  - 웹팩에 내장된 플러그인으로, 별도로 설치할 필요가 없음

- `webpack.config.js` 파일에 플러그인 설정을 추가하자

  - `ProvidePlugin`은 웹팩 모듈에 포함되어 있음

  ```js
  // webpack.config.js
  // ...
  const webpack = require('webpack')

  module.exports = {
    // ...
    plugins = [
      // ...
      new webpack.ProvidePlugin({
        React: 'react',
      })
    ]
  };
  ```
