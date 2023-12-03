# ✔ Concurrent 모드

> 참고) [리액트 18의 신기능 - Concurrent Rendering, Automatic Batching 등](https://www.freecodecamp.org/korean/news/riaegteu-18yi-singineung-dongsiseong-rendeoring-concurrent-rendering-jadong-ilgwal-ceori-automatic-batching-deung/)

## ▶ 블로킹 vs 논블로킹 렌더링

- 리액트의 concurrent 모드를 통해 논블로킹(non-blocking) 렌더링이 가능해짐
- concurrent 모드 이전에는 렌더링을 한번 시작하면 중간에 멈출 수가 없었음

  - 따라서, 컴포넌트 개수가 많은 경우 사용자의 요청에 바로 반응할 수 없었음

- concurrent 모드에서는 렌더링 과정을 여러 개의 작업으로 나눠서 실행 중인 작업을 중단하거나 중단된 작업을 재개할 수 있음

  - 작업이 일정 시간을 초과하거나, 현재 실행 중인 작업보다 우선순위가 더 높은 작업이 들어오면 현재 작업을 중단할 수 있음

## ▶ 작업의 우선순위를 통한 효율적인 CPU 사용

- 렌더링 작업별로 우선순위를 부여하면 높은 우선순위를 가진 작업을 먼저 처리함으로써 CPU를 효율적으로 사용할 수 있음

## ▶ `Suspense`로 가능해진 컴포넌트 함수 내 비동기 처리

- Suspense는 렌더링 과정에서 API 호출과 같은 **비동기 처리를 지원**하는 기능임
- Suspense는 비동기 처리가 완료될 때까지 로딩 애니메이션과 같은 시각 효과를 보여 줄 방법을 제공함

  - 이후 비동기 처리가 완료되면 중단했던 렌더링을 재개함

### 🔹 컴포넌트 함수 내에서 비동기로 모듈 가져오기

- `Suspense` 컴포넌트와 `lazy` 함수를 사용하면 모듈의 비동기 다운로드를 렌더링 과정에 자연스럽게 포함시킬 수 있음

  - `lazy` 함수를 동적 임포트와 함께 호출하면 모듈의 비동기 다운로드를 도와주는 컴포넌트가 반환됨
  - Suspense의 자식 컴포넌트에서 비동기 처리가 시작되면, Suspense 컴포넌트 내부의 모든 렌더링이 멈춘 후 fallback 속성값으로 입력된 컴포넌트가 렌더링됨
  - `lazy` 함수로 만들어진 VideoPlayer 컴포넌트가 렌더링될 때 분할된 코드를 다운로드 받는데, 코드를 받기 전까지 Suspense 내부는 Loading 컴포넌트가 렌더링됨

  ```js
  // App.js
  import { lazy, Suspense } from "react";
  import Loading from "./Loading";

  const VideoPlayer = lazy(() => import("./VideoPlayer"));

  export default function App() {
    return (
      <div>
        <h1>suspense example</h1>
        <Suspense fallback={<Loading />}>
          <h3>watch video</h3>
          <VideoPlayer />
        </Suspense>
      </div>
    );
  }
  ```

### 🔹 컴포넌트 함수 내에서 API로 데이터 받기

- Suspense 컴포넌트 내부에서는 렌더링 중이라고 하더라도 API를 호출할 수 있음
- concurrent 모드로 동작하지 않는 리액트 버전의 경우, 비동기 렌더링을 지원하지 않기 때문에 렌더링 중에 비동기 처리가 발생하면 멈췄다가 나중에 중단된 부분부터 다시 시작할 수 없음

  - 따라서, 동기 렌더링에서의 Suspense는 fallback으로 입력된 컴포넌트가 바로 사용되고, 비동기 처리가 끝나면 다시 한번 렌더링됨

- 렌더링 과정에서 비동기로 데이터를 받는 코드를 작성하기 전 필요한 패키지를 먼저 설치해보자

  - `react-cache`는 렌더링 과정에서 비동기 처리를 지원하기 위해 리액트에서 제공하는 패키지임

- 'Profile.js' 파일을 생성하고, 컴포넌트 함수 내에서 API를 호출하는 코드를 작성하자

  - `read` 메서드를 호출했을 때 이미 받은 데이터가 있다면 그 데이터를 사용하고, 없다면 fetchUser 함수가 실행됨
  - fetchUser 함수가 반환하는 Promise 객체와 함께 예외를 발생시킴
  - Promise 객체와 함께 예외가 발생하면, 부모로 거슬러 올라가면서 가장 가까운 Suspense 컴포넌트를 찾게됨
  - 그러면 Suspense 컴포넌트는 내부 영역을 fallback으로 대체하고, 추후 Promise가 settled 상태가 되면 다시 렌더링하게 됨
  - 참고) `lazy` 함수로 생성한 컴포넌트도 비동기 처리가 시작되면 Promise 객체와 함께 예외를 발생시킴

  ```js
  // profile.js
  import { unstable_createResource } from "react-cache";

  function fetchUser(userId) {
    return new Promise((resolve) =>
      setTimeout(() => resolve({ userId, name: "mike", age: 23 }), 2000)
    );
  }

  const UserCache = unstable_createResource(fetchUser);

  function Profile() {
    const user = UserCache.read(123);
    return (
      <div>
        <p>name: {user.name}</p>
        <p>age: {user.age}</p>
      </div>
    );
  }
  ```

### 🔹 Suspense 내부에서 여러 개의 프로미스 발생시키기

- Suspense 컴포넌트 내부에서 예외로 발생하는 모든 Promise 객체가 settled 상태가 되기 전까지는 Loading 컴포넌트가 렌더링됨

  ```js
  // App.js
  // ...
  const VideoPlayer = lazy(() => import("./VideoPlayer"));

  export default function App() {
    return (
      <div>
        <h1>suspense example</h1>
        <Suspense fallback={<Loading />}>
          <h3>watch video</h3>
          <VideoPlayer />
          <Profile />
        </Suspense>
      </div>
    );
  }
  ```
