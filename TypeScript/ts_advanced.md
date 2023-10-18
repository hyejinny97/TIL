# ✔ 타입스크립트 고급 기능

## ▶ 제네릭

- 제네릭 (generic): 타입 정보가 동적으로 결정되는 타입

  - 같은 규칙을 여러 타입에 적용할 수 있기 때문에 중복 코드를 제거할 수 있음

### 🔹 제네릭 사용하기

- 제네릭은 `<>` 기호를 이용해서 정의하며, 이름은 자유롭게 지정할 수 있음

  - 함수를 호출할 때 타입 T가 결정됨
  - makeArray 함수의 첫번째 매개변수를 알면 타입 T도 알 수 있기 때문에, 호출 시 타입 T의 정보를 명시적으로 전달하지 않아도 됨

  ```ts
  function makeArray<T>(defaultValue: T, size: number): T[] {
    const arr: T[] = [];
    for (let i = 0; i < size; i++) {
      arr.push(defaultValue);
    }

    return arr;
  }

  const arr1 = makeArray<number>(1, 10);
  const arr2 = makeArray<string>("empty", 10);
  const arr3 = makeArray("empty", 10);
  ```

### 🔹 제네릭으로 스택 구현하기

- 제네릭은 데이터 타입에 다양성을 부여해 주기 때문에, 자료구조에서 많이 사용됨

  ```ts
  class Stack<D> {
    private items: D[] = [];

    push(item: D) {
      this.items.push(item);
    }

    pop() {
      return this.items.pop();
    }
  }

  const numberStack = new Stack<number>();
  numberStack.push(10);
  ```

### 🔹 `extends` 키워드로 제네릭 타입 제한하기

- `extends` 키워드를 이용하면 제네릭 타입으로 입력할 수 있는 타입의 종류를 제한할 수 있음

  - `keyof` 키워드는 인터페이스의 모든 속성 이름을 유니온 타입으로 만들어 줌
  - 아래 Korean 타입은 Person 타입에 할당 가능함

  ```ts
  // 예시 1
  function identity<T extends number | string>(p: T): T {
    return p;
  }

  identity(1);
  identity([]); // 타입 에러
  ```

  ```ts
  // 예시 2
  interface Person {
    name: string;
    age: number;
  }

  interface Korean extends Person {
    liveInSeoul: boolean;
  }

  function swapProperty<T extends Person, K extends keyof Person>(
    p1: T,
    p2: T,
    name: K
  ): void {
    const temp = p1[name];
    p1[name] = p2[name];
    p2[name] = temp;
  }

  const p1: Korean = {
    name: "홍길동",
    age: 23,
    liveInSeoul: true,
  };

  const p2: Korean = {
    name: "김삿갓",
    age: 31,
    liveInSeoul: false,
  };

  swapProperty(p1, p2, "age");
  ```

## ▶ 맵드 타입

- 맵드 타입 (mapped)을 이용하면 몇 가지 규칙으로 **새로운 인터페이스**를 만들 수 있음
- 기존 인터페이스의 모든 속성을 선택 속성 또는 읽기 전용으로 만들 때 주로 사용됨

### 🔹 맵드 타입 사용하기

- 맵드 타입은 `in` 키워드를 사용해서 정의함

  - `in` 키워드 오른쪽에 유니온 타입이 올 수 있음

  ```ts
  type T1 = { [K in "prop1" | "prop2"]: boolean };
  // { prop1: boolean, prop2: boolean }
  ```

- 맵드 타입을 사용해 인터페이스의 모든 속성을 '선택 속성' + 'bool 타입'으로 변경

  ```ts
  type MakeBoolean<T> = { [K in keyof T]?: boolean };

  const pMap: MakeBoolean<Person> = {};
  pMap.name = true;
  pMap.age = false;
  ```

### 🔹 `Partial` 내장 타입

- 맵드 타입으로 만들어진 타입스크립트 내장 타입임
- 인터페이스의 모든 속성을 **선택 속성**으로 만들어 주는 맵드 타입

  ```ts
  type Partial<T> = { [P in keyof T]?: T[P] };

  type T1 = Partial<Person>;
  ```

### 🔹 `Readonly` 내장 타입

- 맵드 타입으로 만들어진 타입스크립트 내장 타입임
- 인터페이스의 모든 속성을 **읽기 전용**으로 만들어 주는 맵드 타입

  ```ts
  type Readonly<T> = { readonly [P in keyof T]: T[P] };

  type T2 = Readonly<Person>;
  ```

### 🔹 `Pick` 내장 타입

- 맵드 타입으로 만들어진 타입스크립트 내장 타입임
- 인터페이스에서 **원하는 속성만 추출**해주는 맵드 타입

  - Pick은 인터페이스 T와 해당 인터페이스의 속성 이름 K를 입력으로 받음

  ```ts
  type Pick<T, K extends keyof T> = { [P in K]: T[P] };
  ```

  ```ts
  interface Person {
    name: string;
    age: number;
    language: string;
  }

  type T1 = Pick<Person, "name" | "language">;
  // type T1 = { name: string; language: string; }
  ```

### 🔹 `Record` 내장 타입

- 맵드 타입으로 만들어진 타입스크립트 내장 타입임
- 입력된 **모든 속성을 같은 타입으로 만들어 주는** 맵드 타입

  - 아래 K는 문자열의 서브타입임
  - K로 입력된 모든 문자열을 속성 이름으로 하면서 T를 각 속성의 타입으로 만듦

  ```ts
  type Record<K extends string, T> = { [P in K]: T };

  type T1 = Record<"p1" | "p2", Person>;
  // type T1 = { p1: Person; p2: Person; }
  ```

### 🔹 열거형 타입과 맵드 타입

- 맵드 타입을 이용하면 열거형 타입의 활용도를 높일 수 있음

  - 맵드 타입을 이용하면 아래 FRUIT_PRICE 객체가 Fruit의 모든 원소를 속성으로 가지는게 보장됨

  ```ts
  enum Fruit {
    Apple,
    Banana,
    Orange,
  }

  const FRUIT_PRICE: { [key in Fruit]: number } = {
    [Fruit.Apple]: 1000,
    [Fruit.Banana]: 1500,
  }; // 타입 에러 (∵ Orange 없음)
  ```

## ▶ 조건부 타입

- 조건부(conditional) 타입은 입력된 제네릭 타입에 따라 타입을 결정할 수 있는 기능임

### 🔹 조건부 타입 사용하기

- 조건부 타입은 `extends` 키워드와 `?` 기호를 사용해서 정의함

  - 입력된 제네릭 타입 T가 타입 U의 '서브타입'이면 타입 X를 사용하고, 그렇지 않으면 타입 Y를 사용함

  ```ts
  // 조건부 타입 구조
  T extends U ? X : Y
  ```

  ```ts
  type IsStringType<T> = T extends string ? "yes" : "no";

  type T1 = IsStringType<string>; // 'yes'
  type T2 = IsStringType<number>; // 'no'
  ```

- 조건부 타입에서 유니온 타입을 이용하면 유용한 유틸리티 타입을 많이 만들 수 있음

  - 조건부 타입에 유니온 타입이 입력되면, 각 타입을 하나씩 검사해서 타입을 결정하고 최종 결과는 유니온 타입으로 만들어짐

  ```ts
  type T1 = IsStringType<string | number>; // 'yes' | 'no'
  ```

### 🔹 `Exclude` 내장 타입

- 조건부 타입으로 만들어진 타입스크립트 내장 타입임
- **서브 타입을 제거**해줌

  - 아래 U의 서브 타입을 제거해 줌
  - 유니온 타입에 있는 never 타입은 제거됨

  ```ts
  type Exclude<T, U> = T extends U ? never : T;

  type T1 = Exclude<1 | 3 | 5 | 7, 1 | 5 | 9>; // 3 | 7
  type T2 = Exclude<string | number | (() => void), Function>; // string | number
  ```

### 🔹 `Extract` 내장 타입

- 조건부 타입으로 만들어진 타입스크립트 내장 타입임
- **서브 타입을 추출**해줌 (`Exclude`와 반대로 동작)

  ```ts
  type Extract<T, U> = T extends U ? T : never;

  type T3 = Extract<1 | 3 | 5 | 7, 1 | 5 | 9>; // 1 | 5
  ```

### 🔹 `ReturnType` 내장 타입

- 조건부 타입으로 만들어진 타입스크립트 내장 타입임
- **함수의 반환 타입을 추출**해줌

  - 아래에서 입력된 타입 T가 함수이면 반환 타입이 사용되고, 그렇지 않으면 any 타입이 사용됨
  - `infer` 키워드를 사용해 타입을 추론함

  ```ts
  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

  type T1 = ReturnType<() => string>; // string
  ```

### 🔹 조건부 타입으로 직접 유틸리티 타입 만들기

- 인터페이스에서 값이 문자열인 모든 속성의 이름을 유니온 타입으로 만들어주는 유틸리티 타입 만들기

  - 아래 `[keyof T]`는 인터페이스에서 모든 속성의 타입을 유니온으로 추출해 줌
  - 이때, never 타입은 제외됨

  ```ts
  type StringPropertyNames<T> = {
    [K in keyof T]: T[K] extends String ? K : never;
  }[keyof T];

  type T1 = StringPropertyNames<Person>; // 'name' | 'nation'
  ```

- 인터페이스에서 문자열인 모든 속성을 추출해주는 유틸리티 타입 만들기

  ```ts
  type StringProperties<T> = Pick<T, StringPropertyNames<T>>;

  type T2 = StringProperties<Person>; // { name: string; nation: string; }
  ```

- 인터페이스에서 일부 속성만 제거해주는 유틸리티 타입 만들기

  ```ts
  type Omit<T, U extends keyof T> = Pick<T, Exclude<keyof T, U>>;

  type T1 = Omit<Person, "nation" | "age">; // { name: string }
  ```

- 특정 인터페이스가 다른 인터페이스를 덮어쓰는 유틸리티 타입 만들기

  - 인터페이스 T에 인터페이스 U를 덮어씀
  - 그 결과, age 속성 타입은 문자열로 변경되었고 nation 속성이 새로 추가됨

  ```ts
  type Overwrite<T, U> = { [P in Exclude<keyof T, keyof U>]: T[P] } & U;
  ```

  ```ts
  interface Person1 {
    name: string;
    age: number;
  }

  interface Person2 {
    age: string;
    nation: string;
  }

  type T1 = Overwrite<Person1, Person2>;
  // type T1 = { name: string; age: string; nation: string; }
  ```
