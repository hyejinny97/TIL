# ✔ SELECT문의 기본 형식

```sql
SELECT {열이름} 
    FROM {테이블명}
    WHERE {조건식}
    GROUP BY {열이름|표현식}
    HAVING {그룹조건식}
    ORDER BY {열이름|표현식}
    LIMIT {숫자} OFFSET {숫자};
```

> SELECT 문장 실행 순서

- 순서: `FROM` ⇒ `WHERE` ⇒ `GROUP BY` ⇒ `HAVING` ⇒ `SELECT` ⇒ `ORDER BY` ⇒ `LIMIT/OFFSET`
  - `FROM` 테이블을 대상으로
  - `WHERE` 제약조건에 맞춰 뽑은 후
  - `GROUP BY` 그룹화한다
  - `HAVING` ↳ 그룹 중에 조건과 맞는 것만을
  - `SELECT` 해당 열을 조회한 후
  - `ORDER BY` 정렬하고
  - `LIMIT/OFFSET` 특정 위치의 값을 가져온다


# ✔ SELECT문의 다양한 절

> AS
- 칼럼명이나 테이블명이 너무 길거나 다른 명칭으로 확인하고 싶을 때 ALIAS 활용
- AS를 생략하여 공백을 두고도 별칭으로 표현할 수 있음
- 별칭에 공백, 특수문자 등이 있는 경우 **큰 따옴표**로 묶어서 표기
  - 큰 따옴표 `" "`는 보통 alias(별칭)을 구분할 때 사용 (AS "평균 키")
  - 작은 따옴표 `' '`는 보통 값을 구분할 때 사용 (INSERT INTO ~ VALUES ('값1','값2'...))

  ```sql
  SELECT last_name AS 성 FROM users;
  SELECT last_name 성 FROM users;
  SELECT balance AS "계좌 잔고" FROM users;
  ```

> WHERE
- 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
- **WHERE절**에서 사용할 수 있는 연산자
  1. 비교 연산자: =, >, >=, <, <=
  
  2. 논리 연산자: `AND`, `OR`, `NOT`
   
- **SQL**에서 사용할 수 있는 연산자
  1. `BETWEEN 값1 AND 값2`
      - 값1과 값2 사이의 비교
      - 값1 <= 컬럼 <= 값2와 동일한 의미
  
  2. `IN (값1, 값2, ...)`
      - 목록 중에 값이 하나라도 일치하면 조건 만족
      - 컬럼=값1 OR 컬럼=값2 OR 컬럼=값3와 동일한 의미
  
  3. `LIKE`
      - 비교 문자열과 형태 일치 여부 판단
      - `%`: 0개 이상 문자 (이 자리에 문자열이 없을 수도 있음)
      - `_`: 1개 단일 문자 (반드시 이 자리에 한 개의 문자가 존재해야 함)

  4. `IS NULL`, `IS NOT NULL`
     - NULL여부를 확인할 때는 항상 `=` 대신 `IS`를 사용

  5. 부정연산자 `!=`, `^=`, `<>`, `NOT`
     - 같지 않다 

- 연산자 우선순위
   - 괄호 `()` > `NOT` > 비교연산자, SQL연산자 > `AND` > `OR`
  
  ```sql
  -- 주의! 아래 두 SQL문은 서로 다른 의미를 지님

  -- 1) 키가 175이거나 / 키가 183이면서 몸무게가 80인 사람
  WHERE height = 175 OR height = 183 AND weight = 80;
  -- 2) 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
  WHERE (height = 175 OR height = 183) AND weight = 80;
  ```

  ```sql
   -- ex) 주소가 서울인 데이터 조회
   SELECT * FROM classmates WHERE address='서울';
   -- ex) age가 30이상, 성이 '김'인 사람의 나이와 이름 조회
   SELECT age, first_name FROM users WHERE age >= 30 AND last_name='김';
   ```

> LIKE
- 패턴 일치를 기반으로 데이터를 조회하는 방법
- SQLite는 패턴 구성을 위한 2개의 wildcards(`%`, `_`)를 제공
  
  ```
  2%: 2로 시작하는 값
  %2: 2로 끝나는 값
  %2%: 2가 들어가는 값
  _2%: 아무 값이 하나 있고, 두 번째가 2로 시작하는 값
  1___: 1로 시작하고 총 4자리인 값
  2_%_% / 2__%: 2로 시작하고 적어도 3자리인 값
  ```

  ```sql
  -- ex) 지역 번호가 02인 사람만 조회
  SELECT * FROM users WHERE phone LIKE '02-%';
  -- ex) 이름이 '준'으로 끝나는 사람만 조회
  SELECT * FROM users WHERE first_name LIKE '%준';
  -- ex) 중간 번호가 5114인 사람만 조회
  SELECT * FROM users WHERE phone LIKE '%-5114-%';
  ```

> LIMIT
- 쿼리에서 반환되는 행 수를 제한
- 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용하기도 함
  - OFFSET: 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형
  - SELECT * FROM my_table LIMIT 10 OFFSET 5;
  - 위 SQL문은 '6번째 행부터 10개 행을 조회'를 의미
  
  ```sql
  -- ex) id, name 컬럼 값을 세번째에 있는 하나만 조회
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 3;
  ```


> DISTINCT
- 조회 결과에서 중복 행을 제거
- DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함
    
  ```sql
  -- ex) age 값 전체를 중복없이 조회
  SELECT DISTINCT age FROM classmates;
  ```

> ORDER BY
- 조회 결과 집합을 정렬
- SELECT문에 추가하여 사용
- 정렬 순서를 위한 2개의 키워드 제공
  - `ASC`: 오름차순 (default)
  - `DESC`: 내림차순
  
  ```sql
  -- ex) 나이 순으로 오름차순 정렬하여 상위 10개만 조회
  SELECT * FROM users ORDER BY age ASC LIMIT 10;
  -- ex) 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회
  SELECT * FROM users ORDER BY age, last_name LIMIT 10;
  -- ex) 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회
  SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
  -- ex) 계좌 잔액은 내림차순으로, 성은 오름차순으로 10개만 조회
  SELECT * FROM users ORDER BY balance DESC last_name ASC LIMIT 10;
  ```

> GROUP BY
- SELECT문의 optional 절
- 행 집합에서 요약 행 집합을 만듦
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- 쿼리문에 WHERE 절이 포함된 경우, **반드시 WHERE 절 뒤에 작성**해야 함
- 지정된 컬럼의 값이 같은 행들로 묶음
- **집계함수와 함께 활용**하였을 때 의미가 있음
- 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐
- GROUP BY 절에 명시하지 않은 컬럼은 별도로 지정할 수 없음
  - 그룹마다 하나의 행을 출력하게 되므로 집계 함수 등을 활용해야 함
- GROUP BY 절의 결과는 정렬되지 않음
  - 기존의 순서와 바뀌는 모습도 있음
  - 원칙적으로 관계형 데이터베이스에서는 ORDER BY를 통해 정렬
  
  ```sql
  -- ex) 각 성(last_name)씨가 몇 명씩 있는지 조회
  SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
  ```

> HAVING
- 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음 (실행 순서의 의해)
  - WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문
- 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING을 활용

  ```sql
  -- ex) 여러 성(last_name)씨 중 100명 이상 등장한 성만 조회
  SELECT last_name, COUNT(last_name) FROM users GROUP BY last_name HAVING COUNT(last_name) > 100;
  ```



# ✔ SQLite 집계 함수 (Aggregate Functions)
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
- 여러 행을부터 하나의 결과값을 반환하는 함수
- SELECT 구문에서만 사용됨

1. `COUNT`
   - 그룹의 항목 수를 가져옴
  
    ```sql
    -- ex) 테이블의 전체 행 수 조회
    SELECT COUNT(*) FROM users;
    ```

2. `AVG`
   - 모든 값의 평균을 계산
   - 해당 칼럼이 숫자(INTIGER)일 때만 사용 가능
  
    ```sql
    -- ex) 30살 이상인 사람들의 평균 나이 조회
    SELECT AVG(age) FROM users WHERE age >= 30;
    ```

3. `MAX`
   - 그룹에 있는 모든 값의 최대값을 가져옴
   - 해당 칼럼이 숫자(INTIGER)일 때만 사용 가능
  
    ```sql
    -- ex) 계좌 잔액이 가장 높은 사람과 그 액수 조회
    SELECT first_name, MAX(balance) FROM users;
    ```

4. `MIN`
   - 그룹에 있는 모든 값의 최소값을 가져옴
   - 해당 칼럼이 숫자(INTIGER)일 때만 사용 가능
  
    ```sql
    -- ex) 성이 '이'인 사람 중에 가장 작은 나이를 가진 사람의 이름 조회
    SELECT MIN(age), first_name FROM users WHERE last_name='이';
    ```
    
5. `SUM`
   - 모든 값의 합을 계산
   - 해당 칼럼이 숫자(INTIGER)일 때만 사용 가능



# ✔ 기본 함수와 연산
> 문자열 함수

1. `SUBSTR(문자열, start, length)`
   - 문자열 자르기
   - 시작인덱스는 1, 마지막 인덱스는 -1

2. `TRIM(문자열)`, `LTRIM(문자열)`, `RTRIM(문자열)`
   - 문자열 공백 제거

3. `LENGTH(문자열)`
   - 문자열 길이

4. `REPLACE(문자열, 패턴, 변경값)`
   - 패턴에 일치하는 부분을 변경

    ```sql
    SELECT phone, REPLACE(phone, '-', '') FROM users;
    ```

5. `UPPER(문자열)`, `LOWER(문자열)`
   - 대소문자 변경

6. `문자열1 || 문자열2`
   - 문자열 합치기(concatenation)

    ```sql
    SELECT last_name || first_name 이름 FROM users;
    ```

> 숫자 함수

1. `ABS(숫자)`
   - 절대값

2. `SIGN(숫자)`
   - 부호 (양수 1, 음수 -1, 0은 0)

3. `MOD(숫자1, 숫자2)`
   - 숫자1을 숫자2로 나눈 나머지

4. `CEIL(숫자)`, `FLOOR(숫자)`, `ROUND(숫자, 자리)`
   - 올림, 내림, 반올림

5. `POWER(숫자1, 숫자2)`
   - 숫자1의 숫자 2 제곱

6. `SQRT(숫자)`
   - 제곱근

> 산술 연산자
- +, -, *, /와 같은 산술 연산자와 우선순위를 지정하는 ()기호를 연산에 활용할 수 있음

  ```sql
  SELECT age + 1 FROM users;
  SELECT weight / (height * height * 0.0001) AS BMI FROM users;
  ```