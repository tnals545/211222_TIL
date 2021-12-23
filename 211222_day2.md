# Git 특강 2일차



## 1. 원격 저장소(Remote Repository)

1) **Github에서 원격 저장소 생성**

2) **로컬 저장소와 원격 저장소 연결**

   1) 원격 저장소가 잘 생성되었는지 확인 후, 저장소의 주소를 복사

   2) 기존에 실습 때 만들었던 홈 디렉토리의 TIL 폴더로 가서 vscode 열기

   3) git init을 통해 TIL 폴더를 로컬 저장소로 만들기

      ```bash
      kyle@KYLE MINGW64 ~/TIL
      $ git init
      Initialized empty Git repository in C:/Users/kyle/TIL/.git/
      ```

   4) git remote

      - 로컬 저장소에 원격 저장소를 등록, 조회, 삭제 할 수 있는 명령어

      1. 원격 저장소 등록

         `git remote add <이름> <주소>` 

         ```bash
         $ git remote add origin <https://github.com/edukyle/TIL.git>
         ```

      2. 원격 저장소 조회

         `git remote -v` 

         ```bash
         $ git remote -v
         origin  <https://github.com/edukyle/TIL.git> (fetch)
         origin  <https://github.com/edukyle/TIL.git> (push)
         ```

      3. 원격 저장소 연결 삭제

         `git remote rm <이름>` 혹은 `git remote remove <이름>` 

         > 로컬과 원격 저장소의 연결을 끊는 것, 원격 저장소 자체를 삭제하는 것이 아님

         ```bash
         $ git remote rm origin
         $ git remote remove origin
         ```



 3. **원격 저장소에 업로드**

    	1. 로컬 저장소에서 커밋 생성

    ```bash
    $ git status # 상태 확인
    
    $ git add day1.md
    
    $ git commit -m "Upload TIL Day1"
    
    $ git log --oneline # 커밋 확인
    ```

    

     2. git push

        - `git push <저장소 이름> <브랜치 이름>` 

        - `-u` 옵션을 사용하면, 두 번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```

        - ```bash
          $ git push origin master
          
          [풀이]
          git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
          
          ------------------------------------------------
          
          $ git push -u origin master
          이후에는 $ git push 라고만 작성해도 push가 됩니다.
          ```



4. **원격 저장소에서 정상 업로드 확인**





#### * README.md 파일 push 해보기

- `README.md`는 원격 저장소의 소개와 설명이 담겨있는 일종의 대문 역할
- 반드시 파일 이름을 `README.md`로 지정해야 Github가 인식
- 홈 디렉토리에 있는 TIL 폴더에 `README.md` 파일을 생성하고, 자유롭게 `설명, 각오, 분류 등`을 마크다운 문법으로 작성하고 자신의 Github TIL 원격 저장소에 push









## 2.  .gitignore

> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것

### (1) .gitignore에 작성하는 목록

- 민감한 개인 정보가 담긴 파일 (전화번호, 계좌번호, 각종 비밀번호, API KEY 등)
- OS(운영체제)에서 활용되는 파일
- IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
  - 예) pycharm -> .idea/
- 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
  - 가상 환경 : `venv/`
  - `__pycache__/`



### (2) .gitignore 작성 시 주의 사항

- 반드시 이름을 `.gitignore`로 작성합니다. 앞의 점(.)은 숨김 파일이란 뜻
- `.gitignore` 파일은 `.git` 폴더와 동일한 위치에 생성
- **제외 하고 싶은 파일은 반드시 `git add` 전에 `.gitignore`에 작성**



### (3) .gitignore 쉽게 작성하기

> .gitignore의 내용을 쉽게 작성할 수 있도록 도와주는 두 개의 사이트를 소개합니다. 자신의 개발 환경에 맞는 것을 찾아서 `전체 복사, 붙여넣기`를 하면 됩니다.

1. **웹사이트**

[gitignore.io](https://gitignore.io/)

2. **gitignore 저장소**

https://github.com/github/gitignore









## 3. clone, pull

### (1) git clone

- 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어

- `git clone` 명령어를 사용하면 원격 저장소를 통째로 복제해 내컴퓨터로 옮기기 가능

- `git clone <원격 저장소 주소>`

  ```bash
  $ git clone https://github.com/edukyle/TIL.git
  
  Cloning into 'TIL'...
  remote: Enumerating objects: 3, done.
  remote: Counting objects: 100% (3/3), done.
  remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
  Receiving objects: 100% (3/3), done.
  ```

- git clone을 통해 생성된 로컬 저장소는 `git init`과 `git remote add`가 이미 수행되어 있음





### (2) git pull

- 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어

- `git pull <저장소 이름> <브랜치 이름>` 

  ```bash
  $ git pull origin master
  From <https://github.com/edukyle/git-practice>
   * branch            master     -> FETCH_HEAD
  Updating 6570ecb..56809a9
  Fast-forward
   README.md | 1 +
   1 file changed, 1 insertion(+)
  ```

- `git pull`만 작성하고 `<저장소 이름> <브랜치 이름>`은 생략해도 됨