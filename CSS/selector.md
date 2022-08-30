# ✔ CSS 선택자
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



# ✔ CSS 적용 우선순위 (cascading order)
1. 중요도 (Importance)
   
   - `!important`
   
   - 사용시 주의해야 함

2. 우선순위 (Specificity)
   - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element

3. CSS 파일 로딩 순서