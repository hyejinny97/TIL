# ✔ 테이블 만들기

- 테이블: 2차원 구조의 표 형태
  - 행 = row = record
  - 열 = column = field

## 1️⃣ 데이터베이스와 테이블 설계하기

- 테이블 설계는 테이블 이름, 열 이름, 데이터 형식, 기본 키 등을 설정하는 것을 의미함

## 2️⃣ SQL로 테이블 만들기

### 데이터베이스 생성하기

```
DROP DATABASE IF EXIST naver_db;
CREATE DATABASE naver_db;
```

### 테이블 생성하기

```
USE naver_db;
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id      CHAR(8) NOT NULL PRIMARY KEY,
  mem_name    VARCHAR(10) NOT NULL,
  mem_number  TINYINT NOT NULL,
  addr        CHAR(2) NOT NULL,
  phone1      CHAR(3) NULL,
  phone2      CHAR(8) NULL,
  height      TINYINT UNSIGNED NULL,
  debut_date  DATE NULL
);
```

- NULL: 빈 값을 허용함 (default)
- NOT NULL: 빈 값을 허용하지 않음 (반드시 값을 넣어야 함)
- PRIMARY KEY(기본키)로 지정된 열에는 NOT NULL을 생략해도 당연히 NOT NULL로 취급됨

```
USE naver_db;
DROP TABLE IF EXISTS buy;
CREATE TABLE buy
( num         INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  mem_id      CHAR(8) NOT NULL,
  prod_name   CHAR(6) NOT NULL,
  group_name  CHAR(4) NULL,
  price       INT UNSIGNED NOT NULL,
  amount      SMALLINT UNSIGNED NOT NULL,
  FOREIGN KEY(mem_id) REFERENCE member(mem_id)
);
```

- 주의) AUTO_INCREMENT로 지정한 열은 반드시 PRIMARY KEY나 UNIQUE로 지정해야 함
- 외래 키는 테이블을 만들 때 제일 마지막에 FOREIGN KEY 예약어로 지정함
