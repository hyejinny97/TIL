# ✔ 스토어드 프로시저 사용 방법

- MySQL의 스토어드 프로시저는 SQL에 프로그래밍 기능을 추가해서 일반 프로그래밍과 비슷한 효과를 낼 수 있음

## 1️⃣ 스토어드 프로시저 기본

### 스토어드 프로시저의 개념

- 자주 사용하는 일반적인 쿼리를 반복하는 것보다 스토어드 프로시저로 묶어 놓고, 필요할 때마다 간단히 호출만 하면 훨씬 편리하게 MySQL을 운영할 수 있음

### 스토어드 프로시저의 생성

```sql
DELIMITER $$
CREATE PROCEDURE 스토어드_프로시저_이름(IN 또는 OUT 매개변수)
BEGIN
  // SQL 프로그래밍 코드 작성
END $$
DELIMITER;
```

- `$$`는 스토어드 프로시저의 끝을 의미함
  - `$$` 대신 `$` 1개만 사용해도 되지만 명확하게 표시하기 위해 2개를 사용함
  - `##`, `%%`, `&&`, `//` 등으로 변경 가능
- 스토어드 프로시저를 만드는 시점에는 아직 존재하지 않는 테이블을 사용해도 됨
  - 단, CALL로 실행하는 시점에는 사용한 테이블이 있어야 함

### 스토어드 프로시저의 호출

```sql
CALL 스토어드_프로시저_이름();
```

### 스토어드 프로시저의 삭제

```sql
DROP PROCEDURE 스토어드_프로시저_이름;
```

## 2️⃣ 스토어드 프로시저 실습

### 매개변수의 사용

#### 입력 매개변수의 형식과 호출

```sql
IN 입력_매개변수_이름 데이터_형식
```

```sql
CALL 프로시저_이름(전달_값);
```

- 스토어드 프로시저에서는 실행 시 입력 매개변수를 지정할 수 있음

#### 출력 매개변수의 형식과 호출

```sql
OUT 출력_매개변수_이름 데이터_형식
```

```sql
CALL 프로시저_이름(@변수명);
SELECT @변수명;
```

- 스토어드 프로시저에서 처리된 결과를 출력 매개변수를 통해 얻을 수도 있음
- 출력 매개변수에 값을 대입하기 위해서는 주로 `SELECT ~ INTO`문을 사용함

### 입력 매개변수의 활용

- ex) 멤버 수가 userNumber 매개변수 값 이상이고 멤버 평균 키가 userHeight 매개변수 값 이상인 멤버를 조회하는 procedure를 만들자

  ```sql
  DELIMITER $$
  CREATE PROCEDURE user_proc(
    IN userNumber INT,
    IN userHeight INT)
  BEGIN
    SELECT * FROM member
      WHERE mem_number > userNumber AND height > userHeight;
  END $$
  DELIMITER;

  CALL user_proc(6, 165);
  ```

### 출력 매개변수의 활용

- ex) table에 txtValue 매개 변수를 삽입하고, table에서 id 열의 최댓값을 출력 매개변수에 대입해주는 procedure를 만들자

  ```sql
  DELIMITER $$
  CREATE PROCEDURE user_proc2(
    IN txtValue CHAR(10),
    OUT outValue INT)
  BEGIN
    INSERT INTO table VALUES(NULL, txtValue);
    SELECT MAX(id) INTO outValue FROM table;
  END $$
  DELIMITER;

  CALL user_proc2('텍스트', @myValue);
  SELECT CONCAT('입력된 ID 값 ==>', @myValue);
  ```

### SQL 프로그래밍의 활용

- ex) 가수 그룹의 데뷔 연도가 2015년 이전이면 '고참 가수', 이후이면 '신인 가수'를 출력하는 procedure를 만들자

  ```sql
  DELIMITER $$
  CREATE PROCEDURE ifelse_proc(
    IN memName VARCHAR(10)
  )
  BEGIN
    DECLARE debutYear INT;
    SELECT YEAR(debut_date) INTO debutYear FROM member
      WHERE mem_name = memName;
    IF (debutYear >= 2015) THEN
      SELECT '신인 가수네요.' AS '메시지';
    ELSE
      SELECT '고참 가수네요.' AS '메시지';
    END IF;
  END $$
  DELIMITER;

  CALL ifelse_proc('오마이걸');
  ```

- ex) 테이블의 이름을 입력 매개변수로 받아 조회하는 procedure를 만들자 (동적 SQL 활용)

  ```sql
  DELIMITER $$
  CREATE PROCEDURE dynamic_proc(
    IN tableName VARCHAR(20)
  )
  BEGIN
    SET @sqlQuery = CONCAT('SELECT * FROM ', tableName);
    PREPARE myQuery FROM @sqlQuery;
    EXECUTE myQuery;
    DEALLOCATE PREPARE myQuery;
  END $$
  DELIMITER;

  CALL dynamic_proc('member');
  ```

#### cf) 날짜와 관련된 MySQL 함수

- `YEAR(날짜)`, `MONTH(날짜)`, `DAY(날짜)` 함수를 통해 날짜에서 연, 월, 일을 알 수 있음
- `CURDATE()` 함수를 통해 현재 날짜를 알 수 있음

```sql
SELECT YEAR(CURDATE()), MONTH(CURDATE()), DAY(CURDATE());
```
