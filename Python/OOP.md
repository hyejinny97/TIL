# ✔ 객체지향 프로그래밍 개요

> 객체 (Object)
- 파이썬은 모두 객체로 이루어져 있음
- **객체(object)** = 특정 클래스의 **인스턴스(instance)**
  - 데이터 타입(int, string, list 등) = 클래스
  - 123, 'hello', [1,2,3] = 인스턴스
  
  ```python
  class Person:
    def __init__(self, name, gender):
      self.name = name
      self.gender = gender
    def greeting_message(self):
      return f'안녕하세요, {self.name}입니다.'

  jimin = Person('지민', '남')
  print(jimin.greeting_message())
  # 안녕하세요, 지민입니다.
  
  jieun = Person('지은', '여')
  print(jieun.greeting_message())
  # 안녕하세요, 지민입니다.
  ```

- 속성(attribute): 상태 (데이터, 인스턴스의 변수)
- 조작법(method): 행위 (인스턴스의 함수)

> 객체지향 프로그래밍(Object Oriented Programming, OOP)
- 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
- 절차지향 프로그래밍 vs 객체지향 프로그래밍
  
  ```python
  # 절차지향 프로그래밍
  def area(x, y):
    return x * y
  
  def circumference(x, y):
    return 2 * (x + y)

  a, b, c, d = 10, 30, 300, 20
  r1_area = area(a,b)
  r1_circumference = circumference(a,b)
  r2_area = area(c,d)
  r2_circumference = circumference(c,d)

  # 객체지향 프로그래밍
  class Rectangle: 
    def __init__(self, x, y):
      self.x = x
      self.y = y
    
    def area(x, y):
    return self.x * self.y
  
    def circumference(x, y):
      return 2 * (self.x + self.y)
  
  r1 = Rectangle(10, 30)
  r1.area()
  r1.circumference()

  r2 = Rectangle(300, 20)
  r2.area()
  r2.circumference()
  ```

- 특징: 추상화
- 장점
  - 프로그램을 유연하고 변경이 용이하게 함
  - 소프트웨어 개발과 보수를 간편하게 함
  - 직관적인 코드 분석 가능





# ✔ 객체지향 프로그래밍 문법
1. 클래스 정의
2. 인스턴스 생성
3. 인스턴스 메서드(method) 호출
4. 인스턴스 속성(attribute) 호출

    ```python
    # 1) 클래스 정의
    class MyClass:
      pass
    
    # 2) 인스턴스 생성
    my_instance = MyClass()

    # 3) 인스턴스 메서드 호출
    my_instance.my_method()

    # 4) 인스턴스 속성 호출
    my_instance.my_attribute
    ```
> 클래스와 인스턴스
- 클래스(class): 객체들의 분류
- 인스턴스(instance): 하나하나의 실체/사례

> 인스턴스 속성 (attribute)
- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 인스턴스의 변수
  1. 인스턴스 변수 정의: 생성자 메소드에서 `self.<변수명>`으로 정의
  2. 인스턴스 변수 접근 및 할당: 인스턴스가 생성된 후, `<인스턴스명>.<변수명>`으로 접근 및 할당
  
      ```python
      class Person:
        def __init__(self, name):
          self.name = name   # 인스턴스 변수 정의

      john = Person('john')   # 인스턴스 생성
      print(john.name)   # 인스턴스 변수에 접근
      # john

      john.name = 'John Kim'   # 인스턴스 변수에 접근 및 할당
      print(john.name)
      # John Kim
      ```
  
> 인스턴스 메소드 (method)
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- 인스턴스의 함수
  - 호출 시, 첫번째 인자로 **인스턴스 자기자신(self)**이 전달됨
- 생성자(constructor) 메소드: `__init__(self)`
  ```python
  class Person:
    def __init__(self):
      print('인스턴스가 생성되었음')

  jimin = Person('지민')
  # 인스턴스가 생성되었음
  ``` 
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  - 인스턴스 변수들의 초기값을 설정
- 소멸자(destructor) 메소드: `__del__(self)`
  ```python
  class Person:
    def __del__(self):
      print('인스턴스가 삭제되었음')
  
  jimin = Person('지민')
  del jimin
  # 인스턴스가 삭제되었음
  ```
  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드




# ✔ 객체 비교하기 (== 연산자 vs is 키워드)
1. `==`
   - equal(동등한)
   - 두 변수가 참조하는 객체가 **값이 같은** 경우, True 반환
2. `is`
   - identical(동일한)
   - 두 변수가 **동일한 객체**를 가리키는 경우, True 반환
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b, a is b)
    # True False
  
    a = [1, 2, 3]
    b = a
    print(a == b, a is b)
    # True True
    ```