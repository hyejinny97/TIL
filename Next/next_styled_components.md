## ▶ styled-components 사용하기

- 넥스트는 `css-in-js` 방식으로 스타일 코드를 작성할 수 있는 `styled-jsx` 패키지를 내장하고 있음
- 다른 패키지를 이용해서 `css-in-js` 방식을 사용하려면 몇 가지 설정을 해야함

  - `css-in-js` 방식을 사용하려면 서버사이드 렌더링 스타일 코드를 추출해서 HTML에 삽입하는 과정이 필요함
  - `styled-jsx` 문법으로 작성한 스타일 코드를 추출하는 코드는 넥스트 내부의 `_document.js` 파일에 있음

- 기존 `_document.js` 파일을 확인해보자

  - `getInitialProps` 메서드에서 추출한 스타일 코드는 컴포넌트의 속성값으로 전달함
  - 전달된 스타일 코드는 HTML을 생성할 때 사용됨
  - `_document.js` 파일은 서버사이드 렌더링 시에만 실행됨

  ```js
  // _document.js
  // ...
  import flush from "styled-jsx/server";

  export default class Document extends Component {
    // ...
    static async getInitialProps(ctx) {
      // ...
      const { html, head } = await ctx.renderPage({ enhanceApp });
      const styled = [
        ...flush(),
        // ...
      ];

      return { html, head, styles };
    }
  }
  ```

### 🔹 `_document.js` 파일 작성하기

- 넥스트에서는 'pages' 폴더 밑에 `_document.js` 파일을 작성할 수 있도록 허용함
- `_document.js` 파일을 직접 생성하면, 넥스트는 내장된 `_document.js` 파일 대신 직접 작성한 파일을 사용하게 됨

- `_document.js` 파일을 생성하고, `styled-components`를 사용하는 코드를 작성해보자

  - 넥스트의 Document 컴포넌트를 상속받아서 컴포넌트를 만듦
  - 넥스트에 내장된 'Document' 컴포넌트의 `getInitialProps` 함수에서는 `styled-jsx`의 스타일 코드를 추출함
  - 'MyDocument' 컴포넌트의 `getInitialProps` 메서드에서는 `styled-components`의 스타일 코드를 추출함

  ```js
  // pages/_document.js
  import Document from "next/document";
  import { ServerStyleSheet } from "styled-components";

  export default class MyDocument extends Document {
    static async getInitialProps(ctx) {
      const sheet = new ServerStyleSheet();
      const originalRenderPage = ctx.renderPage;

      try {
        ctx.renderPage = () => {
          return originalRenderPage({
            enhanceApp: (App) => (props) =>
              sheet.collectStyles(<App {...props} />),
          });
        };

        const initialProps = await Document.getInitialProps(ctx);
        return {
          ...initialProps,
          styles: (
            <>
              {initialProps.styles}
              {sheet.getStyleElement()}
            </>
          ),
        };
      } finally {
        sheet.seal();
      }
    }
  }
  ```

- 'page1.js' 파일에서 `styled-components`를 사용해보자

  ```js
  // pages/page1.js
  // ...
  import styled from "styled-components";

  const MyP = styled.div`
    color: blue;
    font-size: 18px;
  `;

  function Page1() {
    return (
      <div>
        <MyP>{`10 + 20 = ${add(10, 20)}`}</MyP>
      </div>
    );
  }
  ```

### 🔹 서버와 클라이언트의 결괏값 일치시키기

- 문제점) 지금까지의 코드에선 `styled-components`가 서버와 클라이언트에서 생성하는 해시값이 서로 다름

  - 해결책) `styled-components`에서 제공하는 바벨 플러그인을 이용하면 서버와 클라이언트의 결괏값을 일치시킬 수 있음

  ```bash
  $ npm install babel-plugin-styled-components
  ```

- 넥스트에서는 프로젝트 루트에 `.babelrc` 파일을 만들어서 바벨을 설정할 수 있음

  - 이때, `next/babel` 프리셋은 항상 포함시켜야 함

  ```json
  {
    "presets": ["next/babel"],
    "plugins": ["babel-plugin-styled-components"]
  }
  ```

- 배포 모드로 빌드 후 실행한 다음, 브라우저에서 'http://localhost:3000/page1'로 접속해보면 `styled-components`로 작성한 스타일 코드가 HTML에 정상적으로 삽입된 것을 확인할 수 있음

  ```html
  <head>
    <style data-style="" data-styled-version="5.0.1">
      .bcMPWx {
        color: blue;
        font-size: 18px;
      }
      data-styled.g1[id="sc-AxjAm"] {
        content: "bcMPWx";
      }
    </style>
  </head>
  ```
