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




## 🛠 실습
- [Django 요청-응답 실습(2022.09.22)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_01)
- [영화 사이트 개발 프로젝트 - 조사 및 기획(2022.09.23)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/project_01)
- [Django form 데이터 주고 받기 실습(2022.09.26)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_02)
- [Django ORM 실습(2022.09.27)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_03)
- [Django urls/templates 분리, models 적용 실습(2022.09.27)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_04)
- [Django CRUD를 통해 메모 사이트 구현 실습(2022.09.28~29)](https://github.com/hyejinny97/TIL/blob/master/Django/practice/practice_05)



## 🔎 참고자료
- [django](https://www.djangoproject.com/)