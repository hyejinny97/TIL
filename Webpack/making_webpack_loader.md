## ▶ 로더 제작하기

- 로더(loader)는 모듈을 입력으로 받아서 원하는 형태로 변경 후 JS 코드를 반환함

  - 로더가 JS 코드로 반환하기 때문에, 웹팩은 CSS, PNG, CSV 확장자를 갖는 모듈도 처리할 수 있음
  - 단, `css-loader`처럼 중간 과정에서 처리되는 로더는 JS가 아닌 다른 형태의 데이터를 반환할 수도 있음

### 🔹 CSV 모듈을 처리하는 로더 제작하기

- 'member.csv' 파일을 만들어 보자

  ```csv
  index,name,age
  1,mike,23
  2,john,26
  ```

- 'src/index.js' 파일을 만들고, CSV 모듈을 사용하는 코드를 입력해보자

  ```js
  // src/index.js
  import members from "./member.csv";

  for (const row of members.rows) {
    const [_, name, age] = row;
    console.log(`${name} is ${age} years old`);
  }
  ```

- 'webpack.config.js' 파일을 만들고, CSV 모듈을 처리하는 로더를 설정해보자

  ```js
  // webpack.config.js
  const path = require("path");

  module.exports = {
    entry: "./src/index.js",
    output: {
      filename: "main.js",
      path: path.resolve(__dirname, "dist"),
    },
    module: {
      rules: [
        {
          test: /\.csv$/,
          use: "./my-csv-loader",
        },
      ],
    },
    mode: "production",
  };
  ```

- 'my-csv-loader.js' 파일을 생성해보자

  - 로더는 모듈의 내용을 문자열로 입력받는 함수임
  - 아래에서 로더는 result 객체의 내용이 담긴 JS 코드를 반환하게 됨

  ```js
  // my-csv-loader.js
  module.exports = function (source) {
    const result = { header: undefined, rows: [] };

    const rows = source.split("./n");
    for (const row of rows) {
      const cols = row.split(",");
      if (!result.header) {
        result.header = cols;
      } else {
        result.rows.push(cols);
      }
    }

    return `export default ${JSON.stringify(result)}`;
  };
  ```
