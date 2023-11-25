## ▶ 에러 페이지 구현하기

- 별도로 에러 페이지를 구현하지 않았다면, 넥스트에서 기본으로 제공되는 에러 페이지가 사용됨

- 에러 페이지를 직접 구현하고 싶으면, `_error.js` 파일을 작성하면 됨

  - statusCode 변수의 값에 따라 다른 에러 메시지를 출력함
  - statusCode 변수의 값이 존재하지 않으면 클라이언트 측에서 발생한 에러임

  ```js
  // pages/_error.js

  ErrorPage.getInitialProps = ({ res, err }) => {
    const statusCode = res ? res.statusCode : err ? err.statusCode : null;
    return { statusCode };
  };

  export default function ErrorPage({ statusCode }) {
    return (
      <div>
        {statusCode === 404 && "페이지를 찾을 수 없습니다."}
        {statusCode === 500 && "알 수 없는 에러가 발생했습니다."}
        {!statusCode && "클라이언트에서 에러가 발생했습니다."}
      </div>
    );
  }
  ```

- 'page2.js' 파일을 수정해 고의로 에러를 발생시켜 보자

  ```js
  // pages/page2.js
  Page2.getInitialProps = async ({ query }) => {
    throw new Error("exception in getInitialProps");
  };
  // ...
  ```

- 배포 모드로 넥스트를 실행한 후, 에러 페이지의 문구를 확인해보자

  - 브라우저에서 'http://localhost:3000/abc'로 접속 시, "페이지를 찾을 수 없습니다." 문구가 뜸
  - 브라우저에서 'http://localhost:3000/page2'로 접속 시, "알 수 없는 에러가 발생했습니다." 문구가 뜸
  - 브라우저에서 'http://localhost:3000/page1'로 접속 후 page2로 이동하는 버튼 클릭 시, "클라이언트에서 에러가 발생했습니다." 문구가 뜸
