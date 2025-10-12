# ✔ 트리의 앙상블

> ['트리의 앙상블' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/5-3.ipynb)

## 1️⃣ 정형 데이터와 비정형 데이터

- 정형 데이터(structured data): 어떤 구조로 되어 있는 데이터
  - CSV, 데이터베이스, 엑셀에 저장하기 쉬운 데이터
  - 지금까지 배운 머신러닝 알고리즘은 정형 데이터에 잘 맞음
- 비정형 데이터(unstructured data): 구조적이지 않은 데이터
  - CSV, 데이터베이스, 엑셀로 표현하기 어려운 데이터
  - ex) 텍스트 데이터, 사진, 디지털 음악 등
  - 신경망 알고리즘은 비정형 데이터에 잘 맞음
- 앙상블 학습(ensemble learning): 정형 데이터를 다루는 데 가장 뛰어난 성과를 내는 알고리즘
  - 이 알고리즘은 대부분 결정 트리를 기반으로 만들어져 있음

## 2️⃣ 랜덤 포레스트

- 가장 대표적인 앙상블 학습 알고리즘으로, 안정적인 성능 덕분에 널리 사용되고 있음
- 결정 트리를 랜덤하게 만들어 결정 트리(나무)의 숲을 만듦
  - 기본적으로 100개의 결정 트리를 아래 방식으로 훈련함
- 그 다음, 각 결정 트리의 예측을 사용해 최종 예측을 만듦
  - 분류인 경우, 각 트리의 클래스별 확률을 평균하여 가장 높은 확률을 가진 클래스를 예측으로 삼음
  - 회귀인 경우, 각 트리의 예측을 평균함
- 랜덤 포레스트는 랜덤하게 선택한 샘플과 특성을 사용하기 때문에, 훈련 세트에 과대적합되는 것을 막아주고 검증 세트와 테스트 세트에서 안정적인 성능을 얻을 수 있음

### 결정 트리 훈련 방식

#### 부트스트랩 샘플

- 먼저 랜덤 포레스트는 각 트리를 훈련하기 위한 데이터를 랜덤하게 만듦
  - 입력한 훈련 데이터에서 샘플을 추출하여 훈련 데이터를 만드는 데, 이때 한 샘플이 중복되어 추출될 수도 있음
- 부트스트랩 샘플: 데이터 세트에서 중복을 허용해서 샘플링하여 만든 데이터
  - 기본적으로, 부트스트랩 샘플은 훈련 세트의 크기와 같게 만듦

#### 랜덤하게 특성 선택

- 각 노드를 분할할 때 전체 특성 중에서 일부 특성을 무작위로 고른 다음 이 중에서 최선의 분할을 찾음
- 분류 모델인 RandomForestClassifier는 기본적으로 전체 특성 개수의 제곱근만큼의 특성을 랜덤하게 선택함
- 회귀 모델인 RandomForestRegressor는 기본적으로 전체 특성을 사용함

### 화이트 와인 분류

#### 1. 와인 데이터셋을 데이터프레임으로 읽어온 후 훈련 세트와 테스트 세트로 나누자

```py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wine = pd.read_csv('https://bit.ly/wine_csv_data')

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)
```

#### 2. 랜덤 포레스트 모델을 교차 검증 해보자

```py
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']))  # 0.997
print(np.mean(scores['test_score']))  # 0.891
```

- 결과를 보면 훈련 세트에 다소 과대적합된 것을 알 수 있음
- 랜덤 포레스트틑 결정 트리의 앙상블이기 때문에 DecisionTreeClassifier가 제공하는 중요한 매개변수를 모두 제공함
  - criterion, max_depth, max_features, min_samples_split, min_impurity_decrease, min_samples_leaf 등
- 또한, 랜덤 포레스트도 결정 트리처럼 특성 중요도를 계산함
  - 각 결정 트리의 특성 중요도를 취합

#### 3. 랜덤 포레스트 모델을 훈련 세트에 훈련한 후 특성 중요도를 확인해보자

```py
rf.fit(train_input, train_target)

print(rf.feature_importances_)
# [0.23167441 0.50039841 0.26792718] 👈 [알코올 도수, 당도, pH]
```

- (5장 1절) 결정 트리 모델에서의 특성 중요도: [0.12345626 0.86862934 0.0079144]
- 비교 결과, 당도의 중요도가 감소하고 알코올 도수와 pH 특성의 중요도가 조금 상승했음
- 랜덤 포레스트는 특성의 일부를 랜덤하게 선택해서 결정 트리를 훈련하기 때문에, 하나의 특성에 과도하게 집중하지 않고 좀 더 많은 특성이 훈련에 기여할 기회를 얻음
- 이로 인해, 과대적합을 줄이고 일반화 성능을 높이는 데 도움이 됨

#### 4. OOB 샘플을 사용해 랜덤 포레스트 모델을 평가해보자

```py
rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
rf.fit(train_input, train_target)

print(rf.oob_score_)  # 0.893
```

- OOB(out of bag) 샘플: 부트스트랩 샘플에 포함되지 않고 남은 샘플
  - 이 샘플을 검증 세트처럼 사용해 모델을 평가할 수 있음
  - OOB 점수를 사용하면 교차 검증을 대신할 수 있어서 결과적으로 훈련 세트에 더 많은 샘플을 사용할 수 있음
- `oob_score`: True로 지정하면, 각 결정 트리의 OOB 점수를 평균하여 출력해줌
- 결과를 보면, 교차 검증에서 얻은 점수와 매우 비슷한 결과를 얻은 것을 알 수 있음

## 3️⃣ 엑스트라 트리

- 랜덤 포레스트와의 공통점

  - 기본적으로 100개의 결정 트리를 훈련함
  - 결정 트리가 제공하는 대부분의 매개변수를 지원함
  - 전체 특성 중에 일부 특성을 랜덤하게 선택하여 노드를 분할하는 데 사용함

- 랜덤 포레스트와의 차이점
  - 부트스트랩 샘플을 사용하지 않고, 각 결정 트리를 만들 때 전체 훈련 세트를 사용함
  - 노드를 분할할 때 가장 좋은 분할을 찾는 것이 아니라, 무작위로 분할함 (즉, splitter='random'인 결정 트리를 사용)
- 무작위로 노드 분할을 하더라도 많은 트리를 앙상블하기 때문에 과대적합을 막고 검증 세트의 점수를 높이는 효과가 있음

#### 1. 엑스트라 트리 모델을 교차 검증 해보자

```py
from sklearn.ensemble import ExtraTreesClassifier

et = ExtraTreesClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(et, train_input, train_target, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']))  # 0.997
print(np.mean(scores['test_score']))  # 0.889
```

- 랜덤 포레스트와 비슷한 결과를 얻음
- 보통 엑스트라 트리가 무작위성이 더 크기 떄문에 랜덤 포레스트보다 더 많은 결정 트리를 훈련해야 함
- 하지만, 랜덤하게 노드를 분할하기 때문에 랜덤 포레스트보다 계속 속도가 빠름

#### 2. 엑스트라 트리 모델을 훈련 세트에 훈련한 후 특성 중요도를 확인해보자

```py
et.fit(train_input, train_target)

print(et.feature_importances_)
# [0.20183568 0.52242907 0.27573525]
```

- 엑스트라 트리도 랜덤 포레스트처럼 결정 트리보다 당도에 대한 의존성이 낮은 걸 알 수 있음

## 4️⃣ 그레이디언트 부스팅

- 깊이가 얕은 결정 트리를 사용하여 이전 트리의 오차를 보완하는 방식으로 앙상블하는 방법
  - 사이킷런의 GradientBoostingClassifier는 기본적으로 깊이가 3인 결정 트리를 100개 사용함
- 경사 하강법을 사용하여 트리를 앙상블에 추가함
  - 분류인 경우 로지스틱 손실 함수를 사용
  - 회귀인 경우 평균 제곱 오차 함수를 사용
- 깊이가 얕은 결정 트리를 사용하기 때문에 과대적합에 강하고 일반적으로 높은 일반화 성능을 기대할 수 있음
- 일반적으로 그레이디언트 부스팅이 랜덤 포레스트보다 조금 더 높은 성능을 얻을 수 있음
- 하지만, 순서대로 트리를 추가하기 때문에 훈련 속도가 느림
  - GradientBoostingClassifier에는 n_jobs 매개변수가 없음

#### 1. 그레이디언트 부스팅 모델을 교차 검증 해보자

```py
from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']))  # 0.888
print(np.mean(scores['test_score']))  # 0.872
```

- 결과를 보면 과대적합 되지 않은 것을 알 수 있음
- 그레이디언트 부스팅은 결정 트리의 개수를 늘려도 과대적합에 매우 강함

#### 2. 학습률을 증가시키고 트리의 개수를 늘려 다시 교차 검증 해보자

```py
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2, random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']))  # 0.946
print(np.mean(scores['test_score']))  # 0.878
```

- 결정 트리 개수를 5배나 늘렸지만 과대적합을 잘 억제하고 있음

#### 3. 그레이디언트 부스팅 모델을 훈련 세트에 훈련한 후 특성 중요도를 확인해보자

```py
gb.fit(train_input, train_target)

print(gb.feature_importances_)
# [0.15887763 0.6799705  0.16115187]
```

- 그레이디언트 부스팅이 랜덤 포레스트보다 당도에 더 집중한 것을 알 수 있음

## 5️⃣ 히스토그램 기반 그레이디언트 부스팅

- 정형 데이터를 다루는 머신러닝 알고리즘 중에 가장 인기가 높은 알고리즘임
- 입력 특성을 256개의 구간으로 나누기 때문에, 노드를 분할할 때 최적의 분할을 매우 빠르게 찾을 수 있음 (그레이디언트 부스팅의 속도를 개선함)
  - 256개의 구간 중에서 하나를 떼어 놓고 누락된 값을 위해서 사용함
  - 따라서, 입력에 누락된 특성이 있더라도 이를 따로 전처리할 필요가 없음

#### 1. 히스토그램 기반 그레이디언트 부스팅 모델을 교차 검증해보자

```py
from sklearn.ensemble import HistGradientBoostingClassifier

hgb = HistGradientBoostingClassifier(random_state=42)
scores = cross_validate(hgb, train_input, train_target, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']))  # 0.932
print(np.mean(scores['test_score']))  # 0.880
```

- 과대적합을 잘 억제하면서 그레이디언트 부스팅보다 조금 더 높은 성능을 제공함

#### 2. 히스토그램 기반 그레이디언트 부스팅 모델을 훈련 세트에 훈련한 후 특성 중요도를 확인해보자

```py
from sklearn.inspection import permutation_importance

hgb.fit(train_input, train_target)
result = permutation_importance(hgb, train_input, train_target, n_repeats=10, random_state=42, n_jobs=-1)

print(result.importances_mean)
# [0.08876275 0.23438522 0.08027708]
```

- 히스토그램 기반 그레이디언트 부스팅은 자체적으로 특성 중요도를 제공하지 않음
- `permutation_importance()`: 특성을 하나씩 랜덤하게 섞어서 모델의 성능이 변화하는지를 관찰하여 어떤 특성이 중요한지를 계산함
  - 훈련 세트 뿐만 아니라 테스트 세트에도 적용할 수 있음
  - 사이킷런에서 제공하는 추정기 모델에 모두 사용 가능
  - n_repeats: 랜덤하게 섞을 횟수
  - 반환값: 특성 중요도(importances), 평균(importances_mean), 표준 편차(importances_std)
- 평균을 보면 랜덤 포레스트와 비슷한 비율임을 알 수 있음

#### 3. 테스트 세트에서 특성 중요도를 확인해보자

```py
result = permutation_importance(hgb, test_input, test_target, n_repeats=10, random_state=42, n_jobs=-1)

print(result.importances_mean)
# [0.05969231 0.20238462 0.049]
```

- 테스트 세트의 결과를 보면 조금 더 당도에 집중하고 있다는 것을 알 수 있음
- 이를 통해 모델을 실전에 투입했을 때 어떤 특성에 관심을 둘지 예상할 수 있음

#### 4. 테스트 세트를 사용해 히스토그램 기반 그레이디언트 부스팅 모델을 평가해보자

```py
hgb.score(test_input, test_target)  # 0.872
```

- 테스트 세트에서 약 87% 정확도를 얻음
- 앙상블 모델이 확실히 결정 트리(86% 정확도)보다 좋은 결과를 얻을 수 있음을 확인함

## cf) 핵심 패키지와 함수

### scikit-learn

#### `RadomForestClassifier` 클래스

- 랜덤 포레스트 분류 클래스
- n_estimators 매개변수
  - 앙상블을 구성할 트리의 개수 지정
  - 기본값: 100
- criterion 매개변수
  - 불순도를 지정
  - 'gini': 지니 불순도
  - 'entropy': 엔트로피 불순도
  - 기본값: 'gini'
- max_depth 매개변수
  - 트리가 성장할 최대 깊이를 지정
  - 기본값: None (리프 노드가 순수하거나, min_samples_split보다 샘플 개수가 적을 때까지 성장함)
- min_samples_split 매개변수
  - 노드를 나누기 위한 최소 샘플 개수
  - 기본값: 2
- max_features 매개변수
  - 최적의 분할을 위해 탐색할 특성의 개수를 지정
  - 기본값: sqrt (특성 개수의 제곱근)
- bootstrap 매개변수
  - 부트스트랩 샘플을 사용할지 지정
  - 기본값: True
- oob_score 매개변수
  - OOB 샘플을 사용하여 훈련한 모델을 평가할지 지정
  - 기본값: False
- n_jobs 매개변수
  - 병렬 실행에 사용할 CPU 코어 수를 지정
  - 기본값: 1 (하나의 코어를 사용)
  - -1로 지정하면 시스템에 있는 모든 코어를 사용함

#### `ExtraTreeClassifier` 클래스

- 엑스트라 트리 분류 클래스
- n_estimators, criterion, max_depth, min_samples_split, max_features, oob_score, n_jobs 매개변수는 랜덤 포레스트와 동일함
- bootstrap 매개변수
  - 부트스트랩 샘플을 사용할지 지정
  - 기본값: False

#### `GradientBoostingClassifier` 클래스

- 그레이디언트 부스팅 분류 클래스
- loss 매개변수
  - 손실 함수를 지정
  - 기본값: 'log_loss' (로지스틱 손실 함수)
- learning_rate 매개변수
  - 트리가 앙상블에 기여하는 정도를 조절
  - 모델의 복잡도 제어 가능
  - 값이 크면 복잡하고 훈련 세트에 과대적합된 모델을 얻을 수 있음
  - 기본값: 0.1
- n_estimators 매개변수
  - 부스팅 단계를 수행하는 트리의 개수
  - 기본값: 100
- subsample 매개변수
  - 사용할 훈련 세트의 샘플 비율을 지정
  - 기본값: 1.0 (훈련 세트 전체를 사용)
- max_depth 매개변수
  - 개별 회귀 트리의 최대 깊이
  - 기본값: 3

#### `HistGradientBoostingClassifier` 클래스

- 히스토그램 기반 그레이디언트 부스팅 분류 클래스
- learning_rate 매개변수
  - 학습률 또는 감쇠율
  - 기본값: 0.1
  - 1.0이면 감쇠가 전혀 없음
- max_iter 매개변수
  - 부스팅 단계를 수행하는 트리의 개수
  - 기본값: 100
- max_bins 매개변수
  - 입력 데이터를 나눌 구간의 개수
  - 기본값: 255 (이보다 크게 지정할 수 없음)
    - 여기에 1개의 구간이 누락된 값을 위해 추가됨
