## ▶ 넥스트에서의 코드 분할

- 넥스트는 기본적으로 페이지별로 번들 파일을 생성함
- 동적 임포트(Dynamic Import) 사용 시에는 해당 모듈의 코드는 별도의 파일로 분할됨
- 여러 페이지에 공통으로 사용되는 모듈도 별도의 파일로 분할됨

### 🔹 동적 임포트로 코드 분할하기

- 동적 임포트를 사용하도록 'page2.js' 파일을 수정하자

  ```js
  // pages/page2.js
  // ...

  export default function Page2({ text, data }) {
    function onClick() {
      import("../src/sayHello").then(({ sayHello }) => console.log(sayHello()));
    }

    return (
      <div>
        // ...
        <button onClick={onClick}>sayHello</button>
      </div>
    );
  }
  ```

  ```js
  // src/sayHello.js
  export function sayHello() {
    return "hello~!";
  }
  ```

- 배포 모드로 넥스트를 실행해보자

  ```bash
  $ npx next build && npx next start
  ```

- 브라우저에서 'http://localhost:3000/page2'로 접속한 후, 버튼을 클릭하는 순간 'sayHello.js' 모듈이 담긴 JS 파일이 전송되는 것을 확인할 수 있음
- `.next/static/chunks` 폴더와 `.next/server` 폴더 밑에 'sayHello.js' 모듈의 코드를 포함하는 번들 파일을 확인할 수 있음

  - 즉, 동적 임포트를 사용하면 클라이언트 뿐만 아니라 서버를 위한 번들 파일도 생성됨

### 🔹 `getInitialProps` 함수에서 동적 임포트 사용하기

- 'page2.js'를 다시 수정해보자

  ```js
  // pages/page2.js
  Page2.getInitialProps = async ({ query }) => {
    const { sayHello } = await import("../src/sayHello");
    console.log(sayHello());
    // ...
  };
  ```

- 브라우저에서 'http://localhost:3000/page2'로 접속을 하면, 'sayHello.js' 모듈이 담긴 JS 파일이 전송되지 않음

  - ∵ `getInitialProps` 함수가 서버 측에서 실행되어 클라이언트로 별도의 파일을 내려 줄 필요가 없기 때문

- 브라우저에서 'http://localhost:3000/page1'로 접속한 후 다시 page2로 이동하는 버튼을 클릭하면, `getInitialProps` 함수가 클라이언트에서 실행되기 때문에 이땐 'sayHello.js' 모듈이 담긴 JS 파일이 전송됨

### 🔹 여러 페이지에서 공통으로 사용되는 코드 분할하기

- 넥스트는 여러 페이지에서 공통으로 사용되는 모듈을 별도의 번들 파일로 분할함

- 'src/util.js' 파일을 만들고, 'page1.js' 파일과 'page2.js' 파일에 'util.js' 모듈을 사용하는 코드를 추가해보자

  - 그 결과, 'util.js' 모듈의 코드는 `.next/static/chunks` 폴더 밑에 있는 파일에 포함된 것을 확인할 수 있음
