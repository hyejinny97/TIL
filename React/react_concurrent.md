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
