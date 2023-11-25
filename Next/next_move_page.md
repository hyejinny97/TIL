## ▶ 페이지 이동하기

- 넥스트는 페이지 이동을 위해 `Link` 컴포넌트와 `Router` 객체를 제공함

### 🔹 `Link` 컴포넌트를 이용해서 페이지 이동하기

- 'page1.js' 파일에서 페이지를 이동하는 코드를 작성해보자

  - 사용자가 `Link` 캄포넌트의 자식 요소를 클릭하면, `href` 속성으로 전달된 페이지로 이동함

  ```js
  // pages/page1.js
  import Link from "next/link";

  function Page1() {
    return (
      <div>
        <Link href="/page2">
          <a>page2로 이동</a>
        </Link>
      </div>
    );
  }
  ```

### 🔹 `Router` 컴포넌트를 이용해서 페이지 이동하기

- 'page2.js' 파일에서 페이지를 이동하는 코드를 작성해보자

  ```js
  // pages/page2.js
  import Router from "next/router";
  // ...

  function Page2({ text, data }) {
    return (
      <div>
        <button onClick={() => Router.push("/page1")}>page1로 이동</button>
      </div>
    );
  }
  ```

- `Link` 컴포넌트를 이용하는 것과 `Router` 객체를 이용하는 것 사이에 기능적인 차이는 없음

  - 단, `Router` 객체가 좀 더 동적인 코드에 적합함
