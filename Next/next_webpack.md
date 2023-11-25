## ▶ 웹팩 설정 변경하기

- 넥스트에서는 정적 파일을 서비스하기 위해 프로젝트 루트의 `static` 폴더를 이용함
- 브라우저 캐싱을 최대로 활용하기 위해서는 파일의 내용이 변경되면 파일의 경로도 변경되는게 좋음

  - 웹팩의 `file-loader`를 사용해서 구현 가능

- 우선, `file-loader` 패키지를 설치하자

  ```bash
  $ npm install file-loader
  ```

- `next.config.js` 파일을 생성하고, 웹팩 설정에 `file-loader`를 추가하자

  - webpack 함수의 첫번째 매개변수로 넥스트의 웹팩 설정이 넘어옴
  - `name: "[path][name].[ext]?[hash]"`: 쿼리 파라미터 부분에 hash를 추가해서 파일의 내용이 변경될 때마다 파일의 경로도 수정되도록 함
  - `emitFile: false`: 넥스트는 `static` 폴더의 정적 파일을 그대로 서비스하기 때문에 복사할 필요가 없음

  ```js
  // next.config.js
  module.exports = {
    webpack: (config) => {
      config.module.rules.push({
        test: /.(png|jpg)$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[path][name].[ext]?[hash]",
              emitFile: false,
              publicPath: "/",
            },
          },
        ],
      });

      return config;
    },
  };
  ```

- `file-loader`가 동작하려면 이미지를 모듈로 다뤄야 함

  ```js
  // pages/page1.js
  import Icon from "../static/icon.png";

  function Page1() {
    return (
      <div>
        // ...
        <img src={Icon} />
        // ...
      </div>
    );
  }

  export default Page1;
  ```
