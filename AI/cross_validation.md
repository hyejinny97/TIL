# ✔ 교차 검증과 그리드 서치

> ['교차 검증과 그리드 서치' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/5-2.ipynb)

## 1️⃣ 검증 세트

- 테스트 세트로 일반화 성능을 올바르게 예측하려면 가능한 한 테스트 세트를 사용하지 말아야 함
  - 테스트 세트를 사용해 자꾸 성능을 확인하다 보면 테스트 세트에 맞추게 됨
  - 모델을 만들고 나서 마지막에 딱 한번만 사용하는 것이 좋음
- 검증 세트: 하이퍼파라미터 튜닝을 위해 모델을 평가할 때, 테스트 세트를 사용하지 않기 위해 훈련 세트에서 다시 떼어 낸 데이터 세트
  - 보통 20~30%를 떼어냄
  - 훈련 데이터가 아주 많다면 적게 떼어내도 문제 없음
- 모델 훈련 및 테스트 과정
  1. 훈련 세트로 모델을 훈련하고 검증 세트로 모델을 평가함
  2. 테스트하고 싶은 매개변수를 바꿔가며 1번 과정을 반복해 가장 좋은 모델을 고름
  3. 최적의 매개변수를 사용해 훈련 세트와 검증 세트를 합쳐 전체 훈련 데이터에서 모델을 다시 훈련함
  4. 마지막으로, 테스트 세트에서 최종 점수를 평가함

#### 1. 와인 데이터셋을 데이터프레임으로 읽어오자

```py
import pandas as pd

wine = pd.read_csv('https://bit.ly/wine_csv_data')
```

#### 2. 입력 데이터와 타깃 데이터를 만들자

```py
data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']
```

#### 3. 훈련 세트와 테스트 세트로 나누자

```py
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

print(train_input.shape, test_input.shape)  # (5197, 3) (1300, 3)
```

#### 4. 훈련 세트를 다시 부분 훈련 세트와 검증 세트로 나누자

```py
sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)

print(sub_input.shape, val_input.shape)  # (4157, 3) (1040, 3)
```

#### 5. 결정 트리 모델을 훈련하고 평가 해보자

```py
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)

print(dt.score(sub_input, sub_target))  # 0.997
print(dt.score(val_input, val_target))  # 0.864
```

- 결과를 보면, 훈련 세트에 과대적합되어 있는 것을 알 수 있음

## 2️⃣ 교차 검증

- 훈련 세트를 여러 폴드로 나눈 다음 한 폴드가 검증 세트의 역할을 하고 나머지 폴드에서는 모델을 훈련하는 과정을 여러 번 반복하는 것
  - 보통 5-폴드 교차 검증이나 10-폴드 교차 검증을 많이 사용함
  - 각 폴드에서 계산한 검증 점수를 평균해 최종 검증 점수를 구함
- 교차 검증(cross validation)을 이용하면 안정적인 검증 점수를 얻고 훈련에 더 많은 데이터를 사용할 수 있음
  - 데이터의 80~90%까지 훈련에 사용할 수 있음

#### 1. 결정 트리 모델을 교차 검증 해보자

```py
from sklearn.model_selection import cross_validate

scores = cross_validate(dt, train_input, train_target)
print(scores)
"""
{'fit_time': array([0.01341891, 0.02167416, 0.02525187, 0.04882073, 0.03598666]), 'score_time': array([0.0027864 , 0.0019815 , 0.00886154, 0.01437068, 0.02624893]), 'test_score': array([0.86923077, 0.84615385, 0.87680462, 0.84889317, 0.83541867])}
"""
```

- `cross_validate()`: 교차 검증 함수
  - 첫 번째 매개변수로 평가할 모델 객체를 전달
  - 그 다음 매개변수에 검증 세트를 떼어 내지 않고 훈련 세트 전체를 전달
  - 기본적으로 5-폴드 교차 검증을 수행함
- fit_time: 모델을 훈련하는 시간
- score_time: 검증하는 시간
- test_score: 검증 폴드의 점수

#### 2. 교차 검증의 최종 점수를 구해보자

```py
import numpy as np

print(np.mean(scores['test_score']))  # 0.856
```

#### 3. 이번엔 결정 트리 모델을 10-폴드 교차 검증 해보자

```py
from sklearn.model_selection import StratifiedKFold

scores = cross_validate(dt, train_input, train_target, cv=StratifiedKFold())

print(np.mean(scores['test_score']))  # 0.856
```

- 교차 검증에서 폴드 수를 변경하거나 교차 검증을 할 때 훈련 세트를 섞으려면 cv 매개변수에서 분할기(splitter)를 지정해야 함

  - cross_validate() 함수는 기본적으로 훈련 세트를 섞어 폴드를 나누지는 않음
  - cross_validate() 함수는 기본적으로 회귀 모델일 경우 cv 매개변수에 KFold 분할기를 사용하고 분류 모델일 경우 타깃 클래스를 골고루 나누기 위해 StratifiedKFold 분할기를 사용함

- 위 코드는 사실상 1번 코드와 동일한 코드임

```py
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)

print(np.mean(scores['test_score']))  # 0.857
```

- n_splits: 몇 폴드 교차 검증을 할지 지정
- shuffle: 폴드를 나누기 전 훈련 세트를 섞음

## 3️⃣ 하이퍼파라미터 튜닝

- 모델 파라미터: 머신러닝 모델이 학습하는 파라미터
- 하이퍼파라미터: 모델이 학습할 수 없어서 사용자가 지정해야만 하는 파라미터
  - 사이킷런과 같은 머신러닝 라이브러리를 사용할 때 이런 하이퍼파라미터는 모두 클래스나 메서드의 매개변수로 표현됨
- 주의) 최적의 값을 찾아야할 매개변수가 여러 개라면, 매개변수를 **동시에** 바꿔가며 최적의 값을 찾아야 함
- 그리드 서치(Grid Search): 하이퍼파라미터 탐색을 자동화해 주는 도구
  - 탐색할 매개변수를 나열하면 교차 검증을 수행하여 가장 좋은 검증 점수의 매개변수 조합을 선택함
  - 마지막으로 이 매개변수 조합으로 최종 모델을 훈련함

#### 1. 그리드 서치를 통해 결정 트리 모델의 하이퍼파라미터를 튜닝 해보자

```py
from sklearn.model_selection import GridSearchCV

params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}

gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)
```

- `GridSearchCV` 클래스: 하이퍼파라미터 탐색과 교차 검증을 한 번에 수행함
- GridSearchCV의 cv 매개변수 기본값은 5임
  - min_impurity_decrease 매개변수의 값마다 5-폴드 교차 검증을 수행하므로 총 25(= 5 \* 5)개의 모델을 훈련함
- 많은 모델을 훈련하기 때문에 GridSearchCV의 n_jobs 매개변수에서 병렬 실행에 사용할 CPU 코어 수를 지정하는 것이 좋음
  - 기본값: 1
  - -1로 지정하면 시스템에 있는 모든 코어를 사용함

#### 2. 최적의 매개변수 조합과 최고의 교차 검증 점수를 확인해보자

```py
print(gs.best_params_)  # {'min_impurity_decrease': 0.0001}
```

- `best_params_` 속성: 그리드 서치로 찾은 최적의 매개변수

```py
print(gs.cv_results_['mean_test_score'])
# [0.86819297 0.86453617 0.86492226 0.86780891 0.86761605]
print(gs.cv_results_['params'][gs.best_index_])
# {'min_impurity_decrease': 0.0001}
```

- `cv_results_` 속성: 교차 검증의 결과를 저장
  - mean_test_score: 각 매개변수에서 수행한 교차 검증의 평균 점수를 저장
  - params: 매개변수
- `best_index_` 속성: 교차 검증의 평균 점수가 가장 높은 값의 인덱스를 반환

#### 3. 최적의 매개변수를 가지고 훈련된 모델을 평가해보자

```py
dt = gs.best_estimator_
print(dt.score(train_input, train_target))  # 0.962
```

- 그리드 서치는 훈련이 끝나면 교차 검증 점수가 가장 높은 모델의 매개변수 조합으로 전체 훈련 세트에서 자동으로 다시 모델을 훈련함
- `best_estimator_` 속성: 최적의 매개변수 조합으로 전체 훈련 세트에서 훈련한 모델

#### 4. 매개변수를 더 추가한 후 다시 그리드 서치 해보자

```py
params = {'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001),
          'max_depth': range(5, 20, 1),
          'min_samples_split': range(2, 100, 10)
          }

gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)
```

#### 5. 최적의 매개변수 조합과 최고의 교차 검증 점수를 확인해보자

```py
print(gs.best_params_)
# {'max_depth': 14, 'min_impurity_decrease': 0.0004, 'min_samples_split': 12}
print(np.max(gs.cv_results_['mean_test_score']))  # 0.868
```

### 랜덤 서치

- 그리드 서치의 단점
  - 매개변수의 값이 수치일 때 값의 범위나 간격을 미리 정하기 어려울 수 있음
  - 너무 많은 매개변수 조건이 있어 그리드 서치 수행 시간이 오래 걸릴 수 있음
- 랜덤 서치는 지정된 횟수만큼 샘플링하여 교차 검증을 수행하기 때문에 그리드 서치보다 교차 검증 수를 줄이면서, 넓은 영역을 효과적으로 탐색할 수 있음
- 랜덤 서치는 매개변수에 탐색할 값을 직접 나열하는 것이 아니라 매개변수를 샘플링할 수 있는 확률 분포 객체를 전달함

#### scipy(싸이파이)

- 적분, 보간, 선형 대수, 확률 등을 포함한 수치 계산 전용 라이브러리
- 파이썬의 핵심 과학 라이브러리 중 하나
- 사이킷런은 넘파이와 싸이파이 기능을 많이 사용함
- `randit()` 클래스

  - 주어진 범위에서 고르게 정숫값을 뽑음
  - = 균등 분포에서 샘플링함

  ```py
  from scipy.stats import randint

  rgen = randint(0, 10)
  rgen.rvs(10)
  # array([6, 4, 3, 6, 3, 1, 1, 6, 1, 6])

  np.unique(rgen.rvs(1000), return_counts=True)
  # (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([121,  99,  81,  98, 106,  85,  93,  94, 109, 114]))
  ```

- `uniform()` 클래스

  - 주어진 범위에서 고르게 실숫값을 뽑음
  - = 균등 분포에서 샘플링함

  ```py
  from scipy.stats import uniform

  ugen = uniform(0, 1)
  ugen.rvs(10)
  # array([0.60857829, 0.2795936 , 0.4059522 , 0.47695652, 0.7427586, 0.9801252 , 0.05012329, 0.79357074, 0.16195204, 0.33820475])
  ```

#### 1. 랜덤 서치를 통해 결정 트리 모델의 하이퍼파라미터를 튜닝 해보자

```py
from scipy.stats import uniform, randint
from sklearn.model_selection import RandomizedSearchCV

params = {'min_impurity_decrease': uniform(0.0001, 0.001),
          'max_depth': randint(20, 50),
          'min_samples_split': randint(2, 25),
          'min_samples_leaf': randint(1, 25),
          }

gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params, n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)
```

- `n_iter`: 샘플링 횟수
- 즉, 위 params에 정의된 매개변수 범위에서 총 100번을 샘플링하여 교차 검증을 수행하고 최적의 매개변수 조합을 찾음

#### 2. 최적의 매개변수 조합과 최고의 교차 검증 점수를 확인해보자

```py
print(gs.best_params_)
# {'max_depth': 39, 'min_impurity_decrease': 0.00034102546602601173, 'min_samples_leaf': 7, 'min_samples_split': 13}
print(np.max(gs.cv_results_['mean_test_score']))  # 0.869
```

#### 3. 최적의 매개변수를 가지고 훈련된 모델을 평가해보자

```py
dt = gs.best_estimator_

print(dt.score(test_input, test_target))  # 0.86
```

- 일반적으로 테스트 세트 점수는 검증 세트 점수보다 조금 작음

## cf) 핵심 패키지와 함수

### scikit-learn

#### `cross_validate()` 함수

- 교차 검증을 수행하는 함수
- 매개변수에 순서대로 교차 검증을 수행할 모델 객체, 특성, 타깃 데이터를 전달함
- scoring 매개변수
  - 검증에 사용할 평가 지표 지정
  - 기본값: (분류 모델인 경우) 'accuracy', (회귀 모델인 경우) 'r2'
- cv 매개변수
  - 교차 검증 폴드 수나 분할기 객체를 지정
  - (회귀인 경우) KFold 클래스, (분류인 경우) StratifiedKFold 클래스
  - 기본값: 5 (5-폴드 교차 검증)
- n_jobs 매개변수
  - 교차 검증을 수행할 때 사용할 CPU 코어 수를 지정
  - 기본값: 1
  - -1로 지정하면 시스템에 있는 모든 코어를 사용함
- return_train_score 매개변수
  - True로 지정하면 훈련 세트의 점수도 반환함
  - 기본값: False

#### `GridSearchCV` 클래스

- 교차 검증으로 하이퍼파라미터 탐색을 수행함
- 최상의 모델을 찾은 후 훈련 세트 전체를 사용해 최종 모델을 훈련함
- 매개변수에 순서대로 그리드 서치를 수행할 모델 객체, 탐색할 모델의 매개변수와 값을 전달함
- scoring, cv, n_jobs, return_train_score 매개변수는 위와 동일함

#### `RandomizedSearchCV` 클래스

- 교차 검증으로 랜덤한 하이퍼파라미터 탐색을 수행함
- 최상의 모델을 찾은 후 훈련 세트 전체를 사용해 최종 모델을 훈련함
- 매개변수에 순서대로 그리드 서치를 수행할 모델 객체, 탐색할 모델의 매개변수와 확률 분포 객체를 전달함
- scoring, cv, n_jobs, return_train_score 매개변수는 위와 동일함
