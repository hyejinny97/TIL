# ✔ 원격저장소 생성 후 경로 설정

- 원격저장소를 생성하면 원격저장소 주소가 생성됨
- 원격저장소 주소 형식:  github.com/GitHub_username/저장소_이름.git
- if 저장소 이름 변경 시, 원격저장소 URL도 변경되므로 로컬 설정 변경이 반드시 필요

*****
> 로컬저장소에 원격저장소를 연결해주는 명령어
```bash
$ git remote add {원격저장소URL 별칭} {원격저장소URL}
```
- 원격 저장소 정보를 로컬 저장소에 추가
- 로컬 저장소에는 한번만 설정해주면 됨
- 일반적으로 원격저장소 url의 별칭을 `origin`으로 많이 씀

```
ex) git remote add origin http://github.com/hyejinny97/TIL.git
```
- `$ git remote -v`: 원격 저장소의 정보를 확인

  

# ✔ 로컬 저장소 -> 원격 저장소

> 로컬 저장소의 변경사항(커밋)을 원격 저장소로 올리는 명령어
```bash
$ git push {원격저장소URL 별칭} {브랜치명}
```  
- 로컬 저장소의 파일/폴더가 아닌 저장소의 **버전(커밋)**이 올라감
- 원격저장소로의 push 권한은 collaborator에게만 있음
```
ex) $ git push origin master
```
*****
> push 실패
1. push 실패 원인
   - 로컬과 원격 저장소의 커밋 이력이 다른 경우 발생

2. push 실패 해결법

   - `$ git pull` ---> 로컬저장소에서 두 커밋을 병합 (merge) ---> `$ git push`

   - 하지만 동시에 같은 파일의 같은 부분이 수정된 경우, merge conflict 발생



# ✔ 원격 저장소 -> 로컬 저장소

> 원격 저장소를 **복제**하여 모든 버전을 가져오는 명령어
```bash
$ git clone {원격저장소URL}
```
- 원격 저장소의 이름의 폴더로 이동해서 활용함
```
ex) $ git clone http://github.com/hyejinny97/TIL.git
```
*****
> 원격저장소에 새롭게 **업데이트된 버전**을 가져오는 명령어
```bash
$ git pull {원격저장소URL 별칭} {브랜치명}
```
- 원격 저장소로부터 변경된 내역을 받아와 로컬 저장소의 버전들과 병합
```
ex) $ git pull origin master
```
