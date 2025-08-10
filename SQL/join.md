# ✔ 두 테이블을 묶는 조인

- 조인(join)은 두 개의 테이블을 서로 묶어서 하나의 결과를 만들어 내는 것을 의미

## 1️⃣ 내부 조인

### 일대다 관계의 이해

- 두 테이블의 조인을 위해서는 테이블이 일대다(one to many) 관계로 연결되어야 함
- 일대다 관계: 한쪽 테이블에는 하나의 값만 존재해야 하지만, 연결된 다른 테이블에는 여러 개의 값이 존재할 수 있는 관계
- 일대다 관계는 주로 기본 키(Primary Key, PK)와 외래 키(Foreign Key, FK) 관계로 맺어져 있음
  - 일대다 관계를 'PK-FK 관계'라고도 부름
- 내부 조인은 두 테이블에 모두 있는 내용만 조인되는 방식임

### 내부 조인의 기본

```
SELECT <열 목록>
  FROM <첫 번째 테이블>
    INNER JOIN <두 번째 테이블>
    ON <조인될 조건>
  [WHERE 검색 조건]
```

- INNER JOIN을 그냥 JOIN이라고만 써도 INNER JOIN으로 인식함
- 두 개의 테이블을 조인하는 경우, 동일한 열 이름이 존재한다면 꼭 테이블\_이름.열\_이름 형식으로 표기해야 함
- ex) 구매 테이블에서 GRL이라는 아이디를 가진 회원의 정보를 조회해라

  ```
  SELECT *
    FROM buy
      INNER JOIN member
      on buy.mem_id = member.mem_id
    WHERE buy.mem_id = 'GRL';
  ```

### 내부 조인의 간결한 표현

- ex) 구매한 기록이 있는 회원들의 아이디/이름/구매 물품/주소/연락처를 조회해라

  ```
  SELECT buy.mem_id, mem_name, prod_name, add, CONCAT(phone1, phone2) '연락처'
    FROM buy
      INNER JOIN member
      on buy.mem_id = member.mem_id
  ```

- FROM 절에 나오는 테이블의 이름 뒤에 별칭(alias)을 줄 수 있음

  ```
  SELECT B.mem_id, M.mem_name, B.prod_name, M.add, CONCAT(M.phone1, M.phone2) '연락처'
    FROM buy B
      INNER JOIN member M
      on buy.mem_id = member.mem_id
  ```

## 2️⃣ 외부 조인

- 외부 조인은 두 테이블을 조인할 때 필요한 내용이 한쪽 테이블에만 있어도 결과를 추출할 수 있음

### 외부 조인의 기본

```
SELECT <열 목록>
  FROM <첫 번째 테이블(LEFT 테이블)>
    <LEFT | RIGHT | FULL> OUTER JOIN <두 번째 테이블(RIGHT 테이블)>
    ON <조인될 조건>
  [WHERE 검색 조건]
```

- LEFT OUTER JOIN (= LEFT JOIN): 왼쪽 테이블의 내용은 모두 출력함
- RIGHT OUTER JOIN (= RIGHT JOIN): 오른쪽 테이블의 내용은 모두 출력함
- FULL OUTER JOIN: 왼쪽이든 오른쪽이든 한쪽에 들어 있는 내용이면 출력함

### 외부 조인의 활용

- ex) 회원으로 가입만 하고, 한 번도 구매한 적이 없는 회원의 목록을 추출하라

  ```
  SELECT DISTINCT M.mem_id, B.prod_name, M.mem_name, M.addr
    FROM member M
      LEFT OUTER JOIN buy B
      ON M.mem_id = B.mem_id
    WHERE B.prod_nem IS NULL
    ORDER BY M.mem_id;
  ```

## 3️⃣ 기타 조인

### 상호 조인

- 상호 조인은 한쪽 테이블의 모든 행과 다른 쪽 테이블의 모든 행을 조인시키는 것을 의미함

- 따라서, 상호 조인 결과의 전체 행 개수는 두 테이블의 각 행의 개수를 곱한 개수가 됨
- 특징
  1. ON 구문을 사용할 수 없음
  2. 랜덤으로 조인하기 때문에 결과의 내용은 의미가 없음
  3. 상호 조인의 주 용도는 테스트하기 위해 대용량의 데이터를 생성할 때임

#### 상호 조인의 기본

```
SELECT <열 목록>
  FROM <첫 번째 테이블>
    CROSS JOIN <두 번째 테이블>;
```

### 자체 조인

- 자체 조인은 자신이 자신과 조인하는 것을 의미함
- 따라서, 자체 조인은 1개의 테이블을 사용함

#### 자체 조인의 기본

```
SELECT <열 목록>
  FROM <테이블> 별칭A
    INNER JOIN <테이블> 별칭B
    ON <조인될 조건>
  [WHERE 검색 조건]
```

- 테이블이 1개지만 다른 별칭을 사용해서 서로 다른 것처럼 사용하면 됨

#### 자체 조인의 활용

- ex) 경리부장 직속 상관의 연락처를 구해라

  ```
  SELECT A.emp "직원", B.emp "직속상관", B.phone "직속상관연락처"
    FROM emp_table A
      INNER JOIN emp_table B
      ON A.manager = B.emp
    WHERE A.emp = '경리부장';
  ```
