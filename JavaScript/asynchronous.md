# ✔ 비동기 프로그래밍

## ▶ 프로미스 (Promise)

- 프로미스: 비동기 상태를 값으로 다룰 수 있는 객체
- ES2015에 JS 표준이 됨
- 프로미스가 널리 보급되기 전에는 콜백 패턴을 많이 사용했음

### 🔹 프로미스 이해하기

- 콜백(callback) 패턴의 문제점

  - 콜백이 조금만 중첩돼도 코드가 상당히 복잡해짐
  - 콜백 패턴은 코드의 흐름이 순차적이지 않기 때문에 가독성이 떨어짐
  - 반면, 프로미스를 사용하면 코드가 순차적으로 실행되게 작성 가능

- 프로미스의 3가지 상태

  ```
  1️⃣대기 중(Pending) ⇨ 처리됨(Settled)
                            ↙     ↘
          2️⃣이행됨(Fulfilled)    3️⃣거부됨(Rejected)
  ```

- 프로미스를 생성하는 방법

  - 방법1) `new` 키워드를 사용해 프로미스 생성

    - pending 상태의 프로미스 생성
    - 비동기로 어떤 작업을 수행한 후, 성공했을 때 resolve 함수를 호출하고 실패했을 때 reject 함수를 호출하면 됨

    ```js
    const p = new Promise((resolve, reject) => {
      // resolve()
      // reject()
    });
    ```

  - 방법2) `reject` 메서드 사용해 프로미스 생성

    - rejected 상태의 프로미스 생성

    ```js
    const p = Promise.reject("error message");
    ```

  - 방법3) `resolve` 메서드 사용해 프로미스 생성

    - fulfilled 상태의 프로미스 생성
    - 입력값이 프로미스인 경우, 그 프로미스 객체 그대로 반환됨
    - 입력값이 프로미스가 아닌 경우, 그 값을 데이터로 가진 프로미스를 반환함

    ```js
    const p = Promise.resolve(123);
    const p = Promise.resolve(
      new Promise((resolve) => setTimeout(() => resolve(10), 1000))
    );
    ```

- `promise.then(onFulfilled, onRejected)`

  - settled 상태의 프로미스를 처리하는 메서드
  - 매개변수
    - `onFulfilled`: 프로미스가 fulfilled될 때 호출되는 Function으로, 이행 값(fulfillment value) 하나를 인수로 받음
    - `onRejected`: 프로미스가 rejected될 때 호출되는 Function으로, 거부 이유(rejection reason) 하나를 인수로 받음
  - 반환값: 프로미스
    - `onFulfilled`/`onRejected` 함수에서 프로미스를 반환하는 경우, 그 프로미스 객체 그대로 반환함
    - 프로미스가 아닌 값을 반환하는 경우, 그 값을 데이터로 가진 프로미스를 반환함
  - 특징
    - 항상 프로미스를 반환하므로, 하나의 프로미스로부터 연속적으로 `then` 메서드를 호출할 수 있음
    - `onFulfilled`/`onRejected` 함수 내부에서 error가 발생하면 rejected 상태의 프로미스를 반환함
    - rejected 상태의 프로미스는 `onRejected` 함수가 존재하는 `then`을 만날 때까지 이동하게 됨
    - `then` 메서드는 항상 연결된 순서대로 호출되기 때문에, 비동기 작업을 동기 프로그래밍 방식으로 코드를 작성할 수 있게 해줌

  ```js
  requestData1()
    .then((data) => {
      return requestData2();
    })
    .then((data) => {
      return data + 1;
    })
    .then((data) => {
      throw new Error("some error");
    })
    .then(null, (error) => {
      console.log(error); // some error
    });
  ```

- `promise.catch(onRejected)`

  - 프로미스 수행 중 발생한 예외를 처리하는 메서드
  - 매개변수
    - `onRejected`: 프로미스가 rejected될 때 호출되는 Function으로, 거부 이유(rejection reason) 하나를 인수로 받음
  - 반환값: 프로미스
  - 특징
    - `then` 메서드의 `onRejected` 함수와 같은 역할을 함
    - 예외 처리는 `then` 메서드의 `onRejected` 함수보다 `catch` 메서드를 이용하는게 가독성 면에서 더 좋음

  ```js
  Promise.reject(10)
    .then((data) => {
      console.log(data);
      return 20;
    })
    .catch((error) => {
      console.log(error); // 10
      return 30;
    })
    .then((data) => {
      console.log(data); // 30
      return 40;
    });
  ```

- `promise.finally(onFinally)`

  - 프로미스가 fulfilled 또는 rejected 상태일 때 호출되는 메서드
  - 매개변수
    - `onFinally`: 프로미스가 settled(fulfilled 또는 rejected)될 때 호출되는 function
  - 반환값: 프로미스
    - 주의) 새로운 프로미스를 생성해 반환하지 않고, **이전에 사용된 프로미스를 그대로 반환함**
  - 특징
    - 프로미스 체인의 가장 마지막에 사용됨
    - 결과와 상관 없이 프로미스가 settled될 때 무언가를 처리하려는 경우에 유용함
    - 이전에 사용된 프로미스를 그대로 반환하므로, settled 상태인 프로미스의 데이터를 건드리지 않고 추가 작업을 할 때 유용함

  ```js
  function requestData() {
    return fetch()
      .catch((error) => {
        console.log(error);
      })
      .finally(() => {
        console.log("finished");
      });
  }

  requestData().then((data) => console.log(data));
  ```

### 🔹 프로미스 활용하기

- `Promise.all(iterable)`

  - 여러 개의 프로미스를 병렬로 처리할 때 사용하는 함수
  - 매개변수
    - `iterable`: 순회 가능한(iterable) 객체
    - iterable 객체의 요소로 프로미스가 아닌 값을 넣으면, 그 값을 데이터로 갖는 settled 상태의 프로미스처럼 처리됨
  - 반환값: 프로미스
    - 입력된 모든 프로미스가 settled 상태가 되어야 settled 프로미스를 반환함
    - 입력된 프로미스들 중 하나라도 rejected 상태가 되면 rejected 프로미스를 반환함
  - 특징
    - `then` 메서드를 이용한 프로미스 체인에서는 각 비동기 작업이 병렬로 처리되지 않는 단점이 있는데, `Promise.all()` 함수를 사용해 이를 해결할 수 있음
    - 비동기 함수 간에 서로 의존성이 없다면 병렬로 처리하는게 더 빠름

  ```js
  Promise.all([requestData1(), requestData2()]).then(([data1, data2]) => {
    console.log(data1, data2);
  });
  ```

- `Promise.race(iterable)`

  - 여러 개의 프로미스 중에서 가장 빨리 처리된 프로미스를 반환하는 함수
  - 매개변수
    - `iterable`: 순회 가능한(iterable) 객체
  - 반환값: 프로미스
    - 입력된 프로미스들 중 하나라도 settled 상태가 되면 settled 프로미스를 반환함
  - 특징
    - 일정 시간 안에 데이터를 받아오지 못하면 특정 처리를 하게 구현할 수 있음

  ```js
  Promise.race([
    requestData(),
    new Promise((_, reject) => setTimeout(reject, 3000)),
  ])
    .then((data) => console.log(data))
    .catch((error) => console.log(error));
  ```

### 🔹 프로미스 사용 시 주의할 점

- `return` 키워드를 잊지 말자

  - `then` 메서드가 반환하는 프로미스 객체의 데이터는 내부 함수가 반환한 값임
  - 따라서, `return` 키워드를 사용하지 않으면 반환한 프로미스 객체의 데이터는 `undefined`가 됨

- 프로미스는 불변 객체임

  - `then` 메서드는 기존 프로미스 객체를 수정하지 않고, 새로운 프로미스를 반환함

- 프로미스를 중첩해서 사용하지 않기

  - 프로미스를 중첩해서 사용하면 콜백 패턴처럼 코드가 복잡해짐
  - 만약, `then` 메서드 내 함수에서 여러 개의 입력값을 받고자 한다면 이전 `then` 메서드에서 `Promise.all` 함수를 사용해 반환해 주면 됨

  ```js
  requestData1()
    .then((result1) => {
      return Promise.all([result1, requestData2(result1)]);
    })
    .then(([result1, result2]) => {
      // ...
    });
  ```

## ▶ async/await

- ES2017에 JS 표준이 됨
- async/await를 이용해서 비동기 코드를 사용하면, 프로미스의 `then` 메서드를 체인 형식으로 호출하는 것보다 가독성이 좋아짐

### 🔹 async/await 이해하기

- async/await 함수는 항상 프로미스를 반환함

  - 함수 내부에서 반환하는 값이 프로미스라면 그 객체 그대로를 반환함
  - 프로미스가 아닌 값을 반환하는 경우, 그 값을 데이터로 가진 프로미스를 반환함
  - 함수 내부에서 error가 발생하는 경우, rejected 상태인 프로미스를 반환함

  ```js
  async function getData() {
    return 123;
  }

  getData().then((data) => console.log(data)); // 123
  ```

  ```js
  async function getData() {
    throw new Error("some error");
  }

  getData().catch((error) => console.log(error)); // some error
  ```

- await 키워드는 async/await 함수 내부에서만 사용됨

  - await 키워드 오른쪽에 프로미스를 입력하면, 그 프로미스가 settled 상태가 될 때까지 기다림

  ```js
  async function getData() {
    const data = await new Promise((resolve) => {
      setTimeout(() => resolve(123), 3000);
    });

    console.log(data); // 123
    return data;
  }

  getData();
  ```

- async/await는 `then` 메서드 체인보다 가독성이 좋음

  - 여러 비동기 함수에 각각 await 키워드를 사용해 호출하면 순차적으로 실행됨
  - 비동기 함수 간에 복잡한 의존성이 존재해도 코드가 직관적임

  ```js
  async function getData() {
    const data1 = await asyncFunc1();
    const data2 = await asyncFunc2();
    return asyncFunc3(data1, data2);
  }
  ```

### 🔹 async/await 활용하기

- async/await 함수 내에서 비동기 함수를 병렬로 실행하는 법

  - 방법1) 각 프로미스를 먼저 생성하고 await 키워드를 나중에 사용
  - 방법2) `Promise.all(iterable)` 함수 사용

  ```js
  // 방법 1
  async function getData() {
    const p1 = asyncFunc1();
    const p2 = asyncFunc2();
    const data1 = await p1;
    const data2 = await p2;
    // ...
  }
  ```

  ```js
  // 방법 2
  async function getData() {
    const [data1, data2] = await Promise.all([asyncFunc1(), asyncFunc2()]);
    // ...
  }
  ```

- async/await 함수 내에서 방생하는 예외는 `try` ~ `catch` 문을 이용해 처리

  ```js
  async function getData() {
    try {
      return await asyncFunc();
    } catch (error) {
      console.log(error);
    }
  }
  ```

- async/await 함수는 Thenable도 프로미스처럼 처리함

  - Thenable: `then` 메서드를 가진 객체로, ES6의 프로미스처럼 동작

  ```js
  class ThenableExample {
    then(resolve, reject) {
      setTimeout(() => resolve(123), 3000);
    }
  }

  async function getData() {
    const rst = await new ThenableExample();
    console.log(rst); // 123
  }
  ```
