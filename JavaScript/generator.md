# ✔ 제너레이터

- 제너레이터(generator): 함수의 실행을 중간에 멈추고 재개할 수 있는 기능
- 제너레이터를 사용하면 필요한 순간에 값을 계산해서 전달할 수 있기 때문에 메모리 측면에서 효율적임

### 🔹 제너레이터 이해하기

- 제너레이터 함수는 별표 `*`와 함께 정의됨

  - `yield` 키워드를 사용해 함수의 실행을 멈출 수 있음
  - 제너레이터 함수를 실행(호출)하면, 제너레이터 객체만 반환되고 실제 함수 내부 코드는 실행되지 않음
  - 제너레이터 객체는 `next`, `return`, `throw` 메서드를 가지고 있음

  ```js
  function* f1() {
    yield 10;
    yield 20;
    return "finished";
  }

  const gen = f1();
  ```

- `next` 메서드를 호출하면, `yield` 키워드를 만날 때까지 실행되고 데이터 객체를 반환

  - `yield` 키워드를 만나면, 데이터 객체는 `done: false`가 됨
  - `yield` 키워드를 만나지 못하면, 데이터 객체는 `done: true`가 됨

  ```js
  console.log(gen.next()); // {value: 10, done: false}
  console.log(gen.next()); // {value: 20, done: false}
  console.log(gen.next()); // {value: 'finished', done: true}
  ```

- `return` 메서드를 호출하면, 데이터 객체는 `done: false`가 됨

  - 이후에 `next` 메서드를 호출해도 `done: false`가 됨

  ```js
  console.log(gen.next()); // {value: 10, done: false}
  console.log(gen.return("abc")); // {value: 'abc', done: true}
  console.log(gen.next()); // {value: undefined, done: true}
  ```

- `throw` 메서드를 호출하면, 예외가 발생한 것으로 처리되기 때문에 catch 문으로 들어가고 데이터 객체는 `done: false`가 됨

  ```js
  function* f1() {
    try {
      yield 10;
      yield 20;
    } catch (e) {
      console.log(e); // some error
    }
  }

  const gen = f1();
  console.log(gen.next()); // {value: 10, done: false}
  console.log(gen.throw("some error")); // {value: undefined, done: true}
  ```

- 제너레이터 객체는 반복 가능(iterable)하면서 반복자(iterator)임

  - 반복자(iterator)인 객체의 특징
    - `next` 메서드를 가지고 있음
    - `next` 메서드는 `value`와 `done` 속성값을 가진 객체를 반환함
    - `done` 속성값은 작업이 끝났을 때 참이 됨
  - 반복 가능(iterable)한 객체의 특징
    - `Symbol.iterator` 속성값으로 함수를 가지고 있음
    - 해당 함수를 호출하면 반복자(iterator)를 반환함

  ```js
  // Array는 반복 가능(iterable)한 객체임
  const arr = [10, 20, 30];
  const iter = arr[Symbol.iterator]();

  console.log(iter.next()); // {value: 10, done: false}
  ```

  ```js
  // 제너레이터 객체는 반복 가능(iterable)한 객체임
  function* f1() {
    yield 10;
    yield 20;
  }

  const gen = f1();

  console.log(gen[Symbol.iterator]() === gen); // true
  ```

- 반복 가능(iterable)한 객체는 `for` ~ `of`문과 전개 연산자에서 유용함

  - `for` ~ `of`문은 반복 가능한 객체로부터 반복자(iterator)를 얻어, `next` 메서드를 호출하면서 `done: true`가 될 때까지 반복함
  - 전개 연산자도 `done: true`가 될 때까지 값을 펼침

  ```js
  for (const v of f1()) {
    console.log(v);
  }
  ```

  ```js
  const arr = [...f1()];
  console.log(arr); // [10, 20]
  ```

### 🔹 제너레이터 활용하기

- 제너레이터를 이용하면 함수형 프로그래밍의 대표적인 함수를 쉽게 구현 가능함

  - 제너레이터를 사용하면 연산이 필요한 순간에만 실행됨 👉 지연 평가 (lazy evaluation)
  - 제너레이터를 사용하면 필요한 연산만 수행됨
    - 따라서, 자연수의 집합처럼 무한대로 값을 표현하는 것도 가능함

  ```js
  function* map(iter, mapper) {
    for (const v of iter) {
      yield mapper(v);
    }
  }

  map([1, 2, 3], (n) => n * 10);
  ```

  ```js
  function* natureNumber() {
    let v = 1;
    while (true) {
      yield v++;
    }
  }

  const values = naturalNumbers();
  ```

- 제너레이터 함수에서 다른 제너레이터 함수를 호출할 때는 `*yield` 키워드를 이용

  - `*yield` 키워드 오른쪽에는 반복 가능한 객체가 올 수 있음

  ```js
  function* f1() {
    yield 2;
    yield 3;
  }

  function* f2() {
    yield 1;
    yield* f1();
    yield 4;
  }

  console.log(...f2()); // 1 2 3 4
  ```

- `next` 메서드의 인수를 통해 제너레이터 함수로 데이터를 전달할 수 있음

  - `next` 메서드를 통해서 전달된 인수는 `yield` 키워드의 결과값으로 받을 수 있음

  ```js
  function* f1() {
    const data = yield;
    console.log(data); // 10
  }

  const gen = f1();

  gen.next(10);
  ```
