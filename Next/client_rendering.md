## ▶ 클라이언트에서만 렌더링 해보기

- 서버사이드 렌더링을 구현하기 위한 사전 작업으로, 클라이언트에서만 렌더링하는 웹사이트를 만들어 보자
- 실습을 위해 먼저 패키지를 설치해보자

  ```bash
  $ npm install react react-dom
  ```

  ```bash
  $ npm install @babel/core @babel/preset-env @babel/preset-react
  ```

  ```bash
  $ npm install webpack webpack-cli babel-loader clean-webpack-plugin html-webpack-plugin
  ```

### 🔹 컴포넌트 생성하기

- 'Home.js', 'About.js' 컴포넌트를 생성하자

  ```js
  // src/Home.js
  export default function Home() {
    return (
      <div>
        <h3>This is home page</h3>
      </div>
    );
  }
  ```

  ```js
  // src/About.js
  export default function About() {
    return (
      <div>
        <h3>This is about page</h3>
      </div>
    );
  }
  ```

- App 컴포넌트를 생성하고, 버튼을 통해 각 페이지로 이동하는 기능을 구현하자

  - 브라우저에서 뒤로 가기 버튼을 클릭하면, `onpopState` 함수가 호출됨
  - `pushState` 메서드를 통해 브라우저에게 주소가 변경됐다는 것을 알림

  ```js
  // src/App.js
  import Home from "./Home";
  import About from "./About";

  export default function App({ page }) {
    const [page, setPage] = useState(page);

    useEffect(() => {
      window.onpopstate = (event) => {
        setPage(event.state);
      };
    }, []);

    function onChangePage(e) {
      const newPage = e.target.dataset.page;
      window.history.pushState(newPage, "", `/${newPage}`);
      setPage(newPage);
    }

    const PageComponent = page === "home" ? Home : About;

    return (
      <div className="container">
        <button data-page="home" onClick={onChangePage}>
          Home
        </button>
        <button data-page="about" onClick={onChangePage}>
          About
        </button>
        <PageComponent />
      </div>
    );
  }
  ```

- 'index.js' 파일을 생성하고, App 컴포넌트를 렌더링하자

  ```js
  // src/index.js
  import ReactDom from "react-dom";
  import App from "./App";

  ReactDom.render(<App page="home" />, document.getElementById("root"));
  ```

### 🔹 웹팩 설정하기

- 'webpack.config.js' 파일을 생성하자

  ```js
  // webpack.config.js
  const path = require("path");
  const HtmlWebpackPlugin = require("html-webpack-plugin");

  module.exports = {
    entry: "./src/index.js",
    output: {
      filename: "[name].[chunkhash].js",
      path: path.resolve(__dirname, "dist"),
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          use: "babel-loader",
        },
      ],
    },
    plugins: [
      new HtmlWebpackPlugin({
        template: "./template/index.html",
      }),
    ],
    mode: "production",
  };
  ```

- 'template/index.html' 파일을 생성하자

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>test-ssr</title>
    </head>
    <body>
      <div id="root"></div>
    </body>
  </html>
  ```

### 🔹 바벨 설정하기

- 'babel.config.js' 파일을 생성하자

  ```js
  // babel.config.js
  const presets = ["@babel/preset-env", "@babel/prest-react"];
  const plugins = [];

  module.exports = { presets, plugins };
  ```

- 'babel.config.js' 파일의 설정은 `babel-loader`가 실행될 때 적용됨

### 🔹 클라이언트 렌더링 확인하기

- 웹팩을 실행해보자

  ```bash
  $ npx webpack
  ```

- 문제점) 브라우저에서 확인해보면 두 개의 버튼과 문구는 잘 보이지만, 버튼을 클릭해도 의도한 대로 동작하지 않음

  - 이유) url이 'file://'로 시작하기 때문에 `pushState` 메서드를 호출할 때 에러가 발생함
  - 해결법) 서버를 띄우는 방식을 이용하면 자동으로 해결됨

- 첫 요청에 대한 응답으로 돌아오는 HTML에는 돔 요소가 없음

  - 버튼이나 문구의 돔 요소는 JS가 실행되면서 추가됨

- 서버사이드 렌더링을 구현하면 브라우저가 JS를 실행하지 않아도 화면의 내용을 확인할 수 있게 됨
