# ✔ 파이썬 모듈 
> 파이썬 기본 모듈
- [날짜/시간 관련 datetime 모듈](#-datetime-모듈)



# ✔ datetime 모듈
- 날짜와 시간을 조작하는 클래스를 제공
- 날짜와 시간 객체: aware객체, naive객체

> datetime.datetime 클래스
- datetime 객체는 date 객체와 time 객체의 모든 정보를 포함하는 단일 객체임

1. `datetime.now(tz=None)` 메서드

   - 현재의 지역 날짜와 시간을 반환

   ```python
   import datetime

   now = datetime.datetime.now()

   print(now)
   # 2022-09-11 14:22:33.146638

   print(f'{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초')
   # 2022년 9월 11일 14시 22분 33초
   ```