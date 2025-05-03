# ✔ SELECT 기본

- SELECT 문은 구축이 완료된 테이블에서 데이터를 추출하는 기능을 함

## 1️⃣ 기본 조회하기: SELECT ~ FROM

### USE 문

```
USE 데이터베이스_이름;
```

- 현재 사용하는 데이터베이스를 지정 또는 변경하는 형식

### SELECT 문의 기본 형식

```
SELECT 열_이름
    FROM  테이블_이름
    WHERE 조건식
    GROUP_BY 열_이름
    HAVING 조건식
    ORDER_BY 열_이름
    LIMIT 숫자
```

### SELECT와 FROM

- ex) marker_db를 선택한 후, 회원 테이블의 모든 열을 조회해라

  ```
  USE marker_db;
  SELECT * FROM member;
  ```

- 테이블 이름을 `데이터베이스_이름.테이블_이름` 형식으로도 표현 가능

  ```
  SELECT * FROM marker_db.member;
  ```

- ex) 회원 테이블에서 주소, 데뷔 날짜, 이름 열만 조회해라

  ```
  SELECT addr, debut_date, mem_name FROM member;
  ```

- 열 이름에 별칭(alias) 지정 가능

  ```
  SELECT addr, debut_date "데뷔 일자", mem_name FROM member;
  ```

## 2️⃣ 특정한 조건만 조회하기: SELECT ~ FROM ~ WHERE

### 기본적인 WHERE 절

- WHERE 절은 조회하는 결과에 특정한 조건을 추가해서 원하는 데이터만 보고 싶을 때 사용
- ex) 회원 테이블에서 그룹명(mem_name)이 '블랙핑크'인 데이터만 조회해라

  ```
  SELECT * FROM member WHERE mem_name = '블랙핑크';
  ```

- ex) 회원 테이블에서 그룹 인원(mem_number)이 4명인 데이터만 조회해라

  ```
  SELECT * FROM member WHERE mem_number = 4;
  ```

### 관계 연산자, 논리 연산자의 사용

- 관계 연산자: >, <, >=, <=, = 등
- 논리 연산자: AND, OR
- ex) 회원 테이블에서 평균 키(height)가 162 이하인 데이터만 조회해라

  ```
  SELECT * FROM member WHERE height <= 162;
  ```

- ex) 회원 테이블에서 평균 키가 165 이상이면서 그룹 인원이 6명 초과인 데이터만 조회해라

  ```
  SELECT * FROM member WHERE height >= 165 AND mem_number > 6;
  ```

### BETWEEN ~ AND

- ex) 회원 테이블에서 평균 키가 163 ~ 165인 데이터만 조회해라

  ```
  SELECT * FROM member WHERE height BETWEEN 163 AND 165;
  ```

### IN()

- ex) 회원 테이블에서 주소가 경기/전남/경남 중 한 곳에 사는 데이터만 조회해라

  ```
  SELECT * FROM member WHERE add IN('경기', '전남', '경남');
  ```

### LIKE

- LIKE는 문자열의 일부 글자를 검색하기 위해 사용
  - 문자열 내 `%`: 여러 문자에 대응하는 기호
  - 문자열 내 `_`: 한 문자에 대응하는 기호
- ex) 회원 테이블에서 그룹 이름의 첫 글자가 '우'로 시작하는 그룹을 조회해라

  ```
  SELECT * FROM member WHERE mem_name LIKE '우%';
  ```

- ex) 회원 테이블에서 그룹 이름의 앞 두글자 뒤에 '핑크'로 끝나는 그룹을 조회해라

  ```
  SELECT * FROM member WHERE mem_name LIKE '__핑크';
  ```

## 3️⃣ 서브 쿼리 (Subquery)

- SELECT 안에 또 다른 SELECT가 들어간 쿼리
- ex) 회원 테이블에서 그룹 이름이 '에이핑크'인 그룹의 평균 키보다 큰 그룹을 조회해라

  ```
  SELECT * FROM member
    WHERE height > (SELECT height FROM member WHERE mem_name = '에이핑크');
  ```
