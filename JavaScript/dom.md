# ✔ DOM 조작
- Document는 문서 한 장(HTML)에 해당하고 이를 조작
- DOM 조작 순서: 선택 (Select) → 변경 (Manipulation)

> DOM 객체의 상속 구조

1. EventTarget
   
   - Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스

2. Node

   - 여러 가지 DOM 타입들이 상속하는 인터페이스

3. Element

   -  Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
   - 부모인 Node와 그 부모인 EventTarget의 속성을 상속

4. Document

   - 브라우저가 불러온 웹 페이지를 나타냄
   -  DOM 트리의 진입점(entry point) 역할을 수행

5. HTMLElement

   - 모든 종류의 HTML 요소
   - 부모 element의 속성 상속

  ![](https://velog.velcdn.com/images/zmin9/post/23590765-86e6-48ec-9f0f-8e4edcbb3033/image.png)



# ✔ DOM 선택
> DOM 선택 관련 메서드

1. `document.querySelector(선택자)`
  
   - 제공한 선택자와 일치하는 element **하나** 선택
   - 제공한 CSS selector를 만족하는 **첫 번째 element 객체**를 반환 (없다면 null)

2. `document.querySelectorAll(선택자)`

   - 제공한 선택자와 일치하는 **여러** element를 선택
   - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
   - 지정된 셀렉터에 일치하는 **NodeList**를 반환

3. `document.getElementById(아이디명)`
   
4. `document.getElementsByTagName(태그명)`

5. `document.getElementByClassName(클래스명)`

> DOM 선택 관련 메서드별 반환 타입

1. 단일 element
  
   - `querySelector()`, `getElementById()` 메서드의 반환값 타입

2. HTMLCollection

   - `getElementsByTagName()`, `getElementsByClassName()` 메서드의 반환값 타입
  
   - 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열)
   - name, id, index 속성으로 각 항목에 접근 가능
   - **Live Collection**으로 DOM의 변경사항을 실시간으로 반영

3. NodeList
   
   - `querySelectorAll()` 메서드의 반환값 타입
  
   - 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열)
   - index로만 각 항목에 접근 가능
   - 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능
   - **Live Collection**으로 DOM의 변경사항을 실시간으로 반영
    
     - 단, `querySelectorAll()`에 의해 반환되는 NodeList는 **Static Collection**으로 실시간으로 반영되지 않음

> Collection

1. Live Collection

   - 문서가 바뀔 때 실시간으로 업데이트 됨
   - DOM의 변경사항을 실시간으로 collection에 반영
   - ex) HTMLCollection, NodeList

2. Static Collection (non-live)
   
   - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
  
   - `querySelectorAll()`의 반환 NodeList만 static collection

> `querySelector_()` vs `getElementBy_()`

- getElementBy_()보단 querySelector(), querySelectorAll()을 사용하는 것을 권장
- 이유
  - id, class 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능
  - ex) document.querySelector('#id’), document.querySelectAll(‘.class')
  
  - `querySelectorAll()`에 의해 반환되는 NodeList는 **Static Collection**으로 실시간으로 반영되지 않음


 
# ✔ DOM 변경
> DOM 변경 관련 메서드

1. `document.createElement(태그명)`
   
   - 작성한 태그명의 HTML 요소를 생성하여 반환

2. `Element.append()`
   
   - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
   - **여러 개**의 **Node 객체, DOMString**을 추가 할 수 있음
   - 반환 값이 없음

3. `Node.appendChild()`
   
   - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
   - 한번에 오직 **하나**의 **Node만** 추가할 수 있음
   - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동

4. `Node.innerText`
   
   - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김)
   - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현

5. `Element.innerHTML`

   - 요소(element) 내에 포함된 HTML 마크업을 반환
   - [참고] XSS 공격에 취약하므로 사용 시 주의
   - XSS (Cross-site Scripting)
     - 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
     - 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함

> `ParentNode.append()` vs `Node.appendChild()`

- append()를 사용하면 DOMString 객체를 추가할 수도 있지만, appendChild()는 Node 객체만 허용
- append()는 반환 값이 없지만, appendChild()는 추가된 Node 객체를 반환
- append()는 여러 Node 객체와 문자열을 추가할 수 있지만, appendChild()는 하나의 Node 객체만 추가할 수 있음



# ✔ DOM 삭제
> DOM 삭제 관련 메서드

1. `ChildNode.remove()`
   
   - Node가 속한 트리에서 해당 Node를 제거

2. `Node.removeChild()`

   - Node는 인자로 들어가는 자식 Node의 부모 Node
   - DOM에서 자식 Node를 제거하고 제거된 Node를 반환



# ✔ DOM 속성
> DOM 속성 관련 메서드

1. `Element.setAttribute(name, value)`
   
   - 지정된 요소의 값을 설정
   - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

2. `Element.getAttribute(attributeName)`
   
   - 해당 요소의 지정된 값(문자열)을 반환
   - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
