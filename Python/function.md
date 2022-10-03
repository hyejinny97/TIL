# ✔ 함수 (function)

- 특정한 기능을 하는 코드의 조각
- 코드 중복 방지, 재사용 용이
- 사용자 함수(Custom Function), 내장함수(Bulit-in Function)
  
> 함수의 기본 구조
1. 선언과 호출 (define & call)
2. 입력 (Input)
3. 범위 (Scope)
4. 결과값 (Output)
   
> 선언과 호출
- 함수의 선언은 def 키워드를 사용함
- 들여쓰기를 통해 Function Body를 작성함
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 호출되면 코드를 실행하고 return을 통해 결과값을 반환하며 종료됨
  ```python
  # 함수 선언
  def 함수명(parameter):
    return 반환할 값
  
  # 함수 호출
  함수명(argument)
  ```



# ✔ 함수의 결과값 (Output)
> return
- 함수는 반드시 값 하나만 return함
- 명시적인 return이 없는 경우엔, None을 반환함
- 함수는 return과 동시에 실행이 종료됨
- return을 통해 두 개 이상의 값을 반환할 경우, 튜플 형식으로 반환됨



# ✔ 함수의 입력 (Input)
> Parameter
- 함수를 실행할 때, 함수 내부에서 사용되는 식별자
  
> Argument
- 함수를 호출할 때, parameter를 통해 전달되는 값
- 파이썬에서 함수를 호출할 때, 함수를 선언할 때와 같은 개수의 매개변수를 입력해야 함
  - 매개변수를 더 많이 넣거나 적게 넣을 경우, TypeError 발생
1. positional arguments
   - 기본적으로 함수 호출 시, argument는 **위치**에 따라 함수 내에 전달됨
2. keyword arguments
   - 직접 **변수의 이름**으로 특정 argument를 전달할 수 있음
   - keyword argument 다음에 positional argument를 활용할 수 없음
3. default argument
   - **기본값**을 지정하여 함수 호출 시, argument값을 설정하지 않도록 함
4. 정해지지 않은 개수의 arguments
   - 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용
   - argument들은 **튜플**로 묶여 처리됨
   - parameter에 `*`를 붙여 표현
5. 정해지지 않은 개수의 keyword arguments
   - 함수가 임의의 개수 argument를 keyword argument로 호출될 수 있도록 지정
   - argument들은 **딕셔너리**로 묶여 처리됨
   - parameter에 `**`를 붙여 표헌

  ```python
  # 1. positional arguments
  def add(x, y):
    return x + y

  add(2,3)

  # 2. keyword arguments
  def add(x, y):
    return x + y
  
  add(x=2, y=5)
  add(y=5, x=2)
  add(2, y=5)

  # 3. default argument
  def add(x, y=0):
    return x + y
  
  add(2)

  # 4. 정해지지 않은 개수의 arguments
  def add(*args):
    return args
  
  add(2, 3, 4, 5)   # 결과: (2, 3, 4, 5)

  # 5. 정해지지 않은 개수의 keyword arguments
  def family(**kwargs):
    return kwargs
  
  family(father='John', mother='Jane')   # 결과: {'father':'John', 'mother':'Jane'}
  ```



# ✔ 함수의 범위 (Scope)
- 함수는 코드 내부에 local scope를 생성
- scope
  - global scope: 코드 어디에서든 참조할 수 있는 공간
  - local scope: 함수가 만든 scope, 함수 내부에서만 참조 가능
- variable
  - global variable: global scope에 정의된 변수
  - local variable: local scope에 정의된 변수

> 객체 수명주기
- 객체는 각자의 수면주기가 존재
1. built-in scope
   - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
   - 모듈이 호출된 시점 이후, 혹은 인터프리터가 끝날 때까지 유지
3. local scope
   - 함수가 호출될 때 생성되고, 함수가 종료될 때까지만 유지

> 이름 검색 규칙 (Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어있음
- **LEGB Rule**: 아래와 같은 순서로 이름을 찾아나감
  1. Local scope: 함수
  2. Enclosed scope: 특정 함수의 상위 함수
  3. Global scope: 함수 밖의 변수, import 모듈
  4. Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성
- 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음





# ✔ 람다 함수
```python
lambda <매개변수> : <표현식>
```
- 표현식을 계산한 결과값을 return문 없이 반환하는 함수
- 이름이 없는 함수(익명함수)
- 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
- def를 사용할 수 없는 곳에서도 사용가능





# ✔ 함수 응용
> 내장 함수 

- `map(function, iterable)`
  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용
  - map object로 결과 반환

- `filter(function, iterable)`
  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용해, 그 결과가 True인 것들만 반환
  - filter object로 결과 반환

- `divmod(숫자1, 숫자2)`
  - 숫자1을 숫자2로 나눈 몫과 나머지를 반환
  - 튜플 형태로 결과 반환 