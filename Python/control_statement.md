# ✔ 제어문 (Control Statement)

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flow chart)로 표현이 가능
  
> 제어문 분류
1. 조건문 (if ~ elif ~ else문)
2. 반복문
   1. while문
   2. for문

> pass 키워드

- 일단 먼저 전체 골격을 잡아놓고 내부 코드는 나중에 천천히 개발할 의도로 pass 키워드를 사용하기도 함
- 골격: 조건문, 반복문, 함수, 클래스 등의 기본 구문

   ```python
   if number > 0:
      pass
   else:
      pass
   ```

> raise NotImplementedError 문

- raise 키워드를 통해 오류를 강제 발생
- 미구현 상태를 표현하는 NotImplementedError 문을 통해 아직 구현되지 않은 부분임을 알림
  
   ```python
    if number > 0:
       raise NotImplementedError
    else:
       raise NotImplementedError
   ```


# ✔ 조건문 (Conditional Statement)
> 조건문 기본
- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
  ```python
  if <조건식>:
    # <조건식>이 참일 때, 실행할 코드
  else:
    # <조건식>이 거짓일 때, 실행할 코드
  ```
- else는 선택적으로 활용 가능함
  
> 복수 조건문
- 복수의 조건식을 활용할 경우, elif를 활용하여 표현함
  ```python
  if <조건식1>:
    # <조건식1>이 참일 때, 실행할 코드
  elif <조건식2>:
    # <조건식2>가 참일 때, 실행할 코드
  else:
    # 위의 모든 <조건식>이 거짓일 때, 실행할 코드
  ```

> 중첩 조건문
- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
  ```python
  if <조건식1>:
    # <조건식1>이 참일 때, 실행할 코드
    if <조건식2>:
      # <조건식2>가 참일 때, 실행할 코드
  else:
    # <조건식1>이 거짓일 때, 실행할 코드
  ```

> 조건 표현식
- 일반적으로 조건에 따라 값을 할당할 때 활용
  ```python
  <true인 경우 값> if <조건식> else <false인 경우 값>
  ```


# ✔ 반복문 (Loop Statement)
- 특정 조건에 도달할 때까지, 계속 반복되는 일련의 문장

> while문
- while문은 조건식이 참인 경우 반복적으로 코드를 실행
- 무한 루프를 돌지 않도록 반드시 종료조건이 필요
  ```python
  while <조건식>:
    # 조건식이 참인 경우 실행할 코드
  ```

> for문
- for문은 (string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회함
- 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음
  ```python
  for <변수명> in <iterable>:
    # 반복해서 실행할 코드
- for문에서 순회가능한 객체(iterable) 종류
  - 순회할 수 있는 자료형: str, tuple, list, dict 등
  - 순회형 함수: range, enumerate 등
- enumerate 순회
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
  - (index, value)형태의 tuple로 구성된 열거 객체 반환
  - `enumerate(iterable, [start=index 시작값])`
  ```python
  fruit = ['apple', 'banana', 'melon']
  
  for idx, val in enumerate(fruit):
    print(idx, val)
  
  # 결과
  # 0 'apple'
  # 1 'banana'
  # 2 'melon'
  ```
- dictionary 순회
  - 딕셔너리는 기본적으로 key를 순회
  - key를 통해 값에 접근
  ```python
  grades = ['john':80, 'eric':90]

  for name in grades:
    print(name, grades[name])
  
  # 결과
  # john 80
  # eric 90
  ```

# ✔ 반복문 제어
> break
- break문을 만나면 반복문은 종료됨
  ```python
  n = 0
  while True:
    if n == 3:
      break
    print(n)
    n += 1
  
  # 결과
  # 0
  # 1
  # 2
  ```

> continue
- continue문을 만나면 continue이후의 코드블록은 수행하지 않고, 다음 반복을 수행하게 됨
  ```python
  for i in range(6):
    if i % 2 == 0:
      continue
    print(i)
  
  # 결과
  # 1
  # 3
  # 5
  ```

> for ~ else
- 끝까지 반복문을 실행한 이후에 else문을 실행
- break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
  ```python
  word = 'apple'

  for char in word:
    if char == 'b':
      print('b가 있습니다')
      break
  else:
    print('b가 없습니다')
  
  # 1) word = 'apple'일때 결과
  # b가 없습니다

  # 2) word = 'banana'일때 결과
  # b가 있습니다
  ```