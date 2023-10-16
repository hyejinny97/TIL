# ✔ 타입 호환성

- 타입 호환성: 어떤 타입을 다른 타입으로 취급해도 되는지 판단하는 것
- 타입스크립트는 타입 호환성을 통해 컴파일 타임에 호환되지 않는 타입을 찾아냄
- 타입 A가 타입 B에 `할당 가능`하다. === 타입 A는 타입 B의 `서브타입(subtype)`이다.

  - 즉, A 타입의 `값의 집합`이 B 타입의 `값의 집합`에 포함되면 A 타입은 B 타입에 할당 가능함

## ▶ 숫자와 문자열의 타입 호환성

- 숫자 타입과 문자열 타입은 서로 할당 가능하지 않음

  ```ts
  function func1(a: number, b: number | string) {
    const v1: number | string = a;
    const v2: number = b; // 타입 에러
  }
  ```

  ```ts
  function func2(a: 1 | 2) {
    const v1: 1 | 3 = a; // 타입 에러
    const v2: 1 | 2 | 3 = a;
  }
  ```

## ▶ 인터페이스의 타입 호환성

- 타입스크립트는 값 자체의 타입보다는 값이 가진 내부 구조에 기반해서 타입 호환성을 검사함

  - 덕 타이핑 (duck typing), 구조적 타이핑 (structural typing)

- 인터페이스 A가 인터페이스 B로 할당 가능하기 위한 조건

  - 1️⃣ B에 있는 모든 필수 속성의 이름이 A에도 존재해야 함
  - 2️⃣ 같은 속성 이름에 대해, A의 속성이 B의 속성에 할당 가능해야 함

- 아래 Person과 Product는 서로 할당이 가능함

  ```ts
  interface Person {
    name: string;
    age: number;
  }

  interface Product {
    name: string;
    age: number;
  }

  const person: Person = { name: "mike", age: 23 };
  const product: Product = person;
  ```

### 🔹 선택 속성이 타입 호환성에 미치는 영향

- 만약 Person의 age가 선택 속성이라면, Person은 Product에 할당 가능하지 않음

  - ∵ Person 값의 집합이 Product 값의 집합보다 커지기 때문

  ```ts
  interface Person {
    name: string;
    age?: number;
  }

  // ...

  const person: Person = { name: "mike" };
  const product: Product = person; // 타입 에러
  ```

- 만약 Product의 age가 선택 속성이라면, Person은 Product에 할당하는데 문제 없음

  - ∵ Product 값의 집합이 Person 값의 집합보다 더 커질뿐임

  ```ts
  // ...

  interface Product {
    name: string;
    age?: number;
  }

  const person: Person = { name: "mike", age: 23 };
  const product: Product = person;
  ```

### 🔹 추가 속성과 유니온 타입이 타입 호환성에 미치는 영향

- 추가 속성이 있으면 값의 집합은 더 작아짐

  ```ts
  interface Person {
    name: string;
    age: number;
    gender: string;
  }
  ```

- 유니온 타입이 있으면 값의 집합은 더 커짐

  ```ts
  interface Product {
    name: string;
    age: number | string;
  }
  ```

## ▶ 함수의 타입 호환성

- 함수는 호출하는 시점에 문제가 없어야 할당 가능함
- 함수 타입 A가 함수 타입 B로 할당 가능하기 위한 조건

  - 1️⃣ A의 매개변수 개수가 B의 매개변수 개수보다 적어야 함
  - 2️⃣ 같은 위치의 매개변수에 대해 B의 매개변수가 A의 매개변수로 할당 가능해야 함
  - 3️⃣ A의 반환값은 B의 반환값으로 할당 가능해야 함

  ```ts
  type F1 = (a: number, b: string) => number;
  type F2 = (a: number) => number;
  type F3 = (a: number) => number | string;

  let f1: F1 = (a, b) => 1;
  let f2: F2 = (a) => 1;
  let f3: F3 = (a) => 1;

  f1 = f2;
  f2 = f1; // 타입 에러
  f2 = f3; // 타입 에러
  ```

### 🔹 배열의 map 메서드를 통해 살펴보는 함수의 타입 호환성

- 아래 addOne 함수는 map 메서드가 입력받는 함수의 타입에 할당 가능함

  - 아래 map 메서드의 제너릭으로 입력한 number는 매개변수 함수의 반환 타입을 의미

  ```ts
  function addOne(value: number): number {
    return value + 1;
  }

  const result = [1, 2, 3].map<number>(addOne);
  // (value: number, index: number, array: number[]) => number
  ```
