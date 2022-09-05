# ✔ body 태그

> `<body></body>` 태그 기본 구조

```html
<!-- body 태그 구조-->
<body>
  <h1>나의 첫번째 HTML</h1>
  <p>이것은 본문입니다.</p>
  <span>이것은 인라인요소</span>
  <a href="https://www.naver.com">네이버로 이동!!</a>
</body>
```

> 블록 레벨 요소 vs 인라인 레벨 요소

1. 블록 레벨 요소
   - h, p, hr, ul, ol, dl, blockquote, pre, div 등
2. 인라인 레벨 요소
   - br, b, strong, i, em, a, img, span 등

> body 태그 내 태그들 종류
- [텍스트 관련 태그](#-텍스트-관련-태그): h, p, hr, br, b, strong, i, em, blockquote, pre
- [목록 관련 태그](#-목록-관련-태그): ul, ol, dl
- [이미지 관련 태그](#-이미지-관련-태그): img
- [하이퍼링크 관련 태그](#-하이퍼링크-관련-태그): a
- [컨테이너 관련 태그](#-컨테이너-관련-태그): div, span
- [표 관련 태그](#-표-관련-태그): table, thead, tbody, tfoot, tr, th, td, caption
- [폼 관련 태그](#-폼-관련-태그): form, input, label



# ✔ 텍스트 관련 태그

> `<h></h>` 태그

- 제목 요소
- h1부터 h6까지 존재해 구조화된 계층 표현 가능

  ```html
  <body>
    <h1>The Crushing Bore</h1>
    <h2>Chapter 1: The dark night</h2>
    <h2>Chapter 2: The eternal silence</h2>
    <h3>The specter speaks</h3>
  </body>
  ```

> `<p></p>` 태그
   
- 텍스트 단락 요소 (paragraph)

  ```html
  <body>
    <p>It was a dark night. Somewhere, an owl hooted. The rain lashed down on the ...</p>
  </body>
  ```

> `<hr>` 태그
   
- 문단 레벨 요소에서의 주제의 분리를 의미하며, 수평선으로 표현됨 (A Horizontal Rule)


  ```html
  <body>
    <p>It was a dark night. Somewhere, an owl hooted. The rain lashed down on the ...</p>
    <hr>
    <p>Our protagonist could not so much as a whisper out of the shadowy figure ...</p>
  </body>
  ``` 

> `<br>` 태그
   
- 텍스트 내에 줄 바꿈 생성
  
  ```html
  <body>
    <p>It was a dark night. Somewhere, an owl hooted.<br>The rain lashed down on the ...</p>
  </body>
  ```

> `<b></b>` & `<strong></strong>` 태그

1. `<b></b>`
   
   - 굵은 글씨 요소
   - 의미가 있는 것이 아닌 표현에만 영향을 주는 요소
  
2. `<strong></strong>`
   
   - 중요한 텍스트를 **강조**하고자 하는 요소 
   - 브라우저에서는 기본적으로 굵은 텍스트로 스타일을 지정
   - 화면판독기에 인식되면 다른 톤의 목소리로 표현

   ```html
   <body>
     <p><b>Insert</b> a tomato slice and a leaf of lettuce between the slices of bread.</b>
     <p>I am counting on you. <strong>Do not</strong> be late!</p>
   </body>
   ```

> `<i></i>` & `<em></em>` 태그
   
1. `<i></i>`
   
   - 기울임 글씨 요소
   - 의미가 있는 것이 아닌 표현에만 영향을 주는 요소
  
2. `<em></em>`
   
   - 중요한 텍스트를 **강조**하고자 하는 요소
   - 브라우저에서는 기본적으로 이탤릭체로 스타일을 지정
   - 화면판독기에 인식되면 다른 톤의 목소리로 표현
  
   ```html
   <body>
     <p>The menu was a sea of exotic words like 
       <i lang="uk-latn">vatrushka</i> and <i lang="fr">soupe à l'oignon</i>.
     </p>
     <p>I am <em>glad</em> you weren't <em>late</em>.</p>
   </body>
   ```

> `<blockquote></blockquote>` 태그

- 인용구 표시 요소
- 브라우저 기본 스타일은 인용구를 표현할 때, 들여쓰기 된 단락으로 나타냄

- `<blockquote></blockquote>` 태그의 속성
  
  - `cite`: 출처를 표기
  
   ```html
   <body>
      <blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
        <p>The HTML Element indicates that the enclosed text is an extended quotation.</p>
      </blockquote>
   </body>
   ```

> `<pre></pre>` 태그
   
- 코드 블록 요소
- HTML에 작성한 내용을 그대로 표현해줌
  - 보통 고정폭 글꼴이 사용되고 공백문자를 유지해줌
   
- `<code></code>`: 일반적인 컴퓨터 코드를 표시

   ```html
   <body>
     <pre>
        택스트 내에서 들여 쓰기 또는 초과 공백을 사용하면 브라우저가 이를 무시하고 렌더링 된 페이지에 공백을 표시하지 않습니다.
        하지만 pre 태그로 텍스트를 감싸면 공백이 텍스트 편집기에서 보는 것과 동일하게 렌더링 됩니다.
        <code>
          var para = document.querySelector('p');

          para.onclick = function() {
            alert('Owww, stop poking me!');
          }
        </code>
     </pre>
   </body>
   ```



# ✔ 목록 관련 태그

> `<ul></ul>` 태그
   
- 순서가 없는 리스트 (unordered list)

  ```html
  <body>
    <ul>
      <li>milk</li>
      <li>eggs</li>
    </ul>
  </body>
  ```

> `<ol></ol>` 태그

- 순서가 있는 리스트 (ordered list)

  ```html
  <body>
    <ol>
      <li>milk</li>
      <li>eggs</li>
    </ol>
  </body>
  ```

> `<dl></dl>` 태그
   
- Description lists로서 용어 및 정의, 질문 및 답변과 같은 일련의 항목 및 관련 설명을 표시할 때 사용

- `<dt></dt>`: 용어, 질문과 같은 상위 항목을 나타내는 요소 (description term)

- `<dd></dd>`: 정의, 답변과 같은 하위 항목을 나타내는 요소 (description definition)

  ```html
  <body>
    <dl>
       <dt>HTML</dt>
       <dd>HTML은 웹 페이지 표시를 위해 개발된 지배적인 마크업 언어다.</dd>
       <dt>CSS</dt>
       <dd>CSS는 마크업 언어가 실제 표시되는 방법을 기술하는 style sheet language다.</dd>
    </dl>
  </body>
  ```



# ✔ 이미지 관련 태그

> `<img>` 태그

- 이미지 삽입 요소

- `<img>` 태그의 속성
       
  - `src`: 이미지 경로 지정 (필수)
  
  - `alt`: 대체 텍스트
    
    - 스크린 리더가 텍스트를 읽어 사용자에게 이미지 설명
    - 네트워크 오류, 콘텐츠 차단, 죽은 링크 등 이미지를 표시할 수 없는 경우 텍스트로 표시

   ```html
   <body>
      <img src="favicon144.png" alt="MDN logo">
   </body>
   ```



# ✔ 하이퍼링크 관련 태그

> `<a></a>` 태그

- href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성

- `<a></a>` 태그의 속성
     
  - `href`: 사이트의 주소가 포함된 링크
  
  - `title`: 링크에 대한 보충 정보로서, 링크에 마우스를 올렸을 때 정보가 나타남

  ```html
  <body>
    <a href="https://www.mozilla.org/en-US/"
      title="The best place to find more information about Mozilla's
        mission and how to contribute">the Mozilla homepage</a>
  </body>
  ```

- 문서 상단이 아닌 HTML 문서 내부의 특정 부분(Document fragments)에 링크 가능
  - 이를 위해, 우선 링크를 시키고 싶은 태그에 id 속성을 넣어 주어야함
  - 특정 id를 가진 태그에 연결하려면 URL 끝에 해시/파운드 기호를 포함하면 됨
  
   ```html
   <!-- contacts.html 파일 -->
   <body>
      <h2 id="Mailing_address">Mailing address</h2>
   </body>
 
   <!-- main.html 파일 -->
   <body>
      <p>Want to write us a letter? Use our <a href="contacts.html#Mailing_address">mailing address</a>.</p>
   </body>
   ```



# ✔ 컨테이너 관련 태그

> `<div></div>` 태그

- 의미 없는 블록 레벨 컨테이너
- CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않음
- 요소 여럿을 묶어 class나 id 속성으로 꾸미기 쉽도록 도움
- 문서의 특정 구역이 다른 언어임을 표시(lang 속성)하는 용도로 사용

  ```html
  <body>
     <div class="shadowbox">
        <p>Here's a very interesting note displayed in a lovely shadowed box.</p>
     </div>
  </body>
  ```

> `<span></span>` 태그
   
- 의미 없는 인라인 컨테이너
- CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않음
- class나 id 속성으로 꾸미기 쉽도록 도움
- 문서의 특정 구역이 다른 언어임을 표시(lang 속성)하는 용도로 사용
  
   ```html
   <body>
      <p><span>Some text</span></p>
   </body>
   ```



# ✔ 표 관련 태그

> `<table></table>` 태그

- `<thead></thead>`, `<tbody></tbody>`, `<tfoot></tfoot>`: table의 각 영역을 명시하기 위한 요소 (선택 사항)

- `<tr></tr>`: 가로 줄 구성

- `<th></th>`, `<td></td>`: 셀(데이터) 구성

- `<caption></caption>`: 표 설명 또는 제목
    
- `<th>`, `<td>` 태그의 속성
 
  - `colspan`: 열 병합
  
  - `rowspan`: 행 병합

   ```html
   <body>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Major</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>홍길동</td>
          <td>Computer Science</td>
        </tr>
        <tr>
          <td>2</td>
          <td>김철수</td>
          <td>Business</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td>총계</td>
          <td colspan="2">2명</td>
        </tr>
      </tfoot>
      <caption>1반 학생 명단</caption>
    </table>
   </body>
   ```



# ✔ 폼 관련 태그

> `<form></form>` 태그

- 정보(데이터)를 서버에 제출하기 위해 사용하는 태그

- `<form>` 태그의 속성
  
  - `action`: form을 처리할 서버의 URL (데이터를 보낼 곳)
  
  - `method`: form을 제출할 때 사용할 HTTP 메서드 (GET, POST 등)
  
  - `enctype`: method가 post인 경우 데이터의 유형
    
    - application/x-www-form-urlencoded: 기본값
    - multipart/form-data: 파일 전송시 (input type이 file이 경우)
  
   ```html
   <body>
      <form action="/search" method="GET">

      </form>
   </body>
   ```

> `<input>` 태그

- 다양한 타입을 가지는 입력 데이터 유형(type)과 위젯이 제공됨

- `<input>` 태그의 속성
  
  - `name`: form control에 적용되는 이름 (이름/값 pair로 서버에 전송됨)
  
  - `value`: form control에 적용되는 값 (이름/값 pair로 서버에 전송됨)
  
  - `type`: 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음
  
  - `required`, `readonly`, `autofocus`, `autocomplete`, `disabled` 등
  
   ```html
   <body>
      <form action="/search" method="GET">
        <input type="text" name="q">
      </form>
   </body>
   ```

- 구글 검색 창에 'HTML'단어를 넣고 submit하면, `https://www.google.com/search?q=HTML`형태로 URL이 바뀌는 것을 확인할 수 있음

- `<input>` 태그의 `type` 속성의 속성값
  
  - `text`: 일반 텍스트 입력
  
  - `password`: 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  
  - `email`: 이메일 형식이 아닌 경우 form 제출 불가
  
  - `number`: min, max, step 속성을 활용하여 숫자 번위 설정 가능
  
  - `file`: accept 속성을 활용하여 파일 타입 지정 가능
  
  - `checkbox`: 다중 선택 
  
  - `radio`: 단일 선택
  
  - `color`: color picker
  
  - `date`: date picker
  
  - `hidden`: 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정

   ```html
   <body>
      <form action="">
        <!-- text type & autofocus -->
        <label for="username">아이디</label>
        <input type="text" name="username" id="username" autofocus>

        <!-- text type & disabled -->
        <label for="name">이름</label>
        <input type="text" name="name" id="name" value="홍길동" disabled>

        <!-- submit type & 제출 버튼 -->
        <input type="submit" value="제출">
      </form>
   </body>
   ```

- `type` 속성의 속성값 중 `checkbox`, `radio`
  
  - 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
  
  - 동일 항목에 대하여는 동일한 `name` 속성을 지정하고, 선택된 항목에 대한 `value` 속성을 지정해야 함

   ```html
   <body>
      <form action="">
        <!-- ckeckbox -->
        <p>checkbox</p>
        <input type="checkbox" name="language" id="html" value="html">
        <label for="html">HTML</label>
        <input type="checkbox" name="language" id="python" value="python">
        <label for="python">python</label>
        <input type="checkbox" name="language" id="java" value="java">
        <label for="java">java</label>

        <!-- radio button -->
        <p>radio button</p>
        <input type="radio" name="feeling" id="happy" value="happy">
        <label for="happy">행복</label>
        <input type="radio" name="feeling" id="sad" value="sad">
        <label for="sad">슬픔</label>
        <input type="radio" name="feeling" id="soso" value="soso">
        <label for="soso">중립</label>
      </form>
   </body>
   ```

> `<label></label>` 태그

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용할 수 있음
  - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함

- `<input>` 태그에 `id` 속성을, `<label></label>` 태그에 `for` 속성을 활용하여 상호 연관 시킴

   ```html
   <label for="login-password">비밀번호</label>
   <input type="password" name="password" id="login-password">
   ```