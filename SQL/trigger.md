# ✔ 자동 실행되는 트리거

- 트리거(trigger)는 INSERT, UPDATE, DELETE 문이 작동할 때 자동으로 실행되는 프로그래밍 기능임
- 트리거는 자동으로 수행하여 사용자가 추가 작업을 잊어버리는 실수를 방지해 줌
- 즉, 트리거를 사용하면 데이터에 오류가 발생하는 것을 막을 수 있음 (데이터의 무결성)

## 1️⃣ 트리거 기본

### 트리거의 개요

- 트리거란 테이블에 INSERT나 UPDATE 또는 DELETE 작업이 발생하면 실행되는 코드임

### 트리거의 기본 작동

- 트리거는 테이블에서 DML(Data Manipulation Language) 문(INSERT, UPDATE, DELETE 등)의 이벤트가 발생할 때 작동함
- 테이블에 미리 부착되는 프로그램 코드라고 생각하면 됨
- 하나의 테이블에 여러 개의 트리거를 부착해도 됨
- 스토어드 프로시저와 문법이 비슷하지만, CALL 문으로 직접 실행시킬 수는 없고 오직 테이블에 INSERT, UPDATE, DELETE 등의 이벤트가 발생할 경우에만 자동으로 실행됨
- 또한, 스토어드 프로시저와 달리 트리거에는 IN, OUT 매개변수를 사용할 수 없음
- 주의) DELETE 트리거는 오직 DELETE 문에만 작동함.
  - `TRUNCATE TABLE 테이블_이름`는 `DELETE FROM 테이블_이름`과 동일한 효과(모든 행의 데이터를 삭제함)를 내지만, TRUNCATE 문이 실행되어도 DELETE 트리거는 작동하지 않음

### 트리거의 생성

```sql
DELIMITER $$
CREATE TRIGGER 트리거_이름
  AFTER DML문
  ON 테이블_이름
  FOR EACH ROW
BEGIN
  -- 트리거 실행 시 작동되는 코드
END $$
DELIMITER;
```

- `AFTER DML문`: 특정 DML문이 발생된 이후에 작동됨
- `FOR EACH ROW`: 각 행마다 적용시킨다는 의미

## 2️⃣ 트리거 활용

- 트리거는 테이블에 입력/수정/삭제되는 정보를 백업하는 용도로 활용할 수 있음
- ex) singer 테이블에 수정/삭제 이벤트가 발생할 때, backup_singer 테이블로 해당 데이터를 백업하는 트리거를 만들자

  ```sql
  DELIMITER $$
  CREATE TRIGGER singer_updateTrg
    AFTER UPDATE
    ON singer
    FOR EACH ROW
  BEGIN
    INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr, '수정', CURATE(), CURRENT_USER());
  END $$
  DELIMITER;
  ```

  ```sql
  DELIMITER $$
  CREATE TRIGGER singer_deleteTrg
    AFTER DELETE
    ON singer
    FOR EACH ROW
  BEGIN
    INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr, '삭제', CURATE(), CURRENT_USER());
  END $$
  DELIMITER;
  ```

  - `OLD` 테이블은 UPDATE/DELETE가 수행될 때, 변경되기 전에 데이터가 잠깐 저장되는 임시 테이블임
  - `CURRENT_USER()` 함수는 현재 작업 중인 사용자를 반환해 줌

## cf) 트리거가 사용하는 임시 테이블

- 테이블에서 INSERT, UPDATE, DELETE 작업이 수행되면 `NEW`, `OLD` 두 개의 시스템 테이블이 임시로 생성됨
- MySQL이 이 테이블들을 생성하고 관리함
- INSERT가 수행 되면

  - 새 값은 테이블에 들어가기 전에 NEW 테이블에 잠깐 들어가 있음

  ```
  INSERT(새 값) → NEW 테이블 → 기존 테이블
  ```

- DELETE가 수행 되면

  - 삭제될 예전 값이 삭제되기 전에 OLD 테이블에 잠깐 들어가 있음

  ```
  DELETE(예전 값) → 기존 테이블 → OLD 테이블
  ```

- UPDATE가 수행 되면

  - 새 값은 NEW 테이블에 잠깐 저장되고, 예전 값은 OLD 테이블에 잠깐 저장됨

  ```
  UPDATE(새 값, 예전 값) → NEW 테이블 → 기존 테이블 → OLD 테이블
  ```
