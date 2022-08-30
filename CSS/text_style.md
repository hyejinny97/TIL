# ✔ CSS 상속
- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속할 수 있음
- 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있음

> 상속되는 요소
- 텍스트 관련 요소
  - font, color, text-align 등
- opacity, visibility 등

> 상속되지 않는 요소
- Box model 관련 요소
  - width, height, margin, padding, border, box-sizing, display 등
- position 관련 요소
  - position, top/right/bottom/left, z-index 등




# ✔ CSS 기본 스타일
> 기본 스타일 종류
- [글꼴 관련 스타일](#-글꼴-관련-스타일)
  - font-family
  - font-size
  - font-style
  - font-weight
- [텍스트 관련 스타일](#-텍스트-관련-스타일)
  - color
  - text-align
  - line-height
  - text-decoration
  - text-shadow
  - text-transform
  - letter-spacing
  - word-spacing



# ✔ 글꼴 관련 스타일

> font-family 속성
- 글꼴 지정하는 속성
- 기본형

  ```css
  선택자 {
    font-family: <글꼴명> | [<글꼴명>, <글꼴명>];
  }
  ```

- 예
  ```css
  body {
    font-family: "맑은 고딕", 돋움, 굴림;
  }
  ```

> font-size 속성
- 글자 크기를 지정하는 속성
- 기본형
  
  ```css
  선택자 {
    font-size: <절대 크기> | <상대 크기> | <크기> | <백분율>;
  }
  ```

> font-style 속성
- 글자를 이탤릭체로 표시할 때 사용하는 속성
- 기본형

  ```css
  선택자 {
    font-style: normal | italic | oblique;
  }
  ```

> font-weight 속성
- 글자 굵기를 지정하는 속성
- 기본형
  
  ```css
  선택자 {
    font-weight: normal | bold | bolder | lighter | 100~900;
  }
  ```


# ✔ 텍스트 관련 스타일
> color 속성
- 글자색을 지정하는 속성
- 기본형

  ```css
  선택자 {
    color: <색상>;
  }
  ```

> text-align 속성
- 텍스트의 정렬 방식을 지정하는 속성
- 기본형

  ```css
  선택자 {
    text-align: start | end | left | right | center | justify | match-parent;
  }
  ```

> line-height 속성
- 줄 간격을 조절하는 속성
- 기본형
  
  ```css
  선택자 {
    line-height: <절대 크기> | <상대 크기> | <백분율>;
  }
  ```

> text-decoration 속성
- 텍스트의 줄을 표시하거나 없애주는 속성
- 기본형

  ```css
  선택자 {
    text-decoration: none | underline | overline | line-through;
  }
  ```

> text-shadow 속성
- 텍스트에 그림자 효과를 추가하는 속성
- 기본형

  ```css
  선택자 {
    text-shadow: none | <가로 길이> <세로 길이> <번짐 정도> <색상>;
  }
  ```

> text-transform 속성
- 텍스트의 대소문자를 변환하는 속성
- 기본형

  ```css
  선택자 {
    text-transform: capitalize | uppercase | lowercase | full-width;
  }
  ```

> letter-spacing 속성
- 글자와 글자 사이의 간격을 조절하는 속성
- 기본형

  ```css
  선택자 {
    letter-spacing: <절대 크기> | <상대 크기> | <백분율>;
  }
  ```

> word-spacing 속성
- 단어와 단어 사이의 간격을 조절하는 속성
- 기본형

  ```css
  선택자 {
    word-spacing: <절대 크기> | <상대 크기> | <백분율>;
  }
  ```