# ✔ 스토어드 함수와 커서

- 스토어드 함수는 MySQL에서 제공하는 내장 함수 외에 직접 함수를 만드는 기능을 제공함
  - 스토어드 프로시저와 유사하지만, 프로시저와 달리 `RETURNS` 예약어를 통해서 하나의 값을 반환해야 하는 특징을 가짐
- 커서는 스토어드 프로시저 안에서 한 행씩 처리할 때 사용하는 프로그래밍 방식임

## 1️⃣ 스토어드 함수

### 스토어드 함수의 개념

- MySQL은 다양한 내장 함수를 제공함
  - ex) `SUM()`, `CAST()`, `CONCAT()`, `CURRENT_DATE()` 등
- 스토어드 함수: 사용자가 직접 만들어서 사용하는 함수

### 스토어드 함수의 생성

```sql
DELIMITER $$
CREATE FUNCTION 스토어드_함수_이름(입력 매개변수)
  RETURNS 반환형식
BEGIN
  // SQL 프로그래밍 코드 작성
  RETURN 반환값;
END $$
DELIMITER;
```

- 스토어드 프로시저 안에서는 SELECT 문을 사용할 수 있지만, 스토어드 함수 안에서는 SELECT 문을 사용할 수 없음
- 스토어드 프로시저는 여러 SQL 문이나 숫자 계산 등의 다양한 용도로 사용하지만, 스토어드 함수는 어떤 계산을 통해서 하나의 값을 반환하는 데 주고 사용함

### 스토어드 함수의 호출

```sql
SELECT 스토어드_함수_이름();
```

### 스토어드 함수의 삭제

```sql
DROP FUNCTION 스토어드_함수_이름;
```

### 스토어드 함수의 사용

- 스토어드 함수를 사용하기 위해서는 먼저 다음 SQL로 스토어드 함수 생성 권한을 허용해줘야 함

  ```sql
  SET GLOBAL log_bin_trust_function_creators = 1;
  ```

- ex) 데뷔 연도를 입력하면, 활동 기간이 얼마나 되었는지를 출력해주는 스토어드 함수를 만들자

  ```sql
  DELIMITER $$
  CREATE FUNCTION calcYearFunc(dYear INT)
    RETURNS INT
  BEGIN
    DECLARE runYear INT; -- 활동기간(연도)
    SET runYear = YEAR(CURDATE()) - dYear;
    RETURN runYear;
  END $$
  DELIMITER;

  SELECT mem_id, mem_name, calcYearFunc(YEAR(debut_date)) AS '활동 횟수'
    FROM member;
  ```

## 2️⃣ 커서로 한 행씩 처리하기

- 커서(cursor)는 테이블에서 한 행씩 처리하기 위한 방식임

### 커서의 기본 개념

- 커서는 첫 번째 행을 처리한 후에 마지막 행까지 한 행씩 접근해서 값을 처리함
- 커서는 대부분 스토어드 프로시저와 함께 사용됨

### 커서의 작동 순서

1. 커서 선언하기
2. 반복 조건 선언하기
3. 커서 열기
4. 데이터 가져오기
5. 데이터 처리하기
6. 커서 닫기

- 위 4, 5번을 반복해서 진행함

#### 1. 커서 선언하기

```sql
DECLARE 커서_이름 CURSOR FOR
  SELECT 열_이름 FROM 테이블_이름;
```

- 커서는 결국 SELECT 문임

#### 2. 반복 조건 선언하기

```sql
DECLARE CONTINUE HANDLER
  FOR NOT FOUND SET 중지_조건;
```

#### 3. 커서 열기

```sql
OPEN 커서_이름;
```

#### 4. 데이터를 가져오기 & 데이터 처리하기 (행 반복)

```sql
cursor_loop: LOOP
  -- 여기에 반복해서 처리할 코드 작성
END LOOP cursor_loop
```

- cursor_loop은 반복할 부분의 이름을 지정한 것 뿐임
- `FETCH`를 통해 한 행씩 읽어올 수 있음
- `LEAVE cursor_loop`을 통해 반복문을 빠져나갈 수 있음

#### 5. 커서 닫기

```sql
CLOSE 커서_이름;
```

### 커서의 사용

- ex) 커서를 활용해, 그룹의 평균 인원수를 구하는 스토어드 프로시저를 만들자

  ```sql
  DELIMITER $$
  CREATE DELIMITER cursor_prc()
  BEGIN
    DECLARE memNumber INT; -- 그룹 인원 수
    DECLARE cnt INT DEFAULT 0; -- 그룹 수
    DECLARE totNumber INT DEFAULT 0; -- 전체 그룹 인원 수
    DECLARE endOfRow BOOLEAN DEFAULT FALSE; -- 마지막 줄인지 여부

    DECLARE memberCursor CURSOR FOR
      SELECT mem_number FROM member;

    DECLARE CONTINUE HANDLER
      FOR NOT FOUND SET endOfRow = TRUE;

    OPEN memberCursor;

    cursor_loop: LOOP
      FETCH memberCursor INTO memNumber;

      IF endOfRow THEN
        LEAVE cursor_loop;
      END IF;

      SET cnt = cnt + 1;
      SET totNumber = totNumber + memNumber;
    END LOOP cursor_loop;

    SELECT (totNumber/cnt) AS '회원의 평균 인원 수';

    CLOSE memberCursor;
  END $$
  DELIMITER;

  CALL cursor_proc();
  ```
