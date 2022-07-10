# ✔ Git 저장소(repository) 생성

> Git 생성 명령어

```bash
$ git init
```
- 로컬 저장소를 생성
- 특정 폴더에 .git 폴더가 생성됨
- 저장소를 생성한 폴더의 버전을 관리함
- `(master)` 표기를 통해 git 저장소가 생성되었는지 알 수 있음
- `$ git init {디렉토리명}`: 새로운 디렉터리를 만들고 저장소를 초기화하는 과정을 한꺼번에 처리
*****
> 버전 관리하지 않을 파일/폴더

  - 일반적인 개발 프로젝트에서 버전 관리가 별도로 필요없는 파일/폴더가 존재  ex) [개발 언어, 개발 환경](https://www.toptal.com/developers/gitignore/)
  - 해결책: 폴더에 `.gitignore`파일을 생성 후, 버전관리가 필요없는 파일/폴더/확장자 목록을 지정
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
*****
> 변경된 파일을 임시저장 해주는 명령어
```bash
$ git add {파일명}
```
- Working Directory 상의 변경 내용을 Staging Area에 추가해줌
  - Untracked file --`add`--> Staged
  - Modified file --`add`--> Staged
- `$ git add .`: working directory에서 수정한 하위 파일들을 한꺼번에 stage area에 올림
*****
> 버전으로 기록 해주는 명령어
```bash
$ git commit -m '커밋메시지'
```

- Staged 상태의 파일을 버전으로 기록
- `$ git commit -am '커밋메시지'`: Tracked files의 경우, add와 commit을 동시에 처리
- `$ git commit --amend`: 가장 최근의 커밋 메시지 수정



# ✔ 상태/버전 확인 
> **Working Directory, Staging Area**에서의 현재 파일 상태를 알려주는 명령어

```bash
$ git status
```
1. Untracked files: 버전으로 관리된 적 없는 새 파일
2. Tracked files: 버전으로 관리되고 있는 파일
     - Changes not staged for commit: 현재 Modified인 상태
     - Changes to be commited: 현재 Staged인 상태
3. Nothing to commit, working tree clean: 커밋하거나 추가할 파일이 전혀 없음 
*****
> **Repository**에 기록된 버전(커밋)을 조회하는 명령어
```bash
$ git log
```
- git log 명령 입력 시, 알 수 있는 정보
  - commit hash (git hash): 커밋을 구별하는 아이디
  - branch
  - 작성자 (author)
  - 버전을 만든 날짜 (date)
  - 커밋 메시지
- 로그 메시지가 많을 경우 한 화면씩 나누어 보여줌
  - `enter`를 누르면 다음 로그 화면을 볼 수 있음
  - `Q`를 누르면 로그 화면을 빠져나옴
- `$ git log -숫자n`: 최근 커밋 n개만 조회
- `$ git log --oneline`: 커밋을 한 줄에 출력
- `$ git log --stat`: 커밋에 관련된 파일까지 함께 출력
- `$ git log --branches`: 각 브랜치의 커밋을 함께 출력
- `$ git log --graph`: 커밋을 그래프 형태로 출력
- `$ git log 브랜치A..브랜치B`: 브랜치A를 기준으로 브랜치B와 비교하여 출력 (즉, 브랜치 A에는 없고 브랜치B에만 있는 커밋을 출력)



# ✔ 변경 사항 확인
> 수정한 파일의 변경 사항을 알 수 있는 명령어
```bash
$ git diff
```
- 최근 버전과 작업 폴더의 수정 파일 사이 차이를 보여줌
- git diff 명령 입력 시, 알 수 있는 정보
  - `-문자열`: 삭제된 내용
  - `+문자열`: 추가된 내용



# ✔ 작업 되돌리기 
> **Working Directory**의 변경 사항을 취소하는 명령어
1. 구 명령어
    ```bash
    $ git checkout -- {파일명}
    ```
2. 신 명령어
    ```bash
    $ git restore {파일명}
    ```

*****
> **Staging Area**에 올라간 파일을 unstage하는 명령어
1. 구 명령어
    ```bash
    $ git reset HEAD {파일명}
    ```
2. 신 명령어
    ```bash
    $ git restore --staged {파일명}
    ```
- 파일명을 지정하지 않으면 stage area에 있는 모든 파일을 되돌림

*****
> **Repository**에 기록된 최신 커밋을 취소하는 명령어
```bash
$ git reset HEAD^
```
- HEAD^: 현재 HEAD가 가리키는 브랜치의 최신 커밋
- 커밋 전에 했던 스테이징도 함께 취소됨
- 취소한 파일은 working directory에 남겨짐
- `$ git reset HEAD~3`: 최근 3개의 커밋을 취소 
- `$ git reset --soft HEAD^`: 최근 커밋을 하기 전 상태로 되돌림
- `$ git reset --mixed HEAD^`: 최근 커밋/스테이징을 하기 전 상태로 되돌림 (= `$ git reset HEAD^`)
- `$ git reset --hard HEAD^`: 최근 커밋/스테이징/파일 수정하기 전 상태로 되돌림, 이 옵션으로 되돌린 내용은 복구 불가

*****
> **Repository**에 기록된 특정 커밋으로 되돌리는 명령어
```bash
$ git reset --hard {되돌아갈 커밋 해시}
```
- 커밋을 되돌리면서, 수정했던 것을 삭제하는 명령어
- 지정한 커밋 해시로 이동하고, 이후 커밋은 취소
- 주의) reset A를 입력하면, A 커밋 이후에 만들었던 모든 커밋들을 삭제하고, A 커밋으로 이동하여 최신 커밋은 A가 됨

*****
> 커밋 삭제하지 않고 되돌리는 명령어
```bash
$ git revert {취소할 커밋 해시}
```
- 커밋을 되돌리지만, 취소한 커밋을 남겨두는 명령어
- 지정한 커밋 해시의 변경 이력을 취소
- 주의) revert A를 입력하면, A 커밋을 지우는 대신 A 커밋에서 변경했던 이력을 취소한 새 커밋을 만듦 (즉, A 커밋의 직전 커밋 상태로 되돌아감)
- revert 명령을 실행하면 기본 편집기가 자동으로 나타나면서 커밋 메시지를 입력할 수 있음

*****
> 수정 중인 파일 감추기 및 되돌리기
```bash
# 커밋하지 않은 수정 내용을 보관
$ git stash [save]

# 감춰둔 파일 목록 중 가장 최근 항목을 꺼내옴
$ git stash pop
```
- 아직 커밋하지 않고 작업 중인 특정 파일들을 잠시 감추고, 당장 필요한 작업들을 먼저 끝낸 후 다시 감춘 파일들을 꺼내올 수 있음
- git stash 명령을 사용하려면 파일이 Tracked file이어야 함
- 가장 최근에 감춘 것을 위에 쌓기 때문에 stash 스택이라고도 표현
- `$ git stash list`: 감춘 파일 목록 조회, 가장 최근에 보관한 것이 stash{0}에 담김
- `$ git stash apply`: stash 목록에서 가장 최근 항목을 되돌리지만, 저장했던 내용은 그대로 남겨둠
- `$ git stash drop`: stash 목록에서 가장 최근 항목을 삭제