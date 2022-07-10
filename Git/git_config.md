# ✔ Git 환경 설정

git은 버전을 저장할 때마다 그 버전을 만든 사용자 정보도 함께 저장하기 때문에, 깃을 사용하기 전에 먼저 사용자 정보를 입력해야 한다

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

   - 한 번만 설정하면 앞으로 사용될 모든 git 저장소에서 같은 사용자 정보를 사용함
   - `$ git config --global user.name {유저명}`

   - `$ git config --global user.email {이메일명}`

2. 설정 확인
   - `$ git config --global --list`

3. 기본 편집기 설정 변경
   - 깃을 설치할 때 기본 편집기로 Vim이 설정됨
   - `$ git config --global core.editor {편집기명}` 

*****
> git local 영역 설정 명령어
```bash
$ git config --local
```
- 해당 디렉토리/.git/config
- **특정 저장소**에만 적용되는 설정

1. Local 사용자 정보 설정
   - 현재 사용중인 저장소에서 Global 사용자 정보가 아닌 다른 사용자 정보를 저장하기 위해 주로 사용
   - `$ git config [--local] user.name {유저명}`
   - `$ git config [--local] user.email {이메일명}`

2. 설정 확인
   - `$ git config --local --list`
