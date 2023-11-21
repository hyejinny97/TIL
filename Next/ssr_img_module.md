## ▶ 이미지 모듈 적용하기

- 웹팩에서는 JS 파일뿐만 아니라 모든 파일이 모듈이 될 수 있음
- 이미지 파일은 보통 `file-loader`나 `url-loader`를 이용해서 처리됨

  - `file-loader`: 리소스 파일은 output 설정에 지정된 폴더로 복사한 후, JS 코드에서는 복사된 파일의 경로를 반환해 줌
  - 클라이언트 코드에서 `file-loader`로 처리된 리소스는 서버 코드에서도 `file-loader`로 처리해야 함

### 🔹 서버 코드도 웹팩으로 번들링하기

- 서버 코드에서 `file-loader`를 실행하려면, 서버 코드도 웹팩으로 번들링해야 함

- 우선, 'node_modules' 폴더 밑에 있는 모듈을 번들 파일에서 제외시켜주는 `webpack-node-externals` 패키지를 설치하자

  - 서버 코드는 언제든지 'node_modules' 폴더 밑에 있는 모듈을 가져와서 사용할 수 있기 때문에, 서버 코드를 번들링할 때는 'node_modules' 폴더 밑에 있는 모듈까지 하나의 번들 파일로 만들 필요는 없음

  ```bash
  $ npm install webpack-node-externals
  ```

- 'webpack.config.js' 파일을 수정해보자

  - `getConfig` 함수: isServer 매개변수에 따라 웹팩 설정을 반환해 줌
  - 클라이언트는 브라우저의 캐싱 효과 때문에 entry 파일명에서 chunkhash를 사용하지만, 서버는 필요없음
  - `target` 속성에 'node'를 입력하면, 웹팩은 노드에 특화된 번들링 과정을 거침
  - `node` 속성에서 '\_\_dirname: false' 설정을 하지 않으면 '\_\_dirname'에 절대 경로인 `/`가 입력됨
  - 서버 코드는 압축할 필요가 없음
  - `file-loader` 실행 시 클라이언트나 서버 중 한쪽에서만 파일을 복사해도 충분함
  - 웹팩 설정 파일에서 배열을 내보내면, 배열의 각 아이템 개수만큼 웹팩이 실행됨

    - 따라서, 아래에선 클라이언트 코드가 먼저 번들링되고 서버 코드가 그 다음에 번들링됨

  ```js
  // webpack.config.js
  // ...
  const nodeExternals = require("webpack-node-externals");

  function getConfig(isServer) {
    return {
      entry: isServer
        ? { server: "./src/server.js" }
        : { main: "./src/index.js" },
      output: {
        filename: isServer ? "[name].bundle.js" : "[name].[chunkhash].js",
        path: path.resolve(__dirname, "dist"),
        publicPath: "/dist/",
      },
      target: isServer ? "node" : "web",
      externals: isServer ? [nodeExternals()] : [],
      node: {
        __dirname: false,
      },
      optimization: isServer
        ? {
            splitChunks: false,
            minimize: false,
          }
        : undefined,
      module: {
        rules: [
          {
            test: /\.js$/,
            use: {
              loader: "babel-loader",
              options: {
                configFile: path.resolve(
                  __dirname,
                  isServer ? ".babelrc.server.js" : ".babelrc.client.js"
                ),
              },
            },
          },
          {
            test: /\.(png|jpg|gif)$/,
            use: {
              loader: "file-loader",
              options: {
                emitFile: isServer ? false : true,
              },
            },
          },
        ],
      },
      plugins: isServer
        ? []
        : [
            new ClearWebpackPlugin(),
            new HtmlWebpackPlugin({
              template: "./template/index.html",
            }),
          ],
      mode: "production",
    };
  }

  module.exports = [getConfig(false), getConfig(true)];
  ```

### 🔹 이미지 모듈 사용하기

- 'App.js'에서 이미지 모듈을 사용해보자

  ```js
  // src/App.js
  import Icon from "./icon.png";

  // ...
  export default function App({ page }) {
    // ...
    return (
      <Container>
        // ...
        <img src={icon} />
      </Container>
    );
  }
  ```

- 'package.json'에서 빌드 명령어와 웹 서버를 띄우는 명령어를 수정하자

  ```json
  {
    // ...
    "scripts": {
      "build": "webpack",
      "start": "node dist/server.bundle.js"
    }
  }
  ```
