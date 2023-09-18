## ▶ CSS 작성 방법 결정하기

### 🔹 일반적인 CSS 파일로 작성하기

- CSS 파일도 ESM 문법을 이용해서 JS로 가져올 수 있음

  ```js
  import "./Button.css";
  ```

- 단점) 클래스명이 충돌할 수 있음
  - 서로 다른 컴포넌트에 동일한 클래스명을 사용할 경우, 이전 클래스명의 스타일을 덮어쓰게 됨

### 🔹 css-module로 작성하기

- 장점) 일반적인 CSS 파일에서 클래스명이 충돌할 수 있는 단점 극복 가능
- css-module 파일의 확장자

  ```
  {이름}.module.css
  ```

- css-module은 클래스명 정보를 담고 있는 object를 반환함

  - 각 클래스명에는 고유한 **해시값**이 들어 있음
  - 따라서, 다른 CSS 파일에서 같은 이름의 클래스명을 사용하더라도 충돌 발생 x

  ```js
  import style from "./Button.module.css"; // 클래스명 정보를 담고 있는 object
  import cn from "classnames";

  function Button({ size }) {
    const isBig = size === "big";
    const label = isBig ? "큰 버튼" : "작은 버튼";

    return (
      <div
        className={cn(style.box, { [style.big]: isBig, [style.small]: !isBig })}
      >
        {label}
      </div>
    );
  }
  ```

  ```js
  // css-module로 작성된 CSS 파일의 style object를 출력한 결과
  {
    big: 'Button_big__1AXxH',
    small: 'Button_small__1G4lx',
    button: 'Button_box__D8Lg-'
  }
  ```

### 🔹 Sass로 작성하기

- 장점) Sass 문법에 있는 변수, 믹스인(mixin) 등을 이용하면 스타일 코드 재사용 가능

  ```scss
  $sizeNormal: 100px;

  .button {
    width: $sizeNormal;
  }
  ```

- Sass 문법으로 작성한 파일은 별도의 빌드 단계를 거쳐 CSS 파일로 변환됨

  - create-react-app에는 Sass를 위한 빌드 시스템이 구축되어 있음

- Sass 모듈 시스템을 이용해 다른 scss 파일을 가져와 스타일 코드 재사용 가능

  ```scss
  @import "./shared.scss";

  .button {
    background-color: $infoColor;
  }
  ```

### 🔹 css-in-js로 작성하기

- `styled-components`: ccs-in-js를 지원하는 패키지

  - styled-components는 일반적인 리액트 컴포넌트처럼 사용 가능
  - tagged template literal 사용

  ```bash
  $ npm install styled-components
  ```

- 장점1) CSS 코드가 JS 안에서 관리되기 때문에 공통되는 CSS 코드를 변수로 관리할 수 있음

  ```js
  import styled from 'styled-components';

  const ButtonCommon = styled.div`
    height: 50px;
  `
  const ButtonBig = styled(ButtonCommon)`
    width: 200px;
  `
  const ButtonSmall = styled(ButtonCommon)`
    width: 100px;
  `

  function Button({ size }) { /* ButtonBig, ButtonSmall 사용 */}
  `
  ```

- 장점2) 동적으로 CSS 코드를 작성하기 쉬움

  - template literal에서 expression을 사용하면 컴포넌트의 속성값을 매개변수로 갖는 함수 작성 가능

  ```js
  import styled from "styled-components";

  const ButtonCommon = styled.div`
    width: ${(props) => (props.isBig ? 200 : 100)}px;
    height: 50px;
  `;

  function Button({ size }) {
    const isBig = size === "big";
    const label = isBig ? "큰 버튼" : "작은 버튼";

    return <ButtonCommon isBig={isBig}>{label}</ButtonCommon>;
  }
  ```
