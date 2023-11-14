## ▶ 바벨을 실행하는 여러 가지 방법

- 바벨을 실행하는 방법 (4가지)

  - 1️⃣ `@babel/cli`로 실행하기
  - 2️⃣ 웹팩에서 `babel-loader`로 실행하기
  - 3️⃣ `@babel/core`로 직접 실행하기
  - 4️⃣ `@babel/register`로 실행하기

- 실습을 위한 바벨 관련 패키지를 설치해보자

  - 바벨을 실행하기 위해서는 `@babel/core` 패키지를 필수로 설치해야 함

  ```bash
  $ npm install @babel/core @babel/cli @babel/plugin-transform-arrow-functions @babel/plugin-transform-template-literals @babel/preset-react
  ```

- 컴파일할 예시 코드를 만들어보자

  ```js
  // src/code.js
  const element = <div>babel test</div>;
  const text = `element type is ${element.type}`;
  const add = (a, b) => a + b;
  ```

### 🔹 `@babel/cli`로 실행하기

- 아래 명령어를 통해 바벨을 실행해보자

  ```bash
  $ npx babel src/code.js --presets=@babel/preset-react --plugins=@babel/plugin-transform-template-literals,@babel/plugin-transform-arrow-functions
  ```

- 바벨을 실행한 결과 코드

  - `@babel/preset-react`: JSX 문법 → `createElement` 함수
  - `@babel/plugin-transform-template-literals`: template literal → 문자열의 `concat` 메서드
  - `@babel/plugin-transform-arrow-functions`: 화살표 함수 → 일반 함수

  ```js
  const element = React.createElement("div", null, "babel test");
  const text = "element type is ".concat(element.type);
  const add = function (a, b) {
    return a + b;
  };
  ```

- 설정할 내용이 많거나 실행 환경에 따라 설정값이 다른 경우 '설정 파일'을 따로 만드는 것이 좋음

  - 바벨 6까지는 `.babelrc` 파일로 설정값을 관리함
  - 바벨 7부터는 `babel.config.js` 파일로 관리하는 것이 좋음

  ```js
  // babel.config.js
  const presets = ["@babel/preset-react"];
  const plugins = [
    "@babel/plugin-transform-template-literals",
    "@babel/plugin-transform-arrow-functions",
  ];

  module.exports = { presets, plugins };
  ```

- 설정 파일을 만든 경우, 아래와 같이 명령어를 간소화할 수 있음

  ```bash
  $ npx babel src/code.js
  ```

### 🔹 웹팩에서 `babel-loader`로 실행하기

- 웹팩을 이용하기 위해 아래의 패키지를 추가 설치해보자

  ```bash
  $ npm install webpack webpack-cli babel-loader
  ```

- `webpack.config.js` 파일을 생성하자

  - `entry` 속성: 웹팩으로 번들링할 파일을 지정
  - `output` 속성: 아래에서 번들링된 결과가 'dist/code/bundle.js' 파일로 저장됨
  - `module`의 `rules` 속성: JS 파일을 `babel-loader`가 처리하도록 설정

    - `babel-loader`는 바벨의 설정 파일 'babel.config.js'을 이용해 처리함

  - `optimization` 속성: JS 파일 압축

  ```js
  // webpack.config.js
  const path = require("path");

  module.exports = {
    entry: "./src/code.js",
    output: {
      path: path.resolve(__dirname, "dist"),
      filename: "code.bundle.js",
    },
    module: {
      rules: [{ test: /\.js$/, use: "babel-loader" }],
    },
    optimization: { minimizer: [] },
  };
  ```

- 아래 명령어를 통해 웹팩이 실행됨

  - 웹팩이 실행되면 'dist/code/bundle.js' 파일이 생성되고, `babel-loader`에 의해 컴파일된 코드를 확인할 수 있음

  ```bash
  $ npx webpack
  ```

### 🔹 `@babel/core`로 직접 실행하기

- 사실 `@babel/cli`와 `babel-loader` 모두 `@babel/core`를 이용해서 바벨을 실행함

- `@babel/core`를 이용해 바벨을 직접 실행해보자

  - `transformSync` 함수를 호출해서 바벨을 실행할 수 있음

  ```js
  // runBabel.js
  const babel = require("@babel/core");
  const fs = require("fs");

  const filename = "./src/code.js";
  const source = fs.readFileSync(filename, "utf8");

  const presets = ["@babel/preset-react"];
  const plugins = [
    "@babel/plugin-transform-template-literals",
    "@babel/plugin-transform-arrow-functions",
  ];

  const { code } = babel.transformSync(source, {
    filename,
    presets,
    plugins,
    configFile: false, // babel.config.js를 사용 x
  });
  ```

- 아래 명령어를 통해 컴파일할 수 있음

  ```bash
  $ node runBabel.js
  ```

- 바벨은 컴파일 시 아래 세 단계를 거치게 됨

  - 1️⃣ 파싱(parse) 단계: 입력된 코드로부터 AST(Abstract Syntax Tree)를 생성함

    - AST: 코드의 구문(syntax)이 분석된 결과를 담고 있는 구조체

  - 2️⃣ 변환(transform) 단계: AST를 원하는 형태로 변환함
  - 3️⃣ 생성(generate) 단계: AST를 코드로 출력함

- `@babel/core`를 직접 사용하는 방식은 자유도가 높다는 장점이 있음

  - 같은 presets를 사용하는 두 가지 설정을 처리해보자
  - 코드가 같다면 AST도 같기 때문에, 같은 코드에 대해서 하나의 AST를 만들어놓고 재사용할 수 있음

  ```js
  const babel = require("@babel/core");
  const fs = require("fs");

  const filename = "./src/code.js";
  const source = fs.readFileSync(filename, "utf8");

  const presets = ["@babel/preset-react"];

  const { ast } = babel.transformSync(source, {
    filename,
    ast: true,
    code: false,
    presets,
    configFile: false,
  });

  const { code: code1 } = babel.transformFromAstSync(ast, source, {
    filename,
    plugins: ["@babel/plugin-transform-template-literals"],
    configFile: false,
  });
  const { code: code2 } = babel.transformFromAstSync(ast, source, {
    filename,
    plugins: ["@babel/plugin-transform-arrow-functions"],
    configFile: false,
  });
  ```
