## ▶ create-react-app으로 시작하기

- `create-react-app`: 리액트로 웹 애플리케이션을 만들기 위한 환경을 제공
- `expo`: 리액트 네이티브의 개발 환경을 제공
- 바벨, 웹팩, 테스트 시스템, HMR(Hot-Module-Replacement), ES6+ 문법, CSS 후처리 등의 개발 환경을 구축해 줌

### 🔹 create-react-app 사용하기

- create-react-app 패키지 설치 및 실행 명령어

  ```bash
  $ npx create-react-app <프로젝트명>
  ```

- project 실행 명령어

  - create-react-app이 로컬 서버를 띄워줌
  - 아래 명령어는 개발 모드에서 동작하므로 배포 시에는 사용 불가

  ```bash
  $ cd <프로젝트명>
  $ npm start
  ```

- project 폴더 내부 구조
  - `index.html`, `index.js`, `package.json` 파일을 제외한 나머지 파일은 수정/삭제 가능
  - 모든 JS, CSS, img, 폰트 파일은 src 폴더 아래에 있어야 함
  - `serviceWorker.js` 파일: PWA(Progressive Web App)와 관련된 코드가 들어있음
  - PWA 기능을 원한다면, `index.js` 파일에 `serviceWorker.register();` 코드를 추가하면 됨

### 🔹 주요 명령어

- `package.json` 파일에서 4가지 npm 스크립트 명령어를 확인할 수 있음

1. 개발 모드로 실행하기

   - 개발 모드로 프로그램을 실행하는 명령어

     ```bash
     $ npm start
     ```

   - HMR에 의해 개발 모드에서 코드를 수정하면 화면에 즉시 반영됨

2. 빌드하기

   - 배포 환경에서 사용할 파일을 만들어 주는 명령어

     ```bash
     $ npm run build
     ```

   - 로컬에서 웹 서버를 실행 시켜주는 명령어

     - serve 패키지: 노드(node.js) 환경에서 동작하는 웹 서버 애플리케이션

     ```bash
      $ npx serve -s build
     ```

3. 테스트 코드 실행하기

   - 테스트 코드 실행 명령어

     - create-react-app에서는 Jest 테스트 프레임워크 사용

     ```bash
     $ npm test
     ```

4. 설정 파일 추출하기

   - 숨겨져 있던 create-react-app 내부 설정 파일을 밖으로 노출시키는 명령어

     - 바벨이나 웹팩의 설정을 변경할 수 있음

     ```bash
     $ npm run eject
     ```

### 🔹 JS 지원 범위

- ES6의 모든 기능을 지원함
- ES6+에서 추가된 객체나 함수를 이용하고 싶다면, 직접 폴리필을 넣어서 사용 가능
- core-js 패키지를 사용하면 다양한 폴리필을 선택적으로 사용할 수 있음

  ```bash
  $ npm install core-js
  ```

### 🔹 코드 분할(code splitting)하기

- 코드 분할을 이용하면 사용자에게 필요한 양의 코드만 내려줄 수 있음
- 동적 임포트 이용해서 코드 분할 가능
- react-router-dom을 이용해서 페이지 단위로 코드 분할 가능

### 🔹 환경 변수 사용하기

- create-react-app에서는 빌드 시점에 환경 변수를 코드로 전달함
- 환경 변수는 `개발`, `테스트`, `배포` 환경별로 다른 값을 적용할 때 유용함
- 환경 변수 코드

  ```js
  process.env.{환경 변수 이름}
  ```

- create-react-app에서는 `NODE_ENV` 환경 변수를 기본으로 제공함

  ```js
  process.env.NODE_ENV;

  // npm start로 실행한 경우 👉 'development'
  // npm test로 실행한 경우 👉 'test'
  // npm run build로 실행한 경우 👉 'production'
  ```

- `NODE_ENV` 환경 변수 외에 다른 환경 변수는 `REACT_APP_` 접두사를 붙여야 함
- 환경 변수는 shell을 이용하거나 `.env` 파일을 이용해 입력 가능
  - ex) `.env.development`, `.env.test`, `.env.production`
- html 파일에서 환경 변수를 사용하려면 `%`로 환경 변수를 감싸주면 됨

  ```html
  <title>%REACT_APP_NODE_VERSION%</title>
  ```

- create-react-app에서는 autoprefixer 패키지를 통해서 CSS에서 `vendor prefix`가 자동으로 붙음
  - CSS3 표준으로 확정되기 이전 또는 브라우저 개발사가 실험적으로 제공하는 기능을 사용하기 위해서는 Vendor Prefix를 사용해야 함
  - 참고) [CSS3 vendor prefix](https://poiemaweb.com/css3-vendor-prefix)
