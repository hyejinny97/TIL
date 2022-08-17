# ✔ 관계형 데이터베이스 (RDB, Relational Database)

- 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
- 키(key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스

> 스키마 (schema)

- 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것
  
  | column명 | datatype |
  | ------- | -------- |
  | id      | INT      |
  | name    | TEXT     |
  | address | TEXT     |
  | age     | INT      |

> 테이블 (table)

- 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
  
  | id  | name | address | age |
  | --- | ---- | ------- | --- |
  | 1   | 홍길동  | 제주      | 20  |
  | 2   | 김길동  | 서울      | 30  |
1. 열 (column)
   - 각 열에 고유한 데이터 형식 지정
   - 열 = 필드
2. 행 (row)
   - 실제 데이터가 저장되는 형태
   - 행 = 레코드 = 값
3. 기본 키 (Primary Key)
   - 각 행의 고유 값
   - 반드시 설정해야하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨



# ✔ 관계형 데이터베이스 관리 시스템 (RDB Management System, RDBMS)

- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
- 종류: MySQL, SQLite, PostegreSQL, ORACLE, SQL Server

> SQLite

- 서버 형태가 아닌 **파일 형식**으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능

> SQLite Data Type

1. NULL
2. INTEGER
   - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수
3. REAL
   - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB
   - 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

> SQLite 관련 명령어

- `.`은 sqlite에서 활용되는 명령어

1. DB 생성 및 접속
   
   ```bash
   $ sqlite3 {파일명.sqlite3}
   ```

2. DB 접속 중지
   
   ```
   sqlite> .quit
   ```

3. 데이터베이스 생성 및 열기
   
   ```
   sqlite> .open {데이터베이스명}
   ```

4. 저장된 데이터베이스명 확인
   
   ```
   sqlite> .databases
   ```

5. 저장된 테이블명 확인
   
   ```
   sqlite> .tables
   ```

6. 특정 테이블 구조 확인
   
   ```
   sqlite> .schema {테이블명}
   ```

7. csv 파일을 table로 만들기
   
   ```
   sqlite> .mode csv
   sqlite> .import {파일명.csv 테이블명}
   ```

8. 터미널 view 변경하기
   
   ```
   sqlite> .headers on
   sqlite> .mode column
   ```

   ```
   ex) 적용 결과

   BMI  weight  height
   ---  ------  ------
   22   60      165
   28   65      150
   22   55      155
   27   70      160
   20   50      155  
   ```

> vs code에서의 SQLite 확장 프로그램
1. vs code에서 SQLite 확장 프로그램 설치
2. sqlite 파일 우클릭 후, Open Database 클릭
3. SQLite 확장 창 내 sqlite 파일 우클릭 후, New Query 클릭하면 화면에 sql 명령어를 작성하는 페이지가 출력됨
4. 코드 작성 후 우클릭
   - Run Query: 전체 코드 실행
   - Run Selected Query: 선택 코드만 실행