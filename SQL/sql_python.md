# ✔ SQL과 파이썬 연결

## 1️⃣ 파이썬 개발 환경 준비

- 파이썬을 MySQL과 연동하기 위해서는 PyMySQL 라이브러리가 필요함

### 파이썬 소개

- 장점
  - 무료로 강력한 기능을 사용할 수 있음
  - 설치와 사용 환경 구축이 쉬움
  - 다양하고 강력한 외부 라이브러리들이 많음

### 파이썬 사용 방법

#### 대화형 모드: 한 줄씩 실행하기

- 파이썬은 IDLE라는 환경에서 코드를 실행함
- 기본적으로 한 줄을 입력하고 엔터키를 누르면 바로 실행되는데, 이러한 방식을 대화형 모드라고 함
- 파이썬은 인터프리터 언어(스크립트 언어)이기에 한 줄을 입력하면 즉시 실행됨
- 대화형 모드에서는 print()를 사용하지 않아도 바로 결과가 출력됨

#### 스크립트 모드: 여러 줄을 한 번에 실행하기

- 여러 줄을 코딩한 후에 한 번에 실행할 수도 있는데, 이러한 방식을 스크립트 모드라고 함

##### cf) 컴파일 언어와 스크립트 언어

- 컴파일 언어: 소스 코드를 실행 가능한 기계어로 일괄 번역한 후에 번역이 완료된 파일(\*.exe, \*.class 등의 파일)이 실행되는 언어
  - ex) C, C++, 자바
- 스크립트 언어(인터프리터 언어): 소스 코드를 한 줄씩 읽어 바로 실행되는 언어
  - ex) 파이썬, 자바스크립트

## 2️⃣ 파이썬과 MySQL의 연동

- 파이썬과 MySQL 데이터베이스를 연동하면 MySQL 워크벤치 없이도 MySQL에 접근하고 사용할 수 있음

### 파이썬에서 데이터 입력

1. 먼저 `pymysql.connect()`로 데이터베이스와 연결(연동)해야함

   ```py
   pymysql.connect(host=서버IP주소, user=사용자, password=암호, db=데이터베이스, charset=문자세트)
   ```

   ```py
   import pymysql

   conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
   ```

2. 커서(cursor)를 생성

   - 커서: 데이터베이스에 SQL 문을 실행하거나 실행된 결과를 돌려받는 통로

   ```py
   cur = conn.cursor()
   ```

3. `커서_이름.execute()` 함수를 사용해 테이블 생성

   - `커서_이름.execute(SQL 문)`: SQL 문이 연결된 데이터베이스에 실행됨

   ```py
   cur.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)")
   ```

4. `커서_이름.execute()` 함수를 사용해 데이터를 입력

   ```py
   cur.execute("INSERT INTO userTable VALUES('hong', '홍지윤', 'hong@naver.com', 1996)")
   ```

5. 앞에서 입력한 데이터는 임시 저장된 상태로 아직 데이터베이스에 완전히 저장되지 않음. 커밋(commit)을 통해 입력한 데이터를 확실하게 저장할 수 있음

   ```py
   conn.commit()
   ```

6. `커서_이름.close()` 함수를 통해 연결한 데이터베이스를 닫을 수 있음

   ```py
   conn.close()
   ```

### 파이썬에서 데이터 조회

1. 먼저 `pymysql.connect()`로 데이터베이스와 연결(연동)함

   ```py
   import pymysql

   conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
   ```

2. 커서(cursor) 생성

   ```py
   cur = conn.cursor()
   ```

3. `커서_이름.execute()` 함수를 사용해 테이블 조회

   - SELECT로 조회한 결과는 커서에 한꺼번에 저장됨

   ```py
   cur.execute("SELECT * FROM userTable")
   ```

4. `커서_이름.fetchone()`을 통해 한 행씩 접근하거나, `커서_이름.fetchall()`을 통해 모든 행에 한꺼번에 접근할 수 있음

   - `fetchone()`로 반환된 행은 튜플 형식으로 구성됨
   - 더이상 조회한 결과가 없으면 None 값을 반환함

   ```py
   row = cur.fetchone()
   rows = cur.fetchall()
   ```

   ```py
   while (True):
    row = cur.fetchone()
    if row == None:
      break
   ```

5. `커서_이름.close()`를 통해 데이터베이스 연결 종료

   ```py
   conn.close()
   ```

## 3️⃣ GUI 응용 프로그램

- GUI: 윈도에 그래픽 환경으로 제공되는 화면
- GUI 응용 프로그램을 작성하면 일반 사용자는 마우스만으로 데이터베이스에 쉽게 접근할 수 있음
- tkinter 라이브러리: 파이썬에서 GUI 관련 모듈을 제공해주는 표준 윈도 라이브러리

### GUI 기본 프로그래밍

#### 기본 윈도의 구성

```py
from tkinter import *

root = Tk()
# 이 부분에 화면을 구성하고 처리하는 코드 추가
root.mainloop()
```

- `Tk()`는 기본이 되는 윈도를 반환함
- `root.mainloop()` 함수: 윈도에 키보드 누르기, 마우스 클릭 등의 다양한 작업이 일어날 때 이벤트를 처리해줌

#### 윈도 제목 및 크기 설정

```py
root = Tk()

root.title("혼공 GUI 연습")
root.geometry("400x200")

root.mainloop()
```

#### 라벨

```py
root = Tk()

label1 = Label(root, text="혼공 SQL은")
label2 = Label(root, text="쉽습니다.", font=("궁서체", 30), bg="blue", fg="yellow")

label1.pack()
label2.pack()

root.mainloop()
```

- 라벨(label): 문자를 표현할 수 있는 위젯
- 위젯(widget): 윈도에 나오는 버튼, 텍스트, 라디오 버튼, 이미지 등을 통합해서 지칭하는 용어
- 모든 위젯들은 `pack()` 함수를 사용해야 화면에 나타남

#### 버튼

```py
def clickButton():
  messagebox.showinfo('버튼 클릭', '버튼을 눌렀습니다..')

root = Tk()

button1 = Button(root, text="여기를 클릭하세요", fg="red", bg="yellow", command=clickButton)
button1.pack(expand=1)

root.mainloop()
```

- 버튼: 마우스로 클릭하면 지정한 작업이 실행되도록 사용되는 위젯
- `command` 옵션으로 사용하자 버튼을 눌렀을 때 지정한 작업을 처리함
- pack 함수에 expand=1 옵션을 넣으면 화면 중앙에 나타남

#### 위젯의 정렬

```py
root = Tk()

button1 = Button(root, text="혼공1")
button2 = Button(root, text="혼공2")
button3 = Button(root, text="혼공3")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

root.mainloop()
```

- pack 함수에 side=LEFT(또는 side=RIGHT)옵션을 넣으면 왼쪽부터(또는 오른쪽부터) 정렬됨
- pack 함수에 side=TOP(또는 side=BOTTOM)옵션을 넣으면 위쪽부터(또는 아래쪽부터) 정렬됨

#### 위젯 사이에 여백 추가

```py
root = Tk()

button1 = Button(root, text="혼공1")
button2 = Button(root, text="혼공2")
button3 = Button(root, text="혼공3")

button1.pack(side=TOPm fill=X, padx=10, pady=10)
button2.pack(side=TOPm fill=X, padx=10, pady=10)
button3.pack(side=TOPm fill=X, padx=10, pady=10)

root.mainloop()
```

- pack 함수에 padx=픽셀값(또는 pady=픽셀값) 옵션을 넣으면 x축(또는 y축)에 패딩을 줄 수 있음

#### 프레임, 엔트리, 리스트 박스

```py
root = Tk()

upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width=10)
editBox.pack(padx=20, pady=20)

listbox = ListBox(downFrame, bg='yellow')
listbox.pack()

listbox.insert(END, "하나")
listbox.insert(END, "둘")
listbox.insert(END, "셋")

root.mainloop()
```

- 프레임(frame): 화면을 여러 구역으로 나눌 때 사용
- 엔트리(entry): 입력 상자를 표현
- 리스트박스(listbox): 목록을 표현
  - END 옵션: 데이터를 제일 뒤에 첨부해줌
