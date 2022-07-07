# ✔ Git 설정 파일


> git system 영역 설정 명령어
```bash
$ git config --system
```
- c:/program Files/Git/etc/gitconfig
- 시스템의 **모든 사용자**와 **모든 저장소**에 적용(관리자 권환)

*****
> git global 영역 설정 명령어
```bash
$ git config --global
```
- c:/Users/사용자계정/gitconfig
- **현재 사용자**에게 적용되는 설정

1. Global 사용자 정보(commit author) 설정

   - 한 번만 설정하면 앞으로 사용될 모든 git 저장소에서 동일하게 사용할 수 있음
   - `$ git config --global user.name "유저명"`

   - `$ git config --global user.email "이메일명"`

2. 설정 확인
   - `$ git config --global --list`

*****
> git local 영역 설정 명령어
```bash
$ git config --local
```
- 해당 디렉토리/.git/config
- **특정 저장소**에만 적용되는 설정

1. Local 사용자 정보 설정
   - 현재 사용중인 저장소에서 Global 사용자 정보가 아닌 다른 사용자 정보를 저장하기 위해 주로 사용
   - `$ git config [--local] user.name "유저명"`
   - `$ git config [--local] user.email "이메일명"`

2. 설정 확인
   - `$ git config --local --list`
