# ✔ 데이터 전처리

> ['데이터 전처리' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/2-2.ipynb)

## 1️⃣ 넘파이로 데이터 준비하기

#### 1. 생선 데이터(35마리의 도미, 14마리의 빙어)를 넘파이로 준비하자

```py
import numpy as np

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, ...]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, ...]

np.column_stack((fish_length, fish_weight))
```

- `column_stack()`: 전달 받은 리스트를 일렬로 세운 다음 차례대로 나란히 연결함
  - 연결할 리스트는 파이썬 튜플(tuple)로 전달함
  - 튜플은 리스트처럼 원소에 순서가 있지만 수정할 수 없음
  - 따라서, 값이 변하지 않는다는 것을 믿을 수 있기 때문에 튜플은 매개변수 값으로 많이 사용함

#### 2. 타깃 데이터도 넘파이로 준비하자

```py
import numpy as np

fish_target = np.concatenate((np.ones(35), np.zeros(14)))
```

- `ones()`: 원하는 개수만큼 1을 채운 배열을 만들어줌
- `zeros()`: 원하는 개수만큼 0을 채운 배열을 만들어줌
- `concatenate()`: 첫 번째 차원을 따라 배열을 연결해줌

## 2️⃣ 사이킷런으로 훈련 세트와 테스트 세트 나누기

#### 1. 생선 데이터와 타깃을 훈련 세트와 테스트 세트로 나누자

```py
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target, stratify=fish_target, random_state=42)
```

- `train_test_split()`: 리스트나 배열을 비율에 맞게 훈련 세트와 테스트 세트로 나눠줌
  - 기본적으로 25%를 테스트 세트로 떼어냄
  - `random_state` 매개변수: 랜덤 시드 지정 가능
  - `stratify` 매개변수: 타깃 데이터를 전달하면 클래스 비율에 맞게 데이터를 나눠줌

## 3️⃣ 수상한 도미 한 마리

#### 1. 훈련 세트로 모델을 훈련하고, 테스트 세트로 평가해보자

```py
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
kn.score(test_input, test_target)  # 1.0
```

#### 2. 특정 도미 데이터를 넣어 예측 결과를 확인해보자

```py
kn.predict([[25, 150]])  # [0.] ❗
```

#### 3. 훈련 세트, 특정 도미 데이터와 이웃 샘플(5개)을 산점도로 확인해보자

```py
import matplotlib.pyplot as plt

distances, indexes = kn.kneighbors([[25, 150]])

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- `kneighbors()`: 주어진 샘플에서 가장 가까운 이웃을 찾아줌
  - 이웃 개수인 `n_neighbors` 값 만큼 반환함 (기본값: 5)
- 산점도 확인 결과, 눈으로 봤을 때 빙어 샘플보다 도미 샘플이 거리가 더 가까워보이지만 이상하게 빙어 샘플이 더 많이 선택된 것을 확인할 수 있음
- 샘플들 간 거리 비율도 이상함

## 4️⃣ 기준을 맞춰라

- 원인) x축(length)은 범위가 좁고(10~40), y축(weight)은 범위가 넓기(0~1000) 때문에 y축으로 조금만 멀어져도 거리가 아주 큰 값으로 계산됨
  - 즉, 생선의 길이(x축)는 가장 가까운 이웃을 찾는데 크게 영향을 미치지 않고, 오로지 생선의 무제(y축)만 고려 대상이 됨
- 두 특성의 스케일(scale)이 다르면 알고리즘이 올바르게 예측할 수 없음
  - 스케일: 값의 범위
- 특히 거리 기반 알고리즘들은 샘플 간의 거리에 영향을 많이 받으므로 제대로 사용하려면 특성값을 일정한 기준으로 맞춰 주어야 함 (데이터 전처리, data preprocessing)
  - 거리 기반 알고리즘 예: k-최근접 이웃 알고리즘
  - 반면, 트리 기반 알고리즘은 특성의 스케일이 다르더라도 잘 작동함
- 표준 점수(z 점수): 각 특성값이 평균에서 표준편차의 몇 배만큼 떨어져 있는지를 나타냄
  - 가장 널리 사용하는 전처리 방법 중 하나
  - 분산: 데이터에서 평균을 뺀 값을 모두 제곱한 다음 평균을 냄
  - 표준편차: 분산의 제곱근
  - 표준화: 데이터를 표준점수로 변환하는 과정

#### 1. 훈련용 생선 데이터를 표준화하자

```py
mean = np.mean(train_input, axis=0)  # [27.29722222 454.09722222]
std = np.std(train_input, axis=0)  # [9.98244253 323.29893931]

train_scaled = (train_input - mean) / std
"""
[[ 0.24070039  0.14198246]
 [-1.51237757 -1.36683783]
 [ 0.5712808   0.76060496]
 ...
]
"""
```

- `mean()`: 평균을 계산함

  - `axis`가 0이면 행을 따라 각 열의 통계 값을 계산함

- `std()`: 표준편차를 계산함

  - `axis`가 0이면 행을 따라 각 열의 통계 값을 계산함

- 브로드캐스팅: 크기가 다른 넘파이 배열에서 자동으로 사칙 연산을 모든 행이나 열로 확장하여 수행하는 기능
  - 브로드캐스팅은 train_input, mean, std처럼 넘파이 배열 사이에서 일어남

#### 2. 테스트용 생선 데이터도 표준화하자

```py
test_scaled = (test_input - mean) / std
```

- 주의) 반드시 훈련 세트의 mean, std를 이용해서 변환해야 함

#### 3. 특정 도미 데이터도 표준화하자

```py
new = ([25, 150] - mean) / std
```

- 주의) 반드시 훈련 세트의 mean, std를 이용해서 변환해야 함

## 5️⃣ 전처리 데이터로 모델 훈련하기

#### 1. 다시 훈련 세트로 모델을 훈련하고, 테스트 세트로 평가해보자

```py
kn.fit(train_scaled, train_target)
kn.score(test_scaled, test_target)  # 1.0
```

#### 2. 특정 도미 데이터를 넣어 예측 결과를 확인해보자

```py
kn.predict([new])  # [1.]
```

#### 3. 훈련 세트, 특정 도미 데이터와 이웃 샘플(5개)을 산점도로 확인해보자

```py
import matplotlib.pyplot as plt

distances, indexes = kn.kneighbors([new])

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- 산점도 확인 결과, 특정 도미 샘플과 가장 가까운 샘플 5개가 전부 도미인 것을 확인할 수 있음

## cf) 핵심 패키지와 함수

### scikit-learn

#### `train_test_split()` 함수

- 훈련 데이터를 훈련 세트와 테스트 세트로 나누는 함수
- test_size 매개변수
  - 테스트 세트로 나눌 비율 지정
  - 기본값: 0.25 (25%)
- shuffle 매개변수
  - 훈련 세트와 테스트 세트로 나누기 전에 무작위로 섞을지 여부
  - 기본값: True
- stratify 매개변수
  - 클래스 레이블이 담긴 배열(일반적으로 타깃 데이터)을 전달하면 클래스 비율에 맞게 훈련 세트와 테스트 세트를 나눔

#### `kneighbors()` 메서드

- k-최근접 이웃 객체의 메서드
- 입력한 데이터에 가장 가까운 이웃을 찾아 거리와 이웃 샘플의 인덱스를 반환함
- 기본적으로 n_neighbors 매개변수에 지정한 개수를 사용해 이웃의 개수를 정함
- return_distance 매개변수
  - False로 지정하면 이웃 샘플의 인덱스만 반환하고 거리는 반환하지 않음
  - 기본값: True
