# ✔ 에러/예외 처리 (Error/Exception Handling)
> 디버깅 (debugging) 방법
1. print() 함수 활용
   - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
   - breakpoint, 변수 조회 등

> 문법 에러 (SyntaxError)
- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일명, 줄번호, 캐럿 기호(^)를 통해 에러가 발생한 위치 표현
1. `EOL (End Of Line)`
2. `EOF (End Of File)`
3. `invalid syntax`
4. `assign to literal`
  
    ```python
    print('hello
    '# File "<ipython-input-6-2a5f5c6b1414>", line 1
    # print('hello
    # ^
    # SyntaxError: EOL while scanning string literal
    
    print(
    # File "<ipython-input-4-424fbb3a34c5>", line 1
    # print(
    # ^
    # SyntaxError: unexpected EOF while parsing
    
    while
    # File "<ipython-input-7-ae84bbebe3ce>", line 1
    # while
    # ^
    # SyntaxError: invalid syntax
    
    5 = 3
    # File "<ipython-input-28-9a762f2c796b>", line 1
    # 5 = 3
    # ^
    # SyntaxError: cannot assign to literal
    ```

> 예외 (Exception)
- 실행 중에 감지되는 에러들
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
- try문 / except절을 이용하여 예외 처리
1. try문
   - 오류가 발생할 가능성이 있는 코드를 실행
   - 예외가 발생되지 않으면, except 없이 실행 종료
2. except문
   - try문에서 예외가 발생하면, except 절이 실행
   - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
3. else문
   - try문에서 예외가 발생하지 않으면 실행
4. finally문
   - 예외 발생 여부와 관계없이 항상 실행

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
- `<표현식>`부분에 예외 타입을 지정하지 않을 경우, 현재 scope에서 활성화된 마지막 예외를 다시 일으킴