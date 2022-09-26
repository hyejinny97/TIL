# ✔ Sending form data (Client)
> Sending and Retrieving form data
- HTML form element를 통해 데이터를 보내고 가져오기
- 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있음

> HTML `<form></form>` 요소

- 데이터가 전송되는 방법을 정의
  - “데이터를 어디(action)로 어떤 방식(method)으로 보낼지”
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당

1. `action` 속성

   - 입력 데이터가 전송될 URL을 지정
   - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함
   - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

2. `method` 속성

   - 데이터를 어떻게 보낼 것인지 정의
   - 입력 데이터의 HTTP request methods를 지정
   - HTML form 데이터는 오직 2가지 방법으로만 전송 할 수 있음 (GET, POST 방식)

> HTML `<input>` 요소

- 사용자로부터 데이터를 입력 받기 위해 사용

1. `type` 속성

   - input 요소의 동작 방식은 type 특성에 따라 현격히 달라짐
   - type을 지정하지 않은 경우, 기본값은 'text'

2. `name` 속성
  
   - form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
   - GET/POST 방식으로 서버에 전달하는 파라미터(name은 키, value는 값)로 매핑
     - GET 방식에서는 URL형식으로 데이터를 전달 
     - Query String Parameters: `?key=value&key=value/`

   ```html
   <!-- articles/templates/throw.html -->
   
   {% extends 'base.html' %}
 
   {% block content %}
    <h1>Throw</h1>
     <form action="/catch/" method="GET">
       <label for="message">Throw</label>
       <input type="text" id="message" name="message">
       <input type="submit">
     </form>
   {% endblock %}
   ```

> HTTP request methods
- HTTP: HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
- HTTP Method 종류: `GET`, `POST`, `PUT`, `DELETE`

1. GET
   
   - 서버로부터 정보를 조회하는 데 사용
   - 즉, 서버에게 리소스를 요청하기 위해 사용
   - 데이터를 가져올 때만 사용해야 함
   - 데이터를 서버로 전송할 때 URL에 포함되어 Query String Parameters를 통해 전송

> Query String Parameters
- 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
- 이러한 문자열은 앰퍼샌드(&)로 연결된 `key=value` 쌍으로 구성되며 기본 URL과 물음표(?)로 구분됨
  
  - 예) `http://127.0.0.1:8000/catch/?message=데이터`
  
  - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
  - `key=value`로 필요한 파라미터의 값을 적음
  - 파라미터가 여러 개일 경우 `&`를 붙여 여러 개의 파라미터를 넘길 수 있음





# ✔ Retrieving form data (Server)
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 됨
- 모든 요청 데이터는 view 함수의 첫번째 인자 **request**에 들어있음

> Request 객체 / Response 객체

- 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
- 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
- 마지막으로 view 함수는 HttpResponse object를 반환
  
  ```python
  # articles/views.py

  def catch(request):
    print(request)
    # <WSGIRequest: GET '/catch/?message=%EB%8D%B0%EC%9D%B4%ED%84%B0%21'>

    print(type(request))
    # <class 'django.core.handlers.wsgi.WSGIRequest'>

    print(request.GET)
    # <QueryDict: {'message': ['데이터']}>

    print(request.GET.get('message'))
    # '데이터'

    message = request.GET.get('message')
    context = {
    'message': message,
    }

    return render(request, 'catch.html', context)
  ```

  ```html
  <!-- articles/templates/catch.html -->

  {% extends 'base.html' %}

  {% block content %}
    <h1>Catch</h1>
    <h2>여기서 {{ message }}를 받았어!!</h2>
  {% endblock %}
  ```
