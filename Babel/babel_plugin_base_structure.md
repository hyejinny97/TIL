## ▶ 바벨 플러그인의 기본 구조

- 바벨은 preset과 plugin을 누구나 제작할 수 있도록 API를 제공함
- 바벨 플러그인의 기본 구조

  - `types` 매개변수를 이용해서 AST 노드를 생성하거나, AST 노드의 타입을 검사할 수 있음

  ```js
  module.exports = function ({ types: t }) {
    const node = t.BinaryExpression("+", t.Identifier("a"), t.Identifier("b"));
    console.log(t.isBinaryExpression(node));
    return {};
  };
  ```

- 바벨 플러그인 함수가 반환하는 값의 형태

  - visitor 객체 내부에서 노드의 타입 이름으로 된 함수를 정의할 수 있음
  - 해당하는 타입의 노드가 생성되면, 같은 이름의 함수가 호출되게 됨

  ```js
  module.exports = function ({ type: t }) {
    return {
      visitor: {
        Identifier(path) {
          console.log(path.node.name);
        },
        BinaryExpression(path) {
          console.log(path.node.operator);
        },
      },
    };
  };
  ```
