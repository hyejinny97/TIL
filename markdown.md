# 마크다운

> 텍스트 기반의 가벼운 마크업 언어



## Heading

- 문서의 제목이나 소제목으로 사용

- `#` 의 개수에 따라 대응대는 수준이 있으며, h1 ~ h6까지 표현 가능

- `#`이후에 띄어쓰기를 반드시 해야함

  

## List

1. 순서가 없는 리스트(ul): - (hypen), * (asterisk)
   - 목록 활용 시, 단계를 tab과 tab + shift로 조절

2. 순서가 있는 리스트(ol): 1.



## Fenced Code Block

- 코드 불록은 백틱 기호 3개(``` )를 활용하여 작성
- 코드 블록에 특정 언어를 명시하면 syntax highlighting 적용 가능

```python
print('Hello python')
```

```html
<h1>
    Hello HTML
</h1>
```



## Inline Code Block

- 코드 블록은 백틱 기호 1개(`)를 활용하여 작성 

  `인라인 코드 블록`



## Link

- `[문자열](URL)`을 통해 링크를 작성 가능

  [마크다운 cheat sheet](https://www.markdownguide.org/cheat-sheet/)
  
  [markdown_practice](./markdown_practice.md)



## 이미지

- `![문자열](URL)`을 통해 이미지 사용 가능

- 절대 경로: c드라이브로부터 생성되는 경로

- 상대 경로: 마크다운 파일과 이미지가 같은 위치에 있으면 볼 수 있음

  ![dog](markdown.assets/dog.jpg)

  

## 인용문

- `>`을 통해 인용문을 작성

> 인용문



## Table(표)

- 마크다운 에디터를 적극 활용하자([본문] - [표] - [표 삽입])

| 제목     | 내용 | 일시 |
| -------- | ---- | ---- |
| 마크다운 |      |      |
| 파이썬   |      |      |
| 알고리즘 |      |      |



## text 강조

- 굵게(bold): `**문자열**`을 통해 **굵게** 가능
- 기울임(italic): `*문자열*`을 통해 *기울임*  가능



## 수평선

- 3개 이상의 asterisks `***` 로 수평선 그릴 수 있음

*****************

- 3개 이상의 dashes `---` 로 수평선 그릴 수 있음

--------

- 3개 이상의 underscores `___` 로 수평선 그릴 수 있음

______

