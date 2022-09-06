# ✔ Bootstrap Components
- Bootstrap의 다양한 UI 요소를 활용할 수 있음
- 기본 제공된 Components를 custormize해서 활용 가능
  
> Components 종류
- [Buttons](#-buttons): Tags, Colors, Outline, Sizes, Disabled state
- [Carousel](#-carousel): Slides Only, With Controls, With Indicators, Crossfade, Individual Interval
- [Dropdowns](#-dropdowns): Single Button, Split Button, Dropdown Sizing, Dark Dropdowns, Dropdowns Directions, Dropdowns Auto Close Behavior, Menu Items Active, Menu Items Disabled, Menu Alignment, Menu Content - Headers/Dividers/Text/Form
- [Modal](#-modal): Modal components, Live Demo, Static Backdrop, Scrolling Long Content, Vertically Centered, Modal Sizing
- [Navbar](#-navbar): Brand, Responsive Nav, Forms, Button, Text, Color, Placement, Scrolling, Offcanvas Navbar




# ✔ Buttons
- 클릭했을 때 어떤 동작이 일어나도록 하는 요소

> Button Tags
 
1. 기본 포맷

   ```
   <a class="btn btn-{color}" href="#" role="button">문자열</a>
   <button class="btn btn-{color}" type="button|submit|reset">문자열</button>
   <input class="btn btn-{color}" type="button|submit|reset" value="문자열">
   ```

   ```html
   <a class="btn btn-primary" href="#" role="button">Link</a>
   <button class="btn btn-primary" type="submit">Button</button>
   <input class="btn btn-primary" type="button" value="Input">
   <input class="btn btn-primary" type="submit" value="Submit">
   <input class="btn btn-primary" type="reset" value="Reset">
   ```
   
> Button Colors

1. 기본 포맷
   
   ```
   <button type="button" class="btn btn-{color}">문자열</button>
   ```

   ```html
   <button type="button" class="btn btn-primary">Primary</button>
   <button type="button" class="btn btn-secondary">Secondary</button>
   <button type="button" class="btn btn-link">Link</button>
   ```

2. color

   - `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`, `link`

> Outline buttons

1. 기본 포맷
   
   ```
   <button type="button" class="btn btn-outline-{color}">문자열</button>
   ```

   ```html
   <button type="button" class="btn btn-outline-primary">Primary</button>
   <button type="button" class="btn btn-outline-secondary">Secondary</button>
   ```

> Button Sizes

1. 기본 포맷
   
   ```
   <button type="button" class="btn btn-{color} btn-{size}">문자열</button>
   ```

   ```html
   <button type="button" class="btn btn-primary btn-lg">Large button</button>
   <button type="button" class="btn btn-primary btn-sm">Small button</button>
   ```

2. size
   
   - `lg`, `sm`

> Disabled state

1. 기본 포맷
   
   ```
   <button type="button" class="btn btn-{color}" disabled>문자열</button>
   <a class="btn btn-{color} disabled" role="button" aria-disabled="true">문자열</a>
   ```

   ```html
   <button type="button" class="btn btn-primary" disabled>Primary button</button>
   <button type="button" class="btn btn-outline-primary" disabled>Primary button</button>
   <a class="btn btn-primary disabled" role="button" aria-disabled="true">Primary link</a>
   ```



# ✔ Carousel
- 콘텐츠(사진)을 순환시키기 위한 슬라이드쇼

> Carousel Slides Only

1. 기본 포맷
   
   ```
   <div class="carousel slide" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="{첫번째 이미지}" class="d-block w-{숫자}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{두번째 이미지}" class="d-block w-{숫자}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{세번째 이미지}" class="d-block w-{숫자}" alt="">
       </div>
     </div>
   </div>
   ```

   ```html
   <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
     </div>
   </div>
   ```

> Carousel With Controls

1. 기본 포맷
   
   ```
   <div id="동일" class="carousel slide" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="{첫번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{두번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{세번째 이미지}" class="d-block w-{size}" alt="">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#동일" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">이전화살표명</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#동일" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">다음화살표명</span>
     </button>
   </div>
   ```

   ```html
   <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Previous</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Next</span>
     </button>
   </div>
   ```

> Carousel With Indicators

1. 기본 포맷
   
   ```
   <div id="동일" class="carousel slide" data-bs-ride="true">
     <div class="carousel-indicators">
       <button type="button" data-bs-target="#동일" data-bs-slide-to="0" class="active"></button>
       <button type="button" data-bs-target="#동일" data-bs-slide-to="1"></button>
       <button type="button" data-bs-target="#동일" data-bs-slide-to="2"></button>
     </div>
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="{첫번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{두번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{세번째 이미지}" class="d-block w-{size}" alt="">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#동일" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">이전화살표명</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#동일" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">다음화살표명</span>
     </button>
   </div>
   ```

   ```html
   <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true">
     <div class="carousel-indicators">
       <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
       <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
       <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
     </div>
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Previous</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Next</span>
     </button>
   </div>
   ```

> Carousel Crossfade

1. 기본 포맷
   
   ```
   <div id="동일" class="carousel slide carousel-fade" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="{첫번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{두번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{세번째 이미지}" class="d-block w-{size}" alt="">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#동일" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">이전화살표명</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#동일" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">다음화살표명</span>
     </button>
   </div>
   ```

   ```html
   <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Previous</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Next</span>
     </button>
   </div> 
   ```

> Carousel Individual Interval

1. 기본 포맷
   
   ```
   <div id="동일" class="carousel slide" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active" data-bs-interval="{초ms}">
         <img src="{첫번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item" data-bs-interval="{초ms}">
         <img src="{두번째 이미지}" class="d-block w-{size}" alt="">
       </div>
       <div class="carousel-item">
         <img src="{세번째 이미지}" class="d-block w-{size}" alt="">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#동일" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">이전화살표명</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#동일" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">다음화살표명</span>
     </button>
   </div>
   ```

   ```html
   <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
     <div class="carousel-inner">
       <div class="carousel-item active" data-bs-interval="10000">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item" data-bs-interval="2000">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Previous</span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="visually-hidden">Next</span>
     </button>
   </div>
   ```



# ✔ Dropdowns
- dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만들 수 있음

> Single Button

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       Dropdown button
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Another action</a></li>
       <li><a class="dropdown-item" href="#">Something else here</a></li>
     </ul>
   </div>
   ```

> Split Button

1. 기본 포맷
   
   ```
   <div class="btn-group">
     <button type="button" class="btn btn-{color}">메뉴명</button>
     <button type="button" class="btn btn-{color} dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
       <span class="visually-hidden">숨겨진 메뉴명</span>
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="btn-group">
     <button type="button" class="btn btn-danger">Action</button>
     <button type="button" class="btn btn-danger dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
       <span class="visually-hidden">Toggle Dropdown</span>
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Another action</a></li>
       <li><a class="dropdown-item" href="#">Something else here</a></li>
       <li><a class="dropdown-item" href="#">Separated link</a></li>
     </ul>
   </div>
   ```

> Dropdown Sizing

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} btn-{size} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button class="btn btn-secondary btn-lg dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       Large button
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Another action</a></li>
       <li><a class="dropdown-item" href="#">Something else here</a></li>
     </ul>
   </div>
   ```

2. size 
   
   - `lg`, `sm`

> Dark Dropdowns

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu dropdown-menu-dark">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       Dropdown button
     </button>
     <ul class="dropdown-menu dropdown-menu-dark">
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Another action</a></li>
       <li><a class="dropdown-item" href="#">Something else here</a></li>
     </ul>
   </div>
   ```

> Dropdowns Directions

1. 기본 포맷
   
   ```
   <div class="dropdown-{direction1} {direction2}">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown-center">
     <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       Centered dropdown
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Action two</a></li>
       <li><a class="dropdown-item" href="#">Action three</a></li>
     </ul>
   </div>

   <div class="dropdown dropup">
     <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       Centered dropdown
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Action two</a></li>
       <li><a class="dropdown-item" href="#">Action three</a></li>
     </ul>
   </div>
   ```

2. direction1
   
   - `center`: 드롭다운 메뉴가 요소 아래 중앙에 위치

3. direction2
  
   - `dropup`: 드롭다운 메뉴가 요소 위에 위치
   
   - `dropend`: 드롭다운 메뉴가 요소 끝부분(LTR인 경우 오른쪽)에 위치
   
   - `dropstart`: 드롭다운 메뉴가 요소 앞부분(LTR인 경우 왼쪽)에 위치

> Dropdowns Auto Close Behavior

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="{auto close behavior}" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="true" aria-expanded="false">
       Default dropdown
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Menu item</a></li>
       <li><a class="dropdown-item" href="#">Menu item</a></li>
       <li><a class="dropdown-item" href="#">Menu item</a></li>
     </ul>
   </div>
   ```

2. auto close behavior
   
   - `true`: 드롭다운 메뉴 밖이나 안을 누르면 메뉴가 자동으로 닫힘
   
   - `false`: 드롭다운 메뉴 밖이나 안을 눌러도 메뉴가 자동으로 닫히지 않음
   
   - `inside`: 드롭다운 메뉴 안을 누르면 메뉴가 자동으로 닫힘
   
   - `outside`: 드롭다운 메뉴 밖을 누르면 메뉴가 자동으로 닫힘

> Menu Items Active

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item active" href="#" aria-current="true">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       Dropdown button
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Regular link</a></li>
       <li><a class="dropdown-item active" href="#" aria-current="true">Active link</a></li>
       <li><a class="dropdown-item" href="#">Another link</a></li>
     </ul>
   </div>
   ```

> Menu Items Disabled

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item disabled" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       Dropdown button
     </button>
     <ul class="dropdown-menu">
     <li><a class="dropdown-item" href="#">Regular link</a></li>
     <li><a class="dropdown-item disabled">Disabled link</a></li>
     <li><a class="dropdown-item" href="#">Another link</a></li>
   </ul>
   </div>
   ```

> Menu Alignment

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu dropdown-menu-{alignment}">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
       <li><a class="dropdown-item" href="#">옵션3</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
       Right-aligned menu example
     </button>
     <ul class="dropdown-menu dropdown-menu-end">
       <li><button class="dropdown-item" type="button">Action</button></li>
       <li><button class="dropdown-item" type="button">Another action</button></li>
       <li><button class="dropdown-item" type="button">Something else here</button></li>
     </ul>
   </div>
   ```

2. alignment
   
   - `start`: 드롭다운 메뉴가 요소의 왼쪽 아래에 위치
  
   - `end`: 드롭다운 메뉴가 요소의 오른쪽 아래에 위치

> Menu Content - 1) Headers

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><h6 class="dropdown-header">헤더명</h6></li>
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
      menu example
     </button>
     <ul class="dropdown-menu">
       <li><h6 class="dropdown-header">Dropdown header</h6></li>
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Another action</a></li>
     </ul>
   </div>
   ```

> Menu Content - 2) Dividers

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">옵션1</a></li>
       <li><hr class="dropdown-divider"></li>
       <li><a class="dropdown-item" href="#">옵션2</a></li>
     </ul>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
      menu example
     </button>
     <ul class="dropdown-menu">
       <li><a class="dropdown-item" href="#">Action</a></li>
       <li><a class="dropdown-item" href="#">Another action</a></li>
       <li><a class="dropdown-item" href="#">Something else here</a></li>
       <li><hr class="dropdown-divider"></li>
       <li><a class="dropdown-item" href="#">Separated link</a></li>
     </ul>
   </div>
   ```

> Menu Content - 3) Text

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button class="btn btn-{color} dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <div class="dropdown-menu text-muted">
        <p>
          Some example text that's free-flowing within the dropdown menu.
        </p>
      </div>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
      menu example
     </button>
     <div class="dropdown-menu p-4 text-muted" style="max-width: 200px;">
       <p>
         Some example text that's free-flowing within the dropdown menu.
       </p>
       <p class="mb-0">
         And this is more example text.
       </p>
     </div>
   </div>
   ```

> Menu Content - 4) Forms

1. 기본 포맷
   
   ```
   <div class="dropdown">
     <button type="button" class="btn btn-{color} dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
       메뉴명
     </button>
     <form class="dropdown-menu">
       <div>
         <label for="" class="form-label">라벨명</label>
         <input type="" class="form-control" id="">
       </div>
       <button type="submit" class="btn btn-{color}">버튼명</button>
     </form>
   </div>
   ```

   ```html
   <div class="dropdown">
     <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
       Dropdown form
     </button>
     <form class="dropdown-menu p-4">
       <div class="mb-3">
         <label for="exampleDropdownFormEmail2" class="form-label">Email address</label>
         <input type="email" class="form-control" id="exampleDropdownFormEmail2" placeholder="email@example.com">
       </div>
       <div class="mb-3">
         <label for="exampleDropdownFormPassword2" class="form-label">Password</label>
         <input type="password" class="form-control" id="exampleDropdownFormPassword2" placeholder="Password">
       </div>
       <div class="mb-3">
         <div class="form-check">
           <input type="checkbox" class="form-check-input" id="dropdownCheck2">
           <label class="form-check-label" for="dropdownCheck2">
             Remember me
           </label>
         </div>
       </div>
       <button type="submit" class="btn btn-primary">Sign in</button>
     </form>
   </div>
   ```



# ✔ Modal
- 사용자와 상호작용 하기 위해서 사용하며, 긴급 상황을 알리는 데 주로 사용
- 현재 열려 있는 페이지 위에 또 다른 레이어를 띄움
- 페이지를 이동하면 자연스럽게 사라짐 (제거를 하지 않고도 배경 클릭시 사라짐 – 옵션에 따라 다름)
- Modal은 자바스크립트를 활용하며, 반드시 target과 id가 일치되어야 함

> Modal components

1. 기본 포맷
   
   ```
   <div class="modal" tabindex="-1">
     <div class="modal-dialog">
       <div class="modal-content">
         <div class="modal-header">
           <h5 class="modal-title">제목</h5>
           <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
         </div>
         <div class="modal-body">
           <p>설명</p>
         </div>
         <div class="modal-footer">
           <button type="button" class="btn btn-{color}" data-bs-dismiss="modal">취소문</button>
           <button type="button" class="btn btn-{color}">확인문</button>
         </div>
       </div>
     </div>
   </div>
   ```

   ```html
   <div class="modal" tabindex="-1">
     <div class="modal-dialog">
       <div class="modal-content">
         <div class="modal-header">
           <h5 class="modal-title">Modal title</h5>
           <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
         </div>
         <div class="modal-body">
           <p>Modal body text goes here.</p>
         </div>
         <div class="modal-footer">
           <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
           <button type="button" class="btn btn-primary">Save changes</button>
         </div>
       </div>
     </div>
   </div>
   ```

> Live Demo

1. 기본 포맷
   
   ```
   <button type="button" class="btn btn-{color}" data-bs-toggle="modal" data-bs-target="#동일">버튼명</button>
   
   <div class="modal fade" id="동일" tabindex="-1" aria-hidden="true">
   </div>
   ```

   ```html
   <!-- Button trigger modal -->
   <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
     Launch demo modal
   </button>
   
   <!-- Modal -->
   <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
     <div class="modal-dialog">
       <div class="modal-content">
         <div class="modal-header">
           <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
           <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
         </div>
         <div class="modal-body">
           ...
         </div>
         <div class="modal-footer">
           <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
           <button type="button" class="btn btn-primary">Save changes</button>
         </div>
       </div>
     </div>
   </div>
   ```

> Static Backdrop

1. 기본 포맷
   
   ```
   <button type="button" class="btn btn-{color}" data-bs-toggle="modal" data-bs-target="#동일">버튼명</button>

   <div class="modal fade" id="동일" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-hidden="true">
   </div>
   ```

   ```html
   <!-- Button trigger modal -->
   <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
     Launch static backdrop modal
   </button>
   
   <!-- Modal -->
   <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
     <div class="modal-dialog">
       <div class="modal-content">
         <div class="modal-header">
           <h5 class="modal-title" id="staticBackdropLabel">Modal title</h5>
           <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
         </div>
         <div class="modal-body">
           ...
         </div>
         <div class="modal-footer">
           <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
           <button type="button" class="btn btn-primary">Understood</button>
         </div>
       </div>
     </div>
   </div>
   ```

> Scrolling Long Content

1. 기본 포맷
   
   ```
   <div class="modal-dialog modal-dialog-scrollable">
   </div>
   ```

   ```html
   <!-- Scrollable modal -->
   <div class="modal-dialog modal-dialog-scrollable">
     ...
   </div>
   ```

> Vertically Centered

1. 기본 포맷
   
   ```
   <div class="modal-dialog modal-dialog-centered">
   </div>
   ```

   ```html
   <!-- Vertically centered modal -->
   <div class="modal-dialog modal-dialog-centered">
     ...
   </div>
   ```

> Modal Sizing

1. 기본 포맷
   
   ```
   <div class="modal-dialog modal-{size}">...</div>
   ```

   ```html
   <div class="modal-dialog modal-xl">...</div>
   <div class="modal-dialog modal-lg">...</div>
   <div class="modal-dialog modal-sm">...</div>
   ```

2. size
   
   - `sm`: 300px
   
   - default: 500px
   
   - `lg`: 800px
   
   - `xl`: 1140px



# ✔ Navbar
- navbar 클래스를 활용하면 네비게이션 바를 제작할 수 있음

> Navbar Brand

1. 기본 포맷
   
   ```
   1) Text
   <nav class="navbar">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">브랜드명</a>
     </div>
   </nav>

   1) Image
   <nav class="navbar">
     <div class="container">
       <a class="navbar-brand" href="#">
         <img src="{이미지 소스}" alt="" width="{숫자}" height="{숫자}">
       </a>
     </div>
   </nav>  

   1) Image and text
   <nav class="navbar">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">
         <img src="{이미지 소스}" alt="" width="{숫자}" height="{숫자}">
         브랜드명
       </a>
     </div>
   </nav>
   ```

   ```html
   <!-- 1) Text -->
   <nav class="navbar bg-light">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">Navbar</a>
     </div>
   </nav>

   <!-- 2) Image -->
   <nav class="navbar bg-light">
     <div class="container">
       <a class="navbar-brand" href="#">
         <img src="/docs/5.2/assets/brand/bootstrap-logo.svg" alt="" width="30" height="24">
       </a>
     </div>
   </nav>

   <!-- 3) Image and text -->
   <nav class="navbar bg-light">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">
         <img src="/docs/5.2/assets/brand/bootstrap-logo.svg" alt="" width="30" height="24" class="d-inline-block align-text-top">
         Bootstrap
       </a>
     </div>
   </nav>
   ```

> Navbar Responsive Nav

1. 기본 포맷
   
   ```
   <nav class="navbar navbar-expand-{breakpoint}">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">브랜드명</a>
       <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#동일">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse" id="동일">
         <ul class="navbar-nav">
           <li class="nav-item">
             <a class="nav-link active" href="#">항목1</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#">항목2</a>
           </li>
           <li class="nav-item">
             <a class="nav-link disabled">항목3</a>
           </li>
         </ul>
       </div>
     </div>
   </nav>
   ```

   ```html
   <nav class="navbar navbar-expand-lg bg-light">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">Navbar</a>
       <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse" id="navbarNav">
         <ul class="navbar-nav">
           <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="#">Home</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#">Features</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#">Pricing</a>
           </li>
           <li class="nav-item">
             <a class="nav-link disabled">Disabled</a>
           </li>
         </ul>
       </div>
     </div>
   </nav>
   ```

> Navbar Forms

1. 기본 포맷
   
   ```
   <nav class="navbar">
     <div class="container-fluid">
       <form class="d-flex" role="search">
         <input class="form-control" type="search">
         <button class="btn btn-[outline]-{color}" type="submit">버튼명</button>
       </form>
     </div>
   </nav>
   ```

   ```html
   <nav class="navbar bg-light">
     <div class="container-fluid">
       <form class="d-flex" role="search">
         <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
         <button class="btn btn-outline-success" type="submit">Search</button>
       </form>
     </div>
   </nav>
   ```

> Navbar Input Groups

1. 기본 포맷
   
   ```
   <nav class="navbar">
     <form class="container-fluid">
       <div class="input-group">
         <span class="input-group-text">문자열</span>
         <input type="" class="form-control">
       </div>
     </form>
   </nav>
   ```

   ```html
   <nav class="navbar bg-light">
     <form class="container-fluid">
       <div class="input-group">
         <span class="input-group-text" id="basic-addon1">@</span>
         <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
       </div>
     </form>
   </nav>
   ```

> Navbar Button

1. 기본 포맷
   
   ```
   <nav class="navbar">
     <form class="container-fluid">
       <button class="btn btn-[outline]-{color}" type="button">버튼명</button>
     </form>
   </nav>
   ```

   ```html
   <nav class="navbar bg-light">
     <form class="container-fluid justify-content-start">
       <button class="btn btn-outline-success me-2" type="button">Main button</button>
       <button class="btn btn-sm btn-outline-secondary" type="button">Smaller button</button>
     </form>
   </nav>
   ```

> Navbar Text

1. 기본 포맷
   
   ```
   <nav class="navbar">
     <div class="container-fluid">
       <span class="navbar-text">텍스트</span>
     </div>
   </nav>
   ```

   ```html
   <nav class="navbar bg-light">
     <div class="container-fluid">
       <span class="navbar-text">
         Navbar text with an inline element
       </span>
     </div>
   </nav>
   ```

> Navbar Color

1. 기본 포맷
   
   ```
   <nav class="navbar navbar-dark bg-{color}">
   </nav>
   ```

   ```html
   <nav class="navbar navbar-dark bg-dark">
     <!-- Navbar content -->
   </nav>
   
   <nav class="navbar" style="background-color: #e3f2fd;">
     <!-- Navbar content -->
   </nav>
   ```

> Navbar Placement

- position: static (default)이므로 display를 지정하지 않으면 Navbar는 static 상태임

1. 기본 포맷
   
   ```
   <nav class="navbar {position type}-{property}">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">브랜드명</a>
    </div>
   </nav>
   ```

   ```html
   <nav class="navbar sticky-top bg-light">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">Sticky top</a>
     </div>
   </nav>
   ```

2. position type

   - `fixed`, `sticky`

3. property
   
   - `top`, `bottom`

> Navbar Scrolling

1. 기본 포맷
   
   ```
   <nav class="navbar navbar-expand-{breakpoint}">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">브랜드명</a>
       <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#동일">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse" id="동일">
         <ul class="navbar-nav navbar-nav-scroll" style="--bs-scroll-height: {크기};">
           <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="#">항목1</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#">항목2</a>
           </li>
           <li class="nav-item">
             <a class="nav-link disabled">항목3</a>
           </li>
         </ul>
       </div>
     </div>
   </nav>
   ```

   ```html
   <nav class="navbar navbar-expand-lg bg-light">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">Navbar scroll</a>
       <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse" id="navbarScroll">
         <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
           <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="#">Home</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#">Link</a>
           </li>
           <li class="nav-item dropdown">
             <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
               Link
             </a>
             <ul class="dropdown-menu">
               <li><a class="dropdown-item" href="#">Action</a></li>
               <li><a class="dropdown-item" href="#">Another action</a></li>
               <li><hr class="dropdown-divider"></li>
               <li><a class="dropdown-item" href="#">Something else here</a></li>
             </ul>
           </li>
           <li class="nav-item">
             <a class="nav-link disabled">Link</a>
           </li>
         </ul>
         <form class="d-flex" role="search">
           <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
           <button class="btn btn-outline-success" type="submit">Search</button>
         </form>
       </div>
     </div>
   </nav>
   ```

> Offcanvas Navbar

1. 기본 포맷
   
   ```
   <nav class="navbar">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">브랜드명</a>
       <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#동일1">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="offcanvas offcanvas-end" tabindex="-1" id="동일1">
         <div class="offcanvas-header">
           <h5 class="offcanvas-title">제목</h5>
           <button type="button" class="btn-close" data-bs-dismiss="offcanvas"></button>
         </div>
         <div class="offcanvas-body">
           <ul class="navbar-nav">
             <li class="nav-item">
               <a class="nav-link active" href="#">항목1</a>
             </li>
             <li class="nav-item">
               <a class="nav-link" href="#">항목2</a>
             </li>
           </ul>
         </div>
       </div>
     </div>
   </nav>
   ```

   ```html
   <nav class="navbar bg-light fixed-top">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">Offcanvas navbar</a>
       <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
         <div class="offcanvas-header">
           <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Offcanvas</h5>
           <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
         </div>
         <div class="offcanvas-body">
           <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
             <li class="nav-item">
               <a class="nav-link active" aria-current="page" href="#">Home</a>
             </li>
             <li class="nav-item">
               <a class="nav-link" href="#">Link</a>
             </li>
             <li class="nav-item dropdown">
               <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                 Dropdown
               </a>
               <ul class="dropdown-menu">
                 <li><a class="dropdown-item" href="#">Action</a></li>
                 <li><a class="dropdown-item" href="#">Another action</a></li>
                 <li>
                   <hr class="dropdown-divider">
                 </li>
                 <li><a class="dropdown-item" href="#">Something else here</a></li>
               </ul>
             </li>
           </ul>
           <form class="d-flex" role="search">
             <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
             <button class="btn btn-outline-success" type="submit">Search</button>
           </form>
         </div>
       </div>
     </div>
   </nav>
   ```



