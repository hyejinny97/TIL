# ✔ Python Datatype

> 파이썬 자료형의 분류
1. None Type
2. Boolean Type (불린형)
3. Numeric Type (수치형)
4. String Type (문자열)
5. Container (컨테이너)

*****
> None
- **값이 없음**을 표현

*****
> Boolean Type
- **True/False** 값을 가짐
- 비교/논리 연산을 수행함에 있어서 활용됨
- `bool()` 함수: 특정 데이터가 True인지 False인지 검증
- 결과값이 False인 데이터: 0, '', [], (), {}, None

*****
> Numeric Type
1. **정수 (int)**
   
   - 모든 정수의 타입은 int
   - 오버플로우(데이터 타입별로 사용할 수 있는 메모리 크기를 넘어서는 상황)가 발생하지 않음
2. **실수 (float)**
   
   - 정수가 아닌 모든 실수는 float 타입
   - 컴퓨터는 2진수로 실수를 표현하므로 floating point rounding error가 발생하기도 함
      ```python
      print(3.14 - 3.02)   # 결과: 0.12000000000001 
      ```
   - 따라서, 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의해야함
3. **복소수 (Complex)**
   
   - 실수부와 허수부(j)로 구성된 복소수는 complex 타입 

*****
> String Type
- 모든 **문자**는 str 타입

- 문자열은 작은 따옴표나 큰 따옴표를 활용하여 표기

- 중첩따옴표: 따옴표 안에 따옴표를 표현할 경우 
  ```python
  print("큰 따옴표 안에 '작은 따옴표'")
  print('작은 따옴표 안에 "큰 따옴표"')
  ```

- 삼중따옴표: 따옴표 안에 따옴표를 표현할 경우, 여러줄을 나눠 입력할 경우
  ```python
  print('''문자열 안에 '작은따옴표'나
  "큰 따옴표"를 표시 가능하고
  여러 줄 입력도 가능함''')
  ```

- 인덱싱이나 슬라이싱을 통해 문자열의 특정 값에 접근할 수 있음

- 문자열 연산자

  - 결합(Concatenation), 반복(Repetition), 포함(Membership)

    ```python
    # 결합
    print('hello' + ' python')   # 'hello python'
    
    # 반복
    print('hello' * 3)   # 'hellohellohello'
    
    # 포함
    print('a' in 'apple')   # True
    ```

- 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\\)를 활용하여 구분

- String Interpolation: 변수를 활용해 문자열 만드는 법

  1. %-formatting
  2. f-string

- 변경 불가 (Immutable), 반복 가능(Iterable)

*****

> cf) Index (인덱스)
- 파이썬에서 인덱스는 정수형 숫자(int)로 정의하며, 0부터 시작함

- s = 'abcde' 일때

  |       | 'a'  | 'b'  | 'c'  | 'd'  | 'e'  |
  | ----- | :--: | :--: | :--: | :--: | :--: |
  | index |  0   |  1   |  2   |  3   |  4   |
  | index |  -5  |  -4  |  -3  |  -2  |  -1  |

1. 인덱싱 (Indexing)
   
   - 변수[인덱스] 
   - 결과: 인덱스 위치에 해당하는 값을 출력
   
   ```python
   s = 'abcde'
   print(s[0])   # 'a'

2. 슬라이싱 (Slincing)

   - 변수[인덱스1 : 인덱스2 : [step]] 

   - 결과: 인덱스1과 (인덱스2 - 1)의 사이값 중 step만큼 건너뛴 값들을 출력 

   ```python
   s = 'abcdef'
   print(s[2:5])    # 'cde'
   print(s[2:5:2])  # 'ce' 
   print(s[5:2:-1]) # 'fed'
   print(s[:3])     # 'abc'
   print(s[5:])     # 'f'
   print(s[::])     # 'abcdef'
   print(s[::-1])   # 'fedcba'
   ```
   

*****

> cf)  Escape sequence

- 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\\)를 활용하여 구분

  | 예약문자 |  내용(의미)   |
  | :------: | :-----------: |
  |    \n    | 줄 바꿈, 개행 |
  |    \t    |      탭       |
  |    \r    |  캐리지리턴   |
  |    \0    |   널(Null)    |
  |    \\    |       \       |
  |    \'    |       '       |
  |   \\"    |       "       |



# ✔ Container (컨테이너)

- 여러 개의 값을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음

> 컨테이너의 분류

1. **시퀀스**형 컨테이너: 순서가 있는 데이터
   1. 문자열 (Immutable): 문자들의 나열
   2. 리스트 (mutable): 변경 가능한 값들의 나열
   3. 튜플 (Immutable): 변경 불가능한 값들의 나열
   4. 레인지 (Immutable): 숫자의 나열
2. **비시퀀스(=컬렉션)**형 컨테이너: 순서가 없는 데이터
   1. 세트 (mutable): 유일한 값들의 모음
   2. 딕셔너리 (mutable): 키-값들의 모음

*****

> Sequence Container (시퀀스형 컨테이너)

- 시퀀스형 주요 공통 연산자

  | 연산         | 설명                                     |
  | ------------ | ---------------------------------------- |
  | s[i]         | s변수의 i번째 항목                       |
  | s[i : j]     | s변수의 i에서 (j-1)까지의 슬라이스       |
  | s[i : j : k] | s변수의 i에서 (j-1)까지 스텝k의 슬라이스 |
  | s + t        | s변수와 t변수 이어붙이기                 |
  | s * n        | s변수를 n번 더함                         |
  | x in s       | s의 항목 중 하나가 x와 같으면 True       |
  | x not in s   | s의 항목에 x가 없으면 True               |
  | len(s)       | s의 길이                                 |
  | min(s)       | s의 가장 작은 항목                       |
  | max(s)       | s의 가장 큰 항목                         |

*****

> List 

- 변경 가능한 값들의 나열된 자료형

- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

- 변경 가능(mutable), 반복 가능(iterable)

- 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분

- 리스트 값 생성

  ```python
  # 값 생성
  list1 = [1, 'apple', True]
  list2 = list()
  list3 = []
  ```

- 리스트 값 접근 및 변경

  ```python
  # 값 접근
  a = [1,2,3]
  print(a[0])   # 1
  
  # 값 변경
  a[0] = '1'
  print(a)   # ['1', 2, 3]
  ```

- 리스트 값 추가 및 삭제

  - 리스트명.append(값)
  - 리스트명.pop(인덱스값)

  ```python
  # 값 추가
  a = [1,2,3]
  a.append(4)
  print(a)   # [1,2,3,4]
  
  # 값 삭제
  a.pop(0)
  print(a)   # [2,3,4]
  ```

*****

> Tuple

- 불변한 값들의 나열

- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

- 변경 불가 (immutable), 반복 가능 (iterable)

- 항상 소괄호 형태로 정의하며, 요소는 콤마로 구분

- 튜플 값 생성

  ```python
  # 값 생성
  tuple1 = (1, 'string', True)
  tuple2 = tuple()
  tuple3 = ()
  ```

- 튜플 값 접근

  ```python
  # 값 접근
  a = (1,2,3,1)
  print(a[1])   # 2
  ```

- 튜플 값 변경/추가/삭제 불가

*****

> Range

```python
# 범위 및 스텝 지정
range(n,m,s)  
```

-  숫자의 시퀀스를 나타내기 위해 사용
- n부터 (m-1)까지 s만큼 증가시키며 숫자의 시퀀스
- 변경 불가 (immutable), 반복 가능(iterable)

*****

> Associative Container (비시퀀스형 컨테이너)

*****

> Set

- 유일한 값들의 모음

- 순서가 없고, 중복된 값 없음

- 변경 가능 (mutable), 반복 가능 (iterable)

- 중괄호 형태로 정의

- 세트 값 생성

  ```python
  # 값 생성
  set1 = {1,2,3,1,2}   # {1,2,3}
  set2 = set()
  ```

- 세트 값 접근 불가

- 세트 값 추가 및 삭제

  - 세트명.add(값)
  - 세트명.remove(값)

  ```python
  # 값 추가
  a = {1,2,3}
  a.add(4)
  print(a)   # {1,2,3,4}
  
  # 값 삭제
  a.remove(1)
  print(a)   # {2,3,4}
  ```

- 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

*****

> Dictionary

- 키-값 쌍으로 이루어진 모음

  - 키 (Key): 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가)
  - 값(Value): 모든 데이터 타입 가능

- 키와 값은 `:`으로 구분되고, 개별 요소는 콤마로 구분됨

- 변경 가능 (mutable), 반복 가능 (iterable)

- 딕셔너리 값 생성

  ```python
  # 값 생성
  dict1 = {'키1': 1, '키2': [1,2,3]}
  dict2 = dict()
  dict3 = {}
  ```

- 딕셔너리 값 접근 및 변경

  ```python
  # 값 접근
  movie = {
      'title':'설국열차',
      'time':126,
      'adult':False
  }
  print(movie['title'])   # '설국열차'
  
  # 값 변경
  movie['time'] = 200
  print(movie)   # movie = {'title':'설국열차', 'time':200, 'adult':False}
  ```

- 딕셔너리 값 추가 및 삭제

  - 딕셔너리명.pop(키)

  ```python
  # 값 추가
  movie = {
      'title':'설국열차',
      'time':126,
      'adult':False
  }
  movie['actor'] = '송강호'
  print(movie) # movie = {'title':'설국열차', 'time':200, 'adult':False, 'actor':'송강호' }  
  
  # 값 삭제
  movie.pop('adult')
  print(movie)   # movie = {'title':'설국열차', 'time':200, 'actor':'송강호'}
  ```



# ✔ 자료형 변환 (Typecasting)

- 파이썬에서 데이터 형태는 서로 변환할 수 있음

1. 암시적 변환 (Implicit)

   - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우

     ```python
     # int + float
     3 + 5.0
     
     # bool +int
     True + 3
     ```

2. 명시적 변환 (Explicit)

   - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우

     ```python
     # int(str|float)
     int('3') + 4
     
     # float(str|int)
     float('3.5') + 5
     
     # str(int|float|list|tuple|dict)
     str(3) + '5'
     ```

     

# ✔ 연산자 (Operator)

> 연산자 분류
1. 논리 연산자 (Logical Operator)
2. 산술 연산자 (Arithmetic Operator)
2. 복합 연산자 (In-place Operator)
2. 비교 연산자 (Comparison Operator)


*****
> 논리 연산자
- 논리식을 판단하여 참(True)/거짓(False)를 반환함

  | 연산자  |                     내용                     |
  | :-----: | :------------------------------------------: |
  | A and B |     A 와 B 모두 True일 경우, True를 반환     |
  | A or B  | A 와 B 둘 중 하나가 True일 경우, True를 반환 |
  |   Not   |     True를 False로, False를 True로 반환      |
*****
> 산술 연산자

- 기본적인 사칙연산 및 수식 계산

  | 연산자 |   내용   |
  | :----: | :------: |
  |   +    |   덧셈   |
  |   -    |   뺄셈   |
  |   *    |   곱셈   |
  |   %    |  나머지  |
  |   /    |  나눗셈  |
  |   //   |    몫    |
  |   **   | 거듭제곱 |

*****

> 복합 연산자

- 연산과 할당이 함께 이뤄짐

  | 연산자  |    내용    |
  | :-----: | :--------: |
  | a += b  | a = a + b  |
  | a -= b  | a = a - b  |
  | a *= b  | a = a * b  |
  | a /= b  | a = a / b  |
  | a //= b | a = a // b |
  | a %= b  | a = a % b  |
  | a **= b | a = a ** b |

*****

> 비교 연산자

- 값을 비교하며, True/False 값을 리터함

  | 연산자 |   내용    |
  | :----: | :-------: |
  |   <    |   미만    |
  |   <=   |   이하    |
  |   >    |   초과    |
  |   >=   |   이상    |
  |   ==   |   같음    |
  |   !=   | 같지 않음 |



