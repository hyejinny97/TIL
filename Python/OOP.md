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

- 장점
  - 프로그램을 유연하고 변경이 용이하게 함
  - 소프트웨어 개발과 보수를 간편하게 함
  - 직관적인 코드 분석 가능





# ✔ 객체지향 프로그래밍 문법
1. 클래스 정의
2. 인스턴스 생성
3. 메서드(method) 호출
   - 인스턴스 메서드 (instance method)
   - 클래스 메서드 (class method)
   - 스태틱 메서드 (static method)
4. 속성(attribute) 호출
   - 인스턴스 속성 (instance attribute)
   - 클래스 속성 (class attribute)

    ```python
    # 1) 클래스 정의
    class MyClass:
      class_variable = '클래스 변수'   # 클래스 속성 정의

      def __init__(self): 
          self.instance_variable = '인스턴스 변수'   # 인스턴스 속성 정의
      
      # 인스턴스 메서드 정의
      def instance_method(self):
          return self, self.instance_variable
      
      # 클래스 메서드 정의
      @classmethod
      def class_method(cls):
          return cls, cls.class_variable
      
      # 스태틱 메서드 정의
      @staticmethod
      def static_method():
          return '스태틱 메서드'
    

    # 2) 인스턴스 생성
    my_instance = MyClass()

    # 3-1) 인스턴스 메서드 호출
    my_instance.instance_method()

    # 3-2) 클래스 메서드 호출
    my_instance.class_method()

    # 3-3) 스태틱 메서드 호출
    my_instance.static_method()

    # 4-1) 인스턴스 속성 호출
    my_instance.instance_variable

    # 4-2) 클래스 속성 호출
    my_instance.class_variable
    ```
> 클래스와 인스턴스
- 클래스(class): 객체들의 분류
- 인스턴스(instance): 하나하나의 실체/사례

*****
> 인스턴스 속성 (instance attribute)
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
  
> 인스턴스 메소드 (instance method)
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- 인스턴스의 함수
  - 호출 시, 첫번째 인자로 인스턴스 **자기자신(self)**이 전달됨
  - 호출한 인스턴스를 의미하는 self 매개변수를 통해 인스턴스 조작 가능

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

*****
> 클래스 속성 (class attribute)
- 한 클래스의 모든 인스턴스라면 똑같은 값을 가지고 있는 속성
- 클래스의 변수
  1. 클래스 변수 정의: 클래스 선언 내부에서 `<변수명>`으로 정의
  2. 클래스 변수 접근 및 할당: `<클래스명>.<변수명>`으로 접근 및 할당
- 인스턴스에서 특정 속성(변수)에 접근할 때, 인스턴스 - 클래스 순으로 namespace 탐색
  - 인스턴스 namespace에 특정 변수가 없으면, 클래스 namespace에서 변수 탐색
  - 따라서, `<인스턴스명>.<변수명>`으로도 클래스 변수에 접근 및 할당이 가능
  
  ```python
  class Circle:
    pi = 3.14
  
  c1 = Circle()
  print(Circle.pi)
  # 3.14
  print(c1.pi)
  # 3.14
  ```

> 클래스 메소드 (class method)
- 클래스가 사용할 메소드
  - 호출 시, 첫 번째 인자로 **클래스(cls)**가 전달됨
  - 클래스를 의미하는 cls 매개변수를 통해 클래스 조작 가능
- `@classmethod` 데코레이터를 사용하여 클래스 메소드를 정의
  - 데코레이터(decorator): 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
  
  ```python
  class MyClass:

    @classmethod
    def class_method(cls, arg1, ...):
      pass
  ```

*****
> 스태틱 메소드 (static method)
- 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
  - 호출 시, 어떠한 인자도 **전달되지 않음**
  - 즉, 스태틱 메소드는 클래스/객체 정보에 접근 및 수정이 불가함
- 속성(변수)을 다루지 않고 단지 기능만을 하는 메소드를 정의하고 싶을때 사용
- `@staticmethod` 데코레이터를 사용하여 정의'
  
  ```python
  class MyClass:

    @staticmethod
    def static_method(arg1, ...):
      pass
  ```



# ✔ 객체지향 프로그래밍 특징
1. 추상화
2. 상속
3. 다형성
4. 캡슐화

> 추상화
- 현실 세계에서 존재하는 모든 사물의 공통 기능을 유추해서 클래스를 만드는 일련의 과정

> 상속
- 두 클래스 사이를 부모-자식 관게로 정립하는 것
- 자식클래스를 정의할 때, 괄호 안에 부모 클래스명을 넣어주면 상속 됨
  
  ```python
  class ChildClass(ParentClass):
    pass
  ```

- 하위 클래스는 상위 클래스의 모든 요소(정의된 속성, 행동, 관계 및 제약 조건)를 상속 받음
- 부모클래스의 속성, 메소드가 자식 클래스에 상속되므로 코드 재사용성이 높아짐
- 파이썬의 모든 클래스는 object로부터 상속됨
- 상속관계에서 namespace는 인스턴스 - 자식클래스 - 부모클래스 순으로 탐색
- 메서드 오버라이딩(덮어쓰기)을 통해서 자식 클래스에서 재정의 가능함
  
  ```python
  class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def talk(self):
      print(f'반갑습니다. {self.name}입니다.')
  
  class Professor(Person):
    def __init__(self, name, age, department):
      self.name = name
      self.age = age
      self.department = department
  
  class Student(Person):
    def __init__(self, name, age, gpa):
      self.name = name
      self.age = age
      self.gpa = gpa
  

  # 인스턴스 생성
  p1 = Professor('박교수', 46, '컴퓨터공학과')
  s1 = Student('김학생', 20, 3,5)

  # 인스턴스 메소드 호출
  p1.talk()   # 반갑습니다. 박교수입니다.
  s1.talk()   # 반값습니다. 김학생입니다.
  ```
#### cf) 상속 관련 함수와 메소드
1. `isinstance(객체명, 클래스명)`
   - 객체가 지정한 클래스의 인스턴스이거나 서브클래스인 경우 True 반환
      
      ```python
      print(isinstance(p1, Person))    # True
      print(isinstance(p1, Professor)) # True
      print(isinstance(p1, Student))   # False
      print(isinstance(s1, Person))    # True
      print(isinstance(s1, Professor)) # False
      print(isinstance(s1, Student))   # True
      ```

2. `issubclass(클래스1명, 클래스2명)`
   - 클래스1이 클래스2의 서브클래스이면 True 반환
   - 클래스2에는 클래스 객체의 튜플로도 지정 가능
     - 클래스 튜플의 모든 항목을 검사한 후, 그 중 하나라도 서브클래스에 해당하면 True 반환
      
      ```python
      print(issubclass(bool, int))   # True
      print(issubclass(float, int))  # False
      print(issubclass(Professor, Person))   # True
      print(issubclass(Professor, (Person, Student)))   # True
      ```

3. `super()`
   - 자식클래스에서 부모클래스의 정보를 그대로 사용하고 싶은 경우
      
      ```python
      class Student(Person):
        def __init__(self, name, age, gpa):
          super().__init__(name, age)   # super() == Person 클래스 
          self.gpa = gpa
      ```

#### cf) 다중 상속
- 두개 이상의 클래스를 상속 받는 경우
- 상속 받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

> 다형성 (Polymorphism)
- 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
- 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답될 수 있음
- 메소드 오버라이딩
  - 상속 받은 메소드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경
  - 부모 클래스의 메소드 이름과 기본 기능을 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
  
  ```python
  class Person:
    def __init__(self, name):
      self.name = name
    
    def talk(self):
      print(f'반갑습니다. {self.name}입니다.')
  
  class Professor(Person):
    def talk(self):
      print(f'{self.name}일세.')
  
  class Student(Person):
    def talk(self):
      super().talk()
      print(f'저는 학생입니다.')
  

  # 인스턴스 생성
  p1 = Professor('박교수')
  s1 = Student('김학생')

  p1.talk()   
  # 김교수일세.
  s1.talk()   
  # 반값습니다. 김학생입니다.
  # 저는 학생입니다.
  ```

> 캡슐화
- 객체의 일부 구현 내용에 대해 외부로부터 직접적인 접근을 차단
- 파이썬에서 기능상으로는 존재하지 않지만, 관용적으로 사용되는 표현이 있음
- 접근제어자 종류
  1. Public Access Modifier
      - 언더바 없이 시작하는 메소드나 속성
      - 어디서나 호출이 가능
      - 하위클래스에서 메소드 오버라이딩 가능
  2. Protected Access Modifier
      - 언더바 1개 `_`로 시작하는 메소드나 속성
      - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
  3. Private Access Modifier
      - 언더바 2개 `__`로 시작하는 메소드나 속성
      - 본 클래스 내부에서만 사용 가능





# ✔ 객체 비교하기 (== 연산자 vs is 키워드)
1. `==` 연산자
   - equal(동등한)
   - 두 변수가 참조하는 객체가 **값이 같은** 경우, True 반환
2. `is` 키워드
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