## ▶ 서버에서 생성된 데이터를 전달하기

- 넥스트에서는 `getInitialProps` 함수를 이용해 페이지 컴포넌트로 props 값을 전달하게 됨
- 각 페이지의 `getInitialProps` 함수는 페이지 진입 직전에 호출됨
- 사용자가 첫 페이지를 요청하면 `getInitialProps` 함수는 서버에서 호출됨
- 이후, 클라이언트에서 페이지 전환을 하면 `getInitialProps` 함수는 클라이언트에서 호출됨

### 🔹 `getInitialProps` 함수를 이용해 서버 데이터 전달하기

- pages 폴더 밑에 'page2.js' 파일을 생성한 후, `getInitialProps` 함수를 정의하자

  - `getInitialProps` 함수의 매개변수로 다양한 정보가 전달됨
  - `getInitialProps` 함수 내부의 API 호출은 서버 또는 클라이언트에서 호출될 수 있음
  - `getInitialProps` 함수가 반환하는 값은 페이지 컴포넌트의 속성값으로 전달됨

  ```js
  // pages/page2.js
  import { callApi } from "../src/api";

  Page2.getInitialProps = async ({ query }) => {
    const text = query.text || "none";
    const data = await callApi();
    return { text, data };
  };

  export default function Page2({ text, data }) {
    return (
      <div>
        <p>this is home page2</p>
        <p>{`text: ${text}`}</p>
        <p>{`data is ${data}`}</p>
      </div>
    );
  }
  ```

  ```js
  // src/api.js
  export function callApi() {
    return Promise.resolve(123);
  }
  ```

### 🔹 넥스트 실행 및 결과 확인하기

- 개발 모드로 넥스트를 실행해보자

  ```bash
  $ npm next
  ```

- 브라우저에서 'http://localhost:3000/page2?text=abc'으로 접속한 후, HTML을 확인해보자

  - 서버에서 생성된 데이터가 페이지의 렌더링 결과에 잘 반영됐음
  - 서버에서 생성된 데이터가 script 태그를 통해 클라이언트로 잘 전달됐음

  ```html
  <!-- ... -->
  <div>
    <p>this is home page2</p>
    <p>text: abc</p>
    <p>data is 123</p>
  </div>
  <!-- ... -->
  <script id="__NEXT_DATA__" type="application/json">
    {
      "props": { "pageProps": { "text": "abc", "data": 123 } },
      "page": "/page2",
      "query": { "text": "abc" },
      "buildId": "development",
      "isFallback": false
    }
  </script>
  ```

### 🔹 `getInitialProps`에서 HTTP 요청 객체 이용하기

- `getInitialProps` 함수의 매개변수로 HTTP 요청/응답 객체도 전달됨

  - 단, HTTP 요청/응답 객체는 `getInitialProps` 함수가 서버에서 호출되는 경우에만 전달됨
  - 클라이언트에서 호출된 경우에는 navigator 전역 변수를 이용해야 함

  ```js
  MyComponent.getInitialProps = async ({ req }) => {
    const userAgent = req ? req.headers["user-agent"] : navigator.userAgent;
    // ...
  };
  ```
