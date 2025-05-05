# ✔ 데이터 변경을 위한 SQL문

## 1️⃣ 데이터 입력: INSERT

- INSERT는 테이블에 데이터를 삽입하는 명령어

### INSERT 문의 기본 문법

```
INSERT INTO 테이블 [(열1, 열2, ...)] VALUES (값1, 값2, ...)
```

- 테이블 이름 다음에 나오는 열은 생략 가능함
- 열 이름을 생략할 경우, VALUES 다음에 나오는 값들의 순서 및 개수는 테이블을 정의할 때의 열 순서 및 개수와 동일해야 함
- ex) hongong1 테이블을 생성한 후, 데이터를 삽입해라

  ```
  USE marker_db;
  CREATE TABLE hongong1 (toy_id INT, toy_name CHAR(4), age INT);

  INSERT INTO hongong1 VALUES (1, '우디', 25);
  INSERT INTO hongong1 (toy_id, toy_name) VALUES (2, '버즈');
  INSERT INTO hongong1 (toy_name, age, toy_id) VALUES ('제시', 20, 3);
  ```

### 자동으로 증가하는 AUTO_INCREMENT

- AUTO_INCREMENT는 열을 정의할 때 1부터 증가하는 값을 입력해줌
- 따라서, INSERT에서는 해당 열이 없다고 생각하고 입력하면 됨
- 주의) AUTO_INCREMENT로 지정한 열은 꼭 PRIMARY KEY로 지정해줘야 함
- ex) hongong2 테이블을 생성한 후, 데이터를 삽입해라

  ```
  CREATE TABLE hongong2 (
    toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);

  INSERT INTO hongong2 VALUES (NULL, '보핍', 25);
  INSERT INTO hongong2 VALUES (NULL, '슬링키', 22);
  INSERT INTO hongong2 VALUES (NULL, '렉스', 21);
  ```

- ex) hongong2 테이블에서 다음으로 삽입되는 데이터의 toy_id는 100부터 시작하도록 변경해라

  ```
  ALTER TABLE hongong2 AUTO_INCREMENT=100;
  INSERT INTO hongong2 VALUES (NULL, '재남', 35);
  ```

- ex) toy_id의 시작값이 1000이고 하고 3씩 증가하는 hongong3 테이블을 생성한 후, 데이터를 삽입해라

  ```
  CREATE TABLE hongong3 (
    toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
  ALTER TABLE hongong3 AUTO_INCREMENT=1000;
  SET @@auto_increment_increment=3;

  INSERT INTO hongong3 VALUES (NULL, '토마스', 20), (NULL, '제임스', 23);
  ```

### 다른 테이블의 데이터를 한 번에 입력하는 INSERT INTO ~ SELECT

```
INSERT INTO 테이블_이름 (열_이름1, 열_이름2, ...)
  SELECT 문;
```

- 주의) SELECT 문의 열 개수는 INSERT할 테이블의 열 개수와 같아야 함

## 2️⃣ 데이터 수정: UPDATE

- UPDATE는 기존에 입력되어 있는 값을 수정하는 명령어

### UPDATE 문의 기본 문법

```
UPDATE 테이블_이름
  SET 열1=값1, 열2=값2, ...
  WHERE 조건;
```

- ex) city_popul 테이블의 도시 이름(city_name) 중에서 'Seoul'을 '서울'로 변경해라

  ```
  UPDATE city_popul
    SET city_name = '서울'
    WHERE city_name = 'Seoul';
  ```

### WHERE가 없는 UPDATE 문

- UPDATE 문에서 WHERE 절은 문법상 생략 가능하지만, WHERE 절을 생략하면 테이블의 모든 행의 값이 변경됨
- ex) city_popul 테이블에서 모든 데이터의 인구 열을 10,000으로 나눠라

  ```
  UPDATE city_popul
    SET population = population / 10000;
  ```

## 3️⃣ 데이터 삭제: DELETE

- DELETE는 기존 행 데이터를 삭제하는 명령어

### DELETE 문의 기본 문법

```
DELETE FROM 테이블_이름 WHERE 조건;
```

- 주의) WHERE 절이 생략되면 전체 행이 삭제됨
- ex) city_popul 테이블에서 'New'로 시작하는 도시 중 상위 5건만 삭제해라

  ```
  DELETE FROM city_popul
    WHERE city_name LIKE 'Nex%'
    LIMIT 5;
  ```

## 4️⃣ 대용량 테이블의 삭제

```
DELETE FROM 테이블_이름;
DROP TABLE 테이블_이름;
TRUNCATE TABLE 테이블_이름;
```

- DROP 문은 테이블 자체를 삭제함
  - 따라서, 빠르게 삭제됨
- DELETE 문과 TRUNCATE 문은 빈 테이블을 남김
  - TRUNCATE 문은 DELETE 문과 달리 WHERE 문을 사용할 수 없어, 조건 없이 전체 행을 삭제할 때만 사용 가능
  - TRUNCATE 문이 DELETE 문보다 속도가 훨씬 빠름
