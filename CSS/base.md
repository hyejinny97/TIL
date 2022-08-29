# ✔ CSS

> CSS 기본 구조

![CSS 기본 구조](https://poiemaweb.com/img/css-syntax.png)

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 (Property): 어떤 스타일 기능을 변경할지 결정
  - 값 (Value): 어떻게 스타일 기능을 변경할지 결정

> CSS 정의 방법

1. 인라인(inline) CSS 정의 
   
   ```html
   <body>
      <h1 style="color: blue; font-size: 100px;">Hello</h1>
   </body>
   ```

2. 내부(embedding) CSS 정의
   
   - `<style></style>` 태그 이용
   
   ```html
   <head>
      <style>
        h1 {
          color: black;
          font-size: 100px;
        }
      </style>
   </head>
   ```

3. 외부(link) CSS 정의
   - 분리된 CSS 파일의 링크를 연결

   ```css
   /* style.css 파일 */
   h1 {
      color: black;
      font-size: 100px;
   }
   ```

   ```html
   <!-- main.html 파일 -->
   <head>
      <link href="style.css" rel="stylesheet">
   </head>
   ```



# ✔ CSS 기초 선택자
> 요소 선택자
- HTML 태그를 직접 선택
- 기본형
  
  ```css
  태그명 {
    스타일 규칙
  }
  ```

- 예
  
  ```css
  p {
    font-style: italic;
  }
  ```

> 클래스 (class) 선택자  
- `.`문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 기본형
  
  ```css
  .클래스명 {
    스타일 규칙
  }
  ```

- 예
  
  ```css
  .accent {
    border: 1px solid #000;
  }
  ```

> 아이디 (id) 선택자
- `#`문자로 시작하며, 해당 아이디가 적용된 항목을 선택
- 일반적으로 하나의 문서에 1번만 사용
- 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장
- 기본형

  ```css
  #아이디명 {
    스타일 규칙
  }
  ```

- 예

  ```css
  #container {
    width: 500px;
  }
  ```