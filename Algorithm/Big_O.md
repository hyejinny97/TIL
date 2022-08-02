# ✔ 알고리즘의 시간복잡도 (Time Complexity)
- 좋은 알고리즘이란, Input을 넣은 후 Output이 나오는 시간이 짧은 알고리즘을 의미

> 알고리즘의 소요 시간 측정하기
- 개개인의 컴퓨팅 환경에 따라 같은 알고리즘이라도 측정 시간은 다름
- 따라서, 환경에 영향을 받지 않는 객관적인 기준이 필요
- 알고리즘의 소요 시간 == 알고리즘 내부에서 일어나는 기본 연산의 총 횟수
- 입력 n개에 따른 소요 시간 == 시간 복잡도

> 시간 복잡도
- 계산 복잡도 이론에서 시간 복잡도는 문제를 해결하는데 걸리는 시간과 입력의 함수 관계를 가리킴
- 단순하게 알고리즘의 수행 시간을 의미
  - 시간 복잡도가 높다 == 느린 알고리즘



# ✔ 빅오 (Big-O 표기법)
- 입력 n이 무한대로 커진다고 가정하고 시간 복잡도를 간단하게 표시하는 것
- 최고차항만 남기고, 계수/상수는 제거
- 내장 함수, 메서드의 시간 복잡도도 확인할 필요가 있음

> 시간 복잡도 종류

   ![시간 복잡도 종류](https://lh6.googleusercontent.com/_gDIHIz_nkM633wxg6BuyPTqXAG1tq93TYkWGHyZK4lMz3yyCVcS4oBchwSxI0X-4K52yFJe4Lj1NTCL4igznIKW2jhYEHyXOI4swRcBfP-aI8cCHYfR1btVFv5TTOXPwtdLANBkz04=s0)
- `O(1)` < `O(logN)` < `O(N)` < `O(NlogN)` < `O(N^2)` < `O(N^3)` < `O(2^N)` < `O(N!)`
1. O(1)
   - 단순 산술 계산(덧셈, 뺄셈, 곱셈, 나눗셈)의 경우
   - a + b, 100 * 200
2. O(logN)
   - 크기 N인 리스트를 반절씩 순회/탐색하는 경우
   - 이진 탐색(Binary Search), 분할정복(Divide & Conquer)
3. O(N)
   - 크기 N인 리스트를 순회하는 경우
4. O(NlogN)
   - 크기 N인 리스트를 반절씩 탐색 * 순회하는 경우
   - 높은 성능의 정렬(Merge/Quick/Heap Sort)
5. O(N^2)
   - 크기 M, N인 2중 리스트를 순회하는 경우
6. O(N^3)
   - 3중 리스트를 순회하는 경우
7. O(2^N)
   - 크기 N인 집합의 부분 집합
8. O(N!)
   - 크기 N인 리스트의 순열

> Big-O Cheatsheet

![데이터구조 빅오](https://hackr.io/blog/media/4-5.png?ezimgfmt=rs:714x402/rscb1/ng:webp/ngcb1)
![정렬 빅오](https://hackr.io/blog/media/3-10.png?ezimgfmt=rs:714x402/rscb1/ng:webp/ngcb1)



# ✔ 파이썬 문자열
> 문자열의 메서드 Big-O
- `.split()`: O(n)
- `.strip()`: O(n)
- `.find()`: O(n)
- `.index()`: O(n)
- `.count()`: O(n)
- `.replace()`: O(n)
- `.join()`: O(n)