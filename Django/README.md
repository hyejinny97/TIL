# 📚 Django

✅ Django란?

장고는 서버를 구현하는 웹 프레임워크로 파이썬을 기반으로 만들어졌다. 

✅ Django의 설계 철학 (Templates System)

1. “표현(template)과 로직(view)을 분리”
   - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
   - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함

2. “중복을 배제”
   - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖음
   - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 함
   - 템플릿 상속의 기초가 되는 철학

✅ Django Framework의 성격

- ‘다소 독선적(Opinionated)’
- 독선적인 프레임워크들은 어떤 특정 작업을 다루는 ‘올바른 방법’에 대한 분명한 의견(규약)을 가지고 있음
- 우리가 온전히 만들고자 하는 것에만 집중할 수 있게 도와줌
- 하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있음



## 📃 목록

- [Django 구조(MTV Design Pattern)](https://github.com/hyejinny97/TIL/blob/master/Django/mtv.md)
  - Software Design Pattern
  - MTV Design Pattern
- [Django 개발 환경 설치](https://github.com/hyejinny97/TIL/blob/master/Django/environment.md)
  - Django 개발 환경
  - Django 프로젝트 구조
  - Django 애플리케이션(앱) 구조
- [요청과 응답](https://github.com/hyejinny97/TIL/blob/master/Django/request_response.md)
  - 요청과 응답: URL → VIEW → TEMPLATE
  - App URL Mapping
  - URL Namespace
  - Django Template Language (DTL)
  - Template Inheritance
  - Template Namespace
- [form 데이터 주고 받기](https://github.com/hyejinny97/TIL/blob/master/Django/form_data.md)
  - Variable Routing
  - Sending form data (Client)
  - Retrieving form data (Server)
- [Django Model](https://github.com/hyejinny97/TIL/blob/master/Django/model.md)
  - Database
  - Django Model
- [Django ORM](https://github.com/hyejinny97/TIL/blob/master/Django/orm.md)
  - ORM
  - ORM 실습 편의를 위한 외부 라이브러리 설치 및 설정
  - QuerySet API
- [Django view 함수를 통한 CRUD](https://github.com/hyejinny97/TIL/blob/master/Django/crud.md)
  - HTTP (HyperText Transfer Protocol)
  - READ
  - CREATE
  - DELETE
  - UPDATE
- [Django ModelForm](https://github.com/hyejinny97/TIL/blob/master/Django/model_form.md)
  - ModelForm
  - ModelForm과 Create & Update
- [Django Admin site](https://github.com/hyejinny97/TIL/blob/master/Django/admin.md)
- [Django Static Files](https://github.com/hyejinny97/TIL/blob/master/Django/static_files.md)
- [Django Media Files](https://github.com/hyejinny97/TIL/blob/master/Django/media_files.md)
  - 이미지 업로드 - 기본 설정
  - 이미지 업로드 - CREATE
  - 이미지 업로드 - READ
  - 이미지 업로드 - UPDATE
  - Django-imagekit 라이브러리
- [Django Auth](https://github.com/hyejinny97/TIL/blob/master/Django/auth.md)
  - Django Auth
  - Django User Model
  - Django AnonymousUser Model
  - Django UserCreationForm
  - Django UserChangeForm
  - Django SetPasswordForm
  - Django PasswordChangeForm
  - Django AdminPasswordChangeForm
  - Django AuthenticationForm
- [User 객체 / AnonymousUser 객체](https://github.com/hyejinny97/TIL/blob/master/Django/user_objects.md)
  - User 객체
  - AnonymousUser 객체
- [회원 가입 / 로그인](https://github.com/hyejinny97/TIL/blob/master/Django/signup_signin.md)
  - 회원가입
    - 회원가입 - CREATE
    - 프로필 상세보기 - READ
    - 프로필 수정하기 - UPDATE
    - 회원탈퇴 - DELETE
  - 로그인
    - 쿠키(Cookie)
    - 세션 (Session)
    - Login
    - Authentication with User
    - Logout
    - Limiting access to logged-in users
- [1:N 관계](https://github.com/hyejinny97/TIL/blob/master/Django/foreign_key.md)
  - one-to-many relationship
  - 1:N 관계 (Article - Comment)
  - Comment 구현 
    - 댓글 생성 - CREATE
    - 댓글 목록 - READ
    - 댓글 삭제 - DELETE
    - 댓글 개수 출력
    - 댓글이 없는 경우 대체 컨텐츠 출력
  - 1:N 관계 (User - Comment)
- [M:N 관계](https://github.com/hyejinny97/TIL/blob/master/Django/MN_relationship.md)
  - Many to many relationship
  - Django ManyToManyField
  - M:N 관계 (Article - User 간의 LIKE)


## 🛠 실습
- [Django 요청-응답 실습(2022.09.22)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_01)
- [영화 리뷰 사이트 개발 프로젝트 - 조사 및 기획(2022.09.23)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/pr_01)
- [Django form 데이터 주고 받기 실습(2022.09.26)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_02)
- [Django ORM 실습(2022.09.27)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_03)
- [Django urls/templates 분리, models 적용 실습(2022.09.27)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_04)
- [Django CRUD를 통해 메모 사이트 구현 실습(2022.09.28~29)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_05)
- [영화 리뷰 사이트 개발 프로젝트 - CRUD(2022.09.30)](https://github.com/hyejinny97/movie_review_1)
- [Django ModelForm 활용 실습(2022.10.04)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_06)
- [Django admin, static files, django-bootstrap5 활용 실습(2022.10.05)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_07)
- [Django 영화 정보 제공 사이트 개발 실습(2022.10.06)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_08)
- [영화 리뷰 사이트 개발 프로젝트 - modelform(2022.10.07)](https://github.com/hyejinny97/movie_review_2)
- [Django Auth를 활용한 회원가입 및 프로필 서비스 개발(2022.10.11)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_09)
- [Django Auth를 활용한 로그인 서비스 개발(2022.10.12)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_10)
- [Django Auth를 활용한 회원 정보 수정 및 탈퇴 서비스 개발(2022.10.13)](https://github.com/hyejinny97/practice_11)
- [영화 리뷰 + 회원 관리 커뮤니티 개발 프로젝트 - Auth(2022.10.14)](https://github.com/hyejinny97/movie-account)
- [Django Media를 활용한 게시판 서비스 개발(2022.10.17)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_12)
- [1:N 관계로 매핑된 게시글-댓글 게시판 서비스 개발(2022.10.18~19)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_13)
- [Django Model 1:N 관계를 매핑하여 게시판 서비스 개발(2022.10.20)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_14)
- [영화 리뷰 + 댓글 + 회원 관리 커뮤니티 개발 프로젝트(2022.10.21)](https://github.com/hyejinny97/movie-community)
- [Django Model M:N 관계를 매핑하여 게시판 서비스 개발(2022.10.24)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_14)



## 🔎 참고자료
- [django 공식 문서](https://www.djangoproject.com/)
- [MDN 문서](https://developer.mozilla.org/en-US/docs/Learn/Server-side)
- [django-bootstrap5 22.1](https://pypi.org/project/django-bootstrap5/)
- [Django GitHub](https://github.com/django/django)
- [django-imagekit 2.0.4](https://pypi.org/project/django-imagekit/2.0.4/)
- [django-widget-tweaks 1.4.12](https://pypi.org/project/django-widget-tweaks/)