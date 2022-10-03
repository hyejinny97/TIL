# ✔ 제너레이터 (generator)
- 이터레이터(iterator)를 직접 만들때 사용하는 코드
  - 이터레이터 객체 예: reversed(), list, set 등
- 함수 내부에 `return` 대신 `yield` 키워드를 사용하면 제너레이터 함수가 됨
- 일반 함수와 달리 함수를 호출해도 함수 내부의 코드가 실행되지 않음
- 제너레이터 객체(generator object)를 반환
  - 제너레이터 객체는 `next()` 함수를 사용해 함수 내부의 코드를 실행
  - 이때 `yield` 키워드 부분까지만 코드를 실행
  - next() 함수의 반환값으로 yield 키워드 뒤에 입력한 값이 출력
  - next() 함수를 호출한 이후 yield 키워드를 만나지 못하고 함수가 끝나면 `StopIteration` 예외 발생
- 장점
  - 함수의 코드를 조금씩 실행함으로써, 메모리의 효율성 증대

  ```python
  def test():
    print('A 지점 통과')
    yield 1
    print('B 지점 통과')
    yield 2
  

  output = test()

  a = next(output)
  # A 지점 통과
  print(a)
  # 1

  b = next(output)
  # B 지점 통과
  print(b)
  # 2

  next(output)
  # StopIteration
  ```