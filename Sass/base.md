# ✔ Sass 설치 및 명령어

## 🔹 Sass 설치

-   아래 명령어로 Sass 설치

    ```bash
    $ npm install sass
    ```

-   Sass 버전 확인 명령어

    ```bash
    $ sass --version
    ```

## 🔹 Sass 빌드

-   브라우저는 Sass 문법을 알지 못하기 때문에 Sass(.scss) 파일을 css 파일로 transpile(compile)해야 함

-   scss 파일 transpile 명령어

    -   `transpile할 scss 파일의 경로:transpile 후 생성될 css 파일의 경로`

    ```bash
    $ sass foo.scss:foo.css
    ```

-   특정 폴더 내 scss 파일 전부 transpile하는 명령어

    -   `input 폴더 경로: output 폴더 경로`

    ```bash
    $ sass src/sass:dist/css
    ```

-   직접 명령어를 작성하는 대신, npm scripts를 사용해보자

    ```json
    {
    	"name": "sass-project",
    	"version": "1.0.0",
    	"description": "",
    	"main": "index.js",
    	"scripts": {
    		"build:sass": "sass src/sass:dist/css"
    	},
    	"keywords": [],
    	"author": "",
    	"license": "ISC"
    }
    ```

    ```bash
    $ npm run build:sass
    ```

-   scss 파일 transpile 시, 2가지 스타일 선택 가능

    -   1. `expanded`: 표준 css 파일 생성 (기본값)
    -   2. `compressed`: 압축된 css 파일 생성

    ```bash
    $ sass --style expanded src/sass:dist/css
    ```

    ```bash
    $ sass --style compressed src/sass:dist/css
    ```

-   scss 파일의 변경을 감지하여, 변경될 때마다 transpile하여 기존 css 파일을 자동 업데이트해주는 명령어

    ```bash
    $ sass --watch src/sass:dist/css
    ```

## 🔹 SASS vs SCSS

-   Sass는 SASS 표기법(.sass)과 SCSS 표기법(.scss)이 있음
    -   SCSS: Sassy CSS로 SASS보다 좀 더 CSS 친화적인 표기법
-   이전에는 SASS 표기법이 기본 표기법이었으나, Sass 3.0부터 SCSS 표기법이 기본 표기법이 됨

    |                  |   SCSS   |       SASS        |  CSS   |
    | :--------------: | :------: | :---------------: | :----: |
    | **중괄호** `{}`  |    O     | X (들여쓰기 사용) |   O    |
    | **세미콜론 `;`** |    O     |         X         |   O    |
    | `:` **뒤 공백**  |    X     |         O         |   X    |
    |    **Mixin**     |  @mixin  |         =         |   X    |
    |   **Include**    | @include |         +         |   X    |
    |    **확장자**    | `.scss`  |      `.sass`      | `.css` |
