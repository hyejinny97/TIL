## ▶ React 개발 환경 직접 구축하기

- 하나의 웹 애플리케이션을 만들기 위해서는 UI, 빌드 시스템, 테스트 시스템, 라우팅 시스템 등 신경써야할 것이 많음
- `create-react-app`을 사용하면 손쉽게 리액트 개발환경을 구축할 수 있음

### 🔹 React, React-DOM

- React와 React-DOM 패키지 설치 명령어

  ```bash
  $ npm install react react-dom
  ```

- React 패키지에는 플랫폼 구분 없이 공통으로 사용되는 리액트의 핵심 기능을 담고 있음
  - 따라서, 웹뿐만 아니라 react-native에서도 사용됨
  - cf) react-native를 이용하면 리액트오 안드로이드와 IOS의 네이티브 앱을 만들 수 있음
- 반면, React-DOM 패키지는 웹에서만 사용됨
  - 따라서, 웹에서의 React-DOM 역할을 하는 react-native 코드가 별도로 존재함

#### ➕ 참고) createElement()

```js
React.createElement(component, props, ...children);
```

- 리액트 요소를 반환하는 함수
- component: 문자열(HTML 태그에 해당하는 돔 요소)이나 리액트 컴포넌트
- props: component가 사용하는 데이터
  - ex) 돔 요소의 경우, style, className 등의 데이터
- children: 해당 컴포넌트가 감싸고 있는 내부의 컴포넌트

  ```html
  <!-- HTML -->
  <div>
    <p>Hello</p>
    <p>World</p>
  </div>
  ```

  ```js
  // JS
  React.createElement(
    "div",
    null,
    createElement("p", null, "Hello"),
    createElement("p", null, "World")
  );
  ```

### 🔹 Babel

- 자바스크립트 코드로 변환해 주는 컴파일러
- 역할
  - ES6 문법으로 작성된 코드를 ES5 문법으로 변환 (최신 JS 문법을 지원하지 않는 환경에서도 최신 문법을 사용 가능하게 함)
  - 코드에서 주석 제거
  - 코드 압축
  - **JSX 문법으로 작성된 코드를 createElement 함수를 호출하는 코드로 변환**
- 따라서, Babel을 사용하면 createElement() 함수를 사용할 필요없이 JSX 문법으로 코드 작성 가능
- Babel 설치 명령어

  - `@babel/cli`: commend line에서 Babel을 실행할 수 있는 파일
  - `@babel/preset-react`: JSX로 작성된 코드를 createElement 함수를 이용한 코드로 변환해주는 바벨 플러그인

  ```bash
  $ npm install @babel/core @babel/cli @babel/preset-react
  ```

- Babel 실행 명령어

  - src 폴더에 있는 모든 JS 파일을 `@babel/preset-react` 프리셋을 이용해서 변환 후, 현재 폴더에 같은 이름의 JS 파일을 생성해 줌
  - watch 모드를 실행하면 src 폴더의 JS 파일을 수정할 때마다 자동으로 변환 후 저장해 줌

  ```bash
  $ npx babel --watch src --out-dir . --presets @babel/preset-react
  ```

#### ➕ 참고) JSX 문법

- createElement() 함수를 사용해서 작성하는 것보다 JSX를 사용하는게 간결하고 가독성도 좋음
- HTML에서 태그를 사용하는 방식과 유사
- 다만, 속성값을 작성하는 방법에서 HTML과 차이가 있음
  - class 대신 className 키워드를 사용
  - 속성값의 데이터 타입이 string이 아닌 경우, 중괄호 `{}`를 사용해서 입력해야 함
  - Inline-style을 적용할 때, 속성 이름에 대시 `-`가 있으면 없애고 camel case로 입력해야 함

#### ➕ 참고) Babel plugin과 preset

- Babel은 한 JS 파일을 입력 받아서 또 다른 JS 파일로 출력해 줌
- 이렇게 JS 파일을 변환해 주는 작업은 plugin 단위로 이루어짐
- 하나의 목적을 위해 여러 개의 plugin이 필요할 수 있는데, 이러한 plugin의 집합을 preset이라고 함
- 따라서, `@babel/preset-react`은 리액트 애플리케이션을 만들 때 필요한 plugin을 모아 놓은 preset임

### 🔹 Webpack

- JS로 만든 프로그램을 배포하기 좋은 형태로 묶어주는 도구
- 역할
  - 여러 개의 JS 파일을 하나의 파일로 합쳐줌
  - JS 파일 압축
  - CSS 전처리
- webpack을 실행하면 보통 하나의 JS 파일이 만들어짐
  - 여러 개의 파일로도 분할 가능
- webpack이 만들어 준 JS 파일을 HTML의 `<script>` 태그에 포함시켜줘야 함
- package.json 파일 생성 명령어

  ```bash
  $ npm init -y
  ```

- webpack 패키지 설치 명령어

  ```bash
  $ npm install webpack webpack-cli
  ```

- webpack 패키지 실행 명령어

  - 여러 개의 JS 파일을 하나의 파일로 합쳐줌
  - dist 폴더 아래에 `main.js` 파일이 생성됨
  - HTML에 `<script src='dist/main.js'>` 태그를 추가해야 함

  ```bash
  $ npx webpack
  ```

#### ➕ 참고) JS의 module system

- 하나의 파일이 하나의 모듈
- ES6부터 모듈 시스템이 지원됨
- ES6 이전에는 commonJS 모듈 시스템을 사용했음
- Webpack은 ESM(ES6의 모듈 시스템)과 commonJS를 모두 지원함

#### ➕ 참고) ESM(ES6의 모듈 시스템)

- default export는 한 파일에서 한 번만 사용 가능
- default로 내보내진 코드는 괄호 없이 가져올 수 있고, 이름 변경이 가능함
- default로 내보내진 코드는 괄호를 사용해서 가져올 수 있고, 이름 변경이 불가함
- 단, as 키워드를 사용해 이름을 변경할 수 있음

  ```js
  // App.js
  export default function func1() {}
  export function func2() {}
  export const var1 = 123;
  ```

  ```js
  // index.js
  import myFunc1, { func2, var1 } from "./App.js";
  import { func2 as myFunc2 } from "./App.js";
  ```

#### ➕ 참고) 클래스형 component, 함수형 component

- 기능적인 측면에서 둘은 동일함
- react 버전 16.8부터 hook이라는 기능이 추가되면서, 함수형 컴포넌트에서도 상태값과 생명 주기 함수 코드를 작성 가능해짐
- 가능한 클래스형 컴포넌트보단 함수형 컴포넌트를 작성하는 것이 좋음!
