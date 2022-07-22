# ✔ API (Application Programming Interface)
- 컴퓨터나 컴퓨터 프로그램 사이의 연결
- 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공
- API 명세(specification): 사용하는 방법을 기술하는 문서나 표준
  - ex) [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)
  - ex) [Naver Developers](https://developers.naver.com/main/)
  - ex) [kakao developers](https://developers.kakao.com/docs)
- 주소(URL)로 요청(request)을 하면, 문서(JSON 등)로 응답(response)해 줌




 
# ✔ Requests 라이브러리
- 파이썬을 위한 HTTP 라이브러리
- requests 메서드를 호출하면 response 객체를 반환해 줌

> Requests 모듈의 메서드
1. `get(url)`
   
   ```python
   import requests
   response = requests.get('https://api.github.com/events')
   ```

2. `post(url, data)`
   
   ```python
   import requests
   response = requests.post('https://httpbin.org/post', data={'key': 'value'})
   ```

3. `put(url, data)`
   
   ```python
   import requests
   response = requests.put('https://httpbin.org/put', data={'key': 'value'})
   ```

4. `delete(url)`
   
   ```python
   import requests
   response = requests.put('https://httpbin.org/delete')
   ```

> URL에서 Parameters 파싱
- URL에서 `?` 뒤에 key와 value쌍으로 데이터가 주어짐 (ex) httpbin.org/get?key=val)
- request할때 `params`라는 keyword argument를 통해서 딕셔너리 형태의 required/optional 인자값들을 같이 전달해줄 수 있음

```python
import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
```

> JSON response
```python
import requests
r = requests.get('https://api.github.com/events')
r.json()
```