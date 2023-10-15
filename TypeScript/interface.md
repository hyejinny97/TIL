# ✔ 인터페이스

- 인터페이스로 타입을 정의할 때는 `interface` 키워드를 사용함

## ▶ 인터페이스로 객체의 타입 정의

- 인터페이스로 객체 내부에 존재하는 각 속성의 타입을 정의함

  - 하나 이상의 속성 타입을 만족하지 못하면 타입 에러가 발생함

  ```ts
  interface Person {
    name: string;
    age: number;
  }

  const p: Person = { name: "mike", age: 23 };
  ```

### 🔹 선택 속성

- 객체에서 없어도 되는 속성
- 인터페이스에서 선택 속성은 물음표 기호 `?`를 사용함

  ```ts
  interface Person {
    name: string;
    age?: number;
  }

  const p: Person = { name: "mike" };
  ```

- 물음표 기호를 사용하지 않고 `undefined`를 유니온 타입으로 추가하면, 선택 속성과는 달리 명시적으로 age 속성을 입력해야 함

  ```ts
  interface Person {
    name: string;
    age: number | undefined;
  }

  const p: Person = { name: "mike" }; // 타입 에러
  ```

### 🔹 읽기 전용 속성

- 값이 변하지 않는 속성
- 인터페이스에서 읽기 전용 속성은 `readonly` 키워드를 사용함

  - 읽기 전용 속성의 값을 수정하려고 하면 컴파일 에러가 발생함

  ```ts
  interface Person {
    readonly name: string;
    age?: number;
  }

  const p: Person = { name: "mike" };
  p.name = "john"; // 컴파일 에러
  ```

### 🔹 정의되지 않은 속성값에 대한 처리

- 보통은 객체가 인터페이스에 정의되지 않은 속성값을 가지고 있어도 할당이 가능함
- 단, 리터럴로 값을 초기화하는 경우엔, 인터페이스에 정의되지 않은 속성값이 있으면 타입 에러가 발생함

  - 아래에서 p3 타입이 p2 타입을 포함하는 더 큰 타입이기 때문에 타입 에러가 발생하지 않음 (타입 호환성)

  ```ts
  interface Person {
    readonly name: string;
    age?: number;
  }

  const p1: Person = {
    name: "mike",
    birthday: "1997-01-01", // 타입 에러
  };

  const p2 = {
    name: "mike",
    birthday: "1997-01-01",
  };
  const p3: Person = p2;
  ```

## ▶ 인터페이스로 정의하는 인덱스 타입

- 인덱스(Index) 타입: 인터페이스에서 속성 이름을 구체적으로 정의하지 않고 값의 타입만 정의하는 것

  ```ts
  interface Person {
    readonly name: string;
    age: number;
    [key: string]: string | number;
  }

  const p1: Person = {
    name: "mike",
    birthday: "1997-01-01",
    age: "25", // 타입 에러
  };
  ```

### 🔹 여러 개의 인덱스를 정의하는 경우

```ts
interface YearPriceMap {
  [year: number]: number;
  [year: string]: string | number;
}

const yearMap: YearPriceMap = {};
yearMap[1998] = 1000;
yearMap[1998] = "abc"; // 타입 에러
yearMap["2000"] = 1234;
yearMap["2000"] = "million";
```

## ▶ 이 외 인터페이스로 할 수 있는 것

### 🔹 인터페이스로 함수 타입 정의

- 인터페이스로 함수를 정의할 때는 속성 이름 없이 정의함

  - 인터페이스로 함수 타입을 정의할 때 함수의 속성값도 같이 정의할 수 있음

  ```ts
  interface GetInfoText {
    (name: string, age: number): string;
    totalCall: number;
  }

  const getInfoText: GetInfoText = function (name, age) {
    getInfoText.totalCall += 1;
    // ...
  };

  getInfoText.totalCall = 0;
  ```

### 🔹 인터페이스로 클래스 구현

- `implements` 키워드를 사용해서 인터페이스를 클래스로 구현할 수 있음

  - 하나의 속성이라도 구현하지 않으면 컴파일 에러가 발생함

  ```ts
  interface Person {
    name: string;
    age: number;
    isYoungerThan(age: number): boolean;
  }

  class SomePerson implements Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }

    isYoungerThan(age: number) {
      return this.age < age;
    }
  }
  ```

### 🔹 인터페이스 확장하기

- 인터페이스를 확장해서 새로운 인터페이스를 만들 수 있음

  ```ts
  interface Person {
    name: string;
    age: number;
  }

  interface Korean extends Person {
    isLiveInSeoul: boolean;
  }

  interface Programmer extends Person, Korean {
    favoriteProgrammerLanguage: string;
  }
  ```

### 🔹 인터페이스 합치기

- 교차 타입 `&`을 이용하면 여러 인터페이스를 하나로 합칠 수 있음

  - 주의) 이때 교차 타입은 속성의 교집합이 아닌 타입이 가질 수 있는 값의 집합에 대한 교집합을 구함
  - 따라서, 아래에서 타입 PP는 합쳐진 두 인터페이스 Person과 Product의 모든 속성값을 포함하게 됨

  ```ts
  interface Person {
    name: string;
    age: number;
  }

  interface Product {
    name: string;
    price: number;
  }

  type PP = Person & Product;

  const pp: PP = {
    name: "a",
    age: 23,
    price: 1000,
  };
  ```
