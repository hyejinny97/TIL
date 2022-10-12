# ✔ User 객체
- User 객체는 인증 시스템의 가장 기본
- [django.contrib.auth > User model](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/)

> User 객체의 Fields
- username 
- password
- email
- first_name
- last_name
- is_staff
- is_active
- is_superuser
- last_login
- date_joined

> User 객체의 Attributes

- `is_authenticated`
  - 로그인 여부
  - 만약 로그인 되어 있다면, True를 반환
  - User 객체는 항상 True를 반환

  ```python
  if request.user.is_authenticated:
      pass
      # do something if user is logged in
  else:
      pass
      # do something if user is logged_out
  ```

- `is_anonymous`
  - 로그아웃 여부
  - 유저가 로그아웃된 상태라면 True를 반환
  - User 객체는 항상 False를 반환

  ```python
  if request.user.is_anonymous:
      pass
      # do something if user is logged out
  else:
      pass
      # do something if user is logged in
  ```

> User 객체의 Methods

- `set_password(raw_password)`
  - User 비밀번호 변경

  ```python
  from django.contrib.auth import get_user_model

  user = get_user_model().objects.get(pk=2)
  user.set_password('new password')
  user.save()
  ```

> User 객체의 Manager methods

- `create_user(username, email=None, password=None, **extra_fields)`
  - User 생성
  
  ```python
  from django.contrib.auth import get_user_model

  user = get_user_model().objects.create_user('john', 'john@google.com', '1q2w3e4r!')
  ```

- `create_superuser(username, email=None, password=None, **extra_fields)`

  ```python
  from django.contrib.auth import get_user_model

  superuser = get_user_model().objects.create_superuser('hong', 'hong@google.com', '1q2w3e4r!')
  ```




# ✔ AnonymousUser 객체
- [django.contrib.auth > AnonymousUser model](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#anonymoususer-object)

> AnonymousUser 객체의 Attributes

- `is_authenticated`
  - 로그인 여부
  - 만약 로그인 되어 있다면, True를 반환
  - AnonymousUser 객체는 항상 False를 반환

  ```python
  if request.user.is_authenticated:
      pass
      # do something if user is logged in
  else:
      pass
      # do something if user is logged_out
  ```

- `is_anonymous`
  - 로그아웃 여부
  - 유저가 로그아웃된 상태라면 True를 반환
  - AnonymousUser 객체는 항상 True를 반환

  ```python
  if request.user.is_anonymous:
      pass
      # do something if user is logged out
  else:
      pass
      # do something if user is logged in
  ```

> AnonymousUser 객체의 Methods

- `get_username()`
  - 항상 빈 문자열을 반환

- `set_password()`, `check_password()`, `save()`, `delete()`
  - NotImplementedError를 일으킴