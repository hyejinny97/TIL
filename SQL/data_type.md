# ✔ MySQL의 데이터 형식

- MySQL에서 제공하는 데이터 형식의 종류는 수십 개 정도이고, 각 데이터 형식마다 크기나 표현할 수 있는 숫자의 범위가 다름

## 1️⃣ 데이터 형식

### 정수형

| 데이터 형식 | 바이트 수 | 숫자 범위         |
| ----------- | --------- | ----------------- |
| `TINYINT`   | 1         | -128 ~ 127        |
| `SMALLINT`  | 2         | -32,768 ~ 32,767  |
| `INT`       | 4         | 약-21억 ~ +21억   |
| `BIGINT`    | 8         | 약-900경 ~ +900경 |

- 소수점이 없는 숫자
- UNSIGNED 예약어를 사용하면 값의 범위가 0부터 시작됨
  - TINY UNSIGNED의 숫자 범위: 0 ~ 255
- ex) 회원 테이블을 생성해라

  ```
  CREATE TABLE member
    (
      mem_number TINYINT NOT NULL,
      height TINYINT UNSIGNED,
      ...
    );
  ```

### 문자형

| 데이터 형식     | 바이트 수 |
| --------------- | --------- |
| `CHAR(개수)`    | 1~255     |
| `VARCHAR(개수)` | 1~16383   |

- CHAR는 고정길이 문자형으로, 자릿수가 고정되어 있음
- VARCHAR는 가변길이 문자형으로, 글자수에 따라 자릿수가 변함
- VARCHAR가 CHAR보다 공간을 효율적으로 운영할 수 있지만, MySQL 내부적으로 성능(빠른 속도)면에서는 CHAR로 설정하는 것이 조금 더 좋음
- ex) 회원 테이블을 생성해라

  ```
  CREATE TABLE member
    (
      mem_id CHAR(8) NOT NULL PRIMARY KEY,
      phone1 CHAR(3),
      phone2 CHAR(8),
      ...
    );
  ```

- 데이터가 숫자 형태라도 연산이나 크기에 의미가 없다면 문자형으로 지정하는 것이 좋음

### 대량의 데이터 형식

| 데이터 형식 | 바이트 수    |
| ----------- | ------------ |
| `TEXT`      | 1~65535      |
| `LONGTEXT`  | 1~4294967295 |
| `BLOB`      | 1~65535      |
| `LONGBLOB`  | 1~4294967295 |

- BLOB(Binary Long Object)는 이미지, 동영상 등의 이진 데이터에서 주로 사용하는 데이터 형식임
- LONGTEXT 및 LONGBLOB으로 설정하면 각 데이터는 최대 4GB까지 입력 가능
- ex) movie 테이블을 생성해라

  ```
  CREATE TABLE movie
    (
      movie_id INT,
      movie_title VARCHAR(30),
      movie_direction VARCHAR(20),
      movie_star VARCHAR(20),
      movie_script LONGTEXT,
      movie_film LONGBLOB
    );
  ```

### 실수형

| 데이터 형식 | 바이트 수 | 설명                        |
| ----------- | --------- | --------------------------- |
| `FLOAT`     | 4         | 소수점 아래 7자리까지 표현  |
| `DOUBLE`    | 8         | 소수점 아래 15자리까지 표현 |

### 날짜형

| 데이터 형식 | 바이트 수 | 설명                             |
| ----------- | --------- | -------------------------------- |
| `DATE`      | 3         | 날짜 (YYYY-MM-DD 형식으로 사용)  |
| `TIME`      | 3         | 시간 (HH:MM:SS 형식으로 사용)    |
| `DATETIME`  | 8         | 날짜, 시간 (YYYY-MM-DD HH:MM:SS) |

## 2️⃣ 변수의 사용

```
SET @변수이름 = 변수의 값; 👈 변수의 선언 및 값 대입
SELECT @변수이름; 👈 변수의 값 출력
```

- ex) 변수끼리 연산해라

  ```
  SET @myVar1 = 5;
  SET @myVar2 = 4.25;

  SELECT @myVar1;
  SELECT @myVar1 + @myVar2;
  ```

- ex) 테이블 조회 시 변수를 활용해라

  ```
  SET @txt = '가수 이름 ==> ';
  SET @height = 166;

  SELECT @txt, mem_name FROM member WHERE height > @height;
  ```

- 주의) LIMIT에는 변수를 사용할 수 없음

  - 대신, PREPARE와 EXECUTE 문을 통해 해결 가능
  - PREPARE는 실행하지 않고 SQL 문만 준비해 놓고, EXECUTE 문에서 실행하는 방식임
  - PREPARE을 통해 SQL 문을 저장할 때, 물음표(?)를 사용해 나중에 값을 채워넣을 수 있음
  - PREPARE를 통해 저장한 SQL 문을 EXECUTE로 실행할 때, USING을 통해 물음표(?)에 변수의 값 대입 가능

- ex) member 테이블에서 키 큰 순으로 정렬한 후, 상위 3건만 조회해라

  ```
  SET @count = 3;
  PREPARE mySQL FROM 'SELECT mem_name, height FROM member ORDER BY height LIMIT ?';
  EXECUTE mySQL USING @count;
  ```

## 3️⃣ 데이터 형 변환

### 함수를 이용한 명시적인 변환

```
CAST (값 AS 데이터_형식 [(길이)])
CONVERT (값, 데이터_형식 [(길이)])
```

- CAST(), CONVERT() 함수는 형식만 다를 뿐 동일한 기능을 함
- CAST(), CONVERT() 함수 안에 올 수 있는 데이터 형식은 CHAR, SIGNED, UNSIGNED, DATE, TIME, DATETIME 등임
  - SIGNED: 부호가 있는 정수
  - UNSIGNED: 부호가 없는 정수
- ex) 구매 테이블에서 평균 가격을 정수형으로 나타내라

  ```
  SELECT CAST(AVG(price) AS SIGNED) '평균 가격' FROM buy;
  SELECT CONVERT(AVG(price), SIGNED) '평균 가격' FROM buy;
  ```

- ex) 구매 테이블에서 가격과 수량을 곱한 실제 구매액을 표시해라

  ```
  SELECT num, CONCAT(CAST(price AS CHAR), 'X', CAST(amount AS CHAR), '=') '가격X수량', price*amount '구매액'
    FROM buy;
  ```

### 암시적인 변환

- CAST(), CONVERT() 함수를 사용하지 않고도 자연스럽게 형이 변환될 수 있음

  ```
  SELECT '100' + '200'; 👉 300
  SELECT CONCAT('100', '200'); 👉 100200
  SELECT CONCAT(100, '200'); 👉 100200
  SELECT 100 + '200'; 👉 300
  ```
