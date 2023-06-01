# ✔ SassScript

-   CSS에서는 불가능한 연산, 변수, 함수 등의 확장 기능을 의미

## 🔹 Data Type

-   property의 값으로 사용할 수 있는 data type (7가지)
-   `type-of()` 함수를 사용해 data type을 확인할 수 있음

1. 숫자형

    - ex) 10, 1.2, 13px

2. 문자열

    -   1. 따옴표를 사용하는 경우 (ex) “Lucida Grande”, ‘http://sass-lang.com’)
    -   2. 따옴표를 사용하지 않는 경우 (ex) bold, sans-serif)

3. 컬러

    - ex) blue, #04a3f9, rgba(255, 0, 0, 0.5)

4. Boolean

    - ex) true, false

5. null

    - property 값이 null인 변수는 transpile되지 않음

6. list

    - 공백 또는 콤마로 구분된 값
    - ex) 1.5em 1em 0 2em
    - ex) Helvetica, Arial, sans-serif

7. map

    - object와 유사한 방식으로, `map-get()` 함수를 사용해 원하는 값을 추출할 수 있음
    - `(key1: value1, key2: value2)`

    ```scss
    // map
    $foundation-palette: (
    	primary: #e44347,
    	mars: #d7525c,
    	saturn: #e4b884,
    	neptune: #5147d7,
    );

    .mars {
    	color: map-get($foundation-palette, mars);
    }
    ```

## 🔹 변수

-   문자열, 숫자, 컬러 등을 변수에 저장해 사용할 수 있음

    -   변수명은 `$`로 시작함

    ```scss
    $font_color: #333;
    $line_height: percentage(20px / $font_size);

    body {
    	color: $font_color;
    	line-height: $line_height;
    }
    ```

-   변수에는 유효범위(scope)가 존재함

    -   코드 블록 내에서 선언된 변수는 블록 내에서만 사용 가능

    ```scss
    $width: 960px; // 전역 변수

    #main {
    	$color: #333; // 지역 변수
    	width: $width;
    	margin: 20px auto;
    	section {
    		p {
    			color: $color;
    		}
    	}
    }
    ```

-   `!global`을 사용해 지역 변수를 전역 변수로 지정할 수 있음

    ```scss
    #main {
    	$color: #333 !global; // 전역 변수
    }
    ```

## 🔹 연산자

### 🔸 숫자 연산자

-   종류: `+`, `-`, `*`, `/`, `%`, `==`, `!=`

-   다른 단위의 값을 연산해도 수행됨

    -   단, 상대적인 값(%, em, rem, vh, vw, vmin, vmax)과 절대적인 값의 연산은 불가
    -   상대적인 값을 갖는 단위의 연산은 동일한 단위를 갖는 값과의 연산만 유효함
    -   CSS3의 `calc()` 함수를 사용하면, 상대적인 값과 절대적인 값의 연사도 가능함

    ```scss
    $width: 100px;

    #foo {
    	width: $width + 10; // 110px
    }
    ```

    ```scss
    $width: 100px;

    #foo {
    	width: $width + 10em; // Error: Incompatible units em and px.
    }
    ```

    ```scss
    #foo {
    	width: 5% + 10%; // 15%
    }
    ```

    ```scss
    #foo {
    	width: calc(25% - 5px);
    }
    ```

-   CSS에서 값을 구분하는 의미를 갖는 `/`가 존재하기 때문에, Sass의 `/` 나눗셈 연산자를 사용하기 위해서는 몇 가지 조건이 필요

    -   1. 변수에 대해 사용
    -   2. 괄호 내에서 사용
    -   3. 다른 연산의 일부로서 사용

    ```css
    p {
    	/*
        font: font-style font-variant font-weight font-size/line-height font-family
      */
    	font: italic bold 12px/30px Georgia, serif;
    }
    ```

    ```scss
    p {
    	$width: 1000px;
    	width: $width / 2; // 변수에 대해 사용 →　width: 500px;
    	height: (500px / 2); // 괄호 내에서 사용 →　height: 250px;
    	margin-left: 5px + 8px / 2px; // 다른 연산의 일부로서 사용 →　margin-left: 9px;
    }
    ```

### 🔸 컬러 연산자

-   모든 산술 연산자는 컬러값에도 사용할 수 있음

    ```scss
    p {
    	color: #010203 + #040506; // #050709
    }

    p {
    	color: #010203 * 2; // #020406
    }

    p {
    	color: rgba(255, 0, 0, 0.75) + rgba(0, 255, 0, 0.75); // rgba(255, 255, 0, 0.75)
    }
    ```

-   단, rgba의 alpha값은 연산되지 않음

    -   alpha값의 연산을 위해서는 `opacify` 함수 또는 `transparentize` 함수를 사용해야 함
    -   `opacify` 함수: 첫번째 인수로 전달받은 alpha값에 두번째 인수를 더해 불투명도를 증가시킴
    -   `transparentize` 함수: 첫번째 인수로 전달받은 alpha값에 두번째 인수를 빼서 불투명도를 감소시킴

    ```scss
    $translucent-red: rgba(255, 0, 0, 0.5);

    p {
    	color: opacify($translucent-red, 0.3); // rgba(255, 0, 0, 0.8);
    	background-color: transparentize(
    		$translucent-red,
    		0.25
    	); // rgba(255, 0, 0, 0.25);
    }
    ```

### 🔸 문자열 연산자

-   `+` 연산자를 사용해 문자열을 연결할 수 있음

    -   따옴표가 있는 문자열과 없는 문자열을 함께 사용하는 경우, 좌항의 문자열을 기준으로 따옴표를 처리함

        ```scss
        p:before {
        	content: "Foo " + Bar; // "Foo Bar"
        	font-family: sans- + "serif"; // sans-serif
        }
        ```

### 🔸 Boolean 연산자

-   종류: `&&`, `||`, `!`

### 🔸 List 연산자

-   리스트를 위한 연산자는 제공되진 않지만, 리스트 함수를 사용하여 필요한 처리를 수행할 수 있음

## 🔹 Interpolation `#{}`

-   변수의 값을 문자열 그대로 삽입 가능하게 해줌
-   `#{}`을 사용하면 property 값, property 명, selector에도 사용 가능

    ```scss
    $name: foo;
    $attr: border;
    $font-size: 12px;
    $line-height: 30px;

    p.#{$name} {
    	// p.foo
    	#{$attr}-color: blue; // border-color: blue;
    	font: #{$font-size} / #{$line-height}; // 12px / 30px
    }
    ```

## 🔹 Ampersand `&`

-   부모 요소를 참조하는 selector

    ```scss
    a {
    	color: #ccc;

    	&.home {
    		// css에서 a.home을 의미
    		color: #f0f;
    	}

    	&:hover {
    		// css에서 a:hover을 의미
    		text-decoration: none;
    	}

    	> span {
    		// css에서 a > span을 의미
    		color: blue;
    	}

    	span {
    		// css에서 a span을 의미
    		color: red;
    	}
    }
    ```

## 🔹 `!default` flag

-   할당되지 않은 변수의 초기값을 설정

    -   이미 값이 할당되어 있는 변수에 사용하면 적용되지 않음

        ```scss
        $content: "First content";
        $content: "Second content?" !default;
        $new_content: "First time reference" !default;

        #main {
        	content: $content; // "First content"
        	new-content: $new_content; // "First time reference"
        }
        ```
