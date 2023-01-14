# ✔ Hello World

## ▶ 코딩 스타일 가이드

- 코딩 스타일의 핵심은 합의된 원칙과 일관성
  - 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요
- 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
  - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
- 참고) 다양한 자바스크립트 코딩 스타일 가이드
  - [Airbnb Javascript Style Guide](https://github.com/airbnb/javascript)
  - [Google Javascript Style Guide](https://google.github.io/styleguide/jsguide.html)
  - [standardjs](https://standardjs.com/#javascript-style-guide-linter-and-formatter)

  
## ▶ 웹 페이지에 스크립트 삽입 방법

1. 내부 스크립트
   
    ```html
    <!DOCTYPE HTML>
    <html>
    <body>
      <script>
        alert( 'Hello, world!' );
      </script>
    </body>
    </html>
    ```

   - `<script>` 태그 내부에 자바스크립트 코드 삽입
  
2. 외부 스크립트
   
    ```html
    <!DOCTYPE HTML>
    <html>
    <body>
      <script src="/path/to/script.js"></script>
    </body>
    </html>
    ```

   - 자바스크립트 코드를 `.js` 파일에 따로 저장 
   - `<script>` 태그의 `src` 속성을 사용해 `.js` 파일과 연결
   - 외부 스크립트의 장점
     - 브라우저는 스크립트를 다운받아 캐시(cache)에 저장함
     - 따라서 여러 페이지에서 동일한 스크립트를 사용하는 경우, 스크립트를 새로 다운받지 않고 캐시로부터 스크립트를 가져와 사용
     - 트래픽 절약, 웹 페이지 속도 향상 등 이점 존재
   - `<script>` 태그 하나에 src 속성과 내부 코드가 둘 다 있을 경우, 내부 코드는 실행되지 않음


## ▶ 코드 기본 구조 

### 🔹 문 (statement)

- 어떤 작업을 수행하는 문법 구조(syntax structure)와 명령어(command)
- 서로 다른 문은 세미콜론으로 구분함
- 코드의 가독성을 높이기 위해, 일반적으로 각 문은 서로 다른 줄에 작성함
  
  ```js
  alert('Hello');
  alert('World');
  ```

### 🔹 세미콜론 (semicolon)

- 서로 다른 문은 세미콜론으로 구분함
- 줄 바꿈이 있다면 세미콜론을 생략할 수 있음
  - 세미콜론 자동 삽입(automatic semicolon insertion)
  - 자바스크립트는 줄 바꿈이 있으면 **대부분** ‘암시적’ 세미콜론으로 해석
  - 주의) 줄 바꿈을 모두 세미콜론으로 해석하진 않음

    ```js
    alert(3 +
    1
    + 2);
    ```

- 자바스크립트가 줄 바꿈을 암시적 세미콜론으로 해석하지 못하는 경우가 있음
  - ex) 첫번째 문 뒤에 줄 바꾼 후, 대괄호로 시작하는 문이 있는 경우
    - 자바스크립트가 대괄호 앞에는 세미콜론이 있다고 가정하지 않기 때문에, 두 개의 문을 단일문으로 처리하면서 에러가 남

    ```js
    alert("에러가 발생합니다.")

    [1, 2].forEach(alert)
    ```

- 따라서, 자바스크립 코드에서 항상 **세미콜론을 사용**하는 것을 권장!

### 🔹 주석 (comment)

- 한 줄짜리 주석: `//` (단축키: `Ctrl + /`)

  ```js
  // 한 줄짜리 주석
  alert('Hello');
  ```

- 여러 줄짜리 주석: `/* ... */` (단축키: `Ctrl + Shift + /`)
  - `/* ... */`안에 또 다른 `/* ... */`가 있으면 에러 발생

  ```js
  /* 여러 줄 
  주석 
  */
  alert('Hello');
  ```

- 서버에 배포하기 전에 코드를 압축해주는 도구가 많이 있는데, 이 도구들은 주석을 삭제해주기 때문에 최종 배포 코드에 영향을 주지 않음





# ✔ 변수와 식별자

## ▶ 식별자(identifier)

- 변수를 구분할 수 있는 변수명
- 식별자는 반드시 `문자`, `달러($)` 또는 `밑줄(_)`로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능

  
## ▶ 선언, 할당, 초기화

1. 선언 (Declaration)
   
   - 변수를 생성하는 행위 또는 시점

2. 할당 (Assignment)
   
   - 선언된 변수에 값을 저장하는 행위 또는 시점

3. 초기화 (Initialization)
   
   - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점
   
   ```javascript
   // 1. 선언
   let foo
   console.log(foo)  // undefined
   
   // 2. 할당
   foo = 11
   console.log(foo)  // 11
   
   // 3. 선언 + 할당
   let bar = 0
   console.log(foo)  // 0
   ```

  
## ▶ 변수 키워드

1. `let`
   
   - 재할당 **가능**, 재선언 **불가능**
     
     ```javascript
     let num = 10       // 선언 및 초기값 할당
     num = 20           // 재할당 가능
     let num            // 재선언 불가 (Uncaught SyntaxError: Identifier 'num' has already been declared)
     ```
   
   - **블록** 스코프 (block scope)
     
     - if, for, 함수 등의 중괄호 `{}` 내부를 가리킴
     - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
     
     ```javascript
     let x = 1
     
     if (x === 1) {
      let x = 2
      console.log(x)   // 2
     }
     
     console.log(x)    // 1
     ```

2. `const`
   
   - 재할당 **불가능**, 재선언 **불가능**
     
     ```javascript
     const num = 10      // 선언 및 초기값 할당
     num = 20            // 재할당 불가 (Uncaught TypeError: Assignment to constant variable.)
     const num           // 재선언 불가 (Uncaught SyntaxError: Identifier 'num' has already been declared)
     ```
   
   - **블록** 스코프 (block scope)
     
     ```javascript
     const x = 1
     
     if (x === 1) {
      const x = 2
      console.log(x)   // 2
     }
     
     console.log(x)    // 1
     ```

3. `var`
   
   - 재할당 **가능**, 재선언 **가능**
     
     ```javascript
     var num = 10        // 선언 및 초기값 할당
     num = 20            // 재할당 가능
     var num           // 재선언 가능
     ```
   
   - **함수** 스코프 (function scope)
     
     - 함수의 중괄호 내부를 가리킴
     - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능
     
     ```javascript
     function foo() {
      var x = 5
      console.log(x)    // 5
     }
     
     console.log(x)     // Uncaught ReferenceError: x is not defined
     ```
   
   - ES6 이전에 변수를 선언할 때 사용되던 키워드
   
   - 문제점: **호이스팅**되는 특성으로 인해 예기치 못한 문제 발생 가능
     
     - 따라서 ES6 이후부터는 **var 대신 const와 let을 사용하는 것을 권장**
  
     ```javascript
     console.log(username)   // undefined
     var username = '홍길동'

     console.log(email)      // Uncaught ReferenceError: Cannot access 'email' before initialization
     let email = 'gildong#gamil.com'

     console.log(age)         // Uncaught ReferenceError: Cannot access 'age' before initialization
     const age = 50         
     ```

  
## ▶ 호이스팅 (hoisting)

- 변수를 선언 이전에 참조할 수 있는 현상

- 변수 선언 이전의 위치에서 접근 시 undefined를 반환

- 자바스크립트는 모든 선언을 호이스팅함

- 즉, var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대(Temporal Dead Zone; TDZ)가 존재하지 않음 
  
  ![var와 let의 호이스팅 차이점 비교](https://publizm.github.io/static/79bc1f4c3de3fe63bf249ad562988f68/867c0/blockLevelScope_2.jpg)