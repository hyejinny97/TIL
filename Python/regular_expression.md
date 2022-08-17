# ✔ 정규 표현식 (Regular Expression)
- 복잡한 문자열을 처리할 때 사용하는 기법 
- 파이썬만의 고유 문법이 아닌 문자열을 처리하는 모든 곳에서 사용됨
  
> 메타 문자 (meta characters)
- 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자
- . ^ $ * + ? { } [ ] \ | ( )

1. 문자 클래스(character class) - `[ ]`
   - `[ ]` 사이의 문자들과 매치
     - 주의) `^` 메타 문자를 사용할 경우에는 반대(not)라는 의미를 가짐
   - `[ ]` 사이에는 어떤 문자도 들어갈 수 있음
   - `[ ]` 안의 두 문자 사이에 하이픈(-)을 사용하면, 두 문자 사이의 범위(From - To)를 의미
  
    ```
    [abc]: a, b, c 중 한 개의 문자와 매치
    [a-zA-Z] : 알파벳 모두와 매치
    [0-9] : 숫자와 매치
    [^0-9]: 숫자가 아닌 문자만 매치
    ```
   
   - 자주 사용하는 `[]` 정규식은 아래와 같이 별도의 표기법으로 표현할 수 있음
    
    ```
    \d: 숫자와 매치 = [0-9]
    \D: 숫자가 아닌 것과 매치 = [^0-9]

    \s: whitespace 문자와 매치 = [ \t\n\r\f\v] (맨 앞의 빈 칸은 공백문자)
    \S: whitespace 문자가 아닌 것과 매치 = [^ \t\n\r\f\v]

    \w: 문자+숫자(alphanumeric)와 매치 = [a-zA-Z0-9_]
    \W: 문자+숫자(alphanumeric)가 아닌 문자와 매치 = [^a-zA-Z0-9_]
    ```

2. 점(Dot) - `.`
   - `\n`을 제외한 모든 문자와 매치
   - 주의) a[.]b: `[]` 내에 `.` 문자가 사용된다면 이것은 "모든 문자"라는 의미가 아닌 문자 `.` 그대로를 의미

    ```
    a.b: a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치 (ex) aab, a0b)
    ```

3. 반복(Kleene star) - `*`
   - 반복을 나타내는 메타 문자
   - `*` 바로 앞에 있는 문자가 **0회부터 무한대**로 반복될 수 있다는 의미

    ```
    ca*t: 문자 'a'가 0회부터 무한대로 반복되면 매치 (ex) ct, cat, caaat)
    ```

4. 반복(Kleene plus) - `+`
   - 반복을 나타내는 다른 메타 문자
   - `+` 바로 앞에 있는 문자가 **1회부터 무한대**로 반복될 수 있다는 의미

    ```
    ca+t: 문자 'a'가 1회부터 무한대로 반복되면 매치 (ex) cat, caaat)
    ```

5. 반복 제한 - `{i, j}`
   - `{ }` 메타 문자를 사용하면 반복 횟수를 고정할 수 있음
   - `{i, j}` 바로 앞에 있는 문자가 **i부터 j까지** 반복될 수 있다는 의미
   
    ```
    ca{2}t: 문자 'a'가 2번 반복되면 매치 (ex) caat)
    ca{2,5}t: 문자 'a'가 2번 ~ 5번 반복되면 매치 (ex) caat, caaat)
    ```
   
   - i 또는 j는 생략 가능

    ```
    {3,}: 반복 횟수가 3 이상이면 매치
    {,3}: 반복 횟수가 3 이하이면 매치
    {0,}: 반복 횟수가 0 이상이면 매치 = Kleene star(*)
    {1,}: 반복 횟수가 1 이상이면 매치 = Kleene plus(+)
    ```

6. 반복 제한 - `?`
   - `?` 바로 앞에 있는 문자가 **0회부터 1회까지** 반복될 수 있다는 의미
   - `{0, 1}`와 동일한 의미

    ```
    ab?c: 문자 'b'가 0번 ~ 1번 반복되면 매치 (ex) ac, abc)
    ```



# ✔ 파이썬의 re 모듈
- 파이썬은 정규 표현식을 지원하기 위해 re (regular expression) 모듈을 제공
- `re.compile(정규식)`는 정규 표현식을 컴파일하는 기능을 하며, 컴파일된 패턴 객체를 반환해 줌

    ```python
    import re

    p1 = re.compile('ab*')
    p2 = re.compile('[a-zA-Z]+@[a-zA-Z]+\.com')   # 이메일 패턴
    p3 = re.compile('[a-zA-Z]{0,4}')
    ```

- 패턴(pattern): 정규식을 컴파일한 결과
- 컴파일된 패턴 객체를 사용하여 문자열 검색 가능
  - match(), search(), findall(), finditer() 메서드를 이용하여 문자열 검색 가능

> match() 메서드   
- 문자열의 **처음부터** 정규식과 매치되는지 조사
- 정규식과 매치되면 **match 객체** 반환, 매치되지 않으면 None 반환

    ```python
    import re

    p = re.compile('[a-z]+')
    m = p.match("python")
    print(m)
    # <re.Match object; span=(0, 6), match='python'>

    m = p.match("3 python")
    print(m)
    # None

    p = re.compile('[a-z ]+')
    m = p.match('string goes here')
    if m:
        print('Match found: ', m.group())
    else:
        print('No match')
    ```

> search() 메서드
- 문자열 **전체**를 검색하여 정규식과 매치되는지 조사
- 정규식과 매치되면 **match 객체** 반환, 매치되지 않으면 None 반환
  
    ```python
    import re

    p = re.compile('[a-z]+')
    m = p.search("python")
    print(m)
    # <re.Match object; span=(0, 6), match='python'>

    m = p.search("3 python")
    print(m)
    # <re.Match object; span=(2, 8), match='python'>
    ```

> findall() 메서드
- 정규식과 매치되는 **모든 substring**을 **리스트**로 반환

    ```python
    import re

    p = re.compile('[a-z]+')
    result = p.findall("life is too short")
    print(result)
    # ['life', 'is', 'too', 'short']
    ```

> finditer() 메서드
- 정규식과 매치되는 **모든 substring**을 **iterable 객체**로 반환

    ```python
    import re

    p = re.compile('[a-z]+')
    result = p.finditer("life is too short")
    print(result)
    # <callable_iterator object at 0x01F5E390>

    for r in result: 
        print(r)
    # <re.Match object; span=(0, 4), match='life'>
    # <re.Match object; span=(5, 7), match='is'>
    # <re.Match object; span=(8, 11), match='too'>
    # <re.Match object; span=(12, 17), match='short'>
    ```

*****
> cf) match 객체의 메서드
- match() 메서드와 search() 메서드의 결과로 match 객체가 반환됨

1. `grop()`
   - 매치된 문자열을 반환해 줌

2. `start()`
   - 매치된 문자열의 시작 위치를 반환해 줌
   - match 메서드에 의해 반환된 match 객체의 start() 결괏값은 항상 0
     - match 메서드는 항상 문자열의 시작부터 조사하기 때문

3. `end()`
   - 매치된 문자열의 끝 위치를 반환해 줌

4. `span()`
   - 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환해 줌

    ```python
    import re

    p = re.compile('[a-z]+')
    m1 = p.match("python")
    
    print(m1.group())   # 'python'
    print(m1.start())   # 0
    print(m1.end())     # 6
    print(m1.span())    # (0, 6)

    m2 = p.search("3 python")
    print(m2.group())   # 'python'
    print(m2.start())   # 2
    print(m2.end())     # 8
    print(m2.span())    # (2, 8)
    ```

> 축약된 형태로 re 모듈 사용하기
- 정규 표현식 컴파일과 match 메서드를 한 번에 수행 가능
- 보통 한 번 만든 패턴 객체를 여러번 사용해야 할 때는, 축약된 형태보다 `re.compile`을 사용하는 것이 편리함

    ```python
    import re

    # 오리지날 형태
    p = re.compile('[a-z]+')
    m = p.match("python")

    # 축약된 형태
    m = re.match('[a-z]+', "python")
    ```