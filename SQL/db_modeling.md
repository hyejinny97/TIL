# ✔ 데이터베이스 모델링

- 데이터베이스 모델링: 테이블의 구조를 설계하는 과정

## 1️⃣ 프로젝트 진행 단계

- 프로젝트: 현실 세계에서 일어나는 업무를 컴퓨터 시스템으로 옮겨놓는 과정 (대규모 소프트웨어를 작성하기 위한 전체 과정)
- 폭포수 모델: 소프트웨어 개발 절차 중 하나로, 폭포가 떨어지듯 개발 단계가 진행됨
- 폭포수 모델 (waterfall model)
  1. 프로젝트 계획
  2. 업무 분석
  3. 시스템 설계
  4. 프로그램 구현
  5. 테스트
  6. 유지보수
- 데이터베이스 모델링은 폭포수 모델에서 업무 분석과 시스템 설계 단계에 해당함

## 2️⃣ 전체 데이터베이스 구성도

- 데이터
  - 하나하나의 단편적인 정보
- 테이블
  - 표 형태
- 데이터베이스
  - 테이블이 저장되는 저장소
- DBMS
  - 데이터베이스 관리 시스템
- 열
  - 테이블의 세로
- 열 이름
  - 각 열을 구분하기 위한 이름
  - 열 이름은 각 테이블 내에서는 서로 달라야 함
- 데이터 형식
  - 열에 저장될 데이터의 형식
  - 데이터 형식은 테이블을 생성할 때 열 이름과 함께 지정해줌
- 행
  - 실질적인 진짜 데이터 (행 데이터)
  - 행의 개수 == 데이터의 개수
- 기본 키 (Primary Key, PK)
  - 각 행을 구분하는 유일한 열
  - 중복되지 않고, 비어있지 않아야 함
- SQL
  - 사람과 DBMS가 소통하기 위한 언어
