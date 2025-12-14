# ✔ k-최근접 이웃 회귀

> ['k-최근접 이웃 회귀' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/3-1.ipynb)

## 1️⃣ k-최근접 이웃 회귀

- 지도 학습 알고리즘은 크게 분류와 회귀(regression)으로 나뉨
  - 분류: 샘플을 몇 개의 클래스 중 하나로 예측
  - 회귀: 임의의 어떤 숫자를 예측
- k-최근접 이웃 분류: 예측하려는 샘플에 가장 가까운 샘플 k개를 선택한 후, 샘플들의 클래스를 확인하여 다수 클래스를 새로운 샘플의 클래스로 예측함
- k-최근접 이웃 회귀: 예측하려는 샘플에 가장 가까운 샘플 k개를 선택한 후, 샘플들의 수치들을 평균하여 샘플의 값을 예측함
- k-최근접 이웃 회귀 알고리즘을 사용해, 농어의 길이(특성)가 주어지면 무게(타겟)를 예측해보자

## 2️⃣ 데이터 준비

#### 1. 생선 데이터(56마리의 농어)를 넘파이로 준비하자

```py
perch_length = np.array([8.4, 13.7, 15.0, ...])
perch_weight = np.array([5.9, 32.0, 40.0, ...])
```

#### 2. 생선 데이터를 산점도로 확인해보자

```py
import matplotlib.pyplot as plt

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

#### 3. 훈련 세트와 테스트 세트로 나누자

```py
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)
```

- 사이킷런에 사용할 휸련 데이터는 반드시 2차원 배열이어야 함
- `reshape()`: 넘파이 배열의 크기를 바꿔줌
  - 크기에 -1을 지정하면 다른 차원을 채우고 남은 원소에 맞게 크기를 설정하게 됨

## 3️⃣ 결정계수(R²)

- 분류에서의 score: 정확도
  - 테스트 세트에 있는 샘플을 정확하게 분류한 개수의 비율
  - 정답을 맞힌 개수의 비율
- 회귀에서의 score: 결정계수(R²)

  ```
  R² = 1 - ((타깃 - 예측)²의 합 / (타깃 - 평균)²의 합)
  ```

  - 대표적인 회귀 문제의 성능 측정 도구
  - 타깃의 평균 정도를 예측하는 수준이라면 R²은 0에 가까워짐
  - 예측이 타깃에 가까워지면 R²은 1에 가까워짐

#### 1. 훈련 세트로 모델을 훈련하고, 테스트 세트로 평가해보자

```py
from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor()
knr.fit(train_input, train_target)
knr.score(test_input, test_target)  # 0.993
```

- 사이킷런의 score() 메서드가 출력하는 값은 높을수록 좋음

#### 2. 테스트 세트에 대한 예측과 타깃의 오차를 구하자

```py
from sklearn.metrics import mean_absolute_error

test_prediction = knr.predict(test_input)
mae = mean_absolute_error(test_target, test_prediction)  # 19.16
```

- `mean_absolute_error()`: 타깃과 예측의 절댓값 오차를 평균함

## 4️⃣ 과대적합 vs 과소적합

- 과대적합(overfitting): 테스트 세트에 비해 훈련 세트의 점수가 너무 높은 경우
  - 해결 방법: 모델을 덜 복잡하게 만들어야 함
- 과소적합(underfitting): 훈련 세트보다 테스트 세트의 점수가 높거나, 두 점수가 모두 낮은 경우
  - 해결 방법: 모델을 더 복잡하게 만들어야 함

#### 1. 훈련한 모델을 사용해 훈련 세트의 점수를 확인해보자

```py
knr.score(train_input, train_target)  # 0.97
```

- 훈련 세트보다 테스트 세트의 점수가 약간 높으니 과소적합임
- 과소적합 해결 방안: 모델을 조금 더 복잡하게 만들면 됨
- k-최근접 이웃 알고리즘으로 모델을 더 복잡하게 만드는 방법은 이웃의 개수 k를 줄이는 것임
  - 이웃의 개수를 줄이면 훈련 세트에 있는 국지적인 패턴에 민감해짐
  - 반대로, 이웃의 개수를 늘리면 데이터 전반에 있는 일반적인 패턴을 따르게 됨

#### 2. 이웃의 개수를 줄인 후, 다시 훈련하고 평가해보자

```py
knr.n_neighbors = 3

knr.fit(train_input, train_target)
knr.score(train_input, train_target)  # 0.98
knr.score(test_input, test_target)  # 0.97
```

- k 값을 줄였더니 훈련 세트의 R² 점수가 높아지고 과소적합 문제를 해결함

## cf) 핵심 패키지와 함수

### scikit-learn

#### `KNeighborsRegressor` 클래스

- k-최근접 이웃 회귀 모델을 만드는 사이킷런 클래스
- n_neighbors 매개변수
  - 이웃의 개수를 지정
  - 기본값: 5

#### `mean_absolute_error()` 함수

- 회귀 모델의 평균 절댓값 오차를 계산함
- 첫 번째 매개변수
  - 타깃
- 두 번째 매개변수
  - 예측값

### numpy

#### `reshape()` 메서드

- 배열의 크기를 바꾸는 메서드
- 바꾸고자 하는 배열의 크기를 매개변수로 전달함
- 바꾸기 전후의 배열 원소 개수는 반드시 동일해야 함
