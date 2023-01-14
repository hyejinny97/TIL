# ✔ 반복문
  
## ▶ while문

- 조건문이 참(true)인 동안 반복 시행
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성
  
  ```javascript
  while (조건식) {
    명령문
  }
  ```

  ```javascript
  let i = 0

  while (i < 6) {
    console.log(i)   // 0 1 2 3 4 5
    i += 1
  }
  ```

  
## ▶ for문

- 세미콜론(;)으로 구분되는 세 부분 으로 구성
  - initialization: 최초 반복문 진입 시 1회만 실행되는 부분
  - condition: 매 반복 시행 전 평가되는 부분
  - expression: 매 반복 시행 이후 평가되는 부분
- 블록 스코프 생성
  
  ```javascript
  for (initialization; condition; expresstion) {
    명령문
  }
  ```

  ```javascript
  for (let i = 0; i < 6; i++) {
    console.log(i)   // 0 1 2 3 4 5
  }
  ```

  
## ▶ for ... in 문

- 주로 **객체(object)**의 **속성(key)**들을 순회할 때 사용
- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

  ```javascript
  for (변수 in object) {
    명령문
  }
  ```
  
  ```javascript
  const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: 'washington D.C.'
  }

  for (let capital in capitals) {
    console.log(capital)   // korea france USA
  }
  ```
  
  
## ▶ for ... of 문

- **반복 가능한(iterable) 객체**를 순회하며 값을 꺼낼 때 사용
  - 반복 가능한(iterable) 객체의 종류: **Array, Map, Set, String** 등
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

  ```javascript
  for (변수 in iterables) {
    명령문
  }
  ```
  
  ```javascript
  const fruits = ['딸기', '바나나', '메론']

  for (let fruit of fruits) {
    console.log(fruit)   // 딸기 바나나 메론
  }
  ```

  
## ▶ 참고) for ... in 문  vs  for ... of 문

1. for ... in 문: **객체(object)** 순회에 적합
  
   - 객체(object)의 경우, 속성(key)를 순회함
   - 배열(iterable)의 경우, 인덱스를 순회함
  
   ```javascript
   // 1. 객체(object)를 순회하는 경우
   const capitals = {
     korea: 'seoul',
     france: 'paris',
     USA: 'washington D.C.'
   }
 
   for (let capital in capitals) {
     console.log(capital)   // korea france USA
   }
 
 
   // 2. 배열(iterable)을 순회하는 경우
   const fruits = ['딸기', '바나나', '메론']
 
   for (let fruit in fruits) {
     console.log(fruit)   // 0 1 2
   }
   ```

2. for ... of 문: **배열(iterable)** 순회에 적합
  
   - 객체(object)의 경우, 에러 발생
   - 배열(iterable)의 경우, 값을 순회함

   ```javascript
   // 1. 객체(object)를 순회하는 경우
   const capitals = {
     korea: 'seoul',
     france: 'paris',
     USA: 'washington D.C.'
   }
 
   for (let capital of capitals) {
     console.log(capital)   // Uncaught TypeError: capitals is not iterable
   }
 
 
   // 2. 배열(iterable)을 순회하는 경우
   const fruits = ['딸기', '바나나', '메론']
 
   for (let fruit in fruits) {
     console.log(fruit)   // 딸기 바나나 메론
   }
   ```