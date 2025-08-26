# ✔ 마켓과 머신러닝

> ['마켓과 머신러닝' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/1-3.ipynb)

## 1️⃣ 생선 분류 문제

- 문제) 도미와 빙어 여러 마리가 섞여 있을 때 이 중 어떤 생선이 도미인지 어떻게 알 수 있을까?
- 머신러닝은 누구도 알려주지 않는 기준을 스스로 찾아서 일을 함

#### cf) 이진 분류

- 분류(classification): 머신러닝에서 여러 개의 종류(또는 클래스) 중 하나를 구별해 내는 것
- 이진 분류(binary classification): 2개의 클래스 중 하나를 고르는 것

### 도미 데이터 준비하기

- 머신러닝은 여러 개의 도미 생선을 보면서 스스로 어떤 생선이 도미인지를 구분할 기준을 찾음

#### 1. 35마리의 도미를 파이썬 리스트로 표현하자

```py
bream_length = [25.4, 26.3, 26.5, ...]
bream_weight = [242.0, 290.0, 340.0, ...]
```

- 특성(feature): 데이터를 표현하는 하나의 성질
- 도미는 '길이'와 '무게' 2가지 특성을 가짐

#### 2. 각 도미를 그래프에 점으로 표시해보자

```py
import matplotlib.pyplot as plt

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- 2개의 특성을 사용해 그린 그래프이므로 2차원 그래프임
- 맷플롯립(matplotlib): 파이썬에서 과학계산용 그래프를 그리는 대표적인 패키지
- `scatter()`: 산점도를 그려줌
  - 산점도(scatter plot): x, y축으로 이뤄진 좌표계에 두 변수(x, y)의 관계를 표현하는 방법
  - 산점도 그래프가 일직선에 가까운 형태로 나타나면 '선형적'이라고 함
- `xlabel()`, `ylabel()`: 각각 x축, y축의 이름을 화면에 표시함
- `show()`: 준비된 그래프를 화면에 출력함

### 빙어 데이터 준비하기

#### 1. 14마리의 빙어를 파이썬 리스트로 표현하자

```py
smelt_length = [9.8, 10.5, 10.6, ...]
smelt_weight = [6.7, 7.5, 7.0, ...]
```

#### 2. 빙어 데이터도 그래프에 표시해보자

```py
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- 맷플롯립은 친절하게 2개의 산점도를 색깔로 구분해서 나타냄

## 2️⃣ 첫 번째 머신러닝 프로그램

- k-최근접 이웃(k-Nearest Neighbors) 알고리즘을 사용해 도미와 빙어 데이터를 구분해보려고 함
- 머신러닝 라이브러리인 사이킷런을 사용하려면 데이터를 2차원 리스트로 만들어야 함

### 데이터 준비하기

#### 1. 도미와 빙어 데이터를 합쳐 2차원 리스트로 만들자

```py
length = bream_length+smelt_length
weight = bream_weight+smelt_weight

fish_data = [[l, w] for l, w in zip(length, weight)]
```

#### 2. 정답 데이터를 만들자

```py
fish_target = [1]*35 + [0]*14
```

- 도미와 빙어를 각각 숫자 1과 0으로 표현함
- 이진 분류의 경우, 찾으려는 대상을 1로 놓고 그 외에는 0으로 놓음
- 이진 분류에서 1을 양성 클래스(positive class), 0을 음성 클래스(negative class)라고 부름

### k-최근접 이웃 알고리즘

- 어떤 데이터에 대한 답을 구할 때 주위의 다른 데이터를 보고 다수를 차지하는 것을 정답으로 사용함
- 사실 k-최근접 이웃 알고리즘은 가장 간단한 머신러닝 알고리즘 중 하나로, 어떤 규칙을 찾기보다는 전체 데이터를 메모리에 가지고 있는 것이 전부임
- 단점
  - 데이터가 많은 경우, 메모리가 많이 필요하고 직선거리를 계산하는 데도 많은 시간이 필요함

#### 1. 준비한 데이터로 알고리즘을 훈련하자

```py
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
```

- 훈련(training): 모델에 데이터를 전달하여 규칙을 학습하는 과정
- `fit()`: 주어진 데이터로 알고리즘을 훈련함

#### 2. 훈련한 모델을 평가해보자

```py
kn.score(fish_data, fish_target)
```

- KNeighborsClassifier 객체에서 score 메서드를 사용하면 **정확도**(accuracy)를 얻을 수 있음
  - 정확도: 정확한 답을 몇 개 맞혔는지를 백분율로 나타낸 값
  - 정확도 = (정확히 맞힌 개수) / (전체 데이터 개수)
- `score()`: 모델을 평가함
  - 0에서 1 사이의 값을 반환함
  - 1은 모든 데이터를 정확히 맞혔음을 의미함

```py
kn.predict([[30, 600]])
```

- `predict()`: 새로운 데이터의 정답을 예측함

## cf) 핵심 패키지와 함수

### matplotlib

#### `scatter()` 함수

- 산점도를 그리는 함수
- 처음 2개의 매개변수로 x축 값, y축 값을 전달함
  - 이 값은 파이썬 리스트(또는 넘파이 배열)임
- c 매개변수로 색깔 지정 가능
  - 16진수
  - 색깔 코드('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
  - 지정하지 않을 경우 10개의 기본 색깔을 사용해 그래프를 그림
- marker 매개변수로 마커 스타일 지정 가능
  - 기본값: o (원)

### scikit-learn

#### `KNeighborsClassifier()` 클래스

- k-최근접 이웃 분류 모델을 만드는 클래스
- n_neighbors 매개변수로 이웃의 개수 지정 가능
  - 기본값: 5
- p 매개변수로 거리를 재는 방법 지정 가능
  - 1: 맨해튼 거리, 2: 유클리드 거리
  - 기본값: 2
- n_jobs 매개변수로 사용할 CPU 코어 지정 가능
  - -1: 모든 CPU 코어 사용
  - 기본값: 1

#### `fit()` 메서드

- 사이킷런 모델을 훈련할 때 사용하는 메서드
- 처음 2개의 매개변수로 훈련에 사용할 특성과 정답 데이터를 전달함

#### `predict()` 메서드

- 사이킷런 모델을 훈련하고 예측할 때 사용하는 메서드
- 특성 데이터 하나만 매개변수로 받음

#### `score()` 메서드

- 훈련된 사이킷런 모델의 성능을 측정하는 메서드
- 처음 2개의 매개변수로 특성과 정답 데이터를 전달함

#### `_fit_X` 속성

```py
kn._fit_X
```

- 모델을 훈련할 때 사용된 입력 데이터를 모두 가지고 있음

#### `_y` 속성

```py
kn._y
```

- 모델을 훈련할 때 사용된 타겟 데이터를 모두 가지고 있음
