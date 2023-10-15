# ✔ 타입스크립트의 여러 가지 타입

## ▶ 타입스크립트의 다양한 타입

- 타입스크립트에서 타입을 선언하는 방법

  - 변수 이름 오른쪽에 콜론과 함께 타입 입력

  ```ts
  const size: number = 123;
  const isBig: boolean = size >= 100;
  const msg: string = isBig ? "크다" : "작다";
  ```

  ```ts
  const values1: number[] = [1, 2, 3];
  const values2: Array<number> = [1, 2, 3];
  ```

  ```ts
  const data: [string, number] = [msg, size];
  ```

### 🔹 `null`, `undefined` 타입

- `null`이나 `undefined` 타입은 다른 타입과 함께 유니온 타입으로 정의할 때 많이 사용됨

  ```ts
  let v1: undefined = undefined;
  let v2: null = null;
  let v3: number | undefined = undefined;
  ```

### 🔹 문자 리터립, 숫자 리터럴 타입

- 숫자 리터럴 타입

  ```ts
  let v1: 10 | 20 | 30;
  v1 = 10;
  ```

- 문자 리터럴 타입

  ```ts
  let v2: "경찰관" | "소방관";
  v2 = "의사"; // 타입 에러
  ```

### 🔹 `any` 타입

- 모든 종류의 값을 허용하는 타입

  - 숫자, 문자열, 함수 등
  - 실제로 타입을 알 수 없는 경우나 타입 정의가 안 된 외부 패키지를 사용하는 경우 사용하기 좋음

  ```ts
  let value: any;

  value = 123;
  value = "456";
  value = () => {};
  ```

### 🔹 `void`, `never` 타입

- `void` 타입: 아무 값도 반환하지 않고 종료되는 함수의 반환 타입을 정의
- `never` 타입: 항상 예외가 발생해서 비정상적으로 종료되거나 무한 푸프 때문에 종료되지 않는 함수의 반환 타입을 정의

  ```ts
  function f1(): void {
    console.log("hello");
  }
  ```

  ```ts
  function f2(): never {
    throw new Error("some error");
  }
  ```

  ```ts
  function f3(): never {
    while (true) {
      // ...
    }
  }
  ```

### 🔹 `object` 타입

- 객체 타입

  - 객체의 속성에 대한 정보가 없기 때문에 특정 속성값에 접근하면 타입 에러가 발생함
  - 속성 정보를 포함해서 타입을 정의하기 위해서는 인터페이스를 사용해야 함

  ```ts
  let v: object;
  v = { name: "abc" };

  console.log(v.prop1); // 타입 에러
  ```

### 🔹 교차 타입, 유니온 타입

- 교차(Intersection) 타입

  - 여러 타입의 교집합
  - `&` 기호로 정의

- 유니온(Union) 타입

  - 여러 타입의 합집합
  - `|` 기호로 정의

  ```ts
  let v1: (1 | 3 | 5) & (3 | 5 | 7);

  v1 = 3;
  v1 = 1; // 타입 에러
  ```

### 🔹 `type` alias

- `type` 키워드로 타입에 별칭을 줄 수 있음

  - 타입 별칭은 타입을 선언할 떄 편리하게 사용할 수 있음
  - 아래 예시의 경우, 'number | string' 타입에 Width라는 별칭을 부여한 후 일반적인 타입처럼 사용함

  ```ts
  type Width = number | string;

  let width: Width;
  width = 100;
  ```

## ▶ 열거형 타입

- 열거형 타입은 `enum` 키워드를 사용해서 정의
- 열거형 타입의 각 원소는 '값'으로 사용될 수 있고, '타입'으로 사용될 수도 있음

  ```ts
  enum Fruit {
    Apple,
    Banana,
    Orange,
  }

  const v1: Fruit = Fruit.Apple;
  const v2: Fruit.Apple | Fruit.Banana = Fruit.Banana;
  ```

- 열거형 타입의 각 원소에 숫자 또는 문자열을 할당할 수 있음
- 다른 타입과 달리 열거형 타입은 **컴파일 후에도 관련된 코드가 남음**

  - 열거형 타입은 **객체**로 존재함
  - 따라서, 일반적인 객체처럼 다룰 수 있고 해당 객체를 런타임에 사용할 수 있음

### 🔹 열거형 타입의 값으로 숫자 할당하기

- 열거형 타입의 첫 번째 원소에 값을 할당하지 않으면 자동으로 0이 할당됨

  - 명시적으로 값을 입력하지 않으면 이전 원소에서 1만큼 증가한 값이 할당됨

  ```ts
  enum Fruit {
    Apple,
    Banana = 5,
    Orange,
  }

  console.log(Fruit.Apple, Fruit.Banana, Fruit.Orange); // 0, 5, 6
  ```

- 열거형 타입의 값으로 숫자를 할당하면, 열거형 타입이 컴파일된 후 각 원소는 이름과 값이 '양방향'으로 매핑됨

  - 따라서, 값을 이용해서 이름을 가져올 수 있음

  ```js
  // 열거형 타입이 컴파일된 결과
  var Fruit;
  (function (Fruit) {
    Fruit[(Fruit["Apple"] = 0)] = "Apple";
    Fruit[(Fruit["Banana"] = 5)] = "Banana";
    Fruit[(Fruit["Orange"] = 6)] = "Orange";
  });
  ```

  ```ts
  console.log(Fruit.Banana); // 5
  console.log(Fruit["Banana"]); // 5
  console.log(Fruit[5]); // Banana
  ```

### 🔹 열거형 타입의 값으로 문자열 할당하기

- 열거형 타입의 값으로 문자열을 할당하면, 열거형 타입이 컴파일된 후 각 원소는 이름과 값이 '단방향'으로 매핑됨

  ```ts
  enum Language {
    Korean = "ko",
    English = "en",
    Japanese = "jp",
  }
  ```

  ```ts
  // 열거형 타입이 컴파일된 결과
  var Language;
  (function (Language) {
    Language["Korean"] = "ko";
    Language["English"] = "en";
    Language["Japanese"] = "jp";
  })(Language || (Language = {}));
  ```

### 🔹 열거형 타입을 위한 유틸리티 함수

- ex) 입력된 값이 열거형 타입에 존재하는 값인지 검사하는 함수

  - 서버로부터 받은 데이터를 검증할 때 유용하게 사용할 수 있음

  ```ts
  function isValidEnumValue(enumObject: any, value: number | string) {
    if (typeof value === "number") {
      return !!enumObject[value];
    } else {
      return Object.keys(enumObject)
        .filter((key) => isNaN(Number(key)))
        .some((key) => enumObject[key] === value);
    }
  }

  console.log(isValidEnumValue(Fruit, 1)); // true
  console.log(isValidEnumValue(Language, "ko")); // true
  ```

### 🔹 상수 열거형 타입

- 열거형 타입은 컴파일 후에도 남아 있기 때문에 번들 파일의 크기가 불필요하게 커질 수 있음
- 상수(const) 열거형 타입을 사용하면, 컴파일 결과에 **열거형 타입의 객체를 남겨 놓지 않을 수 있음**

  - 따라서, 열거형 타입을 상수로 정의하면 열거형 타입의 객체를 사용할 수 없음

  ```ts
  const enum Fruit {
    Apple,
    Banana,
    Orange,
  }

  const fruit: Fruit = Fruit.Apple;
  console.log(isValidEnumValue(Fruit, 1)); // 타입 에러
  ```

## ▶ 함수 타입

- 함수 타입을 정의하기 위해서, '매개변수 타입'과 '반환 타입'이 필요함

  ```ts
  function getInfoText(name: string, age: number): string {
    return `name: ${name}, age: ${age}`;
  }

  const v: string = getInfoText("mike", 23);
  ```

- 자바스크립트에서 함수는 변수에 저장할 수 있음 (함수 표현식)

  - 함수를 저장할 변수의 타입은 아래와 같이 화살표 기호를 사용함

  ```ts
  const getInfoText: (name: string, age: number) => string = function (
    name,
    age
  ) {
    // ...
  };
  ```

### 🔹 선택 매개변수

- 반드시 입력하지 않아도 되는 매개변수
- 매개변수 이름 오른쪽에 물음표 기호 `?`를 입력하면 선택 매개변수가 됨

  - 함수 호출 시 선택 매개변수의 인수를 입력하지 않아도 타입 에러가 발생하지 않음
  - 입력하는 경우에는 반드시 정의된 타입을 만족하는 값을 입력해야 함

  ```ts
  function getInfoText(name: string, age: number, language?: string): string {
    // ...
  }

  getInfoText("mike", 23);
  ```

- 선택 매개변수 오른쪽에 필수 매개변수가 오면 컴파일 에러 발생

  ```ts
  function getInfoText(name: string, language?: string, age: number): string {
    // ...
  }
  ```

- 아래와 같이 `undefined`를 이용해 에러 없이 구현할 있음

  - 단, 사용성과 가독성이 좋지 않음

  ```ts
  function getInfoText(
    name: string,
    language: string | undefined,
    age: number
  ): string {
    // ...
  }

  getInfoText("mike", undefined, 23);
  ```

### 🔹 매개변수의 기본값

- 타입 오른쪽에 `=` 기호를 사용해 매개변수의 기본값을 정의할 수 있음

  - 타입을 입력하지 않아도 매개변수의 기본값을 정의할 수 있음
  - 기본값에 의해 매개변수의 타입이 추론됨
  - 기본값이 있는 매개변수는 선택 매개변수임

  ```ts
  function getInfoText(
    name: string,
    age: number = 15,
    language = "korean"
  ): string {
    // ...
  }

  console.log(getInfoText("mike"));
  ```

### 🔹 나머지 매개변수

- 나머지 매개변수는 배열로 정의할 수 있음

  ```ts
  function getInfoText(name: string, ...rest: string[]): string {
    // ...
  }
  ```

### 🔹 `this` 타입

- 함수의 `this` 타입을 정의하지 않으면 기본적으로 `any` 타입이 사용됨

  ```ts
  function getParam(this: string, index: number): string {
    const params = this.split(",");
    // ...
  }
  ```

### 🔹 원시(primitive) 타입에 메서드 추가하기

- 원시 타입에 메서드를 등록할 때는 인터페이스를 이용함

  ```ts
  interface String {
    getParam(this: string, index: number): string;
  }

  String.prototype.getParam = getParam;
  ```

### 🔹 함수 오버로드(overload)

- 함수 오버로드를 사용하면 하나의 함수에 여러 개의 타입을 정의할 수 있음

  - 매개변수와 반환 타입의 모든 가능한 조합을 정의함
  - 실제 구현하는 쪽에서 정의한 타입은 함수 오버로드의 타입 목록에서 제외됨

  ```ts
  function add(x: number, y: number): number;
  function add(x: string, y: string): string;
  function add(x: number | string, y: number | string): number | string {
    // ...
  }

  const v1: number = add(1, 2);
  console.log(add(1, "2"));
  ```

### 🔹 명명된 매개변수

- 명명된 매개변수의 타입을 아래와 같이 정의할 수 있음

  ```ts
  function getInfoText({
    name,
    age = 15,
    language,
  }: {
    name: string;
    age?: number;
    language?: string;
  }): string {
    // ...
  }
  ```

- 명명된 매개변수의 타입을 다른 코드에서도 재사용하려면 다음과 같이 인터페이스를 사용하면 됨

  ```ts
  interface Parma {
    name: string;
    age?: number;
    language?: string;
  }

  function getInfoText({ name, age = 15, language }: Param): string {
    // ...
  }
  ```
