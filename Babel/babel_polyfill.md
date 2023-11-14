## ▶ 바벨과 폴리필

- JS의 최신 기능을 모두 사용하면서 오래된 브라우저를 지원하려면, **바벨**과 **폴리필** 모두 사용해야 함

  - 주의) 바벨만 사용하면 최신 JS 표준에 추가된 모든 기능을 사용할 수 없음
  - 즉, 바벨을 사용하더라도 폴리필에 대한 설정은 별도로 해야함

- 폴리필(polyfill): **런타임**에 기능이 존재하는지 검사해 기능이 없는 경우 주입함
- ES8에 추가된 `String.padStart` 메서드는 폴리필을 이용해서 추가할 수 있음

  ```js
  if (!String.prototype.padStart) {
    String.prototype.padStart = func; // 폴리필 함수
  }
  ```

### 🔹 `core-js` 모듈의 모든 폴리필 사용하기

- `core-js`: 바벨에서 폴리필을 위해 공식적으로 지원하는 패키지
- 아래처럼 단순히 `core-js` 모듈을 가져오면 해당 모듈의 모든 폴리필이 포함됨

  - 따라서, 낮은 브라우저에서도 promise, Object.values, 배열의 includes 메서드를 사용할 수 있음

  ```js
  // src/code.js
  import "core-js";

  const p = Promise.resolve(10);
  const obj = {
    a: 10,
    b: 20,
    c: 30,
  };
  const arr = Object.values(obj);
  const exist = arr.includes(20);
  ```

- 웹팩을 사용하는 경우, 아래와 같이 `entry` 속성에 `core-js` 모듈을 넣으면 됨

  ```js
  module.exports = {
    entry: ["core-js", "./src/index.js"],
    // ...
  };
  ```

- `core-js` 모듈의 모든 폴리필을 사용할 때의 장단점

  - 장점: `core-js` 모듈 사용법이 간단함
  - 단점: 필요하지 않은 폴리필까지 포함되므로, 번들 파일의 크기가 커짐

### 🔹 `core-js` 모듈에서 필요한 폴리필만 가져오기

- `core-js` 모듈로부터 직접 필요한 폴리필만 가져오자

  ```js
  // src/code.js
  import "core-js/features/promise";
  import "core-js/features/object/values";
  import "core-js/features/array/includes";

  // ...
  ```

- `core-js` 모듈에서 필요한 폴리필만 가져올 때의 장단점

  - 장점: 번들 파일의 크기를 최소화할 수 있음
  - 단점: 폴리필을 추가하는 과정이 번거롭고, 깜빡하고 추가하지 않는 실수를 할 수 있음

### 🔹 `@babel/preset-env` 프리셋 이용하기

- `@babel/preset-env`: 실행 환경에 대한 정보를 설정해 주면, **자동으로 필요한 기능을 주입해 줌**
- `babel.config.js` 파일을 생성한 후, `@babel/preset-env`을 설정해 주자

  - 이에 의해, **특정 버전의 브라우저를 위한 플러그인만 포함되게 됨**
  - `targets`: 지원하는 브라우저 정보
  - `> 0.25%`: 시장 점유율이 0.25% 이상
  - `not dead`: 업데이트가 종료되지 않은 브라우저

  ```js
  // babel.config.js
  const presets = [
    [
      "@babel/preset-env",
      {
        targets: "> 0.25%, not dead",
      },
    ],
  ];

  module.exports = { presets };
  ```

- `useBuiltIns` 속성을 통해 폴리필과 관련된 설정을 할 수 있음

  - `chrome: "40"`: 크롬 버전을 최소 40으로 설정
  - `useBuiltIns: "entry"`: 지원하는 브라우저에서 필요한 폴리필만 포함시킴
  - `corejs`: 바벨에게 `core-js` 버전을 알려 줌

  ```js
  // babel.config.js
  const presets = [
    [
      "@babel/preset-env",
      {
        targets: {
          chrome: "40",
        },
        useBuiltIns: "entry",
        corejs: { version: 3, proposals: true },
      },
    ],
  ];

  module.exports = { presets };
  ```

- `useBuild` 속성에 `entry`를 입력한 경우, `core-js` 모듈을 가져오는 코드는 각 폴리필 모듈을 가져오는 여러 줄의 코드로 변환됨

  - 아래처럼, 크롬 버전 40에 없는 기능에 대한 폴리필이 수십 줄에 걸쳐 출력됨
  - 즉, 불필요하게 많은 폴리필 코드가 추가됨

  ```js
  // 위 src/code.js를 컴파일한 결과
  "use strict";

  require("core-js/modules/es.symbol");
  require("core-js/modules/es.symbol.description");
  // ...
  require("core-js/modules/web.url-search-params");

  var p = Promise.resolve(10);
  var obj = {
    a: 10,
    b: 20,
    c: 30,
  };
  var arr = Object.values(obj);
  var exist = arr.includes(20);
  ```

- `useBuiltIns` 속성에 `usage`를 입력한 경우, 코드에서 사용된 기능의 폴리필만 추가됨

  - `usage`를 입력할 때는 `core-js` 모듈을 가져오는 코드가 필요하지 않음
  - 컴파일 결과, 코드와 관련된 세 개의 폴리필이 추가됨
  - 바벨이 코드에서 사용된 변수의 타입을 추론하지 못하기 때문에, 문자열의 includes 폴리필이 불필요하게 추가됨

    - TS와 같은 정적 타입 언어를 사용한다면 이런 문제를 쉽게 해결 가능

  ```js
  // 위 src/code.js를 컴파일한 결과
  "use strict";

  require("core-js/modules/es.array.includes");
  require("core-js/modules/es.object.values");
  require("core-js/modules/es.promise");

  require("core-js/modules/es.string.includes");
  require("core-js/modules/es.object.to-string");

  var p = Promise.resolve(10);
  var obj = {
    a: 10,
    b: 20,
    c: 30,
  };
  var arr = Object.values(obj);
  var exist = arr.includes(20);
  ```

- `@babel/preset-env` 프리셋을 이용했을 때의 장단점

  - 장점: 폴리필을 직접 작성하지 않아도 되고, 깜빡하고 추가하지 않는 실수를 방지할 수 있음
  - 단점: 폴리필을 직접 추가하는 방식보다 번들 크기가 큼
