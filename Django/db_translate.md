# ✔ DB 데이터 이동

- 로컬에서 구축한 데이터베이스의 데이터를 배포 후 데이터베이스로 복사하는 방법

1. [로컬 환경] 데이터 추출

   - 로컬 데이터베이스(sqlite3)에서 특정 앱의 데이터를 추출
   
   - 데이터가 저장된 `파일이름.json` 파일이 생성됨
 
     ```bash
     python -Xutf8 manage.py dumpdata 앱이름 > 파일이름.json
 
     # 예시
     python -Xutf8 manage.py dumpdata articles > articles.json
     ```

2. 서비스 배포

   - `파일이름.json`을 포함하여 서비스를 재배포

3. [배포 환경] 데이터 저장

   - 추출한 데이터를 배포 환경의 데이터베이스에 저장

     ```bash
     # 헤로쿠 배포를 한 경우, 로컬 환경 터미널에서 입력
     heroku run python manage.py loaddata 파일이름.json
 
     # 배포 서버 터미널에서 직접 입력할 때
     python manage.py loaddata 파일이름.json
     ```

> 주의 사항

- 배포 환경에서 데이터베이스를 마이그레이트(migrate)를 한 상태여야함
- 배포 환경에서 데이터 추가를 하지 않은 상황이어야함(동일 pk 오류 발생 가능)
- 데이터 추가를 한 적이 있다면 아래 명령어로 데이터베이스를 리셋해야 함
  
  ```bash
  heroku run python manage.py flush
  ```