# 장고 실습 12 - Django Media를 활용한 게시판 서비스 개발

## 과정

- [목표](#목표)
- [준비 사항](#준비-사항)
- [요구 사항](#요구-사항)
- [실습 결과 완성본](#실습-결과-완성본)

## 목표

- Django Media를 활용한 이미지 업로드가 가능한 게시판 서비스를 개발합니다.
- [django-imagekit](https://pypi.org/project/django-imagekit/2.0.4/) 라이브러리를 활용해 이미지 썸네일 만들기
  - [참고](https://wayhome25.github.io/django/2017/05/11/image-thumbnail/)
- [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/) 라이브러리를 활용해 form을 직접 customizing하기
- [Django messages framework](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/) 활용

## 준비 사항

> 가상 환경 생성 및 실행

```bash
$ python -m venv venv
```

```bash
$ source venv/Scripts/activate
```

> 패키지 설치

1. Django 
   
   ```bash
   $ pip install django==3.2.13
   ```

2. Code Formatter black 
   
   ```bash
   $ pip install black
   ```

3. django-bootstrap5
   
   ```bash
   $ pip install django-bootstrap5
   ```
   
   - 패키지 설치 후, settings.py의 INSTALLED_APPS에 `'django_bootstrap5',` 추가

4. Pollow

   
   ```bash
   $ pip install Pillow
   ```

5. django-imagekit
   
   ```bash
   $ pip install django-widget-tweaks
   ```

   - 패키지 설치 후, settings.py의 INSTALLED_APPS에 `'imagekit',` 추가
 
6. django-widget-tweaks
   
   ```bash
   $ pip install django-imagekit
   ```

   - 패키지 설치 후, settings.py의 INSTALLED_APPS에 `'widget_tweaks',` 추가

> 설치된 패키지 목록 기록

```bash
$ pip freeze > requirements.txt
```

> 장고 프로젝트 생성 & 앱 생성 및 앱 등록

```bash
$ django-admin startproject pjt .
```

```bash
$ python manage.py startapp articles
```

> SECRET KEY 분리 설정

- secrets.json
  
  ```json
  {
      "SECRET_KEY": "new secret key"
  }
  ```

- settings.py 수정
  
  ```python
  import os, json
  from django.core.exceptions import ImproperlyConfigured
  
  secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json 파일 위치를 명시
  
  with open(secret_file) as f:
      secrets = json.loads(f.read())
  
  def get_secret(setting, secrets=secrets):
      try:
          return secrets[setting]
      except KeyError:
          error_msg = "Set the {} environment variable".format(setting)
          raise ImproperlyConfigured(error_msg)
  
  SECRET_KEY = get_secret("SECRET_KEY")
  ```

- .gitignore에 추가
  
  ```
  secrets.json
  ```

> .gitignore 설정

```
.venv
```

## 요구 사항

> 모델 Model - `M`

- 모델 이름 : Article
- 모델 필드

| 필드 이름     | 역할      | 필드             | 속성                                                                                                                                                   |
| --------- | ------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| title     | 글 제목    | Char           | max_length=80                                                                                                                                        |
| content   | 글 내용    | Text           |                                                                                                                                                      |
| image     | 글 이미지   | Image          | blank=True, upload_to='images/'                                                                                                                      |
| thumbnail | 썸네일 이미지 | ProcessedImage | upload_to='images/',                                             blank=True, processors=[Thumbnail(100, 50)], format='JPEG', options={'quality': 60} |


> 기능 View - `V`

1. 데이터 목록 조회 Read(index)
   
   - `GET` `http://127.0.0.1:8000/articles/`

2. 데이터 정보 조회 Read(detail)

   - `GET` `http://127.0.0.1:8000/articles/<int:pk>/`

3. 데이터 생성 Create

   - `POST` `http://127.0.0.1:8000/articles/create/`
   - 사용자가 글 이미지 **image**와 썸네일 이미지 **thumbnail**를 업로드할 수 있어야합니다.

4. 데이터 수정 Update

   - `POST` `http://127.0.0.1:8000/articles/<int:pk>/update/`

5. 데이터 삭제 Delete

   - `POST` `http://127.0.0.1:8000/articles/<int:pk>/delete/`


> 화면 Template - `T`

1. 목록 페이지
   
   - `GET` `http://127.0.0.1:8000/articles/`
   - 게시글 목록
   - 썸네일 이미지 **thumbnail**가 있으면 썸네일 이미지를 출력합니다.

2. 정보 페이지

   - `GET` `http://127.0.0.1:8000/articles/<int:pk>/`
   - 해당 게시글 정보 출력
   - 글 이미지 **image** 가 있으면 이미지를 출력합니다.

3. 작성 페이지

   - `GET` `http://127.0.0.1:8000/articles/create/` 
   - 게시글 작성 폼
   - 사용자가 이미지를 업로드할 수 있어야합니다.

4. 수정 페이지

   - `GET` `http://127.0.0.1:8000/articles/<int:pk>/update/`
   - 게시글 수정 폼

## 실습 결과 완성본

> 게시판 서비스

![](gif/django_practice_12_animation.gif)