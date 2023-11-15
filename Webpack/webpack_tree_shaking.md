## ▶ 나무 흔들기

- 나무 흔들기(tree shaking): 불필요한 코드를 제거해 주는 기능
- 웹팩은 기본적으로 나무 흔들기 기능을 제공함

  - 하지만, 나무 흔들기 기능이 제대로 동작하지 않는 경우가 있음

### 🔹 나무 흔들기가 실패하는 경우

- 나무 흔들기는 아래와 같은 경우에는 동작하지 않음

  - 1️⃣ 사용되는 모듈이 ESM이 아닌 경우
  - 2️⃣ 사용하는 쪽에서 ESM이 아닌 다른 모듈 시스템을 사용하는 경우
  - 3️⃣ 동적 임포트(Dynamic Import)를 사용하는 경우

- 즉, 사용되는 쪽과 사용하는 쪽 모두 ESM 문법을 사용하면 나무 흔들기가 제대로 동작함

- 실습을 위해 'util_esm.js'과 'util_commonjs.js' 파일을 생성해보자

  - 'util_esm.js'은 ESM(ECMAScript Modules) 문법을 사용 👉 `import`, `export` 키워드 사용
  - 'util_commonjs.js'은 commonJS 문법을 사용 👉 `require`, `module.exports` 키워드 사용

  ```js
  // util_esm.js
  export function func1() {
    console.log("func1");
  }
  export function func2() {
    console.log("func2");
  }
  ```

  ```js
  // util_commonjs.js
  function func1() {
    console.log("func1");
  }
  function func2() {
    console.log("func2");
  }

  module.exports = { func1, func2 };
  ```

- ESM 문법으로 작성된 모듈을 ESM 문법으로 가져오자

  - 웹팩 실행 후 번들 파일을 열어 보면 func2 함수가 보이지 않음
  - 즉, 나무 흔들기에 의해 fun2 함수가 제거되었음

  ```js
  import { func1 } from "./util_esm";
  func1();
  ```

- CommonJS 문법으로 작성된 모듈을 ESM 문법으로 가져오자

  - 웹팩 실행 후 번들 파일을 열어 보면 func2 함수가 보임
  - 즉, 나무 흔들기가 동작하지 않았음

  ```js
  import { func1 } from "./util_commonjs";
  func1();
  ```

- 주의) ESM 문법으로 작성된 모듈을 ESM 문법을 가져오는 경우일지라도, 모듈 내부에서 자신의 함수를 호출하는 경우에는 웹팩이 해당 함수를 제거하지 않음

  - 모듈이 평가(evaluation)될 때 func2 함수가 실행됨
  - 모듈은 최초로 사용될 때 한 번 평가되는데, 이때 전역 변수 arr가 변경됨
  - 웹팩은 모듈이 평가되는 시점에 호출되는 함수를 제거하지 않음

  ```js
  // util_esm.js
  const arr = [];

  export function func1() {
    console.log("func1", arr.length);
  }
  export function func2() {
    arr.push(10);
    console.log("func2");
  }

  func2();
  ```

- 아래와 같이 동적 임포트를 사용하는 코드에서는 나무 흔들기가 동작하지 않음

  ```js
  import("./util_esm").then((util) => util.func1());
  ```

### 🔹 외부 패키지의 나무 흔들기

- 외부 패키지에서도 나무 흔들기가 적용됨

  - 하지만, 외부 패키지는 다양한 모듈 시스템을 사용하기 때문에 나무 흔들기가 제대로 동작하지 않을 수 있음

- 문제점) `lodash` 패키지는 ESM으로 되어 있지 않기 때문에 나무 흔들기가 동작하지 않음

  - 따라서, 아래에서 lodash의 fill 함수만 사용하지만 웹팩으로 만들어진 번들 파일에는 lodash의 모든 코드가 포함되어 있음 (70.4kb)

  ```js
  import { fill } from "lodash";

  const arr = [1, 2, 3];
  fill(arr, "a");
  ```

- 해결책1) `lodash`는 각 함수를 별도의 파일로 만들어서 제공해주기 때문에, 사용하고자 하는 특정 파일만 불러오면 됨

  - 웹팩을 실행하면 번들 파일에는 fill 함수의 코드만 포함됨 (4.16kb)

  ```js
  import fill from "lodash/fill";
  // ...
  ```

- 해결책2) ESM 모듈 시스템을 사용하는 `lodash-es` 패키지를 사용하는 경우, 나무 흔들기가 제대로 적용됨

  ```js
  import { fill } from "lodash-es";
  // ...
  ```

### 🔹 바벨 사용 시 주의할 점

- 우리가 작성한 코드를 바벨로 컴파일한 이후에도 ESM 문법으로 남아 있어야 함

  - `module: false`로 설정하면, 모듈 시스템을 변경하지 않도록 할 수 있음

  ```js
  const presets = [
    [
      "@babel/preset-env",
      {
        module: false,
        // ...
      },
    ],
  ];
  ```
