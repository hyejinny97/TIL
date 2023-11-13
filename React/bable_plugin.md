# ✔ 바벨 플러그인 제작하기

- 바벨은 preset과 plugin을 누구나 제작할 수 있도록 API를 제공함

## ▶ AST 구조 들여다보기

- 바벨은 문자열로 입력되는 코드를 AST(Abstract Syntax Tree)라는 구조체로 만들어 처리함

  - 바벨은 babylon이라는 파서(parser)를 이용해서 AST를 만들게 됨
  - [astexplorer](https://astexplorer.net/) 사이트를 이용하면, 코드로부터 만들어진 AST를 확인할 수 있음

- 플러그인에서는 AST를 기반으로 코드를 변경함

### 🔹 변수 선언 코드로 만들어진 AST

- 아래와 같은 문자열 코드를 AST로 변경한 결과

  - AST의 각 노드는 type 속성이 있음
  - `VariableDeclaration` 타입: 변수 선언
  - `VariableDeclarator` 타입: 선언된 변수
  - `Identifier` 타입: 개발자가 만들어낸 각종 이름
  - `BinaryExpression` 타입: 사칙연산

  ```js
  const v1 = a + b;
  ```

  ```json
  {
    "type": "Program",
    "start": 0,
    "end": 17,
    "body": [
      {
        "type": "VariableDeclaration",
        "start": 0,
        "end": 17,
        "declarations": [
          {
            "type": "VariableDeclarator",
            "start": 6,
            "end": 16,
            "id": {
              "type": "Identifier",
              "start": 6,
              "end": 8,
              "name": "v1"
            },
            "init": {
              "type": "BinaryExpression",
              "start": 11,
              "end": 16,
              "left": {
                "type": "Identifier",
                "start": 11,
                "end": 12,
                "name": "a"
              },
              "operator": "+",
              "right": {
                "type": "Identifier",
                "start": 15,
                "end": 16,
                "name": "b"
              }
            }
          }
        ],
        "kind": "const"
      }
    ],
    "sourceType": "module"
  }
  ```

## ▶ 바벨 플러그인의 기본 구조

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

## ▶ 바벨 플러그인 제작하기: 모든 콘솔 로그 제거

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

## ▶ 바벨 플러그인 제작하기: 함수 내부에 콘솔 로그 추가

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
