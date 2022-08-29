# ✔ body 태그

```html
<!-- body 태그 구조-->
<body>
  <h1>나의 첫번째 HTML</h1>
  <p>이것은 본문입니다.</p>
  <span>이것은 인라인요소</span>
  <a href="https://www.naver.com">네이버로 이동!!</a>
</body>
```

> 블록 레벨 요소

1. `<h></h>`

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

2. `<p></p>`
   
   - 텍스트 단락 요소 (paragraph)

   ```html
   <body>
     <p>It was a dark night. Somewhere, an owl hooted. The rain lashed down on the ...</p>
   </body>
   ```

3. `<hr>`
   
   - 문단 레벨 요소에서의 주제의 분리를 의미하며, 수평선으로 표현됨 (A Horizontal Rule)


   ```html
   <body>
      <p>It was a dark night. Somewhere, an owl hooted. The rain lashed down on the ...</p>
      <hr>
      <p>Our protagonist could not so much as a whisper out of the shadowy figure ...</p>
   </body>
   ``` 

4. `<ul></ul>`
   
   - 순서가 없는 리스트 (unordered list)

    ```html
    <body>
      <ul>
        <li>milk</li>
        <li>eggs</li>
      </ul>
    </body>
    ```

5. `<ol></ol>`
   - 순서가 있는 리스트 (ordered list)

    ```html
    <body>
      <ol>
        <li>milk</li>
        <li>eggs</li>
      </ol>
    </body>
    ```

6. `<dl></dl>`
   
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

7. `<blockquote></blockquote>`

   - 인용구 표시 요소
   - 브라우저 기본 스타일은 인용구를 표현할 때, 들여쓰기 된 단락으로 나타냄
   - 속성
     - `cite`: 출처를 표기
  
   ```html
   <body>
      <blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
        <p>The HTML Element indicates that the enclosed text is an extended quotation.</p>
      </blockquote>
   </body>
   ```

8. `<pre></pre>`
   
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

9. `<div></div>`

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

> 인라인 레벨 요소

1. `<br>`
   
   - 텍스트 내에 줄 바꿈 생성
  
   ```html
   <body>
     <p>It was a dark night. Somewhere, an owl hooted.<br>The rain lashed down on the ...</p>
   </body>
   ```

2. `<b></b>` & `<strong></strong>`

   - `<b></b>`: 굵은 글씨 요소
     - 의미가 있는 것이 아닌 표현에만 영향을 주는 요소
  
   - `<strong></strong>`: 중요한 텍스트를 **강조**하고자 하는 요소 
     - 브라우저에서는 기본적으로 굵은 텍스트로 스타일을 지정
     - 화면판독기에 인식되면 다른 톤의 목소리로 표현

   ```html
   <body>
     <p><b>Insert</b> a tomato slice and a leaf of lettuce between the slices of bread.</b>
     <p>I am counting on you. <strong>Do not</strong> be late!</p>
   </body>
   ```

3. `<i></i>` & `<em></em>`
   
   - `<i></i>`: 기울임 글씨 요소
     - 의미가 있는 것이 아닌 표현에만 영향을 주는 요소
  
   - `<em></em>`: 중요한 텍스트를 **강조**하고자 하는 요소
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

4. `<a></a>`

   - href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
   - 속성
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

5. `<img>`

   - 이미지 삽입 요소
   - 속성
     - `src`: 이미지 경로 지정 (필수)
     - `alt`: 대체 텍스트
       - 스크린 리더가 텍스트를 읽어 사용자에게 이미지 설명
       - 네트워크 오류, 콘텐츠 차단, 죽은 링크 등 이미지를 표시할 수 없는 경우 텍스트로 표시

   ```html
   <body>
      <img src="favicon144.png" alt="MDN logo">
   </body>
   ```

6. `<span></span>`
   
   - 의미 없는 인라인 컨테이너
   - CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않음
   - class나 id 속성으로 꾸미기 쉽도록 도움
   - 문서의 특정 구역이 다른 언어임을 표시(lang 속성)하는 용도로 사용
  
   ```html
   <body>
      <p><span>Some text</span></p>
   </body>
   ```