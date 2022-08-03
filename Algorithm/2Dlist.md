# ✔ 2차원 리스트
- 리스트를 원소로 가지는 리스트
- 2차원 리스트는 행렬(matrix)과 동일
  
  ```python
  # 3 x 4 행렬
  matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
  matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
  ]
  ```

> 특정 값으로 초기화된 2차원 리스트 만들기
1. 직접 작성
   
   ```python
   # 4 x 3 행렬
   matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
   ```
2. 반복문으로 작성
   
   ```python
   # 4 x 3 행렬
   matrix = []
   for _ in range(4):
      matrix.append([0] * 3)
   ```
3. 리스트 컴프리헨션으로 작성
   
   ```python
   # 4 x 3 행렬
   matrix = [[0] * 3 for _ in range(4)]
   ```

> 주의) 리스트 컴프리헨션 vs 리스트 곱셈 연산
1. 리스트 컴프리헨션으로 행렬 작성
  
   ```python
   # n x m 행렬
   n = 4
   m = 3
   matrix = [[0] * m for _ in range(n)]
   
   print(matrix)   # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

   # 원소값 변경 시
   matrix[0][0] = 1
   print(matrix)   # [[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
   ```

   ![리스트 컴프리헨션으로 작성한 행렬](./image/matrix_listcomprehension.png)

2. 리스트 곱셈 연산으로 행렬 작성
   
   ```python
   # n x m 행렬
   n = 4
   m = 3
   matrix = [[0] * m] * n
   
   print(matrix)   # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
   
   # 원소값 변경 시
   matrix[0][0] = 1
   print(matrix)   # [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
   ```

   ![리스트 곱셈 연산으로 작성한 행렬](./image/list_multifly_operation.png)