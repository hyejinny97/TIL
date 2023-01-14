# ✔ 데이터 타입

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐

- 크게 원시 타입 (Primitive type)과 참조 타입 (Reference type)으로 분류됨
  
  ![자바스크립트의 데이터 타입 이미지](https://velog.velcdn.com/images/imjkim49/post/17b7a314-31f4-4285-a2dd-05a4cc78fbf3/image.png)

  
## ▶ 원시 타입 (Primitive type)

- 객체 (object)가 아닌 기본 타입

- 변수에 해당 타입의 값이 담김

- 다른 변수에 복사할 때 **실제 값**이 복사됨
  
  ```javascript
  let message = '안녕하세요'
  
  let greeting = message
  console.log(greeting)     // '안녕하세요'
  
  message = 'Hello'
  console.log(greeting)     // '안녕하세요'
  ```
1. 문자열 (String) 타입
   
   - 텍스트 데이터를 나타내는 타입
   
   - 16비트 유니코드 문자의 집합
   
   - 작은따옴표 또는 큰따옴표 모두 가능
   
   - 템플릿 리터럴 (Template Literal)
     
     - ES6부터 지원
     
     - 따옴표 대신 backtick으로 표현
     
     - `${ expression }` 형태로 표현식 삽입 가능
     
     ```javascript
     const firstName = 'Brandan'
     const lastName = 'Erich'
     const fullName = `${firstName} ${lastName}`
     
     console.log(fullName)   // Brandan Erich
     ```

2. undefined
   
   - 변수의 값이 없음을 나타내는 데이터 타입
   
   - 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨
     
     ```javascript
     let firstName
     console.log(firstName)   // undefined
     
     typeof null              // undefined
     ```

3. null
   
   - 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
   
   - 참고) null 타입과 typeof 연산자
     
     - typeof 연산자: 자료형 평가를 위한 연산자
     - null 타입은 [ECMA 명세의 원시 타입의 정의](https://tc39.es/ecma262/#sec-primitive-value)에 따라 원시 타입에 속하지만, typeof 연산자의 결과는 객체(object)로 표현됨
     
     ```javascript
     let firstName = null
     console.log(firstName)   // null
     
     typeof null              // object 
     ```

4. Boolean 타입
   
   - 논리적 참 또는 거짓을 나타내는 타입
   - true 또는 false로 표현
   - 조건문 또는 반복문에서 유용하게 사용
     - 참고) 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 [자동 형변환 규칙](https://tc39.es/ecma262/#sec-type-conversion)에 따라 true 또는 false로 변환됨
     - | 데이터 타입    | 거짓         | 참         |
       |:---------:|:----------:|:---------:|
       | Undefined | 항상 거짓      | X         |
       | Null      | 항상 거짓      | X         |
       | Number    | 0, -0, NaN | 나머지 모든 경우 |
       | String    | 빈 문자열      | 나머지 모든 경우 |
       | Object    | X          | 항상 참      |

  
## ▶ 참조 타입 (Reference type)

- 객체 (object) 타입의 자료형

- 변수에 해당 객체의 참조 값이 담김

- 다른 변수에 복사할 때 **참조 값**이 복사됨
  
  ```javascript
  let message = ['안녕하세요']
  
  let greeting = message
  console.log(greeting)     // ['안녕하세요']
  
  message[0] = 'Hello'
  console.log(greeting)     // ['Hello']
  ```

1. 배열 (Array)
   
   - 키와 속성들을 담고 있는 참조 타입의 객체(object)
   - 순서를 보장하는 특징이 있음
   - 주로 대괄호를 이용하여 생성하고, 0을 포함한 **양의 정수 인덱스**로 특정 값에 접근 가능 (음의 정수 인덱스로는 접근 불가)
   - 배열의 길이는 `array.length` 형태로 접근 가능
     
     - 참고) 배열의 마지막 원소는 `array.length – 1`로 접근

     ```javascript
     const nums = [1, 2, 3, 4, 5]

     console.log(nums[0])                // 1
     console.log(nums[-1])               // undefined
     
     console.log(nums.length)            // 5
     console.log(nums[nums.length - 1])  // 5
     console.log(nums[nums.length - 2])  // 4
     ```

2. 객체 (Objects)
   
   - 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
   - key는 **문자열 타입**만 가능
     - 따옴표로 문자열을 묶어주지 않아도 됨
     - 다만, key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현해야 함
   - value는 모든 타입(함수포함) 가능
   - 객체 요소 접근은 점 또는 대괄호로 가능
     - 다만, key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

     ```javascript
     const me = {
      name: 'jack',
      phoneNumber: '01012345678',
      'samsung products': {
        buds: 'Galaxy Buds Pro',
        galaxy: 'Galaxy s20',
      },
     }

     console.log(me.name)                     // jack
     console.log(me.phoneNumber)              // 01012345678
     console.log(me['samsung products'])      // {buds: 'Galaxy Buds Pro', galaxy: 'Galaxy s20'}
     console.log(me['samsung products'].buds) // Galaxy Buds Pro
     ```
  
   - 메서드는 객체의 속성이 참조하는 함수
   - `객체.메서드명()` 으로 호출 가능
   - 메서드 내부에서는 `this` 키워드가 객체를 의미함
     
     ```javascript
     const me = {
      firstName: 'John',
      lastName: 'Doe',
      getFullName: function () {
        return this.firstName + this.lastName
      }
     }

     console.log(me.getFullName())   // JohnDoe
     ```

   - ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
     - 속성명 축약
     - 메서드명 축약
     - 계산된 속성명 사용하기
     - 구조 분해 할당
       - 참고) 구조 분해 할당은 배열도 가능함
     - 객체 전개 구문(Spread Operator)

  
## ▶ JSON (JavaScript Object Notation)

- [참고 자료](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/)
- key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
   - 따라서 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수
- 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공
  
   - `JSON.parse()`: JSON ⇒ 자바스크립트 객체

   - `JSON.stringify()`: 자바스크립트 객체 ⇒ JSON



# ✔ 데이터 타입별 메서드
  
## ▶ 문자열 (String)
  
- 참고 자료: [MDN문서](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#instance_methods), [ECMA262](https://tc39.es/ecma262/#sec-string-objects)

1. 문자열 관련 탐색 메서드
   
   - `string.includes(value)`
    
     - 문자열에 value가 존재하는지 판별 후, 참 또는 거짓 반환
  
     ```javascript
     const str = 'a santa at nasa'
     
     str.includes('santa')  // true
     str.includes('asan')   // false
     ```

2. 문자열 관련 변경 메서드

   - `string.split(value)`
    
     - value가 없을 경우, 기존 문자열을 배열에 담아 반환
     - value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환
     - value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환
  
     ```javascript
     const str = 'a cup'

     str.split()    // ['a cup’]
     str.split('')  // ['a', ' ', 'c', 'u', 'p']
     str.split(' ') // ['a', 'cup']
     ```
  
   - `string.replace(from, to)`, `string.replaceAll(from, to)`
  
     - replace: 문자열에 from 값이 존재할 경우, **1개**만 to 값으로 교체하여 반환
     - replaceAll: 문자열에 from 값이 존재할 경우, **모두** to 값으로 교체하여 반환

     ```javascript
     const str = 'a b c d'

     str.replace(' ', '-')      // 'a-b c d'
     str.replaceAll(' ', '-')   // 'a-b-c-d'
     ```
  
   - `string.trim()`, `string.trimStart()`, `string.trimEnd()`
  
     - trim: 문자열 **시작**과 **끝**의 모든 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
     - trimStart: 문자열 **시작**의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
     - trimEnd: 문자열 **끝**의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

     ```javascript
     const str = ' hello '

     str.trim()       // 'hello'
     str.trimStart()  // 'hello '
     str.trimEnd()    // ' hello'
     ```

  
## ▶ 배열 (Arrays)

- 참고 자료: [MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array#%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4_%EB%A9%94%EC%84%9C%EB%93%9C), [ECMA262](https://tc39.es/ecma262/#sec-properties-of-the-array-constructor)
- Spread operator
  - spread operator `…` 를 사용하면 배열 내부에서 배열 전개 가능
    
    - ES5까지는 `Array.concat()` 메서드를 사용
  
  - 얕은 복사에 활용 가능

   ```javascript
   const array = [1, 2, 3]
   const newArray = [0, ...array, 4]

   console.log(newArray) // [0, 1, 2, 3, 4]
   ```

- **Array Helper Methods**
  - 배열을 순회하며 특정 로직을 수행하는 메서드
  - 메서드 호출 시 인자로 **callback 함수**를 받는 것이 특징
  - forEach(), map(), filter(), reduce(), find(), some(), every()


1. 배열 관련 값 추가/삭제 메서드
   
   - `array.push()`
    
     - 배열의 가장 뒤에 요소 추가

     ```javascript
     const nums = [1, 2, 3, 4, 5]

     nums.push(100)
     console.log(nums)   // [1, 2, 3, 4, 5, 100]
     ```

   - `array.pop()`
  
     - 배열의 마지막 요소 제거

     ```javascript
     const nums = [1, 2, 3, 4, 5]
     
     nums.pop()
     console.log(nums)   // [1, 2, 3, 4]
     ```

   - `array.unshift()`
  
     - 배열의 가장 앞에 요소 추가

     ```javascript
     const nums = [1, 2, 3, 4, 5]
     
     nums.unshift(100)
     console.log(nums)   // [100, 1, 2, 3, 4, 5]
     ```

   - `array.shift()`
  
     - • 배열의 첫번째 요소 제거

     ```javascript
     const nums = [1, 2, 3, 4, 5]
     
     nums.shift()
     console.log(nums)   // [2, 3, 4, 5]
     ```

2. 배열 관련 탐색 및 정렬 메서드
   
   - `array.reverse()`
    
     - 원본 배열의 요소들의 순서를 반대로 정렬
  
     ```javascript
     const nums = [1, 2, 3, 4, 5]

     nums.reverse()
     console.log(nums)   // [5, 4, 3, 2, 1]
     ```

   - `array.includes(value)`
    
     - 배열에 특정 값이 존재하는지 판별 후, 참 또는 거짓 반환

     ```javascript
     const nums = [1, 2, 3, 4, 5]

     console.log(nums.includes(1))     // true
     console.log(nums.includes(100))   // false
     ```

   - `array.indexOf(value)`
    
     - 배열에 특정 값이 존재하는지 확인 후, 가장 첫 번째로 찾은 요소의 인덱스 반환
     - 만약 해당 값이 없을 경우 -1 반환

     ```javascript
     const nums = [1, 2, 3, 4, 5]
     let result
     
     result = nums.indexOf(3)
     console.log(result)   // 2

     result = nums.indexOf(100)
     console.log(result)   // -1
     ```

3. 배열 관련 변경 메서드

   - `array.join([separator])`
    
     - 배열의 모든 요소를 연결하여 반환
     - separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

     ```javascript
     const nums = [1, 2, 3, 4, 5]
     let result
     
     result = nums.join()
     console.log(result)   // 1,2,3,4,5

     result = nums.join('')
     console.log(result)   // 12345

     result = nums.join(' ')
     console.log(result)   // 1 2 3 4 5

     result = nums.join('-')
     console.log(result)   // 1-2-3-4-5
     ```

4. Array Helper Methods
   
   - `array.forEach(callback(element[, index[,array]]))`
    
     - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 콜백 함수는 3가지 매개변수로 구성
       - element: 배열의 요소
       - index: 배열 요소의 인덱스
       - array: 배열 자체
     - 반환 값(return)이 **없는** 메서드

     ```javascript
     array.forEach((elemet, index, array) => {
      명령문
     })
     ```

     ```javascript
     const fruits = ['딸기', '수박', '사과']

     fruits.forEach((fruit, idx) => {
      console.log(fruit, idx)
     })
     // 딸기 0 
     // 수박 1
     // 사과 2
     ```

   - `array.map(callback(element[, index[, array]]))`
    
     - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 콜백 함수의 반환 값을 요소로 하는 새로운 **배열** 반환
     - 기존 배열 전체를 다른 형태로 바꿀 때 유용

     ```javascript
     array.map((elemet, index, array) => {
      명령문
     })
     ```

     ```javascript
     const nums = [1, 2, 3, 4, 5]

     const doubleNums = nums.map((num) => {
      return num * 2
     })
     
     console.log(doubleNums)   // [2, 4, 6, 8, 10]
     ```

   - `array.filter(callback(element[, index[, array]]))`
    
     - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 **배열**을 반환
     - 기존 배열의 요소들을 필터링할 때 유용

     ```javascript
     array.filter((elemet, index, array) => {
      명령문
     })
     ```

     ```javascript
     const nums = [1, 2, 3, 4, 5]

     const oddNums = nums.filter((num) => {
      return num % 2
     })
     
     console.log(oddNums)   // [1, 3, 5]
     ```

   - `array.reduce(callback(acc, element, [index[, array]])[, initialValue])`
    
     - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 콜백 함수의 반환 값들을 하나의 **값**(acc)에 누적 후 반환
     - reduce 메서드의 주요 매개변수
       - acc: 이전 callback 함수의 반환 값이 누적되는 변수
       - initialValue(optional): 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
     - 참고) 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

     ```javascript
     array.reduce((acc, elemet, index, array) => {
      명령문
     }, initialValue)
     ```

     ```javascript
     const nums = [1, 2, 3]

     const result = nums.reduce((acc, num) => {
      return acc + num
     }, 0)
     
     console.log(result)   // 6
     ```

   - `array.find(callback(element[, index[, array]]))`
    
     - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 콜백 함수의 반환 값이 참이면, 조건을 만족하는 **첫번째 요소**를 반환
     - 찾는 값이 배열에 없으면 **undefined** 반환

     ```javascript
     array.find((elemet, index, array) => {
      명령문
     })
     ```

     ```javascript
     const avengers = [
      { name: 'Toney Stark', age: 45 },
      { name: 'Steve Rpgers', age: 32 },
      { name: 'Thor', age: 40 }
     ]

     const result = avengers.find((avenger) => {
      return anverger.name === 'Toney Stark'
     })

     console.log(result)   // { name: 'Toney Stark', age: 45 }
     ```

   - `array.some(callback(element[, index[, array]]))`
    
     - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 배열의 요소 중 **하나라도** 주어진 판별 함수를 통과하면 **참**을 반환
     - 모든 요소가 통과하지 못하면 **거짓** 반환
     - 참고) 빈 배열은 항상 **거짓** 반환

     ```javascript
     array.some((elemet, index, array) => {
      명령문
     })
     ```

     ```javascript
     const nums = [1, 3, 5, 7, 9]

     const hasEvenNum = nums.some((num) => {
      return num % 2 === 0
     })

     console.log(hasEvenNum)   // false

     const hasOddNum = nums.some((num) => {
      return num % 2
     })

     console.log(hasOddNum)   // true
     ```

   - `array.every(callback(element[, index[, array]]))`
    
     - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 배열의 **모든** 요소가 주어진 판별 함수를 통과하면 **참**을 반환
     - 하나의 요소라도 통과하지 못하면 **거짓** 반환
     - 참고) 빈 배열은 항상 **참** 반환

     ```javascript
     array.every((elemet, index, array) => {
      명령문
     })
     ```

     ```javascript
     const nums = [2, 4, 6, 8, 10]

     const isEveryNumEven = nums.every((num) => {
      return num % 2 === 0
     })

     console.log(isEveryNumEven)   // ture

     const isEveryNumOdd = nums.every((num) => {
      return num % 2
     })

     console.log(isEveryNumOdd)   // false
     ```