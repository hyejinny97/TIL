# 프로젝트 06 - 영화 사이트 웹 구현

## 과정
- [목표](#목표)
- [준비 사항](#준비-사항)
- [요구 사항](#요구-사항)
- [프로젝트 결과 완성본](#프로젝트-결과-완성본)
- [프로젝트 후기](#프로젝트-후기)

## 목표

- HTML를 통한 웹 페이지 마크업
- CSS를 통한 선택자 활용 및 속성 부여
- 시맨틱 태그를 활용한 기본 레이아웃 구성
- 영화 추천 사이트 메인 레이아웃 구성

## 준비 사항

1. **(필수)** HTML/CSS 환경 구성
2. **(필수)** 웹 페이지를 위한 Assets 다운로드
    - `**index.html`에 마크업을 작성하여 주세요.**
    - `reboot.css` 는 브라우저 기본 설정 CSS를 모두 동일하게 설정하기 위해 사용됩니다.        
    - `style.css` 에 스타일을 작성합니다.
    - `images` 폴더에는 활용할 포스터 이미지가 있습니다.

## 요구 사항


> HTML/CSS을 활용하여 목표로 하는 웹사이트의 레이아웃을 구성합니다. 아래의 필수 사항을 제외한 요소는 자유롭게 꾸며 주세요.

  ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/75c9b7b2-a012-4c52-9df1-71153248d3f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220902T080502Z&X-Amz-Expires=86400&X-Amz-Signature=629c8c33a973a123aa2418db1cb27eff2a17e4a57bf655e2dfb580c70b2d3531&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)



> HTML 기초

- `DOCTYPE`은 html입니다.
- `html`의 언어는 한국어(ko)입니다.
- `meta` 태그에 인코딩 설정을 UTF-8로 설정 해주세요.
- `meta` 태그에 기본 viewport 설정을 해주세요. (width: device-width, initial-scale: 1.0)
- `title` 태그는 영화 추천 사이트 라고 설정 해주세요.



> `header`

웹 사이트의 헤더 부분에는 로고 이미지와 네비게이션 바를 구성합니다.

- 속성
    - 헤더는 항상 상단에 유지 됩니다. **(sticky)**
    - 높이는 80px이며, 좌우 안쪽 여백(padding)은 40px입니다.
- 이미지 배치
    - 로고 이미지는 좌측에 배치합니다.
    - 로고 이미지의 높이는 60px입니다.
    - 로고 이미지는 `images/logo.png` 입니다.
- 네비게이션 바 (`nav`)
    - 네비게이션 바의 항목은 우측에 배치합니다.
    - 총 4개의 항목이 배치되며, 각각 임의의 링크(`#`) 으로 설정합니다.
        - 수직 정렬을 통해 중앙으로 일치시킵니다.



> title `section`

서비스를 소개하는 문구와 배경 이미지가 있는 섹션을 구성합니다.

- 속성
    - 높이는 320px이며, `header` 의 높이만큼 상단 여백을 설정합니다.
    - 수직 정렬을 통해 중앙으로 일치시킵니다.
    - 배경 이미지는 적절하게 삽입하고, 이미지에 맞게 사이즈와 위치를 조절 합니다.
    - `h1` 태그를 활용하여 사이트의 제목을 작성합니다.



> `aside`

<aside>
👉 좌측 레이아웃에 장르 목록을 구성합니다.
</aside>

- aside와 movie는 2:8의 비율을 가집니다.

- 속성
    - 좌측에 위치합니다.
    - 상하좌우 안쪽 여백(padding)은 1rem입니다.
    - `h2` 태그를 활용하여 `장르 목록` 이라고 작성합니다.
    - 개별 장르는 `ul` 태그를 활용 하되 기본 안쪽 여백을 제거합니다.



> movie `section`

<aside>
👉 먼저 3개를 한 줄로 배치하는 것만 진행하고, 추후에 6개로 늘려보세요.
</aside>

- 속성
    - 우측에 위치하며, `aside` 를 제외한 모든 너비를 가집니다.
    - 상하좌우 안쪽 여백(padding)은 24px입니다.
    - 적절한 배경 색상을 적용 시킵니다.
    - `h2` 태그를 활용하여 `실시간 영화 순위` 라고 작성하며, 가운데 정렬을 합니다.
    - 영화는 한 행에 3개씩 배치하며, 각각 너비는 동일합니다.
    - 영화 이미지는 너비를 300px로 설정합니다.
    - 이미지 하단에는 영화명을 작성합니다.



> `footer`

푸터를 구성합니다.

- 속성
    - 푸터는 항상 하단에 유지 됩니다.
    - 높이는 40px이며, 모든 내용은 수직/수평 가운데 정렬을 합니다.
    - 적절한 배경 색상을 적용 시킵니다.


## 프로젝트 결과 완성본

![](../../gif/project_01_movie_animation.gif)



## 프로젝트 후기
> 페어프로그래밍 후기

오늘 처음 pair programming이라는 걸 통해 웹 페이지를 같이 구현해봤다. 우리 조는 2명밖에 없어서 1시간마다 driver, navigator의 역할을 바꿔가며 진행했다. 과연 내가 의사소통을 하면서 동시에 코드를 짤 수 있을까 걱정도 됐지만, 생각보다 같이 의견을 나누면서 한줄씩 코드를 짜나가는게 재미있었고 혼자 구현했을 때보다 시간도 훨씬 단축됐다. 내가 driver일때 조원의 navigation에 따라가면서 체계적으로 HTML/CSS 작성하는 방법이랑 CSS의 새로운 속성에 대해서 배울 수 있었다. 반면 내가 navigator일 때는 전체적인 구조를 예상하며 방향을 잡아줬어야했는데 내가 말하는 과정에서 확실히 개념을 다잡을 수 있었던 것 같아 좋았다.

아쉬운 점이 있다면, 오늘 live share 확장프로그램을 통해 서로 코드를 공유하면서 짜야 했었는데, 사용이 익숙치않아 시간관계 상 각자 코드를 짜고 압축 파일을 주고 받는 식으로 진행되었다. live share 사용법을 찾아본 뒤에 다시 시도해봐야할 것 같다.

> 웹 개발 후기

일단 명세서에 나와있는 대로 모든 요소를 구현했고, 가이드에 나와있는 결과물과 유사하게 구현을 했다. 여기에 몇가지 요소를 더 추가했는데, 헤더 네이게이션 부분의 링크들을 호버하면 배경색과 글자색이 바뀌도록 했다. 또한 영화 이미지를 호버했을때 스케일과 트랜지션을 걸어줘서 천천히 이미지가 커질 수 있게끔 했다. 
여기에 더해 영화 이미지를 호버했을때 검정 배경이 오버레이되면서 흰색 글씨를 띄우게 하고 싶었는데, 여러가지 방법을 논의하고 코드를 짜봤지만 원하는 대로 구현이 되진 않았다. 좀 더 연구를 한 후에 다시 시도해봐야할 것 같다.
