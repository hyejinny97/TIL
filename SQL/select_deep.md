# ✔ SELECT 심화

## 1️⃣ ORDER BY 절

- ORDER BY 절은 결과를 정렬해주는 기능을 함
  - ASC: 오름차순(Ascending) ⇐ 기본값
  - DESC: 내림차순(Descending)
- 결과의 값이나 개수에 대해서는 영향을 미치지 않지만, 결과가 출력되는 순서를 조절함
- 정렬 기준은 여러 개 열로 지정 가능
  - 첫 번째 지정 열로 정렬한 후, 동일한 경우에는 다음 지정 열로 정렬함
- ex) 회원 테이블에서 데뷔 일자가 빠른 순서대로 조회해라

  ```
  SELECT * FROM member ORDER BY debut_date;
  ```

- ex) 회원 테이블에서 평균 키가 164 이상인 그룹들을 키가 큰 순서대로 정렬해라

  ```
  SELECT *
    FROM member
    WHERE height >= 164
    ORDER BY height DESC;
  ```

- ex) 회원 테이블에서 평균 키가 164 이상인 그룹들을 키가 큰 순서대로 정렬하되, 평균 키가 같으면 데뷔 일자가 빠른 순서로 정렬해라

  ```
  SELECT *
    FROM member
    WHERE height >= 164
    ORDER BY height DESC, debut_date ASC;
  ```

### 출력의 개수를 제한: LIMIT

- LIMIT은 출력하는 개수를 제한함
  - 형식: `LIMIT 시작, 개수` == `LIMIT 개수 OFFSET 시작`
- ex) 회원 테이블에서 데뷔 일자가 빠른 그룹 3건만 조회해라

  ```
  SELECT *
    FROM member
    ORDER BY debut_date
    LIMIT 3;
  ```

- ex) 회원 테이블에서 평균 키가 큰 순으로 정렬하되, 3번째부터 2건만 조회해라

  ```
  SELECT *
    FROM member
    ORDER BY height DESC
    LIMIT 3, 2;
  ```

### 중복된 결과를 제거: DISTINCT

- DISTINCT는 조회된 결과에서 중복된 데이터를 1개만 남김
- ex) 회원 테이블에서 회원이 사는 지역을 중복없이 조회해라

  ```
  SELECT DISTINCT addr FROM member;
  ```

## 2️⃣ GROUP BY 절

- GROUP BY 절은 그룹을 묶어주는 역할을 함

### 집계 함수

| 함수명            | 설명                               |
| ----------------- | ---------------------------------- |
| `SUM()`           | 합계를 구함                        |
| `AVG()`           | 평균을 구함                        |
| `MIN()`           | 최솟값을 구함                      |
| `MAX()`           | 최댓값을 구함                      |
| `COUNT()`         | 행의 갯수를 셈                     |
| `COUNT(DISTINCT)` | 행의 갯수를 셈 (중복은 1개만 인정) |

- 집계 함수는 주로 GROUP BY 절과 함께 쓰이며 데이터를 그룹화해주는 기능을 함
- ex) 구매 테이블에서 각 회원 별로 구매한 물건 개수를 조회해라

  ```
  SELECT mem_id "회원 아이디", SUM(amount) "총 구매 개수"
    FROM buy GROUP BY mem_id;
  ```

- ex) 구매 테이블에서 각 회원 별로 구매한 금액의 총합을 조회해라

  ```
  SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
    FROM buy GROUP BY mem_id;
  ```

- ex) 구매 테이블에서 각 회원 별로 한번 구매 시 평균 몇 개를 구매했는지 조회해라

  ```
  SELECT mem_id, AVG(amount) "평균 구매 개수"
    FROM buy
    GROUP BY mem_id;
  ```

- ex) 회원 테이블에서 연락처가 있는 회원만 카운트해라

  - `COUNT(열_이름)`은 열 이름의 값이 NULL인 것을 제외한 행의 개수를 셈

  ```
  SELECT COUNT(phone1) "연락처가 있는 회원 수" FROM member;
  ```

### HAVING 절

- GROUP BY와 관련된 조건절
- HAVING 절은 집계 함수에 대해서 조건을 제한함
- ex) 구매 테이블에서 총 구매액이 1000 이상인 회원을 조회한 후, 총 구매액이 큰 사용자부터 나타내라

  ```
  SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
    FROM buy
    GROUP BY mem_id
    HAVING SUM(price*amount) > 1000
    ORDER BY SUM(price*amount) DESC;
  ```
