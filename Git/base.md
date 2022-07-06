# ✔ git 저장소(repository) 생성
> 로컬 저장소를 생성



## `$ git init`

- 특정 폴더에 .git 폴더가 생성됨
- `(master)` 표기를 통해 git 저장소가 생성되었는지 알 수 있음

1. **버전이랑 상관없는 파일/폴더 관리**

    - 일반적인 개발 프로젝트에서 버전 관리가 별도로 필요없는 파일/폴더가 존재
      - [개발 언어, 개발 환경](https://www.toptal.com/developers/gitignore/)
    - 해결책: 폴더에 `.gitignore`파일을 생성 후, 버전관리가 필요없는 파일 등을 작성
      - 특정 파일: 파일명.txt
      - 특정 폴더: /폴더명
      - 특정 확장자: */.exe
      - 예외 처리: !a.exe
    - 주의) 이미 커밋된 파일은 반드시 삭제해야 .gitignore가 적용됨



# ✔ 버전(커밋) 기록
> 흐름: 1. Working Directory  --`add`-->  2. Staging Area  --`commit`-->  3. Repository

1. 파일을 변경 (modified)
2. 변경된 파일을 임시저장 (staged)
3. 버전을 기록 (commited)

## `$ git add 파일명`

- Working Directory 상의 변경 내용을 Staging Area에 추가해줌
  - Untracked file --`add`--> Staged
  - Modified file --`add`--> Staged
- `$ git add .`: 현재 폴더의 하위 파일들을 모두 추가

## `$ git commit -m '커밋메시지'`

- Staged 상태의 파일을 버전으로 기록
- 변경된 파일만 새로 저장



# ✔ 상태/버전 확인 
## `$ git status`

- **Working Directory, Staging Area**에서의 현재 파일 상태를 알 수 있음
  1. Untracked files: 버전으로 관리된 적 없는 새 파일

  2. Tracked files: 버전으로 관리되고 있는 파일
     - Changes not staged for commit: 현재 Modified인 상태
     - Changes to be commited: 현재 Staged인 상태

  3. Nothing to commit, working tree clean: 커밋하거나 추가할 파일이 전혀 없음 

## `$ git log`

- **Repository**에 기록된 커밋을 조회
- `$ git log -1`: 최근 커밋 1개만 조회
- `$ git log --oneline`: 커밋을 한 줄에 출력
- `$ git log -2 --oneline`: 최근 커밋 2개만 조회해 한 줄에 출력 
