## ▶ 넥스트 시작하기

- `Next.js` vs `create-react-app`

  - 공통점: 리액트를 기반으로 개발 환경을 구축함
  - 차이점: `create-react-app`은 클라이언트 렌더링만 하는 반면, `Next.js`는 서버사이드 렌더링에 특화된 프레임워크임

- 넥스트 실습을 위해 패키지를 설치하자

  ```bash
  $ npm install next react react-dom
  ```

- 넥스트에서 모든 페이지 컴포넌트는 `pages` 폴더 밑에 만들어야 함

  - 넥스트는 리액트 컴포넌트에서 `react` 모듈을 자동으로 포함시켜 주기 때문에, 직접 import 할 필요가 없음

  ```js
  // pages/page1.js
  function Page1() {
    return (
      <div>
        <p>This is home page</p>
      </div>
    );
  }

  export default Page1;
  ```

- 아래 명령어를 통해 개발 모드로 넥스트를 실행해보자

  - 브라우저에서 'http://localhost:3000/page1'으로 접속하면 서버사이드 렌더링 결과를 확인할 수 있음

  ```bash
  $ npx next
  ```

### 🔹 넥스트의 번들 파일 분석하기

- 아래 명령어를 통해 배포 모드로 빌드 후 실행해보자

  - 넥스트는 프로젝트 루트의 `.next` 폴더 밑에 번들 파일을 생성함

  ```bash
  $ npx next build && npx next start
  ```

- `.next/static` 폴더

  - `pages` 폴더: 각 페이지의 번들 파일이 있음
  - `chunks` 폴더: 여러 페이지에서 공통으로 사용하는 번들 파일이 있음
  - `runtime` 폴더: 웹팩과 넥스트의 런타임과 관련된 번들 파일이 있음

  ```plain
  .next/static
      ↳ GtdPiV1KKRdR5ID37_Kh8
          ↳ pages
      ↳ chunks
      ↳ runtime
  ```

- `.next/server/static` 폴더

  - 이 폴더의 번들 파일은 서버에서 실행되는 코드이기 때문에, 코드가 압축되어 있지 않고 'node_modules' 폴더 밑에 있는 외부 모듈의 코드가 포함되어 있지 않음
  - `_document.js`: 서버 측에서 HTML 요소를 추가하는 용도로 사용
  - `page1.html`: 넥스트는 'page1.js'와 같이 정적인 페이지를 자동으로 미리 렌더링해서 최적화함

  ```plain
  .next/server/static
      ↳ GtdPiV1KKRdR5ID37_Kh8
          ↳ _app.js
          ↳ _document.js
          ↳ _error.js
          ↳ 404.html
          ↳ page1.html
  ```

### 🔹 넥스트의 기본 기능 사용하기

- 프로젝트 루트에 `static` 폴더 밑에 정적 파일을 만들고 경로를 입력하면 정적 파일을 서비스 할 수 있음
- 넥스트에서 제공하는 `Head` 컴포넌트를 사용하면 HTML head 태그에 원하는 돔 요소를 삽입할 수 있음

  - 여러 번 사용하는 것도 가능하며 나중에 하나로 합쳐짐

- 넥스트는 `styled-jsx` 패키지를 통해 css-in-js 방식을 지원함

  - `styled-jsx` 패키지 대신, `styled-components`와 같은 다른 패키지를 사용하는 것도 가능

- 프로젝트 루트에 `static` 폴더를 만들고 'icon.png'를 저장한 후, 'page1.js' 파일을 아래와 같이 수정해보자

  - '/static/icon.png'와 같이 경로를 입력하면, 파일의 내용과 상관없이 항상 같은 경로가 사용되므로 브라우저 캐싱에 불리하다는 단점이 있음
  - 아래에서 선언된 스타일은 이 컴포넌트 내부의 p 요소에만 적용됨

  ```js
  import Head from "next/head";

  function Page1() {
    return (
      <div>
        <p>this is home page</p>
        <img src="/static/icon.png" />
        <Head>
          <title>page1</title>
        </Head>
        <Head>
          <meta name="description" content="hello world" />
        </Head>
        <style jsx>{`
          p {
            color: blue;
            font-size: 18px;
          }
        `}</style>
      </div>
    );
  }
  ```

### 🔹 넥스트가 생성한 HTML 분석하기

- 배포 모드에서 실행한 후, 넥스트가 서버에서 렌더링한 HTML 구조를 확인해보자

  - `type="application/json"`인 script 태그는 서버에서 생성된 데이터를 포함함

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8" />
      <title class="jsx-3486526853">page1</title>
      <meta name="description" content="hello world" class="jsx-3486526853" />
      <!-- ... -->
      <style id="__jsx-3486526853">
        p.jsx-3486526853 {
          color: blue;
          font-size: 18px;
        }
      </style>
    </head>

    <body>
      <div id="__next">
        <div class="jsx-3486526853" data-reactroot="">
          <p class="jsx-3486526853">this is home page</p>
          <img src="/static/icon.png" class="jsx-3486526853" />
        </div>
      </div>
      <script id="__NEXT_DATA__" type="application/json">
        {
          "props": { "pageProps": {} },
          "page": "/page1",
          "query": {},
          "buildId": "6kK0CEd3-S2ycNGNIkqc",
          "nextExport": true,
          "autoExport": true,
          "isFallback": false
        }
      </script>
      <!-- ... -->
    </body>
  </html>
  ```
