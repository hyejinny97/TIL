# 장고 실습 03 - Django ORM 실습




## 과정

- [목표](#목표)
- [준비 사항](#준비-사항)
- [실습 문제 들어가기 전에](#실습-문제-들어가기-전에)
- [실습 문제](실습.md)



## 목표

- Django 쿼리셋 API / ORM 실습




## 준비 사항

1. 폴더 내 가상환경 생성
   
   ```bash
   $ python -m venv venv
   ```

2. 가상환경 실행
   
   - window의 경우
     
     ```bash
     $ . venv/scripts/activate
     ```
   
   - mac의 경우
     
     ```bash
     $ . venv/bin/activate
     ```

3. 패키지 설치
   
   ```bash
   $ pip install -r requirements.txt
   ```

4. 서버 정상 실행 확인 후 종료
   
   ```bash
   $ python manage.py runserver
   ```

5. shell_plus 진입
   
   ```bash
   $ python manage.py shell_plus
   ```




## 실습 문제 들어가기 전에

> 실습 모델 정보

- 모델 이름 : Todo (메모장)
- 모델 필드

  | 필드 이름      | 역할     | 필드      | 속성                |
  |:----------:|:------:|:-------:|:-----------------:|
  | id         | 기본키    |         |                   |
  | content    | 할 일 내용 | Char    | max_length=80     |
  | completed  | 완료 여부  | Boolean | default=False     |
  | priority   | 우선순위   | Integer |                   |
  | created_at | 생성 날짜  | Date    | auto_now_add=True |
  | deadline   | 마감 기한  | Date    | null=True         |

> 참고 사이트
- [장고 ORM과 쿼리셋(QuerySets)](https://tutorial.djangogirls.org/ko/django_orm/)
- [Django ORM](http://www.incodom.kr/Django_ORM)
- [장고(Django) - Field lookup](https://tibetsandfox.tistory.com/7)

> shell_plus을 사용해서 실습을 진행하는 이유
- shell을 활용하는 것은 디버깅하는 것과 동일합니다.
- 쿼리셋 API를 사용한 복잡한 로직을 구현할 때 view에서 테스트하는 건 제약이 있기 때문에 shell을 활용하는 방법을 배워야 합니다.