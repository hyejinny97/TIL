## ▶ 코드 분할

- 애플리케이션의 전체 코드를 하나의 번들 파일로 만들면, 불필요한 코드까지 전송되어 사용자의 요청으로부터 페이지가 렌더링되기까지 오랜 시간 걸릴 수 있음

  - 따라서, 많은 수의 사용자를 대상으로 하는 서비스라면, 응답 시간을 최소화하기 위해 코드를 분할하는게 좋음

- 코드를 분할하는 가장 직관적인 방법은 웹팩의 `entry` 설정값에 페이지별로 파일을 입력하는 것임

  - 같은 종류의 모듈을 사용하는 'index1.js', 'index2.js' 파일을 생성해보자
  - 아래 코드에서 웹팩을 실행해보면, 'page1.js', 'page2.js' 두 파일이 생성됨
  - 하지만, 두 파일 모두 같은 모듈의 내용을 포함하고 있기 때문에 비효율적임

  ```js
  // src/index1.js
  import { Component } from "react";
  import { fill } from "lodash";
  import { add } from "./util";

  const result = fill([1, 2, 3], add(10, 20));
  console.log("this is index1", { result, Component });
  ```

  ```js
  // src/index2.js
  import { Component } from "react";
  import { fill } from "lodash";
  import { add } from "./util";

  const result = fill([1, 2, 3], add(10, 20));
  console.log("this is index2", { result, Component });
  ```

  ```js
  // webpack.config.js
  const path = require("path");
  const { CleanWebpackPlugin } = require("clean-webpack-plugin");

  module.exports = {
    entry: {
      page1: "./src/index1.js",
      page2: "./src/index2.js",
    },
    output: {
      filename: "[name].js",
      path: path.resolve(__dirname, "dist"),
    },
    plugins: [new CleanWebpackPlugin()],
    mode: "production",
  };
  ```

### 🔹 `SplitChunksPlugin`

- 웹팩에서는 코드 분할을 위해 기본적으로 `SplitChunksPlugin`을 내장하고 있음

  - `SplitChunksPlugin`의 기본 동작은 아래와 같음
  - `optimization`의 `splitChunks` 속성을 이용하면 코드를 분할할 수 있음
  - `chunks: async` (기본값): 동적 임포트만 분할
  - `chunks: all`: 모든 유형의 chunk를 포함
  - `minSize: 20000`: 파일 크기가 20kb 이상인 모듈만 분할 대상으로 함
  - `minChunks: 1`: 한 개 이상의 chunk(=번들 파일)에 포함되어 있어야 분할됨
  - `cacheGroup`: 파일 분할은 그룹별로 이루어짐

    - 기본적으로 외부 모듈(vendors)과 내부 모듈(default) 두 그룹으로 설정되어 있음
    - 외부 모듈은 내부 모듈보다 비교적 낮은 비율로 코드가 변경되기 때문에, 브라우저에 오래 캐싱될 수 있다는 장점이 있음

  ```js
  // webpack.config.js
  module.exports = {
    //...
    optimization: {
      splitChunks: {
        chunks: "async",
        minSize: 20000,
        minRemainingSize: 0,
        minChunks: 1,
        maxAsyncRequests: 30,
        maxInitialRequests: 30,
        enforceSizeThreshold: 50000,
        cacheGroups: {
          defaultVendors: {
            test: /[\\/]node_modules[\\/]/,
            priority: -10,
            reuseExistingChunk: true,
          },
          default: {
            minChunks: 2,
            priority: -20,
            reuseExistingChunk: true,
          },
        },
      },
    },
  };
  ```

- `SplitChunkPlugin`을 사용해서 위 코드를 분할해보자

  - 아래처럼 설정하고 웹팩을 실행하면, `lodash`와 `react` 모듈은 'vendor.js' 파일로 만들어짐
  - 'util.js' 모듈은 파일의 크기가 작기 때문에, 'page1.js' 파일에 포함됨

  ```js
  // webpack.config.js
  module.exports = {
    entry: {
      page1: "./src/index1.js",
    },
    //...
    optimization: {
      splitChunks: {
        chunks: "all",
        name: "vendor",
      },
    },
  };
  ```

- 'util.js' 모듈을 내부 모듈 그룹으로 분할하기 위해서 아래와 같이 수정해보자

  - 파일 크기 제한에 걸리지 않도록 `minSize: 10`으로 낮게 설정하자
  - 아래처럼 설정하고 웹팩을 실행하면, 'page1.js', 'vendors.js', 'default.js'이 생성됨
  - 'util.js' 모듈은 'default.js' 번들 파일에 포함되게 됨

  ```js
  // webpack.config.js
  module.exports = {
    entry: {
      page1: "./src/index1.js",
    },
    //...
    optimization: {
      splitChunks: {
        chunks: "all",
        minSize: 10,
        cacheGroups: {
          vendors: {
            test: /[\\/]node_modules[\\/]/,
            priority: 2,
            name: "vendors",
          },
          defaultVendors: {
            minChunks: 1,
            priority: 1,
            name: "default",
          },
        },
      },
    },
  };
  ```

- `cacheGroups`에 새로운 그룹을 추가해서 react 패키지만 별도의 번들 파일로 분할해보자

  - reactBundle 그룹의 우선순위가 vendors 그룹보다 높아야, react 모듈이 vendors 그룹에 들어가지 않음
  - 아래처럼 설정하고 웹팩을 실행하면, react 패키지는 'react.bundle.js' 파일로 분할됨

  ```js
  // webpack.config.js
  module.exports = {
    entry: {
      page1: "./src/index1.js",
    },
    //...
    optimization: {
      splitChunks: {
        chunks: "all",
        cacheGroups: {
          defaultVendors: {
            test: /[\\/]node_modules[\\/]/,
            name: "vendors",
            priority: 1,
          },
          reactBundle: {
            test: /[\\/]node_modules[\\/](react|react-dom[\\/])/,
            name: "react.bundle",
            priority: 2,
            minSize: 100,
          },
        },
      },
    },
  };
  ```

### 🔹 동적 임포트 (Dynamic Import)

- 동적 임포트 (Dynamic Import): 동적으로 모듈을 가져올 수 있는 기능
- 웹팩에서 동적 임포트를 사용하면 해당 모듈의 코드는 자동으로 분할됨

  - `import` 함수를 사용하면 동적으로 모듈을 가져올 수 있음
  - `import` 함수는 프로미스 객체를 반환하기 때문에 `then` 메서드로 연결할 수 있음

  ```js
  // src/index3.js
  function myFunc() {
    import("./util").then(({ add }) =>
      import("lodash").then(({ default: _ }) =>
        console.log("value", _.fill([1, 2, 3], add(10, 20)))
      )
    );
  }
  myFunc();
  ```

- `import` 함수는 프로미스 객체를 반환하기 때문에, `Promise.all`을 사용해 위 코드를 수정할 수 있음

  ```js
  // src/index3.js
  async function myFunc() {
    const [{ add }, { default: _ }] = await Promise.all([
      import("./util"),
      import("lodash"),
    ]);

    console.log("value", _.fill([1, 2, 3], add(10, 20)));
  }
  myFunc();
  ```

- 아래처럼 웹팩을 설정하고 실행해보자

  - `chunkFilename` 속성을 이용해서 동적 임포트로 만들어지는 번들 파일의 이름을 설정할 수 있음
  - 아래처럼 설정하고 웹팩을 실행하면, 'page3.js', '1.chunk.js', '2.chunk.js' 세 파일이 생성됨
  - '1.chunk.js' 파일에는 'util.js' 모듈의 코드가 들어감
  - '2.chunk.js' 파일에는 `lodash` 모듈의 코드가 들어감

  ```js
  // webpack.config.js
  const path = require("path");
  const { CleanWebpackPlugin } = require("clean-webpack-plugin");

  module.exports = {
    entry: {
      page3: "./src/index3.js",
    },
    output: {
      filename: "[name].js",
      chunkFilename: "[name].chunk.js",
      path: path.resolve(__dirname, "dist"),
    },
    plugins: [new CleanWebpackPlugin()],
    mode: "production",
  };
  ```

### 🔹 분할된 파일을 `prefetch`, `preload`로 빠르게 가져오기

- 동적 임포트로 모듈을 불러오는 것은 게으른 로딩(lazy loading)으로도 불림

  - lazy loading은 번들 파일의 크기가 큰 경우, 응답 속도가 느리다는 단점이 있음

- 웹팩에서는 동적 임포트를 사용할 때, HTML의 `prefetch`, `preload` 기능을 활용할 수 있도록 옵션을 제공함
- `prefetch`: 가까운 미래에 필요한 파일이라고 브라우저에게 알려 주는 기능

  - HTML에서 `prefetch`로 설정된 파일은 **브라우저가 바쁘지 않을 때 미리 다운로드됨**
  - 이를 통해 lazy loading의 단점을 보완할 수 있음

- `preload`: 지금 당장 필요한 파일이라고 브라우저에게 알리는 기능

  - HTML에서 `preload`로 설정된 파일은 **첫 페이지 로딩 시 즉시 다운로드됨**
  - 따라서, `preload`를 남발하면 첫 페이지 로딩 속도에 부정적이 영향을 줄 수 있으므로 주의해야 함

- 'util.js' 모듈은 `preload`로 설정하고, `lodash` 모듈은 `prefetch`로 설정해보자

  ```js
  // src/index3.js
  async function myFunc() {
    const [{ add }, { default: _ }] = await Promise.all([
      import(/* webpackPreload: true */, "./util"),
      import(/* webpackPrefetch: true */, "lodash"),
    ]);

    console.log("value", _.fill([1, 2, 3], add(10, 20)));
  }
  myFunc();
  ```

- 웹팩 실행 후, 브라우저에서 개발자 모드로 확인한 HTML 요소는 아래와 같음

  - link 태그는 'page3.js' 파일이 실행되면서 웹팩에 의해 삽입됨
  - 즉, '1.chunk.js' 파일은 `prefetch`가 적용됨
  - 하지만, 아래에서 '2.chunk.js' 파일은 `preload` 설정이 HTML 코드에 반영되지 않았음
  - 사실, `preload`는 첫 페이지 요청 시 전달된 HTML 태그 안에 미리 설정되어 있어야 하므로, 웹팩이 지원할 수 있는 기능이 아님
  - 대신, 웹팩은 'page3.js' 파일이 평가될 때 '2.chunk.js' 파일을 즉시 다운로드함으로써 어느 정도는 `preload` 기능을 흉내내게 됨

  ```html
  <html>
    <head>
      <link rel="prefetch" ad="script" href="1.chunk.js" />
      <script charset="utf-8" src="1.chunk.js"></script>
      <script charset="utf-8" src="2.chunk.js"></script>
    </head>
    <body>
      <script type="text/javascript" src="./page3.js"></script>
    </body>
  </html>
  ```
