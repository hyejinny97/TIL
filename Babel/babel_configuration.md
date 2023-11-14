## ▶ 확장성과 유연성을 고려한 바벨 설정 방법

- 실습을 위한 바벨 관련 패키지를 설치해보자

  ```bash
  $ npm install @babel/core @babel/cli @babel/plugin-transform-arrow-functions @babel/plugin-transform-template-literals @babel/preset-react babel-preset-minify
  ```

### 🔹 `extends` 속성으로 다른 설정 파일 가져오기

- common 폴더 아래에 `.babelrc` 파일을 만들어보자

  - plugin에 옵션을 설정할 때는 배열로 만들어서 두 번째 자리에 옵션을 넣으면 됨
  - `loose` 옵션: 문자열을 연결할 때 `concat` 메서드를 사용하는 대신 `+` 연산자를 사용함

  ```js
  // common/.babelrc
  {
    "presets": ["@babel/preset-react"],
    "plugins": [
      [
        "@babel/plugin-transform-template-literals",
        {
          "loose": true
        }
      ]
    ]
  }
  ```

- 새로운 `.babelrc` 파일을 생성한 후, `extends` 속성을 사용해 위 파일의 설정을 가져와보자

  - 설정이 중복되는 경우, 기존 설정은 사라지고 현재 파일의 설정으로 결정됨
  - 따라서, 아래에서 위의 `loose` 옵션은 사라지게 됨

  ```js
  // src/example-extends/.babelrc
  {
    "extends": "../../common/.babelrc",
    "plugins": [
      "@babel/plugin-transform-arrow-functions",
      "@babel/plugin-transform-template-literals"
    ]
  }
  ```

- 아래 명령어를 통해 바벨을 실행할 수 있음

  ```bash
  $ npx babel src/example-extends/code.js
  ```

### 🔹 `env` 속성으로 환경별로 설정하기

- `.babelrc` 파일을 생성한 후, `env` 속성을 통해 환경별로 다른 설정을 주자

  - 배포 환경에서는 압축 preset을 사용하도록 설정함

  ```js
  // src/example-env/.babelrc
  {
    "presets": ["@babel/preset-react"],
    "plugins": [
      "@babel/plugin-transform-template-literals",
      "@babel/plugin-transform-arrow-functions"
    ],
    "env": {
      "production": {
        "presets": ["minify"]
      }
    }
  }
  ```

- 아래 명령어를 통해 '배포 환경'에서 바벨 실행 가능 (윈도우의 경우)

  ```bash
  $ set NODE_ENV=production && npx babel ./src/example-env
  ```

- NODE_ENV 환경 변수를 설정하지 않으면, 기본으로 '개발 환경'에서 바벨이 실행됨

### 🔹 `overrides` 속성으로 파일별로 설정하기

- `.babelrc` 파일을 생성한 후, `overrides` 속성을 사용해 파일별로 설정해보자

  - service1 폴더 하위에서 code2.js 파일을 제외한 모든 파일에 화살표 함수 플러그인을 적용함

  ```js
  // src/example-overrides/.babelrc
  {
    "presets": ["@babel/preset-react"],
    "plugins": ["@babel/plugin-transform-template-literals"],
    "overrides": [
      {
        "include": "./service1",
        "exclude": "./service1/code2.js",
        "plugins": ["@babel/plugin-transform-arrow-functions"]
      }
    ]
  }
  ```

- 아래 명령어를 통해 바벨을 실행할 수 있음

  ```bash
  $ npx babel ./src/example-overrides
  ```
