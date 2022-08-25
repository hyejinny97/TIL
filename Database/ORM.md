# ✔ ORM (Object Relational Mapping)
- **객체(object)로 DB를 조작**하는 것
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
- 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며, Django 프레임워크에서는 내장 Django ORM을 활용

> ORM 모델 설계 및 반영

1. 클래스를 생성하여 내가 원하는 DB의 구조를 만듦
  
   ```python
   from django.db import models
 
   class Genre(models.Model):
     name = models.CharField(max_length=30)
   ```

2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 자동 생성함
   
   ```bash
   $ python manage.py makemigrations
   ```

3. DB에 migrate 함
   
   ```bash
   $ python manage.py migrate
   ```

> Migration (마이그레이션)
- **Model에 생긴 변화를 DB에 반영**하기 위한 방법
   - 파이썬 class 생성 ⇒ DB 내 table 생성 
   -  파이썬 class를 수정, 삭제, 추가한 후 마이그레이션 ⇒ DB 내 기존 table의 컬럼 수정, 삭제, 추가
- 마이그레이션 파일을 만들어 DB 스키마를 반영함
- `makemigrations`: 마이그레이션 파일 생성
- `migrate`: 마이그레이션을 DB에 반영
- Migrate 시, 실제 SQL문 (트랜잭션)
  
  ```sql
  BEGIN;
  CREATE TABLE "db_genre" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "name" varchar(30) NOT NULL
  );
  COMMIT;
  ```



# ✔ ORM 기본조작 (CRUD)
- 데이터베이스 조작 (Database API): 먼저 shell_plus를 실행시킨 후, ORM 조작 가능

  ```bash
  $ python manage.py shell_plus
  ```

  ```python
  IN [1] : Genre.objects.all().query
  ```

  - Genre: `Class Name`
  - objects: `Manager` 
  - all(): `QuerySet API`
  - query: ORM이 실제 실행시키는 쿼리문을 볼 수 있음
    - 반환값이 QuerySet일때만 사용 가능
    - `Genre.objects.get(id=1).query`처럼 개별 object에서는 사용 불가(에러 발생)

> 데이터 생성 (Create)

1. `create()` 메서드 활용하는 방법
   
   ```python
   Genre.objects.create(name='발라드')
   ```

2. 인스턴스를 이용해 조작하는 방법
   
   ```python
   genre = Genre()
   genre.name = '인디밴드'
   genre.save()
   ```

> 데이터 조회 (Read)

1. 전체 데이터 조회 - `all()`
   
   ```python
   Genre.objects.all()
   
   # <QuerySet [<Genre: Genre object (1)>, <Genre: Genre object (2)>]>
   ```

2. 일부 데이터 조회 - `get()`
   
   ```python
   Genre.objects.get(id=1)

   # <Genre: Genre object (1)>
   ```

   - 객체(레코드) 하나를 반환해줌
   - 반환값이 없거나 2개 이상이면 오류를 발생시킴
   - 따라서, Primary Key를 기준으로 하나의 데이터를 조회할 때 주로 사용

3. 일부 데이터 조회 - `filter()`
   
   ```python
   Genre.objects.filter(name='발라드')

   # <QuerySet [<Genre: Genre object (1)>]>
   ```

   - QuerySet 형태로 반환해줌
   - 반환값이 없거나 2개 이상이어도 오류 없이 반환해줌
   - SQL에서 데이터 조회 시 WHERE문과 같은 역할을 해줌
   - 따라서, PK 이외의 컬럼을 기준으로 여러 개의 데이터를 조회할 때 주로 사용

4. 특정 조건을 제외한 데이터들만 조회 - `exclude()`
   
   ```python
   Genre.objects.exclude(name='발라드')

   # <QuerySet [<Genre: Genre object (2)>]>
   ```

   - QuerySet 형태로 반환해줌

> 데이터 수정 (Update)
1. `update()` 메서드 활용하는 방법
   
   ```python
   genre = Genre.objects.get(id=1)
   genre.update(name='트로트')
   ```
   
2. 인스턴스를 이용해 조작하는 방법
  
   ```python
   genre = Genre.objects.get(id=1)
   genre.name = '트로트'
   genre.save()
   ```

> 데이터 삭제 (Delete)
1. `delete()` 메서드 활용하는 방법

   ```python
   genre = Genre.objects.get(id=1)
   genre.delete()
   ```



# ✔ QuerySet API

> 비교연산자

1. `__gt` (greater than) 
   
   - SQL
  
      ```sql
      SELECT * FROM entry WHERE id > 4;
      ```

   - 파이썬
  
      ```python
      Entry.objects.filter(id__gt=4)
      ```

2. `__gte` (greater than equal)
   
    - SQL
  
      ```sql
      SELECT * FROM entry WHERE id >= 4;
      ```

   - 파이썬
  
      ```python
      Entry.objects.filter(id__gte=4)
      ```

3. `__lt` (less than)
   
   - SQL
  
      ```sql
      SELECT * FROM entry WHERE id < 4;
      ```

   - 파이썬
  
      ```python
      Entry.objects.filter(id__lt=4)
      ```

4. `__lte` (less than equal)
   
    - SQL
  
      ```sql
      SELECT * FROM entry WHERE id <= 4;
      ```

   - 파이썬
  
      ```python
      Entry.objects.filter(id__lte=4)
      ```

> 논리 연산자

1. AND 연산자
   
   - SQL

      ```sql
       SELECT * FROM entry WHERE headline = 'Lennon' AND pub_date = '2005-03-31';
      ```
   
   - 파이썬

      ```python
      Entry.objects.filter(headline='Lennon', pub_date='2005-03-31')
      ```

> SQL 연산자

1. `__in`
   
   - SQL
  
      ```sql
      SELECT * FROM entry WHERE id IN (1, 2, 3);
      SELECT * FROM entry WHERE headline IN ('a', 'b', 'c');
      ```

   - 파이썬

      ```python
      Entry.objects.filter(id__in=[1, 2, 3])
      Entry.objects.filter(headline__in='abc')
      ```

2. `__range`
   
   - SQL

      ```sql
      SELECT * FROM entry WHERE pub_date BETWEEN '2005-01-01' AND '2005-03-31';
      ```

   - 파이썬
  
      ```python
      import datetime

      start_date = datetime.date(2005, 1, 1)
      end_date = datetime.date(2005, 3, 31)
      Entry.objects.filter(pub_date__range=(start_date, end_date))
      ```

3. `__startswith` / `__istartswith`
   - i: insensitive로서 대소문자 구분을 안한다는 의미
   - SQL

      ```sql
      SELECT * FROM entry WHERE headline LIKE 'Lennon%';
      SELECT * FROM entry WHERE headline ILIKE 'Lemmon%';
      ```
   
   - 파이썬

      ```python
      Entry.objects.filter(headline__startswith='Lemmon')
      Entry.objects.filter(headline__istartswith='Lennon')
      ```

4. `__endswith` / `__iendswith`
   - i: insensitive로서 대소문자 구분을 안한다는 의미
   - SQL
  
      ```sql
      SELECT * FROM entry WHERE headline LIKE '%Lennon';
      SELECT * FROM entry WHERE headline ILIKE '%Lemmon';
      ```

   - 파이썬
  
      ```python
      Entry.objects.filter(headline__endswith='Lennon')
      Entry.objects.filter(headline__iendswith='Lennon')
      ```

5. `__contains` / `__icontains`
   - i: insensitive로서 대소문자 구분을 안한다는 의미
   - SQL

      ```sql
      SELECT * FROM entry WHERE headline LIKE '%Lennon%';
      SELECT * FROM entry WHERE headline ILIKE '%Lennon%';
      ```

   - 파이썬

      ```python
      Entry.objects.filter(headline__contains='Lennon')
      Entry.objects.filter(headline__icontains='Lennon')
      ```

> SELECT문의 다양한 절

1. LIMIT 절
   
   - SQL
      
      ```sql
      SELECT * FROM entry LIMIT 1;
      SELECT * FROM entry LIMIT 2 OFFSET 3;
      ```

   - 파이썬
  
      ```python
      Entry.objects.all()[0]
      Entry.objects.all()[3:5]
      ```

2. ORDER BY 절
   
   - SQL

      ```sql
      SELECT * FROM entry ORDER BY id;
      SELECT * FROM entry ORDER BY id DESC;
      ```

   - 파이썬
  
      ```python
      Entry.objects.order_by('id')
      Entry.objects.order_by('-id')
      ```

3. 서브쿼리
   
   - SQL
  
      ```sql
      SELECT * 
      FROM entry 
      WHERE blog.id IN (
         SELECT id 
         FROM blog
         WHERE name LIKE '%Cheddar%'
      );
      ```

   - 파이썬

      ```python
      inner_qs = Blog.objects.filter(name__contains='Cheddar')
      entries = Entry.objects.filter(blog__in=inner_qs)
      ```