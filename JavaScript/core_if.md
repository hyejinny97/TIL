# ✔ 조건문
  
## ▶ if문

- 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단

- `if`, `else if`, `else`
  
  - 조건은 소괄호(condition) 안에 작성
  - 실행할 코드는 중괄호{} 안에 작성
  - 블록 스코프 생성
  
  ```javascript
  if (조건식) {
    명령문
  } else if (조건식) {
    명령문
  } else {
    명령문
  }
  ```

  
## ▶ switch문

- 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
- 참고) 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
  - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

- `switch`, `case`, `default`
  
  - 표현식(expression)의 결과값을 이용한 조건문
  - 표현식의 결과값과 case문의 오른쪽 값을 비교
  - break 및 default문은 [선택적]으로 사용 가능
  - **break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행**

  ```javascript
  switch (표현식) {
    case '값1': {
      명령문
      [break]
    }
    case '값': {
      명령문
      [break]
    }
    [default: {
      명령문
    }]
  }
  ```

  ```javascript
  const nation = 'Korea'

  switch(nation) {
    case 'Korea': {
      console.log('안녕하세요')   // 안녕하세요
    }
    case 'France': {
      console.log('Bonjour')      // Bonjour
    }
    default: {
      console.log('Hello')        // Hello
    }
  }
  ```