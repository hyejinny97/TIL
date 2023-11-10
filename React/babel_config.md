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

### 🔹 `@babel/babel-loader`로 실행하기

## ▶ 확장성과 유연성을 고려한 바벨 설정 방법

## ▶ 전체 설정 파일과 지역 설정 파일

## ▶ 바벨과 폴리필
