# ✔ 제약조건으로 테이블을 견고하게

- 테이블을 만들 떄는 테이블의 구조에 필요한 제약조건을 설정해줘야 함
  - ex) 기본 키(PRIMARY KEY), 외래 키(FOREIGN KEY), 고유 키(UNIQUE)

## 1️⃣ 제약조건의 기본 개념과 종류

- 제약조건: 데이터의 무결성을 지키기 위해 제한하는 조건
  - 데이터의 무결성: 결함이 없는 것
- MySQL에서 제공하는 대표적인 제약조건
  - PRIMARY KEY 제약조건
  - FOREIGN KEY 제약조건
  - UNIQUE 제약조건
  - CHECK 제약조건
  - DEFAULT 정의
  - NULL 값 허용

## 2️⃣ 기본 키 제약조건

- 기본 키에 입력되는 값은 중복될 수 없으며, NULL 값이 입력될 수 없음
  - 주민등록번호, Email, 휴대폰 번호 등으로 기본 키 지정 가능
- 대부분의 테이블은 기본 키를 가져야 함
- 테이블은 기본 키를 1개만 가질 수 있음
- 기본 키로 생성한 것은 자동으로 클러스터형 인덱스가 생성됨

### CREATE TABLE에서 설정하는 기본 키 제약조건

#### 방법1

```
USE naver_db;
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id      CHAR(8) NOT NULL PRIMARY KEY,
  mem_name    VARCHAR(10) NOT NULL,
  height      TINYINT UNSIGNED NULL,
);
```

- CREATE TABLE 문에서 특정 열 이름 뒤에 PRIMARY KEY를 붙여주면 기본 키로 설정됨

#### 방법2

```
USE naver_db;
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id      CHAR(8) NOT NULL,
  mem_name    VARCHAR(10) NOT NULL,
  height      TINYINT UNSIGNED NULL,
  PRIMARY KEY (mem_id)
);
```

- 테이블의 제일 마지막에 `PRIMARY KEY(열_이름)`을 붙여주면 그 열이 기본 키로 설정됨

#### cf) 테이블을 삭제하는 순서

- 회원 테이블과 구매 테이블은 기본 키-외래 키로 연결되어 있음
- 기본 키-연결 키 관계로 연결된 테이블은 외래 키가 설정된 테이블을 먼저 삭제해야 함

### ALTER TABLE에서 설정하는 기본 키 제약조건

```
USE naver_db;
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id      CHAR(8) NOT NULL,
  mem_name    VARCHAR(10) NOT NULL,
  height      TINYINT UNSIGNED NULL,
);

ALTER TABLE member
  ADD CONSTRAINT
  PRIMARY KEY (mem_id);
```

- ALTER TABLE 구문을 사용해 이미 만들어진 테이블을 수정할 수 있음

## 3️⃣ 외래 키 제약조건

- 외래 키는 두 테이블 사이의 관계를 연결해 줌
- 외래 키가 설정된 열은 꼭 다른 테이블의 기본 키와 연결됨
  - 기준 테이블: 기본 키가 있는 테이블
  - 참조 테이블: 외래 키가 있는 테이블
- 참조 테이블이 참조하는 기준 테이블의 열은 반드시 기본 키(primary key)나 고유키(unique)로 설정되어 있어야 함

### CREATE TABLE에서 설정하는 외래 키 제약조건

```
DROP TABLE IF EXISTS buy, member;
CREATE TABLE member
( mem_id     CHAR(8) NOT NULL PRIMARY KEY,
  mem_name   VARCHAR(10) NOT NULL,
  height     TYNYINT UNSIGNED NULL
);
CREATE TABLE buy
( num        INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  mem_id     CHAR(8) NOT NULL,
  prod_name  CHAR(6) NOT NULL,
  FOREIGN KEY(mem_id) REFERENCES member(mem_id)
);
```

- CREATE TABLE 끝에 FOREIGN KEY 키워드를 설정해 외래 키 생성 가능
- `FOREIGN KEY(열_이름) REFERENCES 기준_테이블(열_이름)`
- 만약, 기준 테이블의 열이 기준 키나 고유키가 아니라면 외래 키 관계는 성립되지 않음

### ALTER TABLE에서 설정하는 외래 키 제약조건

```
DROP TABLE IF EXISTS buy;
CREATE TABLE buy
( num        INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  mem_id     CHAR(8) NOT NULL,
  prod_name  CHAR(6) NOT NULL,
);

ALTER TABLE buy
  ADD CONSTRAINT
  FOREIGN KEY(mem_id) REFERENCES member(mem_id);
```

### 기준 테이블의 열이 변경될 경우

- 기존 키-외래 키로 맺어진 후에는 기준 테이블의 열 이름이 변경되거나 삭제되지 않음
  - 이유: 열 이름이 변경되면 참조 테이블에 문제가 발생하기 때문
- `ON UPDATE CASCADE` 문/`ON DELETE CASCADE` 문을 사용해 기존 테이블의 데이터가 변경/삭제되면 참조 테이블의 데이터도 변경/삭제할 수 있음

  ```
  DROP TABLE IF EXISTS buy;
  CREATE TABLE buy
  ( num        INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    mem_id     CHAR(8) NOT NULL,
    prod_name  CHAR(6) NOT NULL,
  );

  ALTER TABLE buy
    ADD CONSTRAINT
    FOREIGN KEY(mem_id) REFERENCES member(mem_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE;
  ```

## 4️⃣ 기타 제약조건

### 고유 키 제약조건

- '중복되지 않는 유일한 값'을 입력해야 하는 조건
- 기본 키 제약조건과의 차이점
  - NULL 값을 허용함
  - 테이블에 여러 개의 고유 키를 설정해도 됨

#### CREATE TABLE에서 설정하는 고유 키 제약조건

```
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id     CHAR(8) NOT NULL PRIMARY KEY,
  mem_name   VARCHAR(10) NOT NULL,
  height     TYNYINT UNSIGNED NULL,
  email      CHAR(30) NULL UNIQUE
);
```

### 체크 제약조건

- 입력되는 데이터를 점검하는 조건

#### CREATE TABLE에서 설정하는 체크 제약조건

```
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id     CHAR(8) NOT NULL PRIMARY KEY,
  mem_name   VARCHAR(10) NOT NULL,
  height     TYNYINT UNSIGNED NULL CHECK (height >= 100),
  phone1     CHAR(3) NULL
);
```

- 열의 정의 뒤에 `CHECK(조건)`을 추가하면 됨

#### ALTER TABLE에서 설정하는 체크 제약조건

```
ALTER TABLE member
  ADD CONSTRAINT
  CHECK (phone1 IN ('02', '031', '032', '054', '055', '061'));
```

### 기본값 정의

- 값을 입력하지 않았을 때 자동으로 입력될 값을 미리 지정해 놓는 방법

#### CREATE TABLE에서 설정하는 기본값

```
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id     CHAR(8) NOT NULL PRIMARY KEY,
  mem_name   VARCHAR(10) NOT NULL,
  height     TYNYINT UNSIGNED NULL DEFAULT 160,
  phone1     CHAR(3) NULL
);
```

#### ALTER TABLE에서 설정하는 기본값

```
ALTER TABLE member
  ALTER COLUMN phone1 SET DEFAULT '02';
```

- 기본값이 설정된 열에 기본값을 입력하려면 `default`라고 써주면 됨

  ```
  INSERT INTO member VALUES('SPC', '우주소녀', default, default);
  ```

### 널 값 허용

- `NULL`: 빈 값을 허용
- `NOT NULL`: 빈 값을 허용하지 않음
