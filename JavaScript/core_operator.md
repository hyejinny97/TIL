# ✔ 연산자
  
## ▶ 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- 참고) Increment 및 Decrement 연산자
  - Increment(++): 피연산자의 값을 1 증가시키는 연산자
  - Decrement(--): 피연산자의 값을 1 감소시키는 연산자
  - [Airbnb Style Guide](https://github.com/airbnb/javascript#variables--unary-increment-decrement)에서는 ‘+=’ 또는 ‘-=’와 같이 더 분명한 표현으로 적을 것을 권장

  ```javascript
  let x = 0

  x += 10
  console.log(x)   // 10

  x -= 10
  console.log(x)   // 7

  x *= 10
  console.log(x)   // 70

  x /= 10
  console.log(x)   // 7

  x++
  console.log(x)   // 8 (+= 연산자와 동일)

  x--
  console.log(x)   // 7 (-= 연산자와 동일)
  ```

  
## ▶ 비교 연산자

- 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - ex) 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 크다
    - 소문자가 대문자보다 더 크다
  
  ```javascript 
  const num1 = 1
  const num2 = 100
  console.log(num1 < num2)   // true

  const char1 = 'a'
  const char2 = 'z'
  console.log(char1 > char2)  // false
  ```

1. 동등 비교 연산자 `==`
   
   - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
   - 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
   - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
   - 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음
  
    ```javascript
    const a = 1004
    const b = '1004'
    console.log(a == b)   // true

    const c = 1
    const d = true
    console.log(c == d)   // true

    console.log(a + b)    // 10041004
    console.log(c + d)    // 2
    ```

2. 일치 비교 연산자 `===`
   
   - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
   - [엄격한 비교](https://262.ecma-international.org/5.1/#sec-11.9.6)가 이뤄지며 암묵적 타입 변환이 발생하지 않음
     - 엄격한 비교: 두 비교 대상의 타입과 값 모두 같은지 비교

    ```javascript
    const a = 1004
    const b = '1004'
    console.log(a === b)   // false

    const c = 1
    const d = true
    console.log(c === d)   // false
    ```

  
## ▶ 논리 연산자

- 세 가지 논리 연산자로 구성
  
  - and 연산은 `&&` 연산자를 이용
  
  - or 연산은 `||` 연산자를 이용
  
  - not 연산은 `!` 연산자를 이용

  ```javascript
  console.log(true && false)  // false
  console.log(true && true)   // true
  console.log(1 && 0)         // 0
  console.log(4 && 7)         // 7
  console.log('' && 5)        // ''

  console.log(true || false)   // true
  console.log(false || false)  // false
  console.log(1 || 0)          // 1
  console.log(4 || 7)          // 4
  console.log('' || 5)         // 5

  console.log(!true)           // false
  console.log(!'Bonjour!')     // false
  ```

  
## ▶ 삼항 연산자 (Ternary Operator)

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능
- 참고) [한 줄에 표기하는 것을 권장](https://github.com/airbnb/javascript#comparison--nested-ternaries)