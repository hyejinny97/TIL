# ✔ 배열 (Array)

- 여러 데이터들이 연속된 메모리 공간에 저장되어 있는 자료구조

> 배열(Array) 특징

- 인덱스를 통해 데이터에 빠르게 접근 가능
- 배열의 길이는 변경 불가능하므로, 길이를 변경하고 싶다면 새로 생성해야함
- 데이터 타입은 고정되어 있음

> 파이썬의 경우

- 파이썬에서의 **리스트** (List)가 배열의 특징을 일부 지니고 있음
  - 파이썬 리스트는 배열처럼 인덱스를 통해 빠르게 접근이 가능함

# ✔ 연결 리스트 (Linked List)

- 데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조

> 연결 리스트(Linked List) 특징

- 맨 처음 노드부터 순차적으로 탐색
- 연결리스트의 길이를 자유롭게 변경 가능하므로, 삽입 및 삭제가 편리
- 다양한 데이터 타입 저장 가능
- 데이터가 메모리에 연속적으로 저장되지 않음

> 파이썬의 경우

- 파이썬에서의 **리스트** (List)가 연결 리스트의 특징을 일부 지니고 있음
  - 파이썬 리스트는 연결 리스트처럼 길이 변경 가능(가변 길이)
  - 다양한 데이터 타입 저장 가능
  - 데이터가 메모리에 연속적으로 저장되지 않음

# ✔ 파이썬의 리스트 (List)

- 파이썬의 리스트(List) = 배열(Array) + 연결리스트(Linked List)

> 파이썬 리스트의 시간복잡도
1. 값 접근(인덱싱): O(1)
2. 값 변경: O(1)
3. 값 추가: O(n)
4. 값 삭제: O(n)
5. 값 순회: O(n)
6. 값 접근(슬라이싱): O(K)
   
   | Operation        | Average Case | Amortized Wosrt Case |
   | ---------------- | ------------ | -------------------- |
   | Copy             | O(n)         | O(n)                 |
   | Append           | O(1)         | O(1)                 |
   | Pop last         | O(1)         | O(1)                 |
   | Pop intermediate | O(n)         | O(n)                 |
   | Insert           | O(n)         | O(n)                 |
   | Get Item         | O(1)         | O(1)                 |
   | Set Item         | O(1)         | O(1)                 |
   | Delete Item      | O(n)         | O(n)                 |
   | Iteration        | O(n)         | O(n)                 |
   | Get Slice        | O(k)         | O(k)                 |
   | Del Slice        | O(n)         | O(n)                 |
   | Set Slice        | O(k+n)       | O(k+n)               |
   | Extend           | O(k)         | O(k)                 |
   | Sort             | O(n log n)   | O(n log n)           |
   | Multiply         | O(nk)        | O(nk)                |
   | x in s           | O(n)         |                      |
   | min(s), max(s)   | O(n)         |                      |
   | Get Length       | O(1)         | O(1)                 |

> 파이썬 리스트의 메서드 Big-O

- `.append()`: O(1)
- `.pop()`: O(1)
- `.pop(인덱스)`: O(n)
- `.count()`: O(n)
- `.index()`: O(n)
- `.sort()`: O(n log n)
- `.reverse()`: O(n)

> 파이썬 리스트 관련 내장함수 Big-O

- `len()`: O(1)
- `sum()`: O(n)
- `max()`: O(n)
- `min()`: O(n)
- `sorted()`
- `reversed()`