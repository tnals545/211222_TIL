# CLI

1. GUI와 CLI 정의

- GUI : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
- CLI : 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식



2. 경로
   1. 루트 디렉토리(Root Directory, **`/` **)
      - 모든 파일과 폴더를 담고 있는 최상위 폴더(Windows의 경우 `C드라이브` 의미)
   2. 홈 디렉토리(Home Directory, **`~`** )
      - 사용자의 홈 폴더를 의미
      - Windows의 경우 `C:/사용자(Users)/현재 사용자 계정`
      - Mac의 경우 `/Users/현재 사용자 계정`을 의미



3. 절대 경로와 상대 경로

   1. 절대 경로 : 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
      - 윈도우 바탕 화면의 절대 경로 `C:/Users/kyle/Desktop`
   2. 상대 경로 : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
      - 현재 작업하고 있는 디렉토리가 `C:/Users` 라고 한다면 윈도우 바탕 화면으로의 상대 경로는 `kyle/Desktop` 
      - `./` : 현재 작업하고 있는 폴더
      - `../` : 현재 작업하고 있는 폴더의 부모 폴더

   

4. 터미널 명령어

- `touch` : 파일을 생성하는 명령어

```bash
$ touch text.txt
```



- `mkdir (make directory)` : 새 폴더를 생성하는 명령어

```bash
$ mkdir folder
$ mkdir 'happy hacking'
```



- `ls (list segments)` : 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어 

```bash
# 기본 사용
$ ls 

# all 옵션
$ ls -a

# all, long 옵션 함께 적용
$ ls -a -l

# 여러 옵션 축약 가능
$ ls -al
```



- `mv(move)`: 폴더/파일을 다른 폴더 내로 이동하거나 이름을 변경하는 명령어

```bash
# text.txt를 folder 폴더 안에 넣을 때
$ mv text.txt folder

# text1.txt의 이름을 text2.txt로 바꿀 때
$ mv text1.txt text2.txt
```



- `cd(change directory)`: 현재 작업중인 디렉토리를 변경하는 명령어

```bash
# 현재 작업 중인 디렉토리에 있는 folder 폴더로 이동
$ cd folder

# 절대 경로를 통한 디렉토리 변경
$ cd C:/Users/kyle/Desktop

# 상대 경로를 통한 디렉토리 변경
$ cd ../parent/child
```



- `rm(remove)`: 폴더/파일을 지우는 명령어

```bash
$ rm test.txt
$ rm -r folder
```



- `start, open`: 폴더/파일 여는 명령어(start : Windows, open : Mac)

```bash
# Windows
$ start test.txt

# Mac
$ open test.txt
```



5. 유용한 단축키

- `위, 아래 방향키` : 과거에 작성했던 명령어 조회
- `tab` : 폴더/파일 이름 자동 완성
- `ctrl + a` : 커서가 맨 앞으로 이동
- `ctrl + e` : 커서가 맨 뒤로 이동
- `ctrl + w` : 커서가 앞 단어를 삭제
- `ctrl + l` : 터미널 화면을 깨끗하게 청소 (스크롤 올리면 과거 내역 조회 가능)
- `ctrl + insert` : 복사
- `shift + insert` : 붙여넣기





# 마크다운

제목

# 제목 1

## 제목 2

### 제목 3

#### 제목 4

##### 제목 5

###### 제목 6



목록

순서가 없는 목록

- 목록 1

- 목록 2
- 목록 3
- 과일
  - 수박
  - 참외
  - 바나나
    - 바나나1
    - 바나나2



순서가 있는 목록

1. 목록 1
2. 목록 2
   1. 목록 2-1
   2. 목록 2-2
      1. 목록 2-2-1
      2. 목록 2-2-2

---

(수평선 : (---,***,___)중에 하나 고르고 + 엔터)



강조(스타일링)

1. 기울임(이탤릭체) : *글자*(* *), _글자_(_ _)
2. 굵게(볼드체) : **글자**(** **), __글자__(__ __)
3. 취소선 : ~~글자~~(~~ ~~)

---

코드

인라인 코드 (=한줄)

파이썬에는 `print("Hello World!")`(``) 라고 쓸 수 있습니다.



블록 코드 (=여러줄)

```python
for i in range(10):
	print(i)
```

---

표(table) - 오른쪽마우스 -> 삽입 -> 표

| 동물   | 다리개수 | 종     |
| ------ | -------- | ------ |
| 사자   | 4개      | 포유류 |
| 원숭이 | 2개      | 포유류 |
| 앵무새 | 2개      | 조류   |

행 추가 : ctrl + 엔터

행 삭제 : ctrl + shift + backspace

문자열 이스케이프(\\\\)

\`print()\`

