# ✔ 에러/예외 처리 (Error/Exception Handling)
> 디버깅 (debugging) 방법
1. print() 함수 활용
   - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
   - breakpoint, 변수 조회 등

> 문법 에러 (SyntaxError)
- 괄호의 개수, 들여쓰기 문제 등으로 인해 프로그램이 실행되기도 전에 발생하는 오류
- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일명, 줄번호, 캐럿 기호(^)를 통해 에러가 발생한 위치 표현

1. `EOL (End Of Line)`

2. `EOF (End Of File)`

3. `invalid syntax`

4. `assign to literal`
  
    ```python
    print('hello
    '# SyntaxError: EOL while scanning string literal
    
    print(
    # SyntaxError: unexpected EOF while parsing
    
    while
    # SyntaxError: invalid syntax
    
    5 = 3
    # SyntaxError: cannot assign to literal
    ```

> 예외 (Exception) 또는 런타임 오류 (runtime error)
- 프로그램이 일단 실행된 다음, 실행 중에 발생하는 에러들
- 모든 내장 예외는 Exception Class를 상속받아 이루어짐 ([python built-in-exceptions](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy))
- 사용자 정의 예외를 만들어 관리할 수 있음

1. `ZeroDivisionError`: 0으로 나누고자 할 때 발생

2. `NameError`: namespace 상에 이름이 없는 경우 발생

3. `TypeError`: 타입 불일치, arguments 부족 및 초과 시 발생

4. `ValueError`: 타입은 올바르나 값이 적절하지 않거나 없는 경우에 발생

5. `IndexError`

6. `KeyError`

7. `ModuleNotFoundError`: 존재하지 않는 모듈을 import하는 경우 발생

8. `ImportError`: 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우 발생

9. `IndentationError`: Indentation이 적절하지 않는 경우 발생

10. `KeyboardInterrupt`: 임의로 프로그램을 종료했을 때 발생


> 예외 처리 (Exception Handling)
- 조건문을 이용하여 예외 처리

  ```python
  num = input('값을 입력하시오: ')
  
  if num.isdigit():
    print(2 * int(num))
  else:
    print('정수를 입력하지 않았습니다.')
  ```

- try문 / except절을 이용하여 예외 처리

1. `try`문
   - 오류가 발생할 가능성이 있는 코드를 실행
   - 예외가 발생되지 않으면, except 없이 실행 종료

2. `except`문
   - try문에서 예외가 발생하면, except 절이 실행
   - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

3. `else`문
   - try문에서 예외가 발생하지 않으면 실행

4. `finally`문
   - 예외 발생 여부와 관계없이 항상 실행

   ```python
   nums = [52, 273, 32, 72, 100]

   try:
      idx= int(input('인덱스 값: '))
      print(f'{idx}번째 요소: {nums[idx]}')
   except Exception as e:
      print('type(exception):', type(e))
      print('exception:', e)

   # 인덱스 값: yes
   # type(exception): <class 'ValueError'>
   # exception: invalid literal for int() with base 10: 'yes'
   
   # 인덱스 값: 100
   # type(exception): <class 'IndexError'>
   # exception: list index out of range
   ```

   ```python
   try:
     num = input('값을 입력하시오: ')
     print(100/int(num))
   except ValueError:
     print('숫자를 넣어주세요.')
   except ZeroDivisionError:
     print('0으로 나눌 수 없습니다.')
   except:
     print('에러는 모르지만 에러가 발생하였습니다.')
   ```

   ```python
   try:
     f = open('nooofile.txt')
   except FileNotFoundError:
     print('해당 파일이 없습니다.')
   else:
     print('파일을 읽기 시작합니다.')
     print(f.read())
     print('파일을 모두 읽었습니다.')
     f.close()
   finally:
     print('파일 읽기를 종료합니다.')
   ```


# ✔ 예외 발생 시키기
> raise 문

```python
raise <표현식> (메시지)
```

- raise를 통해 예외를 강제로 발생
  - 아직 구현하지 않은 부분을 강제로 예외 발생
- `<표현식>`부분에 예외 타입을 지정하지 않을 경우, 현재 scope에서 활성화된 마지막 예외를 다시 일으킴
  
  ```python
  num = int(input('정수 입력> '))

  if num > 0:
    raise NotImplementedError
  else:
    raise NotImplementedError
  ```