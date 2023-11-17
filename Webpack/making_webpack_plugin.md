## ▶ 플러그인 제작하기

- 플러그인은 모듈의 내용도 수정할 수 있기 때문에, 로더가 할 수 있는 거의 모든 일을 할 수 있음

### 🔹 번들 파일 목록과 크기 정보를 생성하는 플러그인 제작하기

- src 폴더 아래에 'index1.js', 'index2.js' 두 파일을 생성해보자

  ```js
  // index1.js
  function index1() {
    console.log("this is index1");
  }
  index1();
  ```

  ```js
  // index2.js
  function index2() {
    console.log("this is index2");
  }
  index2();
  ```

- 'webpack.config.js' 파일을 만들고, 위 두 파일을 entry에 입력해보자

  ```js
  // webpack.config.js
  const path = require("path");
  const MyPlugin = require("./my-plugin");

  module.exports = {
    entry: {
      app1: "./src/index1.js",
      app2: "./src/index2.js",
    },
    output: {
      filename: "[name].js",
      path: path.resolve(__dirname, "dist"),
    },
    plugins: [new MyPlugin({ showSize: true })],
    mode: "production",
  };
  ```

- 'my-plugin.js' 파일을 만들어보자

  - 플러그인은 클래스로 정의할 수 있음
  - `apply` 메서드에서는 웹팩의 각 처리 단계에서 호출될 콜백 함수를 등록할 수 있음

    - `compiler.hooks.done.tap()`: 웹팩의 실행이 완료됐을 때 호출되는 콜백 함수를 등록
    - `compiler.hooks.emit.tap()`: 웹팩의 결과 파일을 생성하기 직전에 호출되는 콜백 함수를 등록

  - `compilation.assets`에는 웹팩이 생성할 파일의 목록이 들어 있음

  ```js
  // my-plugin.js
  class MyPlugin {
    constructor(options) {
      this.options = options;
    }

    apply(compiler) {
      compiler.hooks.done.tap("MyPlugin", () => {
        console.log("bundling completed");
      });

      compiler.hooks.emit.tap("MyPlugin", (compilation) => {
        let result = "";
        for (const filename in compilation.assets) {
          if (this.options.showSize) {
            const size = compilation.assets[filename].size();
            result += `${filename}(${size})\n`;
          } else {
            result += `${filename}\n`;
          }
        }

        compilation.assets["fileList.txt"] = {
          source: function () {
            return result;
          },
          size: function () {
            return result.length;
          },
        };
      });
    }
  }

  module.exports = MyPlugin;
  ```

- 웹팩을 실행하면, 'dist/fileList.txt' 파일이 생성됨

  ```plain
  app1.js(959)
  app2.js(1015)
  ```
