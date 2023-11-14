## ▶ 전체 설정 파일과 지역 설정 파일

- 바벨 설정 파일은 크게 두 가지로 나눌 수 있음

  - 1️⃣ 전체(project-wide) 파일: 모든 JS 파일에 적용됨

    - 👉 바벨 버전 7에 추가된 `babel.config.js` 파일

  - 2️⃣ 지역(file-relative) 파일: JS 파일 경로에 따라 결정됨

    - 👉 `.babelrc`, `.babelrc.js` 파일
    - 👉 바벨 설정이 있는 `package.json` 파일

- 프로젝트 루트에 `babel.config.js` 파일을 생성하자

  ```js
  // babel.config.js
  const presets = ["@babel/preset-react"];
  const plugins = [
    [
      "@babel/plugin-transform-template-literals",
      {
        loose: true,
      },
    ],
  ];

  module.exports = { presets, plugins };
  ```

- src/service1 폴더에 `.babelrc` 파일을 생성하자

  ```js
  // src/service1/.babelrc
  {
    "plugins": [
      "@babel/plugin-transform-template-literals",
      "@babel/plugin-transform-arrow-functions"
    ]
  }
  ```

- 아래 명령어를 통해 바벨을 실행해 보자

  - 실행 과정: 지역 설정 파일 → 전체 설정 파일 → 전체 설정과 지역 설정 병합
  - 지역 설정이 전체 설정을 덮어쓰기 때문에, 전체 설정 파일의 loose 옵션이 적용되지 않은 것을 확인할 수 있음

  ```bash
  $ npx babel src
  ```
