# ✔ 가상의 테이블: 뷰

- 뷰를 사용하면 사용자에게 테이블의 필요한 내용만 보이도록 할 수 있음
- 사용자들의 입장에서 뷰는 테이블과 거의 동일한 개체로 취급됨
- 뷰는 테이블처럼 데이터를 가지고 있지는 않음
- 뷰의 실체는 SELECT 문으로 만들어져 있기 때문에 뷰에 접근하는 순간 SELECT가 실행되고 그 결과가 화면에 출력되는 방식임
- 바탕 화면의 '바로 가기 아이콘'과 비슷함
- 단순 뷰: 하나의 테이블과 연관된 뷰
- 복합 뷰: 2개 이상의 테이블과 연관된 뷰

## 1️⃣ 뷰의 개념

### 뷰의 기본 생성

#### 뷰 생성

```
CREATE VIEW 뷰_이름
AS
  SELECT 문;
```

- 일반적으로 뷰 이름 앞에는 'v\_'를 붙임

#### 뷰 접근

```
SELECT 열_이름 FROM 뷰_이름
  [WHERE 조건];
```

#### 예시

- ex) 회원 테이블의 아이디, 이름, 주소에 접근하는 뷰를 생성하자

  ```
  CREATE VIEW v_member
  AS
    SELECT mem_id, mem_name, addr FROM member;
  ```

  ```
  SELECT mem_name, addr FROM v_member
    WHERE addr IN ('서울', '경기');
  ```

### 뷰의 작동

- 뷰는 기본적으로 '읽기 전용'으로 사용되지만, (몇 가지 조건을 만족할 시) 뷰를 통해서 원본 테이블의 데이터를 수정할 수도 있음

#### 뷰를 사용하는 이유

##### 1. 보안(security)에 도움이 됨

- 뷰에만 접근할 수 있도록 함으로써, 테이블에 접근하지 못하도록 권한을 제한할 수 있음

##### 2. 복잡한 SQL을 단순하게 만들 수 있음

- 복잡한 쿼리를 뷰로 생성해 놓으면, 복잡한 SQL을 사용할 때마다 계속 입력할 필요없음

## 2️⃣ 뷰의 실제 작동

### 뷰의 실제 생성, 수정, 삭제

- 기본적인 뷰를 생성하면서 뷰에서 사용될 열 이름을 테이블과 다르게 지정할 수도 있음
  - 열 이름 뒤에 작은따옴표 또는 큰따옴표로 별칭 지정
  - 중간에 띄어쓰기 사용 가능
  - `AS`를 붙여 명시적으로 별칭 지정 가능
- 단, 뷰를 조회할 때는 열 이름에 공백이 있으면 백틱으로 묶어줘야 함

#### 뷰 생성

```
CREATE VIEW v_viewtest1
AS
  SELECT B.mem_id 'Member ID', M.mem_name AS 'Member Name', B.prod_name "Product Name", CONCAT(M.phone1, M.phone2) AS "Office Phone"
  FROM buy B
    INNER JOIN member M
    ON B.mem_id = M.mem_id;
```

```
SELECT DISTINCT `Member ID`, `Member Name` FROM v_viewtest1;
```

#### 뷰 수정

```
ALTER VIEW v_viewtest1
AS
  SELECT B.mem_id '회원 아이디', M.mem_name AS '회원 이름', B.prod_name "제품 이름", CONCAT(M.phone1, M.phone2) AS "연락처"
  FROM buy B
    INNER JOIN member M
    ON B.mem_id = M.mem_id;
```

```
SELECT DISTINCT `회원 아이디`, `회원 이름` FROM v_viewtest1;
```

#### 뷰 삭제

```
DROP VIEW v_viewtest1;
```

### 뷰의 정보 확인

```
DESCRIBE v_viewtest1;
```

- 주의) PRIMARY KEY 등의 정보는 확인되진 않음

### 뷰를 통한 데이터의 수정/삭제

- 뷰를 통해서 테이블의 데이터를 수정/삭제할 수도 있음
- ex) v_member 뷰를 수정해보자

  ```
  UPDATE v_member SET addr = '부산' WHERE mem_id='BLK';
  ```

- ex) v_member 뷰에 데이터를 삽입해보자

  ```
  INSERT v_member(mem_id, mem_name, addr) VALUES('BTS', '방탄소년단', '경기');
  ```

  - NOT NULL인 mem_number 열을 입력해주지 않아서 에러가 발생함
  - 뷰를 통해서 데이터를 입력하려면, 뷰에서 보이지 않는 테이블의 열의 속성을 NULL로 바꾸거나 기본값(Default)을 지정해야 함

- ex) 평균 키가 167 이상인 뷰를 생성한 후, 150 미만인 데이터를 삭제하자

  ```
  CREATE VIEW v_height167
  AS
    SELECT * FROM member WHERE height >= 167;
  ```

  ```
  DELETE FROM v_height167 WHERE height < 150;
  ```

### 뷰를 통한 데이터의 입력

- `WITH CHECK OPTION` 키워드를 통해 뷰에 설정된 값의 범위가 벗어나는 값은 입력되지 않도록 할 수 있음
- ex) v_height167 뷰에 키가 167 미만인 데이터를 입력해보자

  ```
  ALTER VIEW v_height167
  AS
    SELECT * FROM member WHERE height >= 167
      WITH CHECK OPTION;
  ```

  ```
  INSERT INTO v_height167 VALUES('TOB', '텔레토비', 4, '영국', NULL, NULL, 140, '1995-01-01');
  ```

  - 키가 167 미만인 데이터를 입력하니 에러가 발생함

### cf) 단순 뷰와 복합 뷰

- 단순 뷰: 하나의 테이블로 만든 뷰
- 복합 뷰: 두 개 이상의 테이블로 만든 뷰
- 복합 뷰는 읽기 전용으로, 테이블에 데이터를 입력/수정/삭제할 수 없음

```
CREATE VIEW v_complex
AS
  SELECT B.mem_id, M.mem_name, B.prod_name, M.addr
  FROM buy B
    INNER JOIN member M
    ON B.mem_id = M.mem_id;
```

### 뷰가 참조하는 테이블의 삭제

- 테이블은 뷰가 참조하고 있어도 삭제됨
- 테이블을 삭제하면 관련 뷰를 조회할 수 없음
- `CHECK TABLE` 문으로 뷰의 상태를 확인할 수 있음

  ```
  CHECK TABLE v_height167;
  ```
