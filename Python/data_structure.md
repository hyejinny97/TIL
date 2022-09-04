# ✔ 데이터 구조 (Data Structure)
- 데이터타입.메서드()

> 데이터 타입
1. 시퀀스 (순서가 있는 데이터 구조)
   - 문자열(string)
   - 리스트(list)
2. 컬렉션 (순서가 없는 데이터 구조)
   - 세트(set)
   - 딕셔너리(dictionary)



# ✔ 시퀀스 타입의 methods

> 문자열 (String)
1. 문자열 관련 탐색/검증 메서드
   - `문자열.find(x)`: x의 첫번째 **인덱스**를 반환, 없으면 **-1**을 반환
   - `문자열.index()`: x의 첫번째 **인덱스**를 반환, 없으면 **오류** 발생
   - `문자열.isalpha()`: 알파벳 문자이면 True 반환
   - `문자열.isdigit()`: 숫자이면 True 반환
   - `문자열.isalnum()`: 알파벳 또는 숫자로만 구성되면 True 반환
   - `문자열.isupper()`: 대문자이면 True 반환
   - `문자열.islower()`: 소문자이면 True 반환
   - `문자열.istitle()`: 타이틀 형식이면 True 반환
   - `문자열.count(x)`: 문자열에서 특정 문자의 갯수를 반환
  
      ```python
      print('banana'.count('a'))
      # 3
      print('banana'.count('na'))
      # 2
      ```

2. 문자열 관련 변경 메서드
   - `문자열.replace(old, new, [갯수])`: 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
     -  갯수를 지정하면 해당 갯수만큼만 시행
      
      ```python
      print('wooooowoo'.replace('o', '!', 2))
      # w!!ooowoo
      print('happyhacking'.replace('happy', 'angry'))
      # angryhacking
      print('happyhacking'.replace('happy', ''))
      # hacking
      ```

   - `문자열.strip([chars])`: 공백이나 특정 문자를 제거
     - 문자열을 지정하지 않으면 공백이나 개행(\n)을 제거
     - 제거할 문자를 여러 개 넣으면, 해당하는 모든 문자들을 제거
     - `.strip()`: 양쪽을 제거
     - `.lstrip()`: 왼쪽을 제거
     - `.rtrip()`: 오른쪽을 제거
      
      ```python
      print('     와우!!\n'.strip())
      # '와우!!'
      print('와우!!'.rstrip('!'))
      # '와우'
      print('Hello World'.strip('Hd'))
      # 'ello Worl'
      ```

   - `문자열.split(sep=None, maxsplit=-1)`: 공백이나 특정 문자를 기준으로 분리
     - 문자열을 특정한 단위로 나눠 **리스트**로 반환
     - sep이 따로 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주, 선행/후행 공백은 빈 문자열에 포함시키지 않음
     - maxsplit이 -1인 경우에는 제한이 없음
      
      ```python
      print('a b c'.split())
      # ['a', 'b', 'c']
      ```

   - `'구분자'.join([iterable])`: iterable한 컨테이너 요소들을 구분자로 함쳐 **문자열**로 반환
     - iterable에 문자열이 아닌 값이 있으면 TypeError 발생
      
      ```python
      print(''.join(['a', 'b']))
      # ab
      print(','.join('happy'))
      # h,a,p,p,y
      ```

   - `문자열.capitalize()`: 가장 첫 번째 글자를 대문자로 변경
   - `문자열.title()`: `'`나 공백 이후를 대문자로 변경
   - `문자열.upper()`: 모두 대문자로 변경
   - `문자열.lower()`: 모두 소문자로 변경
   - `문자열.swapcase()`: 대문자와 소문자를 서로 변경

> 리스트 (List)
1. 리스트 관련 값 추가/삭제 메서드
   - `리스트.append(x)`: 리스트 마지막에 항목 x를 추가
   - `리스트.extend(iterable)`: 리스트에 iterable의 항목을 추가
      - `[리스트1] = [리스트1] + [리스트2]`와 같은 기능
      
      ```python
      names = ['john', 'jenny']
      names.extend(['nick', 'tom'])
      print(names)
      # ['john', 'jenny', 'nick', 'tom']
      ```

   - `리스트.insert(i, x)`: 리스트 인덱스 i에 항목 x를 삽입
     - 인덱스 i가 리스트 길이보다 큰 경우, 맨 뒤에 삽입
   - `리스트.remove(x)`: 첫번째 항목 x를 제거
     - 항목 x가 존재하지 않을 경우 ValueError 발생
   - `리스트.pop(i)`: 리스트의 인덱스 i에 있는 항목을 반환 후 제거
     - 인덱스를 지정하지 않을 경우, 리스트 가장 마지막 항목을 반환 후 제거
   - `리스트.clear()`: 모든 항목을 삭제함

2. 리스트 관련 탐색 및 정렬
   - `리스트.index(x, start, end)`: 첫번째 항목 x의 **인덱스**를 반환
     - 리스트에 항목 x가 없는 경우 ValueError를 발생
     - start와 end를 지정해주면 두 인덱스의 항목 사이에서 x를 찾아 인덱스를 반환해줌
   - `리스트.reverse()`: 리스트를 거꾸로 정렬
     - **원본** 리스트를 거꾸로 정렬
     - None을 반환
     - `reversed(리스트) 함수`: 원본이 아닌 복제본을 정렬해, 거꾸로 정렬된 리스트를 반환
   - `리스트.sort()`: 리스트를 오름차순으로 정렬
     - `reverse=True` 옵션을 통해 내림차순으로 정렬 가능
     - **원본** 리스트를 정렬
     - None을 반환
     - `sorted(리스트) 함수`: 원본이 아닌 복제본을 정렬해, 정렬된 리스트를 반환
   - `리스트.count(x)`: 리스트에서 항목 x의 갯수를 반환



# ✔ 컬렉션 타입의 methods

> 세트 (Set)
1. 세트 관련 값 추가/삭제 메서드
   - `세트.copy()`: 세트의 얕은 복사본을 반환
   - `세트.add(x)`: 항목 x가 세트에 없다면 추가
   - `세트.pop()`: 세트에서 랜덤하게 항목을 반환하고, 해당 항목을 제거
     - 세트가 비어있을 경우 KeyError 발생
   - `세트.remove(x)`: 세트에서 항목 x를 삭제
     - 항목 x가 존재하지 않을 경우 KeyError 발생
   - `세트.discard(x)`: 세트에 항목 x가 있는 경우 삭제
   - `세트s.update(세트t)`: 세트t의 모든 항목 중 세트 s에 없는 항목 추가
   - `세트.clear()`: 모든 항목을 제거

2. 세트 관련 검증 메서드
   - `세트s.isdisjoint(세트t)`: 세트s가 세트t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우 True 반환
   - `세트s.issubset(세트t)`: 세트s가 세트t의 하위 세트인 경우 True 반환
   - `세트s.issuperset(세트t)`: 세트s가 세트t의 상위 세트인 경우 True 반환

3. 수학에서의 집합과 관련된 기호
   - 세트1 `+` 세트2: 세트1과 세트2의 합집합
   - 세트1 `-` 세트2: 세트1과 세트2의 차집합
   - 세트1 `&` 세트2: 세트1과 세트2의 교집합
   - 세트1 `^` 세트2: 세트1과 세트2의 대칭 차집합'

      ![집합](https://2506709490-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKLx6PA5iF3Uq2IzQsf%2F-LKM6rLq40OpYV8Jv5il%2F-LKM7iM3pCfbS4h6Lq-6%2FC7EEA172-39EF-49BA-876D-CD2A72D5E2DC.png?alt=media&token=d054a78a-98bc-4085-bfdb-7405dbe5dd70)

> 딕셔너리 (Dictionary)
1. 딕셔너리 관련 탐색 메서드
   - `딕셔너리.keys()`: 딕셔너리의 모든 키를 담은 dict_key 객체를 반환
   - `딕셔너리.values()`: 딕셔너리의 모든 값을 담은 dict_values 객체를 반환
   - `딕셔너리.items()`: 딕셔너리의 모든 (키,값)의 쌍을 담은 dict_items 객체를 반환
   - `딕셔너리.get(k, default=None)`: 키 k의 **값**을 반환
     - default를 지정할 경우, 키 k가 없을 때 default를 반환
     - default를 지정하지 않을 경우, 키 k가 없을 때 None을 반환
      
      ```python
      # 1) 딕셔너리[키]를 통해 값에 접근하는 경우 
      # 키가 없을때 KeyError가 발생
      my_dict = {'apple':'사과', 'banana':'바나나'}
      my_dict['melon']
      # KeyError 발생

      # 2) get(키) 메서드를 통해 값에 접근하는 경우
      # 키가 없으면 default를 반환
      my_dict = {'apple':'사과', 'banana':'바나나'}
      print(my_dict.get('melon'))
      # None
      print(my_dict.get('melon', 100))
      # 100
      ```

2. 딕셔너리 관련 값 변경/삭제 메서드
   - `딕셔너리.pop(k, [default])`: 키 k의 **값**을 반환하고, 딕셔너리에서 삭제
     - default를 지정할 경우, 키 k가 없을 때 default를 반환
     - default를 지정하지 않을 경우, 키 k가 없을 때 KeyError 발생
   - `딕셔너리.update(키=값)`: 인자로 넘겨준 키, 값을 딕셔너리에 덮어씀
      
      ```python
      my_dict = {'apple':'사과', 'banana':'바나나'}
      my_dict.update(apple='문경 사과')
      print(my_dict)
      # {'apple':'문경 사과', 'banana':'바나나'}
      ```

   - `딕셔너리.clear()`: 모든 항목 제거