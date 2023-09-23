# ✔ 함수

- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분
  - 함수 선언식 (function declaration)
  - 함수 표현식 (function expression)
- 참고) JavaScript의 함수는 [일급 객체(First-class citizen)](https://developer.mozilla.org/ko/docs/Glossary/First-class_Function)에 해당
  - 함수를 다른 변수와 동일하게 다루는 언어는 일급 함수를 가졌다고 표현
  - 일급 객체: 다음의 조건들을 만족하는 객체를 의미함
    - 변수에 할당 가능
    - 함수를 다른 함수의 인자로 전달 가능
    - 함수가 함수를 반환할 수 있음

## ▶ 함수 선언식 (function declaration)

- 함수의 이름과 함께 정의하는 방식
- 3가지 부분으로 구성

  - 함수의 이름 (name)
  - 매개변수 (args)
  - 함수 body (중괄호 내부)

  ```javascript
  function 함수명(매개변수) {
    명령문;
  }

  함수명(); // 함수 호출
  ```

- 함수 선언식의 데이터 타입은 function

  ```javascript
  function add(args) {}

  console.log(typeof add); // fuction
  ```

- 호이스팅 일어남

  - 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생
  - 즉, 함수 호출 이후에 선언 해도 동작

  ```javascript
  add(2, 7); // 9

  function add(num1, num2) {
    return num1 + num2;
  }
  ```

## ▶ 함수 표현식(function expression)

- 함수를 표현식 내에서 정의하는 방식
  - 참고) 표현식: 어떤 하나의 값으로 결정되는 코드의 단위
- 함수의 이름을 생략하고 익명 함수로 정의 가능
  - 익명 함수(anonymous function): 이름이 없는 함수
  - 익명 함수는 함수 표현식에서만 가능
- 3가지 부분으로 구성

  - 함수의 이름 (생략 가능)
  - 매개변수 (args)
  - 함수 body (중괄호 내부)

  ```javascript
  const 함수명 = function (매개변수) {
    명령문;
  };

  함수명(); // 함수 호출
  ```

- 함수 표현식의 데이터 타입은 function

  ```javascript
  const sub = function sub(args) {};

  console.log(typeof sub); // fuction
  ```

- 호이스팅 일어나지 않음

  - 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
  - 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

  ```javascript
  sub(7, 2); // Uncaught ReferenceError: Cannot access 'sub' before initialization

  const sub = function (num1, num2) {
    return num1 - num2;
  };
  ```

  - 함수 표현식을 var 키워드로 작성한 경우, 변수가 선언 전 undefined로 초기화 되어 다른 에러가 발생

  ```javascript
  console.log(sub); // undefined
  sub(7, 2); // Uncaught TypeError: sub is not a function

  var sub = function (num1, num2) {
    return num1 - num2;
  };
  ```

- **[Airbnb Style Guide](https://github.com/airbnb/javascript#functions--declarations)에선 함수 선언식보다 함수 표현식을 권장**

## ▶ 함수의 매개변수와 인자

1. 기본 인자(default arguments)

   - 인자 작성 시 ‘=’ 문자 뒤 기본 인자 선언 가능
   - 기본값으로 함수 호출을 넣을 수도 있음
     - 입력값이 `undefined`인 경우에만 호출되어 기본값이 사용됨
     - 이를 통해 매개변수에서 필수값을 표현할 수도 있음

   ```javascript
   const greeting = function (name = "Anonymous") {
     return `Hi ${name}`;
   };

   greeting(); // Hi Anonymous
   ```

   ```javascript
   const required = function () {
     throw new Error("no parameter");
   };

   const printLog = function (a = required()) {
     return { a };
   };

   printLog(1); // { a: 1 }
   printLog(); // 에러 발생: no parameter
   ```

2. 매개변수와 인자의 개수 불일치 허용

   - 매개변수보다 인자의 개수가 많을 경우

   ```javascript
   const noArgs = function () {
     return 0;
   };

   noArgs(1, 2, 3); // 0

   const twoArgs = function (arg1, arg2) {
     return [arg1, arg2];
   };

   twoArgs(1, 2, 3); // [1, 2]
   ```

   - 매개변수보다 인자의 개수가 적을 경우

   ```javascript
   const threeArgs = function (arg1, arg2, arg3) {
     return [arg1, arg2, arg3];
   };

   threeArgs(); // [undefined, undefined, undefined]
   threeArgs(1); // [1, undefined, undefined]
   threeArgs(1, 2); // [1, 2, undefined]
   ```

3. Rest Parameter

   - rest parameter `…` 를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음
     - python 의 \*args 와 유사
   - 만약 rest parameter로 처리한 매개변수에 인자가 넘어오지 않을 경우에는, 빈 배열로 처리

   ```javascript
   const restOpr = function (arg1, arg2, ...restArgs) {
     return [arg1, arg2, restArgs];
   };

   restArgs(1, 2, 3, 4, 5); // [1, 2, [3, 4, 5]]
   restArgs(1, 2); // [1, 2, []]
   ```

   - ES5에서는 `arguments` 키워드가 비슷한 역할을 함
     - 단점: `arguments`는 배열이 아니기 때문에, 배열처럼 사용하기 위해서는 배열로 변환하는 과정이 필요

   ```javascript
   const printLog = function (a) {
     const rest = Array.from(arguments).splice(1);
     return { a, rest };
   };

   printLog(1, 2, 3); // { a: 1 , rest: [2, 3]}
   ```

4. Spread Operator

   - spread operator `…` 를 사용하면 배열 인자를 전개하여 전달 가능

   ```javascript
   const spreadOpr = function (arg1, arg2, arg3) {
     return arg1 + arg2 + arg3;
   };

   const numbers = [1, 2, 3];
   spreadOpr(...numbers); // 6
   ```

5. Named Parameter

   - 객체 비구조화 (Object Destructuring)을 통해 구현할 수 있음
   - 함수 호출 시 매개변수의 이름과 값을 동시에 적을 수 있으므로 가독성이 높음

   ```js
   const numbers = [10, 20, 30];
   const rst = getValues({ numbers, greaterThan: 5, lessThan: 25 });
   ```

   - Named Parameter를 이용하면, Optional Parameter의 활용도가 올라감

   ```js
   const numbers = [10, 20, 30];
   const rst = getValues({ numbers, greaterThan: 5 });
   ```

## ▶ 화살표 함수 (Arrow Function)

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 함수의 매개변수가 단 하나 뿐이라면, ‘( )’ 도 생략 가능
- 함수 몸통이 표현식 하나라면 ‘{ }’과 ‘return’도 생략 가능

  ```javascript
  const arrow1 = function (name) {
    return `hello, ${name}`
  }

  // 1. function 키워드 삭제
  const arrow2 = (name) => { return `hello, ${name}` }

  // 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
  const arrow3 = name => { return `hello, ${name}` }

  // 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제
  가능
  const arrow4 = name => `hello, ${name}
  ```
