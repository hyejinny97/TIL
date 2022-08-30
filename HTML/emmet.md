# ✔ Emmet Syntax
- 자동완성 기능으로  HTML/CSS의 작업 속도를 향상시킬 수 있음
- visual studio code에서는 별다른 설정 없이 바로 사용 가능

> Child `>`
- 자식 태그

  ```html
  <!-- nav>ul>li -->
  <nav>
    <ul>
      <li></li>
    </ul>
  </nav>
  ```

> Sibling `+`
- 자매 태그

  ```html
  <!-- div+p+bq -->
  <div></div>
  <p></p>
  <blockquote></blockquote>
  ```

> Climb-up `^`
- 종속을 벗어나 상위 레벨과 자매 태그 형성
  
  ```html
  <!-- div+div>p>span+em^bq -->
  <div></div>
  <div>
      <p><span></span><em></em></p>
      <blockquote></blockquote>
  </div>
  ```

  ```html
  <!-- div+div>p>span+em^^bq -->
  <div></div>
  <div>
      <p><span></span><em></em></p>
  </div>
  <blockquote></blockquote>
  ```

> Multiplication `*`
- 여러 태그를 동시에 입력 가능

  ```html
  <!-- ul>li*5 -->
  <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>
  ```

> Grouping `()`
- 여러 태그들을 한 그룹으로 묶어 구분해줌
  
  ```html
  <!-- div>(header>ul>li*2>a)+footer>p -->
  <div>
    <header>
       <ul>
          <li><a href=""></a></li>
          <li><a href=""></a></li>
       </ul>
    </header>
    <footer>
        <p></p>
    </footer>
  </div>
  ```

  ```html
  <!-- (div>dl>(dt+dd)*3)+footer>p -->
  <div>
    <dl>
       <dt></dt>
       <dd></dd>
       <dt></dt>
       <dd></dd>
       <dt></dt>
       <dd></dd>
    </dl>
  </div>
  <footer>
    <p></p>
  </footer>
  ```

> ID `#` and CLASS attributes `.`
- id 속성, class 속성을 포함한 태그

  ```html
  <!-- #header -->
  <div id="header"></div>
  ```

  ```html
  <!-- .title -->
  <div class="title"></div>
  ```

  ```html
  <!-- form#search.wide -->
  <form id="search" class="wide"></form>
  ```

  ```html
  <!-- p.class1.class2.class3 -->
  <p class="class1 class2 class3"></p>
  ```

> Custom attributes `[]`
- 특정 속성과 속성값을 포함한 태그

  ```html
  <!-- p[title="Hello world"] -->
  <p title="Hello world"></p>
  ```

  ```html
  <!-- td[rowspan=2 colspan=3 title] -->
  <td rowspan="2" colspan="3" title=""></td>
  ```

  ```html
  <!-- [a='value1' b="value2"] -->
  <div a="value1" b="value2"></div>
  ```

> Text `{}`
- {}안에 적은 텍스트는 태그 사이의 content가 됨

  ```html
  <!-- a{Click me} -->
  <a href="">Click me</a>
  ```
  
  ```html
  <!-- p>{Click }+a{here}+{ to continue} -->
  <p>Click <a href="">here</a> to continue</p>
  ```

> Item numbering `$`
- 연속되는 태그의 값(속성값, 텍스트)에 숫자를 순서대로 입력
- $ 앞에 있는 숫자를 하나씩 증가시킴

  ```html
  <!-- ul>li.item$*5 -->
  <ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
  </ul>
  ```

  ```html
  <!-- h$[title=item$]{Header $}*3 -->
  <h1 title="item1">Header 1</h1>
  <h2 title="item2">Header 2</h2>
  <h3 title="item3">Header 3</h3>
  ```

  ```html
  <!-- ul>li.item$$$*5 -->
  <ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
    <li class="item004"></li>
    <li class="item005"></li>
  </ul>
  ```

  ```html
  <!-- ul>li.item$@-*5 -->
  <ul>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
  </ul>
  ```

  ```html
  <!-- ul>li.item$@3*5 -->
  <ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
  </ul> 
  ```