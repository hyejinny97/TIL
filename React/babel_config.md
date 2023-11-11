# ✔ 바벨 실행 및 설정하기

- 바벨 (Babel): 입력과 출력이 모두 JS 코드인 **컴파일러**

  - 초기 바벨: ES6 코드를 ES5로 변환해주는 컴파일러
  - 현재 바벨: 리액트의 JSX 문법, TS와 같은 정적 타입 언어, 코드 압축, proposal 단계에 있는 문법 등을 사용

- `create-react-app`, `next.js`, `vue-cli`, `nuxt` 등의 도구는 바벨과 웹팩을 기본적으로 포함함

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

## ▶ 확장성과 유연성을 고려한 바벨 설정 방법

- 실습을 위한 바벨 관련 패키지를 설치해보자

  ```bash
  $ npm install @babel/core @babel/cli @babel/plugin-transform-arrow-functions @babel/plugin-transform-template-literals @babel/preset-react babel-preset-minify
  ```

### 🔹 `extends` 속성으로 다른 설정 파일 가져오기

- common 폴더 아래에 `.babelrc` 파일을 만들어보자

  - plugin에 옵션을 설정할 때는 배열로 만들어서 두 번째 자리에 옵션을 넣으면 됨
  - `loose` 옵션: 문자열을 연결할 때 `concat` 메서드를 사용하는 대신 `+` 연산자를 사용함

  ```js
  // common/.babelrc
  {
    "presets": ["@babel/preset-react"],
    "plugins": [
      [
        "@babel/plugin-transform-template-literals",
        {
          "loose": true
        }
      ]
    ]
  }
  ```

- 새로운 `.babelrc` 파일을 생성한 후, `extends` 속성을 사용해 위 파일의 설정을 가져와보자

  - 설정이 중복되는 경우, 기존 설정은 사라지고 현재 파일의 설정으로 결정됨
  - 따라서, 아래에서 위의 `loose` 옵션은 사라지게 됨

  ```js
  // src/example-extends/.babelrc
  {
    "extends": "../../common/.babelrc",
    "plugins": [
      "@babel/plugin-transform-arrow-functions",
      "@babel/plugin-transform-template-literals"
    ]
  }
  ```

- 아래 명령어를 통해 바벨을 실행할 수 있음

  ```bash
  $ npx babel src/example-extends/code.js
  ```

### 🔹 `env` 속성으로 환경별로 설정하기

- `.babelrc` 파일을 생성한 후, `env` 속성을 통해 환경별로 다른 설정을 주자

  - 배포 환경에서는 압축 preset을 사용하도록 설정함

  ```js
  // src/example-env/.babelrc
  {
    "presets": ["@babel/preset-react"],
    "plugins": [
      "@babel/plugin-transform-template-literals",
      "@babel/plugin-transform-arrow-functions"
    ],
    "env": {
      "production": {
        "presets": ["minify"]
      }
    }
  }
  ```

- 아래 명령어를 통해 '배포 환경'에서 바벨 실행 가능 (윈도우의 경우)

  ```bash
  $ set NODE_ENV=production && npx babel ./src/example-env
  ```

- NODE_ENV 환경 변수를 설정하지 않으면, 기본으로 '개발 환경'에서 바벨이 실행됨

### 🔹 `overrides` 속성으로 파일별로 설정하기

- `.babelrc` 파일을 생성한 후, `overrides` 속성을 사용해 파일별로 설정해보자

  - service1 폴더 하위에서 code2.js 파일을 제외한 모든 파일에 화살표 함수 플러그인을 적용함

  ```js
  // src/example-overrides/.babelrc
  {
    "presets": ["@babel/preset-react"],
    "plugins": ["@babel/plugin-transform-template-literals"],
    "overrides": [
      {
        "include": "./service1",
        "exclude": "./service1/code2.js",
        "plugins": ["@babel/plugin-transform-arrow-functions"]
      }
    ]
  }
  ```

- 아래 명령어를 통해 바벨을 실행할 수 있음

  ```bash
  $ npx babel ./src/example-overrides
  ```

## ▶ 전체 설정 파일과 지역 설정 파일

## ▶ 바벨과 폴리필
