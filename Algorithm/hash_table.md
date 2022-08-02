# ✔ 해시 테이블 (Hash Table)

- 해시테이블: 해시함수를 사용하여 키를 해시값으로 매핑하고, 이 해시값을 인덱스 혹은 주소 삼아 데이터의 값(value)을 키와 함께 저장하여 검색을 빠르게 하기 위한 자료 구조
- 해시: 해시 함수를 통해 얻어진 값
- 해시 함수: 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수 ([SHA256](https://emn178.github.io/online-tools/sha256.html))
  ![해시테이블](https://images.velog.io/images/sunhwa508/post/f656386f-7460-4278-b549-2306d1fbaa98/image.png)

> 파이썬의 경우

- 파이썬에서의 **딕셔너리** (Dictionary)가 해시테이블의 특징을 지니고 있음
  - 딕셔너리는 해시테이블을 이용하여 Key:Value 저장
  - 딕셔너리는 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠름

# ✔ 파이썬의 딕셔너리 (Dictionary)

> 파이썬 딕셔너리의 시간복잡도

1. 값 접근: O(1)

2. 값 변경: O(1)

3. 값 삭제: O(1)

4. 값 순회: O(n)
   
   | Operation   | Average Case | Amortized Worst Case |
   | ----------- | ------------ | -------------------- |
   | k in d      | O(1)         | O(n)                 |
   | Copy        | O(n)         | O(n)                 |
   | Get Item    | O(1)         | O(n)                 |
   | Set Item    | O(1)         | O(n)                 |
   | Delete Item | O(1)         | O(n)                 |
   | Iteration   | O(n)         | O(n)                 |

# ✔ 파이썬의 셋 (Set)

> 파이썬 세트의 필요성

1. 데이터의 중복이 없어야 할 때(고유값들로 이루어진 데이터가 필요할 때)
2. 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번히 필요할 때

> 파이썬 셋의 시간복잡도
1. 값 탐색: O(1)
2. 값 제거: O(1)
3. 합집합: O(n)
4. 교집합: O(n)
5. 차집합: O(n)
6. 대칭차집합: O(n)
   
   | Operation | Average Case             | Worst Case           |
   | --------- | ------------------------ | -------------------- |
   | x in 세트   | O(1)                     | O(n)                 |
   | 합집합       | O(len(s1) + len(s2))     |                      |
   | 교집합       | O(min(len(s1), len(s2))) | O(len(s1) * len(s2)) |
   | 차집합       | O(len(s1))               |                      |
   | 대칭차집합     | O(len(s1))               | O(len(s1) * len(s2)) |
