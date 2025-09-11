# ✔ 선형 회귀

> ['선형 회귀' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/3-2.ipynb)

## 1️⃣ k-최근접 이웃의 한계

#### 1. 농어 데이터를 가지고, k-최근접 이웃 회귀 모델을 훈련해보자

```py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, ...])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, ...])

train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

knr = KNeighborsRegressor(n_neighbors=3)
knr.fit(train_input, train_target)
```

#### 2. 길이가 50cm인 농어의 무게를 예측해보자

```py
knr.predict([[50]])  # [1033.33] ❗
```

- 문제점) 실제 50cm 농어의 무게는 훨씬 더 많이 나감

#### 3. 훈련 세트와 50cm 농어, 이 농어의 최근접 이웃을 산점도에 표시해보자

```py
import matplotlib.pyplot as plt

distances, indexes = knr.kneighbors([[50]])

plt.scatter(train_input, train_target)
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
plt.scatter(50, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- 원인) 50cm 농어에서 가장 가까운 것은 45cm 근방이기 때문에 이 샘플들의 무게를 평균했음
- 길이가 100cm인 농어도 1,033g으로 예측할 것임
- k-최근접 이웃의 한계
  - k-최근접 이웃 회귀는 가장 가까운 샘플을 찾아 타깃을 평균하기 때문에, 새로운 샘플이 훈련 세트의 범위를 벗어나면 엉뚱한 값을 예측할 수 있음

## 2️⃣ 선형 회귀

- 널리 사용되는 대표적인 회귀 알고리즘
- 특성과 타깃 사이의 관계를 잘 나타내는 선형 방정식을 찾음
- 선형 회귀가 찾은 특성과 타깃 사이의 관계는 선형 방정식의 계수(또느 가중치)에 저장됨
  - 머신러닝에서 종종 가중치는 방정식의 기울기와 절편을 모두 의미하는 경우가 많음
- 특성이 하나인 경우, 어떤 직선을 학습함

  - 하나의 직선이 그리려면 기울기와 절편이 있어야 함

  ```
  y = a * x + b
  ```

#### 1. 농어 데이터를 가지고, 선형 회귀 모델을 훈련해보자

```py
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(train_input, train_target)
```

#### 2. 길이가 50cm인 농어의 무게를 예측해보자

```py
lr.predict([[50]])  # [1241.84]
```

- k-최근접 이웃 회귀를 사용했을 때에 비해 농어의 무게를 아주 높게 예측했음

#### 3. 계수와 절편을 확인해보자

```py
print(lr.coef_, lr.intercept_)  # [39.017] -709.019
```

- 1차원 그래프에서 x는 농어의 길이, y는 농어의 무게임

  ```
  y = 39.017 * x - 709.019
  ```

- `lr.coef_`: 계수 또는 가중치
- `lr.intercept_`: 절편
- 모델 파라미터: 'coef\_'와 'intercept\_'처럼 머신러닝 알고리즘이 찾은 값
- 모델 기반 학습: 최적의 모델 파라미터를 찾는 알고리즘 훈련 과정
  - ex) 선형 회귀 등 대부분의 머신러닝 알고리즘
- 사례 기반 학습: 훈련 세트를 저장하는 것이 전부인 알고리즘 훈련 과정
  - ex) k-최근접 이웃 알고리즘

#### 4. 훈련 세트와 50cm 농어, 1차 방정식 그래프를 산점도에 표현해보자

```py
plt.scatter(train_input, train_target)
plt.plot([15, 50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])
plt.scatter(50, 1241.8, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- 바로 이 직선이 선형 회귀 알고리즘이 데이터셋에서 찾은 최적의 직선임
- 길이가 50cm인 농어에 대한 예측은 이 직선의 연장선에 있음
- 이제 훈련 세트 범위를 벗어난 농어의 무게도 예측할 수 있게 됨

#### 5. 훈련 세트와 테스트 세트로 모델을 평가해보자

```py
lr.score(train_input, train_target)  # 0.94
lr.score(test_input, test_target)  # 0.82
```

- 훈련 세트와 테스트 세트가 전체적으로 약간씩 낮기 때문에 과소적합 되었다고 볼 수 있음
- 문제점) 선형 회귀가 만든 직선을 보면 왼쪽 아래로 내려가 있음. 이 직선대로 예측하면 농어의 길이가 아주 작을 때 농어의 무게가 0g 이하로 내려갈텐데 현실에서는 있을 수 없는 일임

## 3️⃣ 다항 회귀

- 산점도를 보면 일직선이라기보다 왼쪽 위로 조금 구부러진 곡선에 가까움
- 따라서, 최적의 직선을 찾기보다 최적의 곡선을 찾아보자
- 다항 회귀: 다항식을 사용한 선형 회귀

#### 1. 농어의 길이를 제곱한 항을 입력 데이터에 추가해보자.

```py
train_poly = np.column_stack((train_input ** 2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))

print(train_poly.shape, test_poly.shape)  # (42, 2) (14, 2)
```

- 2차 방정식의 그래프를 그리려면 길이를 제곱한 항이 훈련 세트에 추가되어야 함
- 길이를 제곱 또는 세제곱하더라도 여전히 선형 회귀로 다룰 수 있음
  - 이유: 선형 회귀의 선형은 입력과 타깃 사이의 관계가 아니라 가중치(계수)와 타깃 사이의 관계를 의미하기 때문

#### 2. 새로운 데이터로 선형 회귀 모델을 다시 훈련해보자.

```py
lr = LinearRegression()
lr.fit(train_poly, train_target)
```

#### 3. 길이가 50cm인 농어의 무게를 예측해보자

```py
lr.predict([[50**2, 50]])  # [1573.98]
```

- 위에서 훈련한 모델보다 더 높은 값을 예측함

#### 4. 계수와 절편을 확인해보자

```py
print(lr.coef_, lr.intercept_)  # [1.01, -21.56] 116.05
```

- 2차원 그래프에서 x는 농어의 길이, y는 농어의 무게임

  ```
  y = 1.01 * x² - 21.56 * x + 116.05
  ```

#### 5. 훈련 세트와 50cm 농어, 1차 방정식 그래프를 산점도에 표현해보자

```py
point = np.arange(15, 50)
plt.scatter(train_input, train_target)
plt.plot(point, 1.01*point**2 - 21.6*point + 116.05)
plt.scatter([50], [1574], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

- 짧은 직선을 이어서 그리면 마치 곡선처럼 표현할 수 있음
- 그래프를 보니 훈련 세트의 경향을 잘 따르고 있고 무게가 음수로 나오지도 않을 것 같음

#### 6. 훈련 세트와 테스트 세트로 모델을 평가해보자

```py
lr.score(train_poly, train_target)  # 0.97
lr.score(test_poly, test_target)  # 0.98
```

- 훈련 세트와 테스트 세트에 대한 점수가 크게 높아졌음
- 하지만, 과소적합이 아직 남아 있음

## cf) 핵심 패키지와 함수

### scikit-learn

#### `LinearRegression` 클래스

- 사이킷런의 선형 회귀 클래스
- fit_intercept 매개변수
  - False이면 절편을 학습하지 않음
  - 기본값: True
- coef\_ 속성
  - 특성에 대한 계수를 포함한 배열
  - 이 배열의 크기는 특성의 개수와 같음
- intercept\_ 속성
  - 절편
