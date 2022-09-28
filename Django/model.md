# ✔ Database

- 체계화된 데이터의 모임
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
- Database 기본 구조: 스키마(Schema), 테이블(Table)

> Schema

- 뼈대(Structure)

- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
  
  | column | datatype |
  |:------:|:--------:|
  | id     | INT      |
  | name   | TEXT     |
  | age    | INT      |
  | email  | TEXT     |

> Table

- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합

- 관계(Relation)라고도 부름
  
  | id  | name | age | email          |
  | --- | ---- | --- | -------------- |
  | 1   | hong | 42  | hong@email.com |
  | 2   | kim  | 16  | kim@email.com  |
  | 3   | kang | 29  | kang@email.com |
1. 필드(field)
   
   - 속성, 컬럼(Column)
   - 각 필드에는 고유한 데이터 형식이 지정됨
     - INT, TEXT 등

2. 레코드(record)
   
   - 튜플, 행(Row)
   - 테이블의 데이터는 레코드에 저장됨

3. PK (Primary Key)
   
   - 기본 키
   - 각 레코드의 고유한 값 (식별자로 사용)
   - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
   - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨

> 쿼리(Query)

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어
- "Query를 날린다" == “데이터베이스를 조작한다”





# ✔ Django Model

- Django는 Model을 통해 데이터에 접근하고 조작
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조 (layout)

> Model 작성

- models.py 작성

- 일반적으로 각각의 모델 **클래스**는 하나의 데이터베이스 **테이블**에 매핑(mapping)됨

- 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것
  
  | Column  | Data Type   |
  |:-------:|:-----------:|
  | title   | VARCHAR(10) |
  | content | TEXT        |
  
  ```python
  # articles/models.py
  from django.db import models
  
  class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
  ```

- 각 모델은 `django.models.Model` 클래스의 서브 클래스
  
  - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
  - 클래스 상속 기반 형태의 Django 프레임워크 개발

- models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의

> Django Model Field

- Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형 (INT, TEXT 등)을 정의

- 데이터 유형에 따라 다양한 모델 필드를 제공
  
  - DataField(), CharField(), IntegerField() 등
  - 참고: <https://docs.djangoproject.com/en/3.2/ref/models/fields/>

1. `CharField(max_length=None, **options)`
   
   - 길이의 제한이 있는 문자열을 넣을 때 사용
   
   - `max_length`
     - 필드의 최대 길이(문자) 지정
     - CharField의 필수 인자
     - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용됨

2. `TextField(**options)`
   
   - 글자의 수가 많을 때 사용
   - max_length 옵션 작성 시 사용자 입력 단계에서는 반영 되지만, 모델과 데이터베이스 단계에는 적용되지 않음 (CharField를 사용해야 함)
   - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음

3. `DateTimeField()`

   - Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
   - DateField를 상속받는 클래스
   
   - `auto_now_add`
     - 최초 생성 일자 (Useful for creation of timestamps)
     - 데이터가 실제로 만들어질 때 현재 날짜와 시간으로 자동으로 초기화 되도록 함
   - `auto_now`
     - 최종 수정 일자 (Useful for “last-modified” timestamps)
     - 데이터가 수정될 때마다 현재 날짜와 시간으로 자동으로 갱신되도록 함

> Model 변경사항 반영

1. makemigrations

   ```bash
   $ python manage.py makemigrations
   ```

   - 모델의 변경사항에 대한 새로운 migration을 만들 때 사용
   - 파이썬으로 작성된 설계도

2. migrate 

   ```bash
   $ python manage.py migrate  
   ```

   - makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정 (db.sqlite3 파일에 반영)
   - 결과적으로 모델의 변경사항과 데이터베이스를 동기화

3. showmigrations

   ```bash
   $ python manage.py showmigrations
   ```

   - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
   - `X` 표시가 있으면 migrate가 완료되었음을 의미

4. sqlmigrate

   ```bash
   $ python manage.py sqlmigrate articles 0001
   ```

   - 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인 할 수 있음

> 추가 필드 정의 후, Model 변경사항 반영
- 기존에 id, title, content 필드를 가진 테이블에 2개의 필드가 추가되는 상황

  ```python
  # articles/models.py

  class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  ```

- 추가 모델 필드 작성 후 다시 한번 **makemigrations** 진행 필수
- 이미 존재하는 테이블에 새로운 컬럼이 추가되면, 이러한 컬럼들은 기본적으로 빈 값을 갖고 추가될 수 없음
  - 따라서, 추가되는 컬럼에 대한 **기본 값을 설정**하는 과정이 진행됨
  - 방법1) 다음 화면으로 넘어가서 새 컬럼의 기본 값을 직접 입력하는 방법
  - 방법2) 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성하는 방법

    ```
    You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.
    
      1) Provide a one-off default now (will be set on all existing rows)
      2) Quit, and let me add a default in models.py
    
    Select an option: 
    ```

  - 위 화면에서 아무것도 입력하지 않고 Enter를 입력하면, Django에서 기본적으로 파이썬의 timezone 모듈의 now 메서드 반환 값을 기본 값으로 사용하도록 해줌

    ```
    Please enter the default value now, as valid Python
    You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
    Type 'exit' to exit this prompt
    [default: timezone.now] >>>
    ```

- 새로운 설계도(마이그레이션 파일)가 만들어 진 것을 확인한 후, **migrate** 진행 필수