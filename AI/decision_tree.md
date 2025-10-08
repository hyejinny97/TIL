# ✔ 결정 트리

> ['결정 트리' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/5-1.ipynb)

## 1️⃣ 로지스틱 회귀로 와인 분류하기

#### 1. 와인 데이터셋을 데이터프레임으로 읽어오자

```py
import pandas as pd

wine = pd.read_csv('https://bit.ly/wine_csv_data')
wine.head()
```

<img src='./와인_데이터셋.png' alt='와인 데이터셋' width='250px' />

- 특성: alcohol, sugar, pH
- 타깃: 레드 와인(0), 화이트 와인(1)
- 레드 와인과 화이트 와인을 구별하는 이진 분류 문제임
- 즉, 전체 와인 데이터에서 화이트 와인(양성 클래스)을 골라내는 문제임

```py
wine.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   alcohol  6497 non-null   float64
 1   sugar    6497 non-null   float64
 2   pH       6497 non-null   float64
 3   class    6497 non-null   float64
dtypes: float64(4)
memory usage: 203.2 KB
"""
```

- `info()`: 데이터프레임의 각 열의 데이터 타입과 누락된 데이터가 있는지 확인 가능
  - 누락된 값이 있다면 그 데이터를 버리거나 평균값으로 채운 후 사용할 수 있음
  - 주의) 평균값으로 누락된 값을 채울 때, 반드시 훈련 세트의 평균값으로 데스트 세트의 누락된 값으로 채워야 함

```py
wine.describe()
```

<img src='./describe_메서드.png' alt='describe 메서드' width='400px' />

- `describe()`: 열에 대한 간락한 통계를 출력해 줌
  - 최소, 최대, 평균값, 표준편차, 1사분위수, 중간값(2사분위수), 3사분위수 등

#### 2. 입력 데이터와 타깃 데이터를 만들자

```py
data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']
```

#### 3. 훈련 세트와 테스트 세트로 나누자

```py
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

print(train_input.shape, test_input.shape)  # (5197, 3) (1300, 3)
```

#### 4. 훈련 세트와 테스트 세트를 표준화 전처리하자

```py
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
```

#### 5. 로지스틱 회귀 모델을 훈련하고 테스트 해보자

```py
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_scaled, train_target)

print(lr.score(train_scaled, train_target))  # 0.781
print(lr.score(test_scaled, test_target))  # 0.778
```

- 훈련 세트와 테스트 세트의 점수가 모두 낮으니 다소 과소적합 되었음

### 설명하기 쉬운 모델과 어려운 모델

- 위에서 만든 모델을 설명하기 위해 로지스틱 회귀가 학습한 계수와 절편을 출력해보자

  ```py
  print(lr.coef_, lr.intercept_)
  # [[ 0.51268071  1.67335441 -0.68775646]] [1.81773456]
  ```

- 사실 우리는 저 모델이 왜 저런 계수 값을 학습했는지 정확히 이해하기 어려움
- 대부분의 머신러닝 모델은 이렇게 학습의 결과를 설명하기 어려움
- 반면, 결정 트리는 비교적 비전문가에게도 설명하기 쉬운 모델을 만듦

## 2️⃣ 결정 트리

- 예/아니오에 대한 질문을 이어나가면서 정답을 찾아 학습하는 알고리즘
- 비교적 예측 과정을 이해하기 쉽고 성능도 뛰어남
- 분류의 경우, 리프 노드에서 가장 많은 클래스가 예측 클래스가 됨
- 회귀의 경우, 리프 노드에 도달한 샘플의 타깃을 평균하여 예측값으로 사용함

#### 1. 결정 트리 모델을 훈련하고 테스트 해보자

```py
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)

print(dt.score(train_scaled, train_target))  # 0.997
print(dt.score(test_scaled, test_target))  # 0.859
```

- 훈련 세트에 대한 점수는 매우 높은데 테스트 세트에 대한 점수는 많이 상대적으로 낮으므로 과대적합된 모델임

#### 2. 훈련한 결정 트리를 이미지로 확인해보자

```py
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10,7))
plot_tree(dt)
plt.show()
```

<img src='./plot_tree.png' alt='결정 트리' width='350px' />

- `plot_tree()`: 결정 트리를 이해하기 쉬운 트리 그림으로 출력해줌
- 노드(node): 훈련 데이터의 특성에 대한 테스트를 표현함
  - 결정 트리를 구성하는 핵심 요소
  - 루트 노드(root node): 맨 위의 노드
  - 리프 노드(leaf node): 맨 아래 끝에 달린 노드
- 가지(branch): 테스트의 결과(True, False)를 나타냄
  - 하나의 노드는 2개의 가지를 가짐
- 너무 복잡하니 트리의 깊이를 제한해서 다시 출력해보자

```py
plt.figure(figsize=(10,7))
plot_tree(dt, max_depth=1, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()
```

<img src='./plot_tree_max_depth.png' alt='깊이를 1로 제한한 결정 트리' width='350px' />

- `max_depth`: 트리 깊이를 제한
  - 1로 주면 루트 노드를 제외하고 하나의 노드를 더 확장하여 그림
- `filled`: 클래스마다 색깔을 부여하고, 어떤 클래스의 비율이 높아지면 점점 진한 색으로 표시함
- `feature_names`: 특성의 이름을 전달
- 결과 분석
  - 'sugar <= -0.239': 테스트 조건
  - 'gini = 0.367': 불순도
  - 'samples = 5197': 총 샘플 수
  - 'value = [1258, 3939]': 클래스별 샘플 수 (음성 클래스, 양성 클래스)

### 불순도

- 결정 트리가 최적의 질문을 찾기 위한 기준임
- DecisionTreeClassifier 클래스의 `criterion` 매개변수

  - 노드에서 데이터를 분할할 기준을 정함
  - 기본값: 'gini'(지니 불순도)
  - 'entropy'로 지정하여 엔트로피 불순도를 사용할 수 있음

- 지니 불순도 (gini impurity)

  - 노드에 두 클래스 비율이 정확히 1/2씩이라면 불순도는 0.5가 되어 최악이 됨
  - 노드에 하나의 클래스만 있다면 불순도는 0이 되어 가장 작음(순수 노드)

  ```
  지니 불순도 = 1 - (음성 클래스 비율² + 양성 클래스 비율²)
  ```

- 엔트로피 불순도 (entropy impurity)

  ```
  엔트로피 불순도 = -음성 클래스 비율 * log₂(음성 클래스 비율) - 양성 클래스 비율 * log₂(양성 클래스 비율)
  ```

- 결정 트리 모델은 부모 노드와 자식 노드의 불순도 차이가 가능한 크도록 트리를 성장시킴

  - 다시 말해, 정보 이득이 최대가 되도록 데이터를 나눔
  - 노드를 순수하게 나눌수록 정보 이득이 커짐

  ```
  부모와 자식 사이의 불순도 차이
  = 정보 이득 (information gain)
  = 부모의 불순도
    - (왼쪽 노드 샘플 수 / 부모 샘플 수) * 왼쪽 노드 불순도
    - (오른쪽 노드 샘플 수 / 부모 샘플 수) * 오른쪽 노드 불순도
  ```

### 가지치기

- 결정 트리는 제한 없이 성장하면 훈련 세트에 과대적합되기 쉬움 (일반화가 잘 안됨)
- 가지치기는 결정 트리의 성장을 제한하는 방법임
- 사이킷런의 결정 트리 알고리즘은 여러 가지 가지치기 매개변수를 제공함
- 결정 트리에서 가지치기를 하는 가장 간단한 방법은 트리의 깊이를 지정하는 것임

#### 1. 트리의 깊이를 제한한 후, 결정 트리 모델을 훈련하고 테스트 해보자

```py
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_scaled, train_target)

print(dt.score(train_scaled, train_target))  # 0.845
print(dt.score(test_scaled, test_target))  # 0.842
```

- 결과를 확인해보니, 훈련 세트의 성능은 낮아졌지만 테스트 세트의 성능은 거의 그대로임

#### 2. 훈련한 결정 트리를 이미지로 확인해보자

```py
plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()
```

<img src='./tree_max_depth_3.png' alt='트리의 max_depth가 3인 결정 트리' width='700px' />

- 사실, **결정 트리는 표준화 전처리 과정이 필요 없음**
  - 결정 트리는 불순도를 기준으로 샘플을 나누는데, 불순도는 클래스별 비율을 가지고 계산함
  - 즉, 특성값의 스케일은 불순도를 계산하는데 아무런 영향을 미치지 않음

#### 3. 전처리하기 전의 데이터로 결정 트리 모델을 다시 훈련하고 테스트 해보자

```py
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_input, train_target)

print(dt.score(train_input, train_target))  # 0.845
print(dt.score(test_input, test_target))  # 0.842
```

#### 4. 훈련한 결정 트리를 이미지로 다시 확인해보자

```py
plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()
```

<img src='./no_scaled_tree.png' alt='전처리하지 않은 결정 트리' width='700px' />

- 결과를 보면, 같은 트리지만 특성값을 표준점수로 바꾸지 않아 이해하기가 훨씬 쉬움

#### 5. 특성 중요도를 확인해보자

```py
print(dt.feature_importances_)
# [0.12345626 0.86862934 0.0079144 ]
```

- 특성 중요도: 결정 트리에 사용된 특성이 불순도를 감소하는데 기여한 정도를 나타낸 값
- `feature_importances_`: 특성 중요도
  - 어떤 특성이 가장 유용한지 계산해 줌
  - 각 노드의 정보 이득과 전체 샘플에 대한 비율을 곱한 후 특성별로 더하여 계산함
  - 중요도 값을 모두 더하면 1이 됨
- pH(0.0079144), 알코올 도수(0.12345626), 당도(0.86862934) 순으로 높은 것을 알 수 있음
- 결정 트리의 특성 중요도를 특성 선택에 활용할 수 있음

## cf) 핵심 패키지와 함수

### pandas

#### `info()` 함수

- 데이터프레임의 요약된 정보를 출력함
  - 인덱스
  - 컬럼 타입
  - null이 아닌 값의 개수
  - 메모리 사용량
- verbose 매개변수
  - False이면 각 열에 대한 정보를 출력하지 않음
  - 기본값: True

#### `describe()` 함수

- 데이터프레임 열의 통계 값을 제공함
  - 수치형인 경우
    - 최소
    - 최대
    - 평균
    - 표준편차
    - 사분위값
  - 문자열 같은 객체 타입의 열인 경우
    - 가장 자주 등장하는 값과 횟수
- percentiles 매개변수
  - 백분위수를 지정
  - 기본값: [0.25, 0.5, 0.75]

### scikit-learn

#### `DecisionTreeClassifier` 클래스

- 결정 트리 분류 클래스
- criterion 매개변수

  - 불순도를 지정
  - 'entropy': 엔트로피 불순도
  - 'gini': 지니 불순도
  - 기본값: 'gini'

- splitter 매개변수

  - 노드를 분할하는 전략을 선택
  - 'best': 정보 이득이 최대가 되도록 분할함
  - 'random': 임의로 노드를 분할함
  - 기본값: 'best'

- max_depth 매개변수

  - 트리가 성장할 최대 깊이를 지정함
  - 기본값: None (리프 노드가 순수하거나, min_samples_split보다 샘플 개수가 적을 때까지 성장함)

- min_samples_split 매개변수

  - 노드를 나누기 위한 최소 샘플 개수
  - 기본값: 2

- max_features 매개변수

  - 최적의 분할을 위해 탐색할 특성의 개수를 지정
  - 기본값: None (모든 특성을 사용)

- min_impurity_decrease 매개변수
  - 어떤 노드의 '정보 이득 \* (노드의 샘플 수) / (전체 샘플 수)' 값이 이 매개변수의 값보다 작으면 더 이상 분할되지 않음

#### `plot_tree()` 함수

- 결정 트리 모델을 시각화함
- 첫 번째 매개변수로 결정 트리 모델 객체를 전달

- max_depth 매개변수

  - 나타낼 트리의 깊이를 지정
  - 기본값: None (모든 노드를 출력)

- feature_names 매개변수

  - 특성의 이름을 지정

- filled 매개변수
  - True이면 타깃값에 따라 노드 안에 색을 채움
