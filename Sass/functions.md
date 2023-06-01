# ✔ Sass Built-in Functions

## 🔹 Number Functions

1. `percentage()`

    - 숫자값을 %로 변환

    ```code
    percentage(0.2)          => 20%
    percentage(100px / 50px) => 200%
    ```

2. `round()`

    - 소수점 이하 반올림

    ```code
    round(10.6px) => 11px
    ```

3. `ceil()`

    - 소수점 이하 올림

    ```code
    ceil(10.4px) => 11px
    ```

4. `floor()`

    - 소수점 이하 내림

    ```code
    floor(10.6px) => 10px
    ```

5. `abs()`

    - 절대값

    ```code
    abs(-10px) => 10px
    ```

## 🔹 Introspection Functions

1. `type-of()`

    - data type 취득

    ```code
    type-of(blue)   => color
    ```

2. `unit()`

    - data unit 취득

    ```code
    unit(10px * 5em) => "em*px"
    ```

3. `unitless()`

    - 값에 단위가 있는지 확인

    ```code
    unitless(100)   => true
    ```

4. `comparable()`

    - 값을 합산, 감산, 비교 가능한지 확인

    ```code
    comparable(100px, 3em) => false
    ```

## 🔹 String Functions

1. `quote()`

    - 따옴표 붙이기

    ```code
    quote(foo)   => "foo"
    ```

2. `unquote()`

    - 따옴표 제거

    ```code
    unquote("foo") => foo
    ```

## 🔹 List Functions

1. `length()`

    - list의 element 수 취득

    ```code
    length(10px 20px 30px)              => 3
    length((width: 10px, height: 20px)) => 2
    ```

2. `nth()`

    - list의 n번째 요소 취득

    ```code
    nth(10px 20px 30px, 1)                 => 10px
    nth((Helvetica, Arial, sans-serif), 3) => sans-serif
    nth((width: 10px, length: 20px), 2)    => length 20px
    ```

3. `index()`

    - list 내 특정 요소의 index 취득

    ```code
    index(1px solid red, solid)                       => 2
    index(1px solid red, dashed)                      => null
    ```

4. `append()`

    - list의 마지막에 단일 요소 추가

    ```code
    append(10px 20px, 30px)      => 10px 20px 30px
    append((blue, red), green)   => blue, red, green
    append(10px 20px, 30px 40px) => 10px 20px (30px 40px)
    append(10px, 20px, comma)    => 10px, 20px
    append((blue, red), green, space) => blue red green
    ```

5. `join()`

    - list와 list 결합

    ```code
    join(10px 20px, 30px 40px)      => 10px 20px 30px 40px
    join((blue, red), (#abc, #def)) => blue, red, #abc, #def
    join(10px, 20px)                => 10px 20px
    join(10px, 20px, comma)         => 10px, 20px
    join((blue, red), (#abc, #def), space) => blue red #abc #def
    ```

6. `zip()`

    - 복수의 list를 각자의 순서에 맞추어 재결합

    ```code
    zip(1px 1px 3px, solid dashed solid, red green blue)
    => 1px solid red, 1px dashed green, 3px solid blue
    ```

## 🔹 Map Functions

1. `map-get()`

    - map의 key로 value 취득

    ```code
    map-get(("foo": 1, "bar": 2), "foo") => 1
    map-get(("foo": 1, "bar": 2), "baz") => null
    ```

## 🔹 Color Functions

1. `adjust-hue()`

    - 색상(hue) 변경

    ```scss
    $base-color: #ad141e;

    .adjust-hue {
    	color: adjust-hue($base-color, 20%);
    	// => #ad3d14
    }
    ```

2. `saturate()`, `desaturate()`

    - 채도(saturation) 변경

    ```scss
    $base-color: #ad141e;

    p {
    	.saturate {
    		color: saturate($base-color, 20%);
    	}

    	.desaturate {
    		color: desaturate($base-color, 20%);
    	}
    }
    ```

3. `darken()`, `lighten()`

    - 휘도(lightness) 변경

    ```scss
    $base-color: #ad141e;

    p {
    	.darken {
    		color: darken($base-color, 10%);
    	}

    	.lighten {
    		color: lighten($base-color, 10%);
    	}
    }
    ```

4. `rgba()`

    - 투명도(opacity) 변경

    ```scss
    $base-color: #ad141e;

    .rgba {
    	color: rgba($base-color, 0.7);
    }
    ```

5. `opacify()`, `transparentize()`

    - alpha 연산
    - `opacify()`: 불투명도 증가시킴
    - `transparentize()`: 불투명도 감소시킴

    ```scss
    $base-color: rgba(255, 0, 0, 0.5);

    .opacify {
    	color: opacify($base-color, 0.3); // rgba(255, 0, 0, 0.8)
    }

    .transparentize {
    	color: transparentize($base-color, 0.25); // rgba(255, 0, 0, 0.25)
    }
    ```

6. `tint()`, `shade()`

    - 색상이 흰색(tint)과 검정색(shade)의 값으로 혼합
    - `tint()`: lighten과 유사
    - `shade()`: darken과 유사

    ```scss
    $base-color: #ad141e;

    .tint {
    	color: tint($base-color, 10%);
    }

    .shade {
    	color: shade($base-color, 10%);
    }
    ```
