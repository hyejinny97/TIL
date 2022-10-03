# ✔ 파이썬 모듈 
> 파이썬 기본 모듈
- [math 모듈](#-math-모듈)
- [random 모듈](#-random-모듈)
- [datetime 모듈](#-datetime-모듈)



# ✔ math 모듈
- 수학과 관련된 기능을 제공

1. `sin(x)`, `cos(x)`, `tan(x)`
   
   - 사인값, 코사인값, 탄젠트값을 구함

   ```python
   import math

   print(math.sin(1))
   # 0.8414709848078965
   print(math.cos(1))
   # 0.5403023058681398
   print(math.tan(1))
   # 1.5574077246549023
   ```

2. `log(x[, base])`
   
   - 로그값을 구함

   ```python
   import math

   print(math.log(8, 2))
   # 3.0
   ```

3. `ceil(x)`, `floor(x)`
   
   - 올림, 내림

   ```python
   import math

   print(math.ceil(2.5))
   # 3
   print(math.floor(2.5))
   # 2
   ```

4. `round(x)`

   - 반올림
   - 주의) 수학시간에 배운 반올림 방식과 약간 다름
     - 정수 부분이 짝수일 때, 소수점이 5이면 내림
     - 정수 부분이 홀수일 때, 소수점이 5이면 올림

   ```python
   import math

   print(round(1.5))
   # 2
   print(round(2.5))
   # 2
   ```


# ✔ random 모듈
- 랜덤한 값을 생성할 때 사용하는 모듈

1. `random()`

   - 0.0 <= x < 1.0 사이의 float를 반환

   ```python
   import random

   print(random.random())
   # 0.34938877573733607
   ```

2. `uniform(최소값, 최대값)`

   - 지정한 범위 사이의 **float**를 반환 (최소값 이상 최대값 미만의 난수)

   ```python
   import random

   print(random.uniform(10, 20))
   # 11.303178202241043
   ```

3. `randrange([최소값], 최대값)`

   - 지정한 범위 사이의 **int**를 반환 (최소값 이상 최대값 미만의 난수)
   - 최소값을 지정하지 않으면, 0부터 최대값 사이의 값을 반환

   ```python
   import random

   print(random.randrange(10, 20))
   # 16
   ```   

4. `choice(리스트)`

   - 리스트 내부에 있는 요소를 랜덤하게 선택
  
   ```python
   import random

   print(random.choice([1, 2, 3, 4, 5]))
   # 2
   ```   

5. `shuffle(리스트)`

   - 리스트의 요소들을 랜덤하게 섞음
   - 반환값은 `None`

   ```python
   import random

   nums = [1, 2, 3, 4, 5]
   random.shuffle(nums)
   print(nums)
   # [4, 2, 1, 3, 5]
   ```  

6. `sample(리스트, k=숫자)`

   - 리스트의 요소 중에 k개를 뽑음

   ```python
   import random

   print(random.sample([1, 2, 3, 4, 5], k=2))
   # [2, 5]
   ```    




# ✔ datetime 모듈
- 날짜와 시간을 조작하는 클래스를 제공
- 날짜와 시간 객체: aware객체, naive객체

> datetime 클래스
- datetime 객체는 date 객체와 time 객체의 모든 정보를 포함하는 단일 객체임

1. `now(tz=None)` 메서드

   - 현재의 지역 날짜와 시간을 반환

   ```python
   import datetime

   now = datetime.datetime.now()

   print(now)
   # 2022-09-11 14:22:33.146638

   print(f'{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초')
   # 2022년 9월 11일 14시 22분 33초
   ```