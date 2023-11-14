## ▶ 바벨 플러그인 제작하기

### 🔹 모든 콘솔 로그를 제거하는 바벨 플러그인 제작

- 콘솔 로그 코드의 AST 구조

  - 콘솔 로그 코드는 `ExpressionState` 타입으로 시작됨
  - `CallExpression` 타입: 함수 또는 메서드를 호출
  - `MemberExpression` 타입: 메서드 호출

  ```js
  console.log("asdf");
  ```

  ```json
  {
    "type": "Program",
    "start": 0,
    "end": 20,
    "body": [
      {
        "type": "ExpressionStatement",
        "start": 0,
        "end": 20,
        "expression": {
          "type": "CallExpression",
          "start": 0,
          "end": 19,
          "callee": {
            "type": "MemberExpression",
            "start": 0,
            "end": 11,
            "object": {
              "type": "Identifier",
              "start": 0,
              "end": 7,
              "name": "console"
            },
            "property": {
              "type": "Identifier",
              "start": 8,
              "end": 11,
              "name": "log"
            },
            "computed": false,
            "optional": false
          },
          "arguments": [
            {
              "type": "Literal",
              "start": 12,
              "end": 18,
              "value": "asdf",
              "raw": "'asdf'"
            }
          ],
          "optional": false
        }
      }
    ],
    "sourceType": "module"
  }
  ```

- 콘솔 로그를 제거하는 플러그인 작성

  ```js
  // plugins/remove-log.js
  module.exports = function ({ types: t }) {
    return {
      visitor: {
        ExpressionStatement(path) {
          if (t.isCallExpression(path.node.expression)) {
            if (t.isMemberExpression(path.node.expression.callee)) {
              const memberExp = path.node.expression.callee;
              if (
                memberExp.object.name === "console" &&
                memberExp.property.name === "log"
              ) {
                path.remove();
              }
            }
          }
        },
      },
    };
  };
  ```

- 위에서 만든 플러그인을 바벨 설정해 추가해서 사용 가능

  ```js
  // babel.config.js
  const plugins = ["./plugins/remove-log.js"];
  module.exports = { plugins };
  ```

### 🔹 함수 내부에 콘솔 로그 추가하는 바벨 플러그인 제작

- 함수의 AST 구조

  - `FunctionDeclaration` 타입: 함수 정의
  - `BlockStatement` 타입 노드의 body 속성에 한수의 모든 내부 코드에 대한 노드가 배열로 담겨져 있음

  ```js
  function f1(p1) {
    let v1;
  }
  ```

  ```json
  {
    "type": "Program",
    "start": 0,
    "end": 35,
    "body": [
      {
        "type": "FunctionDeclaration",
        "start": 2,
        "end": 35,
        "id": {
          "type": "Identifier",
          "start": 11,
          "end": 13,
          "name": "f1"
        },
        "expression": false,
        "generator": false,
        "async": false,
        "params": [
          {
            "type": "Identifier",
            "start": 14,
            "end": 16,
            "name": "p1"
          }
        ],
        "body": {
          "type": "BlockStatement",
          "start": 18,
          "end": 35,
          "body": [
            {
              "type": "VariableDeclaration",
              "start": 24,
              "end": 31,
              "declarations": [
                {
                  "type": "VariableDeclarator",
                  "start": 28,
                  "end": 30,
                  "id": {
                    "type": "Identifier",
                    "start": 28,
                    "end": 30,
                    "name": "v1"
                  },
                  "init": null
                }
              ],
              "kind": "let"
            }
          ]
        }
      }
    ],
    "sourceType": "module"
  }
  ```

- 이름이 'on'으로 시작하는 모든 함수에 콘솔 로그를 추가하는 플러그인 작성

  ```js
  // plugins/insert-log.js
  module.exports = function ({ types: t }) {
    return {
      visitor: {
        FunctionDeclaration(path) {
          if (path.node.id.name.substr(0, 2) === "on") {
            path
              .get("body")
              .unshiftContainer(
                "body",
                t.expressionStatement(
                  t.callExpression(
                    t.memberExpression(
                      t.identifier("console"),
                      t.identifier("log")
                    ),
                    [t.stringLiteral(`call ${path.node.id.name}`)]
                  )
                )
              );
          }
        },
      },
    };
  };
  ```

- 위에서 만든 플러그인을 바벨 설정해 추가해서 사용 가능

  ```js
  // babel.config.js
  const plugins = ["./plugins/insert-log.js"];
  module.exports = { plugins };
  ```
