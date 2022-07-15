# ✔ 파일 객체 불러오기
> open(), close()
```python
# 파일 객체를 불러옴
f = open('파일명', mode='r', encoding='utf-8')

# 파일 작업 수행 후, 파일 객체를 닫음
f.close()
```
- file object를 반환
- 두번째 인자(mode): 파일이 사용될 방식 지정
  - `'r'`(read): 파일을 읽음
  - `'w'`(write): 파일을 씀 (덮어씀)
  - `'a'`(append): 파일에 덧붙이려함 (파일에 기록되는 모든 데이터는 자동으로 끝에 붙음)
  - `'r+'`: 파일을 읽고 씀

> with open()
```python
with open('파일명', mode='r', encoding='utf-8') as f:
  # 작업 수행
```
- with 키워드를 사용하면 따로 `.close()`를 통해 파일 객체를 닫지 않아도 됨
- 작업 수행 도중 예외가 발생하더라도 파일이 자동으로 닫힘 



# ✔ 파일 객체의 methods
> 파일 읽기
- `파일명.read([size])`
  ```python
  f.read()
  ```
  - **size 만큼**의 데이터를 읽고 문자열을 반환
  - size를 지정하지 않거나 음수로 지정하면, 파일의 내용 **전체**를 읽어서 반환
  - 문자열 끝에 개행문자(`\n`)가 포함된 문자열을 반환
  - 파일의 끝에 도달하면, 빈 문자열('')을 반환
- `파일명.readline()`
  ```python
  f.readline()
  ```
  - 파일에서 **한 줄**만 읽어서 반환
  - 문자열 끝에 개행문자(`\n`)가 포함된 문자열을 반환
  - 파일의 끝에 도달하면, 빈 문자열('')을 반환
- `파일명.readlines()` 또는 `list(파일명)`
  ```python
  f.readlines()
  list(f)
  ```
  - 파일의 **모든 줄**을 읽어 리스트로 반환
  - 문자열 끝에 개행문자(`\n`)가 포함
- `for` 반복문 이용
  ```python
  for line in f:
    print(line, end='')
  ```
  - 파일에서 한 줄씩 꿑까지 읽어서 반환 
  - 문자열 끝에 개행문자(`\n`)가 포함

> 파일 쓰기
- `파일명.write([문자열])`
  ```python
  f.write('string here\n')
  # 12
  ```
  - 문자열을 파일에 쓰고, 출력된 문자들의 갯수를 반환
  - string type이 아닌 다른 데이터타입들은 인자로 넘겨줄 수 없음



# ✔ JSON (JavaScript Object Notation)
- JSON은 프로그래밍 언어의 데이터 타입으로 데이터 교환이 가능한 텍스트 포맷임
- `파일명.json`
- 사람이 데이터를 읽고 쓰기 쉽게 해줌
- 컴퓨터가 데이터를 파싱하고 생성하기 쉽게 해줌
  ```json
  {
     "이름": "홍길동", 
     "나이": 25, 
     "특기": ["농구", "도술"],
      "가족관계": {"아버지": "홍판서", "어머니": "춘섬"}, 
     "결혼 여부": true 
  }
  ```

> json 표준 모듈
- JSON 데이터를 쉽게 처리하고자 사용하는 모듈
- `json.dump(파이썬 객체, 파일 객체)`
  ```python
  import json

   data = {'name': '홍길동', 'birth': '0525', 'age': 30}
   with open('myinfo.json', 'w') as f:
      json.dump(data, f)
  ```
  - 직렬화 (serializing): 파이썬 객체 -> JSON 파일
  - 파이썬 데이터 객체를 받아서 JSON 텍스트 파일로 변환해줌
- `json.load(파일 객체)`
  ```python
  import json

  with open('myinfo.json') as f:
    data = json.load(f)
  
  print(type(data))
  # <class 'dict'>
  print(data)
  # {'name': '홍길동', 'birth': '0525', 'age': 30}
  ```
  - 역 직렬화 (deserializing): JSON 파일 -> 파이썬 객체
  - JSON 텍스트 파일을 파이썬의 데이터 객체로 변환해 줌
- `json.dumps(파이썬 객체)`
  ```python
   import json
   
   d = {"name":"홍길동", "birth":"0525", "age": 30}
   json_data = json.dumps(d)
   print(json_data)
   # '{"name": "\\ud64d\\uae38\\ub3d9", "birth": "0525", "age": 30}'
   ```
  - 직렬화 (serializing): 파이썬 객체 -> JSON 문자열
  - dumps() 함수는 기본적으로 데이터를 아스키 형태로 저장하기 때문에 한글 문자열이 마치 깨진 것처럼 보임
    ```python
     # 아스티 형태의 문자열로 변경되는 것을 방지하는 방법
     json_data = json.dumps(d, ensure_ascii=False)
     print(json_data)
     # '{"name": "홍길동", "birth": "0525", "age": 30}'
     ```
- `json.loads(JSON 문자열)`
  ```python
  json.loads(json_data)
  # {'name': '홍길동', 'birth': '0525', 'age': 30}
  ```
  - 역 직렬화 (deserializing): JSON 문자열 -> 파이썬 객체
