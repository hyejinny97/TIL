# ✔ 훈련 세트와 테스트 세트

> ['훈련 세트와 테스트 세트' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/2-1.ipynb)

## 1️⃣ 지도 학습과 비지도 학습

- 머신러닝 알고리즘은 크게 지도 학습, 비지도 학습, 강화 학습으로 나눌 수 있음
- 지도 학습 알고리즘은 입력(데이터)과 타깃(정답)으로 이뤄진 훈련 데이터가 필요함
  - 타킷(정답)이 있으니 정답을 맞히는 것을 학습함
  - ex) k-최근접 이웃 알고리즘
- 비지도 학습 알고리즘은 타깃 없이 입력 데이터만 사용함
  - 무언가 정답을 맞히는 대신 데이터를 잘 파악하거나 변형하는 데 도움을 줌
- 강화 학습은 타깃이 아니라 알고리즘이 행동한 결과로 얻은 보상을 사용해 학습됨

## 2️⃣ 훈련 세트와 테스트 세트

- 머신러닝 알고리즘의 성능을 제대로 평가하려면 훈련 데이터와 평가에 사용할 데이터가 각각 달라야 함
  - 훈련 세트: 훈련에 사용되는 데이터
  - 테스트 세트: 평가에 사용하는 데이터

#### 1. 생선 데이터(35마리의 도미, 14마리의 빙어)와 타깃을 파이썬 리스트로 준비하자

```py
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, ...]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, ...]

fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14
```

- 입력으로 사용된 길이와 무게를 특성(feature)이라고 함
- 하나의 생선 데이터를 샘플(sample)이라고 부름

#### 2. 생선 데이터와 타깃을 훈련 세트와 테스트 세트로 나누자

```py
train_input = fish_data[:35]
train_target = fish_target[:35]

test_input = fish_data[35:]
test_target = fish_target[35:]
```

#### 3. 훈련 세트로 모델을 훈련하고, 테스트 세트로 평가해보자

```py
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
kn.score(test_input, test_target)  # 정확도: 0.0 ❗
```

## 3️⃣ 샘플링 편향

- 훈련 세트와 테스트 세트에 샘플이 골고루 섞여 있지 않아 샘플링이 한쪽으로 치우쳐진 현상
- 훈련 세트와 테스트 세트에 있는 샘플의 클래스 비율이 다르면 제대로 된 지도 학습 모델을 만들 수 없음

## 4️⃣ 넘파이

- 넘파이는 파이썬의 대표적인 배열 라이브러리임
- 고차원의 배열을 손쉽게 만들고 조작할 수 있는 간편한 도구를 많이 제공함
- 1차원 배열은 선이고, 2차원 배열은 면, 3차원 배열은 공간을 나타냄

#### 1. 파이썬 리스트를 넘파이 배열로 변경하자

```py
import numpy as np

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)
```

- `array()` 함수: 파이썬 리스트를 넘파이 배열로 변환해줌
- 넘파이는 친절하게 배열의 차원을 구분하기 쉽도록 행과 열을 가지런히 출력해줌

```py
input_arr.shape  # (49, 2) = (샘플 수, 특성 수)
```

- `shape` 속성: 배열의 크기를 알려줌

#### 2. 49개의 생선 데이터를 무작위로 섞은 후 훈련 세트와 테스트 세트로 분리하자

```py
index = np.arange(49)
np.random.seed(42)
np.random.shuffle(index)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]
```

- `arange()` 함수: n개의 연속적인 숫자를 담은 배열을 반환함 (0 ~ n-1)
- 넘파이에서 무작위 결과를 만드는 함수들은 실행할 때마다 다른 결과를 만듦
  - 초기에 랜덤 시드(random seed)를 지정하면 일정한 결과를 얻을 수 있음
- `shuffle()` 함수: 주어진 배열을 무작위로 섞음
- 넘파이의 '배열 인덱싱': 1개의 인덱스가 아닌 여러 개의 인덱스로 한 번에 여러 개의 원소를 선택할 수 있음

  ```py
  input_arr[[1, 3]]
  """
  [[ 26.3 290. ]
   [ 29.  363. ]]
  """
  ```

#### 3. 훈련 세트와 테스트 세트를 산점도로 표시해보자

```py
import matplotlib.pyplot as plt

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- 2차원 배열은 행과 열 인덱스를 콤마로 나누어 저장함

## 5️⃣ 두 번째 머신러닝 프로그램

#### 1. 새로 만든 훈련 세트로 모델을 훈련하고, 테스트 세트로 평가해보자

```py
kn.fit(train_input, train_target)
kn.score(test_input, test_target)  # 정확도: 1.0
```

- `fit()` 메서드를 실행할 때마다 KNeighborsClassifier 클래스의 객체는 이전에 학습한 모든 것을 잃어버림

```py
kn.predict(test_input)
# array([0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0])
```

- 사이킷런 모델의 입력과 출력은 모두 넘파이 배열임

## cf) 핵심 패키지와 함수

### numpy

#### `seed()` 함수

- 넘파이에서 난수를 생성하기 위한 정수 초깃값을 지정함
- 초깃값이 같으면 동일한 난수를 뽑을 수 있음
- 따라서, 랜덤 함수의 결과를 동일하게 재현하고 싶을 때 사용함

#### `arange()` 함수

- 일정한 간격의 정수 또는 실수 배열을 만듦
  - 기본 간격: 1
- 매개 변수가 하나이면 종료 숫자를 의미함

  ```py
  np.arange(3)  # [0, 1, 2]
  ```

- 매개 변수가 2개면 시작 숫자, 종료 숫자를 의미함

  ```py
  np.arange(1, 3)  # [1, 2]
  ```

- 매개 변수가 3개면 마지막 매개변수가 간격을 나타냄

  ```py
  np.arange(1, 3, 0.2)
  # [1., 1.2, 1.4, 1.6, 1.8, 2., 2.2, 2.4, 2.6, 2.8]
  ```

#### `shuffle()` 함수

- 주어진 배열을 랜덤하게 섞음
- 다차원 배열일 경우, 첫 번째 축(행)에 대해서만 섞음
