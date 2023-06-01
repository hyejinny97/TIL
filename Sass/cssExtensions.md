# ✔ CSS Extensions

-   Sass의 유용한 확장 기능으로, Nesting/import/extend/조건/반복/Mixin/function이 존재함

## 🔹 Nesting

-   Sass를 사용하면 중첩으로 선언할 수 있음

    -   HTML의 구조를 반영해 CSS를 기술할 수 있다는 장점이 있음

    ```scss
    #navbar {
    	width: 80%;
    	height: 23px;

    	li {
    		float: left;
    		a {
    			font-weight: bold;
    		}
    	}
    }
    ```

-   하지만, 너무 깊은 nesting은 가독성을 나쁘게 하고 selector를 복잡하게 만들 수 있으니 주의해야 함

-   property에도 nesting을 적용할 수 있음

    ```scss
    .funky {
    	font: {
    		family: fantasy;
    		size: 30em;
    		weight: bold;
    	}
    }
    ```

## 🔹 @import

-   `@import` directive를 사용하여 분리된 stylesheet 파일을 import할 수 있음
-   Sass의 `@import`는 기존의 CSS의 `@import`보다 편리한 기능을 제공

    -   1. 확장자 생략 가능
    -   2. 여러 개의 파일 한 번에 import 가능
    -   3. 변수를 사용해 import 가능

        ```scss
        @import "foo.scss";

        // 1) 확장자 생략 가능
        @import "foo";

        // 2) 여러 개의 파일 한 번에 import 가능
        @import "rounded-corners", "text-shadow";

        // 3) 변수를 사용해 import 가능
        $family: "Open+Sans";
        @import url("http://fonts.googleapis.com/css?family=#{$family}");
        ```

-   top-level이 아닌 CSS rule 또는 `@media` rule 내에 포함시키는 것도 가능함

    ```scss
    // _example.scss
    .example {
    	color: red;
    }
    ```

    ```scss
    #main {
    	@import "example";
    }
    ```

### ➕ partial

-   여러 개의 파일로 분할하는 것 또는 분활된 파일을 의미함
-   partial된 Sass 파일명 앞에 underscore `_`를 붙여야 함
-   partial된 Sass 파일을 import하는 경우, underscore `_`는 생략 가능
-   역할) partial된 Sass 파일은 import 시에는 CSS 파일로 transpile되지 않고, import가 완료된 이후 CSS 파일로 transpile됨
-   최신 버전에서는 `_`을 붙이지 않아도 에러가 발생하지 않음
-   `@import` 대신 SCSS에 새로 추가된 Module System (`@use`, `@forward`)를 사용하는 방법도 있음

## 🔹 @extend

-   기존 스타일 상속 가능

    ```scss
    .error {
    	border: 1px #f00;
    	background-color: blue;
    }

    .seriousError {
    	@extend .error;

    	border-width: 3px;
    	border-color: darkblue;
    }
    ```

-   `@extend`를 `@media` 블록 내에서 사용할 수는 없음

-   `@extend`를 사용할 경우 예상치 못한 부작용이 발생할 수 있으므로, `@extend`의 사용은 가급적 자제하고 `Mixin`을 사용하는 것을 추천

## 🔹 Placeholder Selectors

-   재사용 가능한 rule set을 `%` 키워드로 지정하는 `@extend` 전용 selector임
-   Placeholder Selector은 상속만을 위한 rule set으로 자신은 transpile되지 않음

    ```scss
    %input-style {
    	font-size: 14px;
    }

    .input-black {
    	@extend %input-style;

    	color: black;
    }
    ```

## 🔹 조건문

### 🔸 if()

-   `if()` 함수는 주어진 조건을 판단하여 결과를 반환함
-   JS의 삼항연산자와 유사하게 동작

    -   `if(condition, if_true, if_false)`

    ```scss
    $type: ocean;

    p {
    	color: if($type == ocean, blue, black); // color: blue;
    }
    ```

### 🔸 @if ~ @else

-   `@if` ~ `@else`를 사용하면 조건 분기가 가능함

    ```scss
    $type: monster;

    p {
    	@if $type == ocean {
    		color: blue;
    	} @else if $type == matador {
    		color: red;
    	} @else if $type == monster {
    		color: green;
    	} @else {
    		color: black;
    	}
    }
    ```

## 🔹 반복문

### 🔸 @for

-   `@for`...`from`...`through`로 반복 가능

    ```scss
    @for $i from 1 through 3 {
    	// 1부터 3까지 반복
    	.item-#{$i} {
    		width: 2em * $i;
    	}
    }
    ```

### 🔸 @each

-   `@each`...`in` 사용으로 list 또는 map의 요소에 대해 반복 가능

    ```scss
    // List 반복
    @each $animal in puma, sea-slug, egret, salamander {
    	.#{$animal}-icon {
    		background-image: url("/images/#{$animal}.png");
    	}
    }
    ```

    ```scss
    // Map 반복
    @each $header, $size in (h1: 2em, h2: 1.5em, h3: 1.2em) {
    	#{$header} {
    		font-size: $size;
    	}
    }
    ```

### 🔸 @while

-   `@while`로 반복 가능

    ```scss
    $i: 6;
    @while $i > 0 {
    	.item-#{$i} {
    		width: 2em * $i;
    	}
    	$i: $i - 2;
    }
    ```

## 🔹 Mixin

-   중복을 방지하기 위해 사용 빈도가 높은 마크업을 사전에 정의하여 필요할 때에 불러 사용하는 방법
-   `@Mixin`을 사용해 선언하고, `@include`로 불러들임

    ```scss
    @mixin circle {
    	width: 50px;
    	height: 50px;
    	border-radius: 50%;
    }

    .box {
    	@include circle;

    	background: #f00;
    }
    ```

-   `@extend`와 유사하나, JS 함수와 같이 argument를 전달 받을 수 있다는 차이가 있음

    ```scss
    @mixin circle($size) {
    	width: $size;
    	height: $size * 2;
    	border-radius: 50%;
    }

    .box {
    	@include circle(100px);

    	background: #f00;
    }
    ```

-   argument의 기본값을 설정할 수도 있음

    ```scss
    @mixin circle($size: 10px) {
    	width: $size;
    	height: $size * 2;
    	border-radius: 50%;
    }

    .box {
    	// 인수가 전달되지 않으면 초기값을 사용한다.
    	@include circle();
    	background: #f00;
    }
    ```

-   Mixin을 사용한 유용한 예

    ```scss
    @mixin vendorPrefix($property, $value) {
    	@each $prefix in -webkit-, -moz-, -ms-, -o-, "" {
    		#{$prefix}#{$property}: $value;
    	}
    }

    .border_radius {
    	@include vendorPrefix(transition, 0.5s);
    }
    ```

    ```scss
    @mixin position(
    	$position,
    	$top: null,
    	$right: null,
    	$bottom: null,
    	$left: null
    ) {
    	position: $position;
    	top: $top;
    	right: $right;
    	bottom: $bottom;
    	left: $left;
    }

    .box {
    	@include position(absolute, $top: 10px, $left: 50%);
    }
    ```

-   직접 Mixin을 작성하는 대신, Sass Framework/Library를 사용하는 방법도 있음
    -   [Bourbon: Sass Mixins Library](http://bourbon.io/)
    -   [Compass: CSS Authoring Framework](http://compass-style.org/)
    -   [Susy: Sass grid framework](http://susy.oddbird.net/)

## 🔹 Function

-   function은 mixin과ㅗ 유사하나 반환값에 차이가 있음

    -   `mixin`: style markup을 반환
    -   `function`: `@return` directive를 통해 값을 반환

    ```scss
    $grid-width: 40px;
    $gutter-width: 10px;

    @function grid-width($n) {
    	@return $n * $grid-width + ($n - 1) * $gutter-width;
    }

    #sidebar {
    	width: grid-width(5);
    } // width: 240px;
    ```

## 🔹 Comment

-   CSS는 멀티 라인 주석 `/* */`만을 지원하지만, Sass는 `/* */`와 `//` 모두 사용 가능
-   단, 한 줄 주석 `//`은 transpile 후 CSS에서 사라지고, 멀티 라인 주석 `/* */`은 CSS에 나타남
