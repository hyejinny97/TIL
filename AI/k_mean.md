# ✔ k-평균

> ['k-평균' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/6-2.ipynb)

## 1️⃣ k-평균 알고리즘 소개

- k-평균 군집 알고리즘은 평균값을 자동으로 찾아줌
  - 평균값 = 클러스터 중심 = 센트로이드
- 처음에는 랜덤하게 클러스터 중심을 선택하고 점차 가장 가까운 샘플의 중심으로 이동하는 비교적 간단한 알고리즘임

### k-평균 알고리즘의 작동 방식

1. 무작위로 k개의 클러스터 중심을 정함
2. 각 샘플에서 가장 가까운 클러스터 중심을 찾아 해당 클러스터의 샘플로 지정함
3. 클러스터에 속한 샘플의 평균값으로 클러스터 중심을 변경함
4. 클러스터 중심에 변화가 없을 때까지 2번으로 돌아가 반복함

## 2️⃣ KMeans 클래스

#### 1. 과일 데이터를 불러온 후, 2차원 배열로 펼치자

```py
import numpy as np

fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)  # (샘플 개수, 너비 x 높이)
```

#### 2. k-평균 모델을 훈련해보자

```py
from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)
```

- `n_clusters`: 클러스터 개수

#### 3. 군집된 결과를 확인해보자

```py
print(km.labels_)
"""
[2 2 2 2 2 0 2 2 2 2 2 2 2 2 2 2 2 2 0 2 2 2 2 2 2 2 0 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 0 2 0 2 2 2 2 2 2 2 0 2 2 2 2 2 2 2 2 2 0 0 2 2 2 2 2 2 2 2 0 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1]
"""
```

- `labels_` 속성: 군집된 결과가 저장됨
  - 배열의 길이는 샘플의 개수와 같음
  - 각 샘플이 어떤 레이블에 해당되는지 나타냄
  - n_cluster를 3으로 지정했기 때문에 labels\_ 배열의 값은 0, 1, 2 중 하나임

```py
print(np.unique(km.labels_, return_counts=True))
# (array([0, 1, 2], dtype=int32), array([112,  98,  90]))
```

- 첫 번째 클러스터(레이블 0)가 112개의 샘플을, 두 번째 클러스터(레이블 1)가 98개의 샘플을, 세 번째 클러스터(레이블 2)가 90개의 샘플을 모은 것을 확인할 수 있음

#### 4. 각 클러스터 내 샘플들을 이미지로 출력해보자

```py
import matplotlib.pyplot as plt

def draw_fruits(arr, ratio=1):
    n = len(arr)
    rows = int(np.ceil(n/10))
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                axs[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()
```

- (샘플 개수, 너비, 높이)의 3차원 배열을 입력받아 가로로 10개씩 이미지를 출력하는 함수

```py
draw_fruits(fruits[km.labels_==0])
```

<img src='./labels_0_fruit.png' alt='레이블이 0인 과일 사진' width='300px' />

- 넘파이 배열에 불리언 인덱싱을 적용해 레이블이 0인 과일 사진을 모두 그림
- 레이블이 0인 클러스터는 대부분 파인애플이고 사과와 바나나가 약간 섞여 있음

```py
draw_fruits(fruits[km.labels_==1])
```

<img src='./labels_1_fruit.png' alt='레이블이 1인 과일 사진' width='300px' />

- 레이블이 1인 클러스터는 모두 바나나로만 이루어져 있음

```py
draw_fruits(fruits[km.labels_==2])
```

<img src='./labels_2_fruit.png' alt='레이블이 2인 과일 사진' width='300px' />

- 레이블이 2인 클러스터는 모두 사과로만 이루어져 있음
- k-평균 알고리즘이 샘플들을 명확하게 구별해내지는 못했지만, 훈련 데이터에 타깃 레이블을 전혀 제공하지 않았음에도 스스로 비슷한 샘플들을 아주 잘 모은 것 같음

## 3️⃣ 클러스터 중심

#### 1. 훈련한 모델이 최종적으로 찾은 클러스터 중심을 이미지로 출력해보자

```py
draw_fruits(km.cluster_centers_.reshape(-1, 100, 100), ratio=3)
```

<img src='./k_means_cluster_center.png' alt='클러스터 중심' width='400px' />

- `cluster_centers` 속성: 최종적으로 찾은 클러스터 중심이 저장됨

#### 2. 100번째 샘플의 예측 결과를 확인해보자

```py
print(km.transform(fruits_2d[100:101]))
# [[3400.24197319 8837.37750892 5279.33763699]]
```

- `transform()`: 훈련 데이터 샘플에서 클러스터 중심까지 거리로 변환
  - 반드시 입력값으로 2차원 배열을 넣어야 함 (슬라이싱 연산자를 사용한 이유)
- 이처럼 클러스터 중심을 특성 공학처럼 사용해 데이터셋을 저차원(10,000 → 3)으로 변환할 수 있음
- 첫 번째 클러스터까지의 거리가 3400.2로 가장 작음

```py
print(km.predict(fruits_2d[100:101]))
# [0]
```

- `predict()`: 가장 가까운 클러스터 중심을 예측 클래스로 출력
- 100번째 샘플을 레이블 0(파인애플)으로 예측했음

```py
draw_fruits(fruits[100:101])
```

<img src='./100_sample_fruit.png' alt='100번째 샘플의 과일 사진' width='100px' />

- 파인애플로 잘 예측한 것을 확인할 수 있음

#### 3. 최적의 클러스터 중심을 찾기 위해 반복한 횟수를 출력해보자

```py
print(km.n_iter_)  # 4
```

- k-평균 알고리즘은 반복적으로 클러스터 중심을 옮기면서 최적의 클러스터를 찾음
- `n_iter_` 속성: 반복한 횟수 저장

### 지금까지의 과정에서 문제점

- n_clusters를 3으로 지정한 것은 타깃에 대한 정보를 활용한 셈임
- 실전에서는 클러스터 개수조차 알 수 없음

## 4️⃣ 최적의 k 찾기

- k-평균 알고리즘의 단점 중 하나는 클러스터 개수를 지정해야 한다는 것임
- 사실, 군집 알고리즘에서 적절한 k값을 찾기 위한 완벽한 방법은 없음

### 엘보우(elbow) 방법

- 적절한 클러스터 개수를 찾기 위한 대표적인 방법
- 이너셔(inertia): 클러스터 중심과 클러스터에 속한 샘플 사이 거리의 제곱 합
  - 클러스터에 속한 샘플이 얼마나 가깝게 모여 있는지를 나타내는 값으로 생각할 수 있음
  - 일반적으로 클러스터 개수가 늘어나면 클러스터 개개의 크기는 줄어들기 때문에 이너셔도 줄어듦
- 엘보우 방법은 클러스터 개수를 늘려가면서 이너셔의 변화를 관찰하여 최적의 클러스터 개수를 찾는 방법임
  - 클러스터 개수를 증가시키면서 이너셔를 그래프로 그리면 감소하는 속도가 꺾이는 지점이 있는데, 이 지점을 최적의 클러스터 개수로 결정할 수 있음

#### 1. 클러스터 개수를 증가시키면서 이너셔를 그래프로 그려보자

```py
inertia = []
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init='auto', random_state=42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)

plt.plot(range(2, 7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()
```

<img src='./k-inertia-graph.png' alt='100번째 샘플의 과일 사진' width='400px' />

- `inertia_` 속성: 이너셔 값을 저장
- k=3에서 이너셔가 줄어드는 속도가 살짝 꺾인 것으로 보아, 최적의 클러스터 개수는 3개인 것 같음

## cf) 핵심 패키지와 함수

### scikit-learn

#### `KMeans` 클래스

- k-평균 알고리즘 클래스
- n_clusters 매개변수
  - 클러스터 개수를 지정
  - 기본값: 8
- init 매개변수
  - 초기화 방법을 지정
  - 기본값: 'k-means++'
- n_init 매개변수
  - 반복 횟수를 지정
  - 기본값: 'auto'
    - init 매개변수가 'k-means++'일 경우 1이고, 'random'일 경우 10임
- max_iter 매개변수
  - k-평균 알고리즘의 한 번 실행에서 최적의 센트로이드를 찾기 위해 반복할 수 있는 최대 횟수
  - 기본값: 300
