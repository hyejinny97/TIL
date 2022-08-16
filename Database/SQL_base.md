# ✔ SQL (Structured Query Language)
- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

> SQL 분류
1. DDL (Data Definition Language)
   - 데이터 정의 언어
   - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
   - CREATE, DROP, ALTER
2. DML (Data Manipulation Language)
   - 데이터 조작 언어
   - 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
   -  INSERT, SELECT, UPDATE, DELETE
3. DCL (Data Control Language)
   - 데이터 제어 언어
   - 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
   - GRANT, REVOKE, COMMIT, ROLLBACK



# ✔ 테이블 생성 및 삭제

> 테이블 생성 명령문
- 데이터베이스에서 테이블 생성
  
   ```sql
   CREATE TABLE {테이블명} (
      열이름1 데이터타입,
      열이름2 데이터타입
   );
  ```

> 테이블 삭제 명령문
- 데이터베이스에서 테이블 제거

  ```sql
  DROP TABLE {테이블명}
  ```

> 필드 제약 조건
- `NOT NULL`: NULL값 입력 금지
- `UNIQUE`: 중복값 입력 금지 (NULL 값은 중복 입력 가능)
- `PRIMARY KEY`: 기본키
  - 테이블에서 반드시 하나만 존재
  - NOT NULL이면서 UNIQUE한 열
- `FOREIGN KEY`: 외래키
  - 다른 테이블의 Key
- `CHECK`: 조건으로 설정된 값만 입력 허용
- `DEFAULT`: 기본 설정값
  
  ```sql
  CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER DEFAULT 1 CHECK (0 < age)
  );
  ```



# ✔ Create Read Update Delete
- `C` ⇒ INSERT: 새로운 데이터 삽입(추가)
- `R` ⇒ SELECT: 저장되어있는 데이터 조회
- `U` ⇒ UPDATE: 저자되어있는 데이터 갱신
- `D` ⇒ DELETE: 저장되어있는 데이터 삭제

> INSERT
- 테이블에 단일 행 삽입
- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력
  
  ```sql
  -- 열이름 명시해서 값을 넣는 방법
  INSERT INTO {테이블명} (열1, 열2) VALUES (값1, 값2);

  -- 열 갯수와 동일하게 값을 넣을 경우, 열 이름 생략 가능
  INSERT INTO {테이블명} VALUES (값1, 값2, 값3);
  
  -- 여러 데이터를 한꺼번에 넣는 방법
  INSERT INTO {테이블명} VALUES 
      (값1, 값2, 값3),
      (값4, 값5, 값7),
      (값8, 값9, 값0);
  ```
- `rowid`: SQLite에서 PRIMARY KEY가 없는 경우, 자동으로 증가하는 PK 열

> SELECT
- 테이블에서 테이터를 조회
- SELECT문은 SQLite에서 가장 기본이 되는 문이며 다양한 절과 함계 사용
  - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY 등
  
  ```sql
  SELECT {열이름1, 열이름2} FROM {테이블명};
  ```


# ✔ SELECT문의 다양한 절

> SELECT ~ LIMIT
- 쿼리에서 반환되는 행 수를 제한
- 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용하기도 함
  - OFFSET: 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형
  - SELECT * FROM my_table LIMIT 10 OFFSET 5;
  - 위 SQL문은 '6번째 행부터 10개 행을 조회'를 의미
  
  ```sql
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
  ```

> SELECT ~ WHERE
- 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
   
   ```sql
   SELECT * from classmates WHERE address='서울';
   ```

> SELECT DISTINCT ~
- 조회 결과에서 중복 행을 제거
- DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함
    
  ```sql
  SELECT * from classmates WHERE address='서울';
  SELECT DISTINCT age FROM classmates;
  ```