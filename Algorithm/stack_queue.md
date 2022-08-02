# ✔ 스택 (Stack)

- 데이터를 한쪽에서만 넣고 빼는 자료구조
- `LIFO(Last-In First-Out, 후입선출)`
- 가장 마지막에 들어온 데이터가 가장 먼저 나감

> 스택 자료구조의 대표 동작

1. `push`
   - 스택 끝부분에 새로운 데이터를 삽입하는 행위
2. `pop`
   - 스택의 가장 마지막 데이터를 가져오는 행위

> 스택의 필요성

1. 뒤집기, 되돌리기, 되돌아가기
   - ex) 브라우저 히스토리, ctrl + z, 단어 뒤집기
2. 마무리되지 않은 일을 임시 저장
   - ex) 괄호 매칭, 함수 호출, 백트래킹, DFS

> 파이썬의 경우

- 파이썬은 **리스트** (List)로 스택을 간편하게 사용할 수 있음
1. `.append()`
   - 리스트의 끝부분에 새로운 데이터를 삽입
2. `.pop()`
   - 리스트의 가장 마지막 데이터를 삭제 후 반환

# ✔ 큐 (Queue)

- 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조
- `FIFO(First-In First-Out, 선입선출)`
- 가장 먼저 들어온 데이터가 가장 먼저 나감

> 큐 자료구조의 대표 동작

1. `dequeue`
   - 큐의 맨 앞 데이터를 가져오는 행위
2. `enqueue`
   - 규의 맨 뒤에 데이터를 삽입하는 행위

> 큐의 필요성

1. 입력된 시간 순서대로 데이터 처리
   - ex) 은행 업무, 프린터의 인쇄 대기열, BFS

> 파이썬의 경우

- 파이썬은 **리스트** (List)로 큐를 간펀하게 사용할 수 있음
1. `.append()`
   - 리스트의 끝부분에 새로운 데이터를 삽입
2. `.pop(0)`
   - 리스트의 맨 앞 데이터를 삭제 후 반환
   - 단점: 시간복잡도 O(n)
     - 맨 앞 데이터가 빠지면서 리스트의 인덱스가 하나씩 당겨지기 때문
     - 따라서, 리스트를 이용한 큐 자료구조는 데이터를 뺄 때 비효율적임
     - 해결방법: 리스트 대신 **`덱 (deque)`** 이용

# ✔ 덱(Deque, Double-Ended Queue)

- 양 방향으로 삽입과 삭제가 자유로운 큐 자료구조
- 덱은 양 방향 삽입, 추출이 모두 큐보다 훨씬 빠름

> 파이썬의 덱 (deque) - `collections.deque()`

1. `.append()`
   
   - 덱의 끝부분에 새로운 데이터를 삽입

2. `.popleft()`
   
   - 덱의 맨 앞 데이터를 삭제 후 반환

3. `.appendleft()`
   
   - 덱의 맨 앞에 새로운 데이터를 삽입

4. `.pop()`
   
   - 덱의 맨 뒤 데이터를 삭제 후 반환
   
   ```python
   # 리스트를 이용한 풀이
   n = 5
   queue = list(range(1, n + 1))
   while len(queue) > 1:
      print(queue.pop(0), end=" ")    # 1 3 5 7 4 2
      queue.append(queue.pop(0))

   print(queue[0])   # 6


   # 덱을 이용한 풀이
   from collections import deque

   n = 5
   queue = deque(range(1, n + 1))
   while len(queue) > 1:
      print(queue.popleft(), end=" ")   # 1 3 5 7 4 2 
      queue.append(queue.popleft())

   print(queue[0])   # 6
   ```

> 파이썬 덱의 시간복잡도
1. 값 추가: O(1)
2. 값 삭제: O(1)

   | Operation  | Average Case | Amortized Worst  Case |
   | ---------- | ------------ | --------------------- |
   | Copy       | O(n)         | O(n)                  |
   | Append     | O(1)         | O(1)                  |
   | AppendLeft | O(1)         | O(1)                  |
   | Pop        | O(1)         | O(1)                  |
   | PopLeft    | O(1)         | O(1)                  |
   | Extend     | O(k)         | O(k)                  |
   | ExtendLeft | O(k)         | O(k)                  |
   | Rotate     | O(k)         | O(k)                  |
   | Remove     | O(n)         | O(n)                  |
