# ✔ SQL 프로그래밍

- 스토어드 프로시저는 MySQL에서 프로그래밍 기능이 필요할 때 사용하는 데이터베이스 개체임
- 스토어드 프로시저의 구조

  - CALL을 통해 스토어드 프로시저 실행 가능

  ```
  DELIMITER $$
  CREATE PROCEDURE 스토어드_프로시저_이름()
  BEGIN
    이 부분에 SQL 프로그래밍 코딩
  END $$
  DELIMITER ;

  CALL 스토어드_프로시저_이름();
  ```

## 1️⃣ IF 문

### IF 문의 기본 형식

```
IF <조건식> THEN
  SQL 문장들
END IF;
```

#### 예시

```
DROP PROCEDURE IF EXISTS ifProc1;
DELIMITER $$
CREATE PROCEDURE ifProc1()
BEGIN
  IF 100 = 100 THEN
    SELECT '100은 100과 같습니다.';
  END IF;
END $$
DELIMITER ;

CALL ifProc1();
```

- 'SQL 문장들'이 한 문장이라면 그 문장만 써도 되지만, 두 문장 이상이 처리되어야 할 때는 BEGIN~END로 묶어주어야 함
- SELECT 뒤에 문자가 나오면 그냥 화면에 출력해 줌 (print와 유사한 기능)

### IF ~ ELSE 문

```
IF <조건식> THEN
  SQL 문장들
ELSE
  SQL 문장들
END IF;
```

#### 예시

```
DROP PROCEDURE IF EXISTS ifProc2;
DELIMITER $$
CREATE PROCEDURE ifProc2()
BEGIN
  DECLARE myNum INT;
  SET myNum = 200;
  IF myNum = 100 THEN
    SELECT '100입니다.';
  ELSE
    SELECT '100이 아닙니다.';
  END IF;
END $$
DELIMITER ;

CALL ifProc2();
```

- DECLARE 예약어를 사용해서 변수를 선언하고, SET 예약어로 값 할당 가능

### IF 문의 활용

- ex) 아이디가 APN인 회원의 데뷔 일자가 5년이 넘었는지 확인해보고, 5년이 넘었으면 축하 메시지를 출력하라

  ```
  DROP PROCEDURE IF EXISTS ifProc3;
  DELIMITER $$
  CREATE PROCEDURE ifProc3()
  BEGIN
    DECLARE debutDate DATE; -- 데뷔 일자
    DECLARE curDate DATE; -- 오늘
    DECLARE days DATE; -- 활동한 일수

    SELECT debut_date INTO debutDate
      FROM market_db.member
      WHERE mem_id = 'APN';

    SET curDate = CURRENT_DATE();
    SET days = DATEDIFF(curDate, debutDate);

    IF (days/365) >= 5 THEN
      SELECT CONCAT('데뷔한 지', days, '일이나 지났습니다. 축하합니다!');
    ELSE
      SELECT '데뷔한 지' + days + '일밖에 안되었네요.';
    END IF;
  END $$
  DELIMITER ;

  CALL ifProc3();
  ```

- 'INTO 변수'를 통해 변수에 결과 저장 가능

#### 날짜 관련 함수

- `CURRENT_DATE()`: 오늘 날짜
- `CURRENT_TIMESTAMP()`: 오늘 날짜 및 시간
- `DATEDIFF(날짜1, 날짜2)`: 날짜2부터 날짜1까지 일수로 몇일인지

## 2️⃣ CASE 문

- IF 문은 참/거짓 두 가지로 분기하지만(2중 분기), CASE 문은 2가지 이상의 조건으로 분기 가능(다중 분기)

### CASE 문의 기본 형식

```
CASE
  WHEN 조건1 THEN
    SQL 문장들1
  WHEN 조건2 THEN
    SQL 문장들2
  WHEN 조건3 THEN
    SQL 문장들3
  ELSE
    SQL 문장들4
END CASE;
```

- WHEN 다음에 조건이 나오는데, 조건이 여러 개라면 WHEN을 여러 번 반복함
- 모든 조건에 해당하지 않으면 마지막 ELSE 부분을 수행함

#### 예시

```
DROP PROCEDURE IF EXISTS caseProc;
DELIMITER $$
CREATE PROCEDURE caseProc()
BEGIN
  DECLARE point INT;
  DECLARE credit CHAR(1);
  SET point = 88;

  CASE
    WHEN point >= 90 THEN
      SET credit = 'A';
    WHEN point >= 80 THEN
      SET credit = 'B';
    WHEN point >= 70 THEN
      SET credit = 'C';
    WHEN point >= 60 THEN
      SET credit = 'D';
    ELSE
      SET credit = 'F';
  END CASE;
  SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;

CALL caseProc();
```

### CASE 문의 활용

- ex) 회원들의 총 구매액을 계산해서 회원의 등급을 4단계로 나누자

  ```
  SELECT M.mem_id, M.mem_name, SUM(price*amount) "총 구매액",
      CASE
        WHEN (SUM(price*amount) >= 1500) THEN '최우수고객'
        WHEN (SUM(price*amount) >= 1000) THEN '우수고객'
        WHEN (SUM(price*amount) >= 1) THEN '일반고객'
        ELSE '유령고객'
      END "회원등급"
    FROM buy B
      RIGHT OUTER JOIN member M
      ON B.mem_id = M.mem_id
    GROUP BY mem_id
    ORDER BY SUM(price*amount) DESC;
  ```

## 3️⃣ WHILE 문

### WHILE 문의 기본 형식

```
WHILE <조건식> DO
  SQL 문장들
END WHILE;
```

#### 예시

```
DROP PROCEDURE IF EXISTS whileProc;
DELIMITER $$
CREATE PROCEDURE whileProc()
BEGIN
  DECLARE i INT;
  DECLARE hap INT;
  SET i = 1;
  SET hap = 0;

  WHILE (i <= 100) DO
    SET hap = hap + i;
    SET i = i + 1;
  END WHILE;
  SELECT '1부터 100까지의 합 ==>', hap;
END $$
DELIMITER ;

CALL whileProc();
```

### WHILE 문의 응용

```
DROP PROCEDURE IF EXISTS whileProc2;
DELIMITER $$
CREATE PROCEDURE whileProc2()
BEGIN
  DECLARE i INT;
  DECLARE hap INT;
  SET i = 1;
  SET hap = 0;

  myWhile; -- WHILE 문을 myWhile이라는 레이블로 지정함
  WHILE (i <= 100) DO
    IF (i%4 = 0) THEN
      SET i = i + 1;
      ITERATE myWhile;
    END IF;
    SET hap = hap + i;
    IF (hap > 1000) THEN
      LEAVE myWhile;
    END IF;
    SET i = i + 1;
  END WHILE;

  SELECT '1부터 100까지의 합(4의 배수 제외, 1000 넘으면 종료)==>', hap;
END $$
DELIMITER ;

CALL whileProc2();
```

- `ITERATE [레이블]`: 지정한 레이블로 가서 계속 진행함
- `LEAVE [레이블]`: 지정한 레이블을 빠져나감 (즉, WHILE 문이 종료됨)

## 4️⃣ 동적 SQL

- SQL 문은 대부분 내용이 고정되어 있음
- 상황에 따라 내용 변경이 필요할 때 동적 SQL을 사용하면 변경되는 내용을 실시간으로 적용시켜 사용할 수 있음
- 미리 SQL을 준비한 후에 나중에 실행하는 것을 동적 SQL이라고 함

### PREPARE과 EXECUTE

```
PREPARE myQuery FROM 'SELECT * FROM member WHERE mem_id = "BLK"';
EXECUTE myQuery;
DEALLOCATE PREPARE myQuery;
```

- `PREPARE`: SQL 문을 실행하지는 않고 미리 준비만 함
- `EXECUTE`: 준비한 SQL 문을 실행함
- 실행 후에는 `DEALLOCATE PREPARE`로 문장을 해제해주는 것이 좋음

### 동적 SQL의 활용

```
DROP TABLE IF EXISTS gate_table;
CREATE TABLE gate_table (id INT AUTO_INCREMENT PRIMARY KEY, entry_time DATETIME);

SET @curDate = CURRENT_TIMESTAMP();

PREPARE myQuery FROM 'INSET INTO gate_table VALUES(NULL, ?)';
EXECUTE myQuery USING @curDate;
DEALLOCATE PREPARE myQuery;
```

- PREPARE 문에서는 `?`로 향후에 입력될 값을 비워 놓고, EXECUTE에서 `USING`으로 `?`에 값을 전달할 수 있음
- 이를 통해, 실시간으로 필요한 값들을 전달해서 동적으로 SQL 실행 가능함
- 스토어드 프로시저에서 DECLARE로 먼저 선언한 후 변수를 사용해야 하지만, 일반 SQL에서는 별도의 선언 없이 `@변수명`으로 변수 할당 가능함
