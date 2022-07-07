# ✔ Github Flow 

> Github Flow의 기본 원칙
1. master branch는 반드시 배포 가능한 상태여야 한다
2. feature branch는 각 기능의 의도를 알 수 있어야 한다
3. Commit message는 매우 중요하며, 명확하게 작성한다
4. **Pull Request**를 통해 협업한다
5. 변경사항을 반영하고 싶다면, master branch에 병합한다

*****
> Workflow 분류
1. Feature Branch Workflow
   - Shared repository model
   - 작업자가 저장소의 소유권이 **있는** 경우
    ```bash
    # 1) clone을 통해 원격저장소를 로컬저장소에 복제
    $ git clone {원격저장소URL}
    
    # 2) 기능 추가를 위해 branch 생성 및 기능 구현(커밋 발생)
    $ git checkout -b {브랜치명}

    # 3) 원격 저장소에 브랜치 반영
    $ git push {원격저장소URL 별칭} {브랜치명}

    # 4) github 저장소에서 Pull Request(PR) 실행

    # 5) 권한자가 master에 branch를 병합(또는 드랍)

    # 6) 병합 완료된 branch 삭제

    # 7) 작업자는 다시 병합된 master를 pull
    $ git pull {원격저장소URL 별칭} {브랜치명}
    ```
2. Forking Workflow
   - Fork & Pull model
   - 작업자가 특정 저장소의 소유권이 **없는** 경우
    ```bash
    # 1) 소유권이 없는 원격 저장소를 Fork를 통해 나의 원격 저장소에 복제

    # 2) clone을 통해 원격저장소를 로컬저장소에 복제
    $ git clone {원격저장소URL}

    # 3) 기능 추가를 위해 branch 생성 및 기능 구현(커밋 발생)
    $ git checkout -b {브랜치명}

    # 4) 나의 원격 저장소에 브랜치 반영
    $ git push {원격저장소URL 별칭} {브랜치명}

    # 5) github 저장소에서 원본 사용자에게 Pull Request(PR) 실행

    # 6) 권한자가 master에 branch를 병합(또는 드랍)

    # 7) 병합 완료된 branch 삭제

    # 8) 작업자는 다시 병합된 master를 pull
    ```