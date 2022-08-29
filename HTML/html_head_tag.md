# ✔ html 태그 

> `<html></html>` 태그 기본 구조

```html
<!-- html 태그 구조 -->
<html lang="en">
</html>
```

- 문서의 기본 언어 설정 (한국어의 경우, lang="ko")


# ✔ head 태그

> `<head></head>` 태그 기본 구조

```html
<!-- head 태그 구조 -->
<head>
  <title>HTML 학습</title>
  <meta charset="UTF-8">
  <link href="style.css" rel="stylesheet">
  <script src="javascript.js"></script>
  <style>
    p {
    color: black;
    }
  </style>
</head>
```

> `<title></title>` 태그
   
- HTML문서 전체의 타이틀
- 브라우저 상단 탭의 타이틀
    
  ```html
  <head>
    <title>HTML 학습</title>
  </head>
  ```

> `<meta>` 태그
   
- 문서 레벨 메타데이터 요소
  - 문서의 인코딩(character set) 특정
  - 저자(name)와 설명(content) 추가

- Open Graph Data
  
  - 메타 데이터를 표현하는 새로운 규약
  - Facebook이 웹 사이트에 더 풍부한 메타 데이터를 제공하기 위해 발명한 메타 데이터 프로토콜
  - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
  - 참고자료: [Open Graph Data](https://ogp.me/)
  
  ```html
  <head>
    <meta charset="UTF-8">
    <meta name="author" content="HJ Yun">
    <meta name="description" content="I learned HTML">
    <meta property="og:title" content="The Rock" />
    <meta property="og:type" content="video.movie" />
    <meta property="og:url" content="https://www.imdb.com/title/tt0117500/" />
    <meta property="og:image" content="https://ia.media-imdb.com/images/rock.jpg" />
  </head>
  ```

    ![Open Graph Data을 설명하는 이미지](https://miro.medium.com/max/1400/1*PHdFEeCVNiPYUFC3IX45MA.png)

> `<link>` 태그
   
- 외부 리소스 (CSS 파일, favicon 등) 연결 요소

  ```html
  <head>
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  </head>
  ```

> `<script></script>` 태그
   
- 스크립트 요소 (JavaScript 파일/코드)

  ```html
  <head>
    <script src="javascript.js"></script>
  </head>
  ```

> `<style></style>` 태그
   
- CSS 직접 작성

  ```html
  <head>
    <style>
     p {
     color: black;
     }
    </style>
  </head>
  ```