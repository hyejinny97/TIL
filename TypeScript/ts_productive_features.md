# ✔ 생산성을 높이는 타입스크립트의 기능

## ▶ 타입 추론 (Type Inference)

- 명시적으로 타입 코드를 작성하지 않아도 타입스크립트가 타입을 추론할 수 있는 경우가 많음

### 🔹 let 변수의 타입 추론

- 타입을 명시하지 않아도 할당된 값에 의해 타입이 추론됨

  ```ts
  let v1 = 123; // v1 타입: number
  let v2 = "abc"; // v2 타입: string

  v1 = "a"; // 타입 에러
  v2 = 456; // 타입 에러
  ```

### 🔹 const 변수의 타입 추론

- const 변수는 let 변수보다 엄격하게 타입이 결정됨

  - `typeof` 키워드는 변수의 타입을 추출할 때 사용됨
  - 아래에서 const 변수는 리터럴 자체가 타입이 됨

  ```ts
  const v1 = 123; // v1 타입: 123
  const v2 = "abc"; // v2 타입: "abc"

  let v3: typeof v1 | typeof v2; // v3 타입: 123 | "abc"
  ```

### 🔹 배열과 객체의 타입 추론

- 배열/객체의 타입을 정의하지 않아도 추론됨

  - 비구조화 할당의 경우에도 타입 추론이 됨

  ```ts
  const arr = [10, 20, 30]; // arr 타입: number[]
  const [n1, n2, n3] = arr; // 각 n1, n2, n3 타입: number
  ```

  ```ts
  const obj = { id: "abcd", age: 123, language: "korean" };
  // obj 타입: { id: string; age: number; language: string; }
  const { id, age, language } = obj;
  ```

- 여러 가지 타입으로 구성된 배열에서 타입 추론하는 경우, 여러 가지 타입을 하나로 통합하는 과정을 거쳐야 함

  - 다른 타입으로 할당 가능한 타입은 제거됨
  - 제거 후 남은 모든 타입은 유니온 타입으로 만들어짐

  ```ts
  interface Person {
    name: string;
    age: number;
  }

  interface Korean extends Person {
    liveInSeoul: boolean;
  }

  interface Japanese extends Person {
    liveInTokyo: boolean;
  }

  const p1: Person = { name: "mike", age: 23 };
  const p2: Korean = { name: "mike", age: 25, liveInSeoul: true };
  const p3: Japanese = { name: "mike", age: 27, liveInTokyo: false };

  const arr1 = [p1, p2, p3]; // arr1 타입: Person[]
  const arr2 = [p2, p3]; // arr2 타입: (Korean, Japanese)[]
  ```

### 🔹 함수의 매개변수와 반환값에 대한 타입 추론

- 함수의 매개변수와 반환값도 타입 추론이 적용됨

  - 기본값이 있는 매개변수는 자동으로 타입 정보가 추가됨
  - 함수의 반환값도 타입 추론에 의해 자동으로 타입 정보가 추가됨

  ```ts
  function func1(a = "abc", b = 10) {
    return `${a} ${b}`;
  }
  // func1(a?: string, b?: number): string
  ```

- 함수 내에서 return 키워드가 여러 번 등장해도 타입 추론이 적용됨

  ```ts
  function func2(value: number) {
    if (value < 10) {
      return value;
    } else {
      return `${value} is too big`;
    }
  }
  // func2(value: number): string | number
  ```

## ▶ 타입 가드 (Type Guard)

- 타입 가드는 조건문을 이용해 타입의 범위를 좁히는 기능임
- 타입 가드를 잘 활용하면 불필요한 타입 단언(Type Assertion) 코드를 피할 수 있음

  - 타입스크립트에서 타입 가드가 없었다면, 아래처럼 `as` 키워드를 이용해서 타입 단언을 해야함

  ```ts
  function print(value: number | string) {
    if (typeof value === "number") {
      console.log((value as number).toFixed(2));
    } else {
      console.log((value as string).trim());
    }
  }
  ```

### 🔹 `typeof` 키워드

- 타입스크립트는 `typeof`를 통해 아래 if문 내부에서 value를 숫자로 인식함

  - 따라서, `as` 키워드를 사용해 타입 단언을 할 필요가 없음

  ```ts
  function print(value: number | string) {
    if (typeof value === "number") {
      console.log(value.toFixed(2));
    } else {
      console.log(value.trim());
    }
  }
  ```

### 🔹 `instanceof` 키워드

- 클래스의 경우에 `instanceof` 키워드가 타입 가드로 사용될 수 있음

  ```ts
  class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  }

  class Product {
    name: string;
    price: number;

    constructor(name: string, price: number) {
      this.name = name;
      this.price = price;
    }
  }

  function print(value: Person | Product) {
    if (value instanceof Person) {
      console.log(value.age);
    } else {
      console.log(value.price);
    }
  }

  const person = new Person("mike", 23);
  print(person);
  ```

- 주의) 인터페이스의 경우에는 `instanceof` 키워드를 사용할 수 없음

  - ∵ 인터페이스는 컴파일 후에 삭제되므로 `instanceof` 키워드의 오른쪽에 올 수 없음
  - 대신, 식별 가능한 유니온 타입을 이용해 인터페이스를 구별할 수 있음

### 🔹 식별 가능한 유니온 (discriminated union) 타입

- 인터페이스에서 식별 가능한 유니온 타입은 같은 이름의 속성을 정의하고 속성의 타입은 모두 겹치지 않게 정의하면 됨

  - 즉, 식별 가능한 유니온 타입은 값의 집합에서 서로 겹치는 부분이 없음
  - 아래 두 인터페이스에서 공통 속성으로 존재하고 속성값이 서로 다른 'type' 속성이 식별 가능한 유니온 타입이라고 할 수 있음
  - value의 'type' 속성의 값을 비교하는 것으로 타입 가드가 동작함

  ```ts
  interface Person {
    type: "person";
    name: string;
    age: number;
  }

  interface Product {
    type: "product";
    name: string;
    price: number;
  }

  function print(value: Person | Product) {
    if (value.type === "person") {
      console.log(value.age);
    } else {
      console.log(value.price);
    }
  }
  ```

- 식별 가능한 유니온 타입은 서로 겹치지 않기 때문에 switch문에서 사용하기 좋음

  ```ts
  function print(value: Person | Product) {
    switch (value.type) {
      case "person":
        console.log(value.age);
        break;
      case "product":
        console.log(value.price);
        break;
    }
  }
  ```

### 🔹 타입을 검사하는 함수

- 타입을 검사하는 함수를 타입 가드로 활용할 수도 있음

  - `is` 키워드 왼쪽에는 매개변수 이름을, 오른쪽에는 타입 이름을 넣음

  ```ts
  function isPerson(x: any): x is Person {
    return (x as Person).age !=== undefined;
  }

  function print(value: Person | Product) {
    if (isPerson(value)) {
      console.log(value.age);
    } else {
      console.log(value.price);
    }
  }
  ```

### 🔹 `in` 키워드

- `in` 키워드를 이용해 특정 속성 이름의 존재를 검사하는 것으로 타입 가드가 동작함

  ```ts
  function print(value: Person | Product) {
    if ("age" in value) {
      console.log(value.age);
    } else {
      console.log(value.price);
    }
  }
  ```
