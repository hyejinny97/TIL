# ✔ Bootstrap Utilities
> Utilities 종류
- [Colors](#-colors): color, opacity
- [Display](#-display): display, responsive display
- [Position](#-position): position, translate
- [Spacing](#-spacing): margin, padding, gap
- [Text](#-text): alignment, wrapping, transform, size, weight, style, line height, decoration



# ✔ Colors
- text나 background의 색을 지정하는 utility classes

> Colors

1. 기본 포맷

   ```
   text|bg-{color}
   ```

   ```html
   <p class="text-primary">text-primary</p>
   <p class="text-secondary">text-secondary</p>
   <p class="bg-danger">bg-danger</p>
   ```

2. color
   
   - `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`, `body`, `muted`, `white`, `black-50`, `white-50` 

> Opacity

1. 기본 포맷
   ```
   text|bg-opacity-{불투명도}
   ```

   ```html
   <div class="text-primary text-opacity-75">This is 75% opacity primary text</div>
   <div class="text-primary text-opacity-50">This is 50% opacity primary text</div>
   ```

2. 불투명도
   - 숫자로 지정
   - 숫자가 높으면 투명도 감소, 숫자가 낮으면 투명도 증가

   

# ✔ Display
> Display

1. 기본 포맷

   - breakpoint를 따로 지정해주지 않으면 xs이 default가 됨 

   ```
   d-[{breakpoint}]-{value}
   ```

   ```html
   <div class="d-inline p-2 text-bg-primary">d-inline</div>
   <div class="d-inline p-2 text-bg-dark">d-inline</div>
   ```

2. value
   
   - `none`, `inline`, `inline-block`, `block`, `grid`, `table`, `table-cell`, `table-row`, `flex`, `inline-flex`

> Responsive Display
- screen size에 따라 display를 변화시킬 수 있음

   ```html
   <!-- Hidden only on lg -->
   <div class="d-lg-none d-xl-block">Hidden only on lg</div>
   
   <!-- Visible only on sm -->
   <div class="d-none d-sm-block d-md-none">Visible only on sm</div>
   ```



# ✔ Position
> Position

1. 기본 포맷

   ```
   position-{position type} {property}-{position}
   ```

   ```html
   <div class="position-relative">
      <div class="position-absolute top-0 start-0"></div>
      <div class="position-absolute bottom-0 start-0"></div>
   </div>
   ```

2. position type
  
   - `static`, `relative`, `absolute`, `fixed`, `sticky`

3. property
   
   - `top`, `bottom`, `start`, `end`

4. position
   
   - 숫자 (퍼센트%를 뜻함)
     - 예) 50: 특정 sides로부터 50%
  
> Center elements

1. 기본 포맷

   ```
   translate-{이동방향 및 크기}
   ```

   ```html
   <div class="position-relative">
      <div class="position-absolute top-50 start-50 translate-middle"></div>
      <div class="position-absolute top-0 start-50 translate-middle-x"></div>
      <div class="position-absolute top-50 start-0 translate-middle-y"></div>
   </div>
   ```

2. 이동방향 및 크기
   
   - `middle`: translateX(-50%) and translateY(-50%)
   
   - `middle-x`: translateX(-50%)
  
   - `middle-y`: translateY(-50%)
  
   


# ✔ Spacing
- 반응형 margin, padding, gap utility classes

> Margin, Padding

1. 기본 포맷
   - breakpoint를 따로 지정해주지 않으면 xs이 default가 됨  

   ```
   {property}{sides}-[{breakpoint}]-{size}
   ```

   ```html
   <!-- 블록요소 수평 중앙 정렬 -->
   <div class="mx-auto" style="width: 200px;">
      Centered element
   </div>
   ```

2. property
   
   - `m`: margin
   
   - `p`: padding

3. sides
  
   - `t`: margin-top or padding-top
   
   - `b`: margin-bottom or padding-bottom

   - `s`: (start) margin-left or padding-left in LTR, argin-right or padding-right in RTL

   - `e`: (end) margin-right or padding-right in LTR, margin-left or padding-left in RTL

   - `x`: *-left and *-right
   
   - `y`: *-top and *-bottom
   
   - blank: top, bottom, left, right 네 방향 모두

4. size

   - 0: 0rem (0px)
   - 1: 0.25rem (4px)
   - 2: 0.5rem (8px)
   - **3: 1rem (16px)**
   - 4: 1.5rem (24px)
   - 5: 3rem (48px)
   - auto: 특정 sides의 margin을 자동 설정
  
   

# ✔ Text
- text의 alignment, wrapping, weight 등을 조절하는 utility classes

> Text alignment

1. 기본 포맷

   ```
   text-[{breakpoint}]-{alignment}
   ```

   ```html
   <p class="text-start">Start aligned text on all viewport sizes.</p>
   <p class="text-center">Center aligned text on all viewport sizes.</p>
   <p class="text-sm-end">Start aligned text on viewports sized SM (small) or wider.</p>
   ```

2. alignment
   
   - `start`, `center`, `end`
  
   
> Text wrapping and overflow

1. 기본 포맷
   
   ```
   text-{wrapping}
   ```

   ```html
   <div class="badge bg-primary text-wrap" style="width: 6rem;">
    This text should wrap.
   </div>

   <div class="text-nowrap bg-light border" style="width: 8rem;">
    This text should overflow the parent.
   </div>
   ```

2. wrapping
   
   - `wrap`, `nowrap` (=overflow)
  
   
> Text transform

1. 기본 포맷
   
   ```
   text-{transform}
   ```

   ```html
   <p class="text-lowercase">Lowercased text.</p>
   <p class="text-uppercase">Uppercased text.</p>
   <p class="text-capitalize">CapiTaliZed text.</p>
   ```

2. transform
   
   - `lowercase`, `uppercase`, `capitalize`
  
   

> Font size

1. 기본 포맷

   ```
   fs-{숫자}
   ```

   ```html
   <p class="fs-1">.fs-1 text</p>
   <p class="fs-2">.fs-2 text</p>
   ```

2. 숫자
   
   - 숫자 1~6
   - `<h1>` ~ `<h6>` 태그의 크기처럼 text 크기가 변경됨
  
   

> Font weight and italics

1. 기본 포맷
   
   ```
   fw-{font weight}
   fst-{font style}
   ```

   ```html
   <p class="fw-bold">Bold text.</p>
   <p class="fw-light">Light weight text.</p>
   ```

   ```html
   <p class="fst-italic">Italic text.</p>
   <p class="fst-normal">Text with normal font style</p>
   ```

2. font weight
   
   - `bold`, `bolder`, `semibold`, `normal`, `light`, `lighter`

3. font style

   - `normal`, `italic`

   
> Line height

1. 기본 포맷

   ```
   lh-{줄간격 크기}
   ```

   ```html
   <p class="lh-1">This is a long paragraph written to show how the line-height of an element is affected by our utilities. Classes are applied to the element itself or sometimes the parent element. These classes can be customized as needed with our utility API.</p>
   <p class="lh-sm">This is a long paragraph written to show how the line-height of an element is affected by our utilities. Classes are applied to the element itself or sometimes the parent element. These classes can be customized as needed with our utility API.</p>
   ```

2. 줄간격 크기
  
   - 절대크기: 숫자
  
   - 키워드: `sm`, `base`, `lg`
  
   

> Text decoration

1. 기본 포맷

   ```
   text-decoration-{decoration}
   ```

   ```html
   <p class="text-decoration-underline">This text has a line underneath it.</p>
   <a href="#" class="text-decoration-none">This link has its text decoration removed</a>
   ```

2. decoration

   - `underline`, `line-through`, `none`
  
   