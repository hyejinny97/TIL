## ▶ AST 구조 들여다보기

- 바벨은 문자열로 입력되는 코드를 AST(Abstract Syntax Tree)라는 구조체로 만들어 처리함

  - 바벨은 babylon이라는 파서(parser)를 이용해서 AST를 만들게 됨
  - [astexplorer](https://astexplorer.net/) 사이트를 이용하면, 코드로부터 만들어진 AST를 확인할 수 있음

- 플러그인에서는 AST를 기반으로 코드를 변경함

### 🔹 변수 선언 코드를 AST로 변환하기

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
