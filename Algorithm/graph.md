# ✔ 그래프 (Graph)
- 정점(Vertex)과 이를 연결하는 간선(Edge)들의 집합으로 이루어진 비선형 자료구조
- ex) 소셜 네크워크, 지하철 노선도

> 그래프 관련 용어
1. 정점(Vertex) = 노드(Node)
   - 간선으로 연결되는 점
2. 간선(Edge)
   - 정점 간의 관계(연결)를 연결하는 선
3. 경로(Path)
   - 시작 정점부터 도착 정점까지 거치는 정점을 나열한 것
4. 인접(Adjacency)
   - 두 개의 정점이 하나의 간선으로 직접 연결된 상태

    ![그래프 그림](https://annajeong.github.io/assets/images/algorithm/graph-def)

> 그래프 종류
1. 무방향 그래프 (Undirected graph)
   - 간선의 방향이 없는 가장 일반적인 그래프
   - 간선을 통해 양방향의 정점 이동 가능
   - 차수(Degree): 하나의 정점에 연결된 간선의 개수
   - 모든 정점의 차수 합 = 간선 수 x 2

2. 유방향 그래프 (Directed graph)
   - 간선의 방향이 있는 그래프
   - 간선의 방향이 가리키는 정점으로 이동 가능
   - 차수(Degree): 진입 차수와 진출 차수로 나누어짐
     - 진입 차수(In-degree): 외부 정점에서 한 정점으로 들어오는 간선의 수
     - 진출 차수(Out-degree): 한 정점에서 외부 정점으로 나가는 간선의 수

> 그래프의 표현
1. 인접 행렬 (Adjacency matrix)
   - 두 정점을 연결하는 간선이 있으면 0, 있으면 1을 가지는 행렬로 표현하는 방식
   - 문제에서는 보통 간선으로 연결된 두 정점의 목록으로 그래프를 표현함
   - 특징: 직관적이고 만들기 편하지만, 불필요하게 공간이 낭비됨
    
    ```python
    # 무방향 그래프의 인접 행렬 만들기

    node = 7   # 정점 개수
    edge = 7   # 간선 개수
    
    graph = [[0] * node for _ in range(node)]

    for _ in range(edge):
      n1, n2 = map(int, input().split())
      graph[n1][n2] = 1
      graph[n2][n1] = 1
    
    # 인접 행렬 결과
    graph = [
      [0, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 1, 1, 0, 0],
      [1, 0, 0, 0, 1, 1, 0],
      [0, 1, 0, 0, 0, 0, 0],
      [0, 1, 1, 0, 0, 0, 1],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0]
    ]
    ```

    ![무방향 그래프 인접행렬](https://t1.daumcdn.net/cfile/tistory/99F7B9485B54360A21?download)
    ![유방향 그래프 인접행렬](https://t1.daumcdn.net/cfile/tistory/995B6A485B54360B2C)

2. 인접 리스트 (Adjacency list)
   - 리스트를 통해 각 정점에 대한 인접 정점들을 순차적으로 표현하는 방식
   - 인덱스 번호가 정점의 번호를 의미
   - 특징: 연결된 정점만 저장하여 효율적이므로 자주 사용됨
    
    ```python
      # 무방향 그래프의 인접 리스트 만들기

      node = 7   # 정점 개수
      edge = 7   # 간선 개수
      
      graph = [[] for _ in range(node)]

      for _ in range(edge):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    # 인접 리스트 결과
    graph = [
      [1, 2],
      [0, 3, 4],
      [0, 4, 5],
      [1],
      [1, 2, 6],
      [2],
      [4]
    ]
    ```