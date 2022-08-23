# ✔ DB modeling
- 데이터베이스의 구조나 형식으로 모델 구조만 보고 어떤 데이터를 다루는지 알 수 있음

> 데이터 모델링 종류

1. 개념적 데이터 모델링
   - 데이터의 요구사항을 찾고 분석하는 과정
   - 핵심 개체(Entity) 사이의 관계를 찾아내고 표현

2. 논리적 데이터 모델링
   - 데이터베이스 설계 프로세스의 과정
   - 정보의 논리적인 구조와 규칙을 명확하게 표현하는 기법/과정

3. 물리적 데이터 모델링
   - 논리적 데이터 모델이 데이터 저장소로서 어떻게 실제로 저장되는지 구현




# ✔ 개체 관계 모델 (ERD, Entity Relation Diagram)

> 용어
- 개체 (Entity): 업무가 관여하는 정보
- 속성 (Attribute): 개체가 가지는 성격, 데이터 타입과 크기 및 제약사항 지정
- 관계 (Relationship): 개체 간의 관계, 연관성

> 관계

1. 수적 관계 (Cardinality)
   - 1:1 관계: A는 B를 하나 가짐, B도 A를 하나 가짐
   - 1:N 관계: A는 B를 여러 개 가짐, B는 A의 하나에 해당
   - M:N 관계: A는 B를 여러 개 가짐, B는 A를 여러 개 가짐

2. 옵션 관계 (Optionality)
   - 필수(1)
   - 선택(0)

> crow’s foot
- zero or many
  
  ![zero or many](https://vertabelo.com/blog/crow-s-foot-notation/crows-foot-notation-zero-or-many.png)

- one or many

  ![one or many](https://vertabelo.com/blog/crow-s-foot-notation/crows-foot-notation-one-or-many.png)

- one and only one

  ![one and only one](https://vertabelo.com/blog/crow-s-foot-notation/crows-foot-notation-one.png)

- zero or one

  ![zero or one](https://vertabelo.com/blog/crow-s-foot-notation/crows-foot-notation-one-or-zero.png)



# ✔ 정규화
- 데이터베이스 테이블을 설계하는 과정에서 중복성을 제거하여 성능을 향상하는 것

> 정규화 종류

1. 제 1 정규화
   - 도메인 원자값 (Atomic Column)
   - 한 속성에 여러 개의 속성이 포함되거나, 같은 유형의 속성이 여러 개로 나눠져 있는 경우 제거

2. 제 2 정규화
   - 부분적 함수 종속성 제거
   - PK가 아닌 모든 칼럼은 PK에 종속되도록 구성

3. 제 3 정규화
   - 이행적 함수 종속성 제거 (X → Y, Y → Z)
   - 일반 속성 간의 함수 종속 관계가 존재하지 않아야 함