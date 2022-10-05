# ✔ Admin site
- Django의 가장 강력한 기능 중 하나인 automatic admin interface 알아보기
- 관리자 페이지
  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
  - 모델 class를 admin.py에 등록하고 관리
  - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

> admin 계정 생성 & admin site 로그인
- username과 password를 입력해 관리자 계정을 생성
  - email은 선택사항이기 때문에 입력하지 않고 enter를 입력하는 것이 가능
  - 비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력을 이어가도록 함
  
  ```bash
  $ python manage.py createsuperuser
  ```

- `http://127.0.0.1:8000/admin/` 로 접속 후 로그인
- 계정만 만든 경우, Django 관리자 화면에서 모델 클래스는 보이지 않음

> admin에 모델 클래스 등록
- 모델의 record를 보기 위해서는 admin.py에 등록 필요
- 등록 후, admin 페이지에서 데이터를 조작 가능

  ```python
  # articles/admin.py

  from django.contrib import admin
  from .models import Article

  admin.site.register(Article)
  ```