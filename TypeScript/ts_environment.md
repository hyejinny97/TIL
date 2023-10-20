# ✔ 타입스크립트 환경 구축하기

## ▶ create-react-app과 next에서 타입스크립트 사용하기

### 🔹 create-react-app에서 타입스크립트 사용하기

- 아래 명령어만 입력하면 타입스크립트 개발 환경이 구축됨

  ```bash
  $ npx create-react-app my-cra --template typescript
  ```

### 🔹 next에서 타입스크립트 사용하기

- next는 프로젝트 폴더에 `tsconfig.json` 파일이 있으면 타입스크립트 개발 환경이라고 인식함
- `tsconfig.json` 파일을 생성한 후, 아래 명령어를 실행하면 next가 `tsconfig.json` 파일에 몇 가지 설정을 자동으로 해줌

  ```bash
  $ npx next
  ```

## ▶ 프레임워크를 사용하지 않고 타입스크립트 환경 구축하기

- 아래 명령어를 통해 프로젝트 폴더를 생성하고 기본적인 설정을 해보자

  - `npm tsx --init`: `tsconfig.json` 파일이 생성됨

  ```bash
  $ npm init -y
  $ npm install typescript react react-dom
  $ npm install @types/react @types/react-dom
  $ npx tsc --init
  ```

### 🔹 `tsconfig.json` 파일에 설정하기

- `jsx` 옵션을 react로 설정하면 JSX 문법으로 작성된 코드가 `React.createElement` 함수 호출로 변환됨
- `outDir` 옵션으로 폴더를 설정해 주면 컴파일된 결과 파일이 설정한 폴더에 생성됨

  ```json
  {
    // ...
    "jsx": "react",
    "outDir": "./dist"
  }
  ```

### 🔹 타입스크립트로 간단한 리액트 코드 작성하기

- `src` 폴더를 생성하고 그 아래에 `App.tsx` 파일과 `index.tsx` 파일을 생성하자
- 아래 명령어를 통해 타입스크립트를 컴파일할 수 있음

  - `outDir` 옵션으로 설정한 폴더를 열어보면, JSX 코드가 `React.createElement` 코드로 변환된 것을 확인할 수 있음

  ```bash
  $ npx tsc
  ```

## ▶ 기타 환경 설정하기

### 🔹 자바스크립트와 타입스크립트를 같이 사용하기

- `tsconfig.json` 파일에 `"allowJs: true"` 옵션을 추가하면 자바스크립트 파일을 가져올 때 에러 없이 컴파일 됨

### 🔹 외부 패키지 사용하기

- lodash 패키지를 사용하기 위해 아래와 먼저 같이 설치해야 함

  - `@types/lodash`을 설치했기 때문에 타입스크립트는 lodash의 타입 정보를 알 수 있음

  ```bash
  $ npm install lodash @types/lodash
  ```

- IDE로 vscode를 사용하면 외부 패키지의 API 목록을 확인할 수 있고, API가 제공하는 함수의 매개 변수 타입과 반환 타입을 확인할 수 있음

### 🔹 자바스크립트가 아닌 모듈과 `window` 객체의 타입 정의하기

- 이미지나 폰트 등 자바스크립트가 아닌 모듈을 가져오려고 하면 컴파일 에러가 발생함

  - 이유) 타입스크립트는 `png` 모듈의 타입을 모르기 때문임
  - 해결법) 타입스크립트에 `png` 확장자를 가지는 모듈의 타입이 문자열이라고 알려줌

  ```ts
  // 컴파일 에러 발생
  import Icon from "./icon.png";
  ```

  ```ts
  // 해결 방법
  declare module "*.png" {
    const content: string;
    export default content;
  }
  ```

- `window` 객체에 우리가 원하는 속성을 추가하고자 할 때 에러 발생

  - 이유) `window` 객체의 타입에는 방금 추가한 속성이 없다고 판단하기 때문
  - 해결법) 기존 정의된 `window` 타입에 우리가 작성한 속성을 추가하면 됨

  ```ts
  // 컴파일 에러 발생
  window.myValue = 123;
  ```

  ```ts
  // 해결 방법
  interface Window {
    myValue: number;
  }
  ```

### 🔹 자바스크립트 최신 문법 사용하기

- `padStart` 메서드는 ES2017에 추가된 문법이므로, 이를 타입스크립트 파일에 그냥 사용하면 컴파일 에러가 발생함

  - 해결법) `tsconfig.json` 파일의 `lib` 옵션에 `es2017`을 추가하면 됨
  - 주의) 타입스크립트는 폴리필을 추가해 주지는 않으므로, `padStart`를 위한 폴리필은 직접 추가해야 함

  ```json
  {
    "compileOptions": {
      "lib": ["dom", "es5", "scripthost", "es2017"]
      // ...
    }
  }
  ```
