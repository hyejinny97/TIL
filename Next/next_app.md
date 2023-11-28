## ▶ 페이지에서 공통 기능 구현하기

- 모든 페이지에서 공통으로 필요한 기능은 `pages/_app.js` 파일에서 구현할 수 있음
- `pages` 폴더 밑에 `_app.js` 파일을 만들어보자

  - `Component` 속성값: 현재 렌더링하려는 페이지의 컴포넌트
  - `pageProps` 속성값: 해당 페이지의 `getInitialProps` 함수가 반환한 값

  ```js
  // pages/_app.js
  import Link from "next/link";

  export default function MyApp({ Component, pageProps }) {
    return (
      <div>
        <Link href="/page1">
          <a>page1</a>
        </Link>
        <Link href="/page2">
          <a>page2</a>
        </Link>
        <Component {...pageProps} />
      </div>
    );
  }
  ```

- MyApp 컴포넌트는 페이지가 전환되는 경우에도 unmount 되지 않음

  - 따라서, MyApp 컴포넌트에서 전역 상탯값을 관리할 수도 있음
