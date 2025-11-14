# ✔ 순환 신경망으로 IMDB 리뷰 분류하기

> ['순환 신경망으로 IMDB 리뷰 분류하기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/9-2.ipynb)

## 1️⃣ IMDB 리뷰 데이터셋

- 유명한 인터넷 영화 데이터베이스인 imdb.com에서 수집한 리뷰를 감상평에 따라 긍정과 부정으로 분류해 놓은 데이터셋임
- 총 50,000개의 샘플이 있고, 훈련 데이터와 테스터 데이터에 각각 25,000개씩 나누어짐

### 자연어 처리

- Natural Language Processing, NLP
- 컴퓨터를 사용해 인간의 언어를 처리하는 분야
- 음성 인식, 기계 번역, 감성 분석 등의 분야가 있음
- IMDB 리뷰를 감상평에 따라 분류하는 작업은 감성 분석에 해당함
- 자연어 처리 분야에서는 훈련 데이터를 종종 말뭉치(corpus)라고 부름

### 토큰 (Token)

- 텍스트 데이터를 신경망에 전달하기 전 숫자 데이터로 변환해야 하는데, 일반적인 방법은 데이터에 등장하는 단어마다 고유한 정수를 부여하는 것임
- 동일한 단어는 동일한 정수에 매핑하고, 단어에 매핑되는 정수는 단어의 의미나 크기와 관련이 없음
- 일반적으로 영어 문장은 모두 소문자로 바꾸고 구둣점을 삭제한 다음 공백을 기준으로 분리하는데, 이렇게 분리된 단어를 토큰이라고 부름
- 한글은 조사가 발달되어 있기 때문에 공백으로 나누는 것만으로 부족하고, 일반적으로 형태소 분석을 통해 토큰을 만듦
- 하나의 샘플은 여러 개의 토큰으로 이루어져 있고, 1개의 토큰이 하나의 타임스텝에 해당함
- 토큰에 할당하는 정수 중에 몇 개는 특정한 용도로 예약되어 있는 경우가 많음
  - 0: 패딩
  - 1: 문자의 시작
  - 2: 어휘 사전에 없는 토큰
- 어휘 사전: 훈련 세트에서 고유한 단어를 뽑아 만든 목록
  - 만약 테스트 세트 안에 어휘 사전에 없는 단어가 있다면 2로 변환하여 신경망 모델에 주입하게 됨

#### 1. IMDB 리뷰 데이터셋을 가져와 적재해보자

```py
from tensorflow.keras.datasets import imdb

(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=200)

print(train_input.shape, test_input.shape)  # (25000,) (25000,)
```

- 실제, IMDB 리뷰 데이터셋은 영어로 된 문장이지만 편리하게도 케라스에는 이미 정수로 바꾼 데이터가 포함되어 있음
- `load_data()` 함수: 전체 어휘 사전에 있는 단어를 등장 횟수 순서대로 나열한 다음 가장 많이 등장한 단어 'num_words'개만큼 단어를 선택함
- `num_words`: 전체 데이터셋에서 가장 자주 등장하는 단어 개수를 지정
- num_words=200으로 지정했기 때문에 어휘 사전에는 200개의 단어만 들어가 있음
  - 어휘 사전에 없는 단어는 모두 2로 표시되어 나타남

```py
print(len(train_input[0]))  # 218
print(len(train_input[1]))  # 189
```

- 데이터는 개별 리뷰를 담은 파이썬 리스트 객체로 이루어진 넘파이 배열임
- IMDB 리뷰 데이터 텍스트의 길이가 제각각이기 때문에, 고정 크기의 2차원 배열에 담기 보다는 리뷰마다 별도의 파이썬 리스트로 담아야 메모리를 효과적으로 관리할 수 있음
- 여기서 하나의 리뷰가 하나의 샘플이 됨

```py
print(train_input[0])
"""
[1, 14, 22, 16, 43, 2, 2, 2, 2, 65, 2, 2, 66, 2, 4, 173, 36, 2, 5, 25, 100, 43, 2, 112, 50, 2, 2, 9, 35, 2, 2, 5, 150, 4, 172, 112, 167, 2, 2, 2, 39, 4, 172, 2, 2, 17, 2, 38, 13, 2, 4, 192, 50, 16, 6, 147, 2, 19, 14, 22, 4, 2, 2, 2, 4, 22, 71, 87, 12, 16, 43, 2, 38, 76, 15, 13, 2, 4, 22, 17, 2, 17, 12, 16, 2, 18, 2, 5, 62, 2, 12, 8, 2, 8, 106, 5, 4, 2, 2, 16, 2, 66, 2, 33, 4, 130, 12, 16, 38, 2, 5, 25, 124, 51, 36, 135, 48, 25, 2, 33, 6, 22, 12, 2, 28, 77, 52, 5, 14, 2, 16, 82, 2, 8, 4, 107, 117, 2, 15, 2, 4, 2, 7, 2, 5, 2, 36, 71, 43, 2, 2, 26, 2, 2, 46, 7, 4, 2, 2, 13, 104, 88, 4, 2, 15, 2, 98, 32, 2, 56, 26, 141, 6, 194, 2, 18, 4, 2, 22, 21, 134, 2, 26, 2, 5, 144, 30, 2, 18, 51, 36, 28, 2, 92, 25, 104, 4, 2, 65, 16, 38, 2, 88, 12, 16, 2, 5, 16, 2, 113, 103, 32, 15, 16, 2, 19, 178, 32]
"""
```

- IMDB 리뷰 데이터가 이미 정수로 변환되어 있는 것을 알 수 있음

```py
print(train_target[:20])
# [1 0 0 1 0 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1]
```

- 타깃값은 0(부정)과 1(긍정)로 나누어짐

#### 2. 훈련 세트에서 검증 세트를 떼어내자

```py
from sklearn.model_selection import train_test_split

train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)
```

#### 3. 훈련 세트 내 각 샘플의 리뷰 길이를 분석해보자

```py
import numpy as np

lengths = np.array([len(x) for x in train_input])
print(np.mean(lengths), np.median(lengths))  # 239.00925 178.0
```

- 리뷰의 평균 단어 개수는 239개이고 중간값이 178인 것으로 보아 리뷰 길이 데이터는 한쪽에 치우친 분포를 보일 것 같음

```py
import matplotlib.pyplot as plt

plt.hist(lengths)
plt.xlabel('length')
plt.ylabel('frequency')
plt.show()
```

<img src='./9-2_review_length_histogram.png' alt='리뷰 길이 히스토그램' width='350px' />

- 평균이 중간값보다 높은 이유는 오른쪽 끝에 아주 큰 데이터가 있기 때문이었음
- 대부분의 리뷰 길이는 300 미만임
- 리뷰는 대부분 짧아서 아래에서는 중간값보다 훨씬 짧은 100개의 단어만 사용할 예정임
- 100개의 단어보다 작은 리뷰는 길이를 100에 맞추기 위해 패딩이 필요함
  - 보통 패딩을 나타내는 토큰으로는 0을 사용함

#### 4. 훈련 세트 입력값의 길이를 100으로 맞추자

```py
from tensorflow.keras.preprocessing.sequence import pad_sequences

train_seq = pad_sequences(train_input, maxlen=100)
print(train_seq.shape)  # (20000, 100)
```

- `pad_sequence()` 함수: 시퀀스 데이터의 길이를 맞춰줌
- `maxlen` 매개변수: 원하는 길이 지정
  - 이보다 긴 경우는 잘라내고 짧은 경우는 0으로 패딩함
- `truncating` 매개변수: 시퀀스 데이터가 잘리는 위치 지정
  - 기본값: 'pre' (앞부분을 자름)
  - 'post'로 지정하면 시퀀스의 뒷부분을 자름
- `padding` 매개변수: 시퀀스 데이터에 패딩을 추가하는 위치 지정
  - 기본값: 'pre' (앞부분에 패딩을 추가함)
  - 'post'로 지정하면 시퀀스의 뒷부분에 패딩을 추가함
  - 하지만, 시퀀스의 마지막에 있는 단어가 셀의 은닉 상태에 가장 큰 영향을 미치게 되므로 마지막에 추가하는 것은 일반적으로 선호하지 않음

```py
print(train_seq[0])
"""
[ 10   4  20   9   2   2   2   5  45   6   2   2  33   2   8   2 142   2
   5   2  17  73  17   2   5   2  19  55   2   2  92  66 104  14  20  93
  76   2 151  33   4  58  12 188   2 151  12   2  69   2 142  73   2   6
   2   7   2   2 188   2 103  14  31  10  10   2   7   2   5   2  80  91
   2  30   2  34  14  20 151  50  26 131  49   2  84  46  50  37  80  79
   6   2  46   7  14  20  10  10   2 158]
"""

print(train_input[0][-10:])
# [6, 2, 46, 7, 14, 20, 10, 10, 2, 158]
```

- 첫 번째 샘플의 앞뒤에 패딩값 0이 없는 것으로 보아 100보다는 길었을 것 같음
- 원본 샘플의 끝이 출력값과 일치하는 것을 보아 샘플의 앞부분이 잘렸음을 알 수 있음

```py
print(train_seq[5])
"""
[  0   0   0   0   1   2 195  19  49   2   2 190   4   2   2   2 183  10
  10  13  82  79   4   2  36  71   2   8   2  25  19  49   7   4   2   2
   2   2   2  10  10  48  25  40   2  11   2   2  40   2   2   5   4   2
   2  95  14   2  56 129   2  10  10  21   2  94   2   2   2   2  11 190
  24   2   2   7  94   2   2  10  10  87   2  34  49   2   7   2   2   2
   2   2   2   2  46  48  64  18   4   2]
"""
```

- 여섯 번째 샘플의 앞부분에 0이 있는 것으로 보아 100보다 짧았을 것 같음
- 패딩은 뒷부분이 아니라 앞부분에 추가됐음

#### 5. 검증 세트 입력값의 길이도 100으로 맞추자

```py
val_seq = pad_sequences(val_input, maxlen=100)
```

## 2️⃣ 순환 신경망 만들기

### 원-핫 인코딩

- 정수값을 배열에서 해당 정수 위치의 원소만 1이고 나머지는 모두 0으로 변환하는 것
- 토큰을 정수로 변환한 데이터를 신경망에 주입하면 큰 정수가 큰 활성화 출력을 만드는 문제가 있음
- 원-핫 인코딩을 사용하면 토큰 정숫값에 있는 크기 속성을 없애고 각 정수를 고유하게 표현할 수 있음
- 정수로 변환된 토큰을 원-핫 인코딩으로 변환하려면 어휘 사전 크기의 벡터가 만들어짐

#### 1. 순환 신경망 모델을 만들자

```py
from tensorflow import keras

model = keras.Sequential()
model.add(keras.layers.Input(shape=(100, 200)))
model.add(keras.layers.SimpleRNN(8))
model.add(keras.layers.Dense(1, activation='sigmoid'))
```

- `SimpleRNN` 클래스: 가장 간단한 순환층 제공
  - `activation` 매개변수의 기본값은 'tanh'로 하이퍼볼릭 탄젠트 함수를 사용함
- Input 함수의 첫 번째 입력 차원(100): 샘플의 길이
- Input 함수의 두 번째 입력 차원(200): 원-핫 인코딩된 배열 길이

#### 2. 훈련 세트의 입력 데이터를 원-핫 인코딩하자

```py
train_oh = keras.utils.to_categorical(train_seq)

print(train_oh.shape)
# (20000, 100, 200)
print(train_oh[0][0][:12])
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
print(np.sum(train_oh[0][0]))
# 1.0
```

- imdb.load_data() 함수에서 200개의 단어만 사용하도록 지정했기 때문에, 훈련 데이터에 포함될 수 있는 정숫값의 범위는 0(패딩 토큰)에서 199까지임
- 이 범위를 원-핫 인코딩으로 표현하면 배열의 길이가 200이 됨
- 즉, 200개 중 하나만 1이고 나머지는 모두 0으로 만듦
- `to_categorical()` 함수: 정수 배열을 입력하면 자동으로 원-핫 인코딩된 배열을 반환해 줌

#### 3. 검증 세트의 입력 데이터도 원-핫 인코딩하자

```py
val_oh = keras.utils.to_categorical(val_seq)
```

#### 4. 순환 신경망 모델의 구조를 확인하자

```py
model.summary()
```

<img src='./9-2_rnn_summary.png' alt='rnn 구조' width='650px' />

- 순환층에 사용된 모델 파라미터 개수(1,672) = 200 x 8 + 8 x 8 + 8

## 3️⃣ 순환 신경망 훈련하기

#### 1. 모델을 컴파일하고 훈련하자

```py
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-simplernn-model.keras', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

history = model.fit(train_oh, train_target, epochs=100, batch_size=64, validation_data=(val_oh, val_target), callbacks=[checkpoint_cb, early_stopping_cb])
```

<img src='./9-2_rnn_fit_result.png' alt='rnn 훈련 결과' width='800px' />

- 9번째 에포크에서 조기 종료되었고 검증 세트에 대한 정확도는 약 73% 정도임

#### 2. 훈련 손실과 검증 손실 그래프를 그려보자

```py
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
```

<img src='./9-2_rnn_loss_graph.png' alt='훈련 손실과 검증 손실 그래프' width='400px' />

## 4️⃣ 단어 임베딩을 사용하기

### 원-핫 인코딩의 단점

```py
print(train_seq.nbytes, train_oh.nbytes)
# 8000000 3200000000
```

- 입력 데이터가 엄청 커짐
- train_seq 배열의 크기는 8M 정도인데 train_oh의 크기는 3.2GB에 달함

### 단어 임베딩

- Word Embedding
- 정수로 변환된 토큰을 비교적 작고 고정된 크기의 실수 밀집 벡터로 변환함
- 밀집 벡터는 단어 사이의 관계를 표현할 수 있음
- 순환 신경망에서 텍스트를 처리할 때 즐겨 사용하는 방법임
- 단어 임베딩으로 만들어진 벡터는 원-핫 인코딩된 벡터보다 훨씬 의미 있는 값으로 채워져 있기 때문에 자연어 처리에서 더 좋은 성능을 내는 경우가 많음
- 입력으로 정수 데이터를 받고 원-핫 인코딩보다 훨씬 작은 크기로 벡터를 표현하기 때문에, 메모리를 절약하고 더 많은 단어를 사용할 수 있음

#### 1. 가장 많이 등장하는 단어 500개까지 선택해서 IMDB 리뷰 데이터셋을 다시 준비해보자

```py
(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)

train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)
```

#### 2. 임베딩 층을 추가한 순환 신경망 모델을 만들자

```py
model_emb = keras.Sequential()
model_emb.add(keras.layers.Input(shape=(100,)))
model_emb.add(keras.layers.Embedding(500, 16))
model_emb.add(keras.layers.SimpleRNN(8))
model_emb.add(keras.layers.Dense(1, activation='sigmoid'))
```

- `Embedding` 클래스: 임베딩 층을 제공
  - 처음에는 다른 층처럼 모든 벡터가 랜덤하게 초기화되지만 훈련을 통해 데이터에서 좋은 단어 임베딩을 학습함
  - 첫 번째 매개변수(500): 어휘 사전의 크기
  - 두 번쨰 매개변수(16): 임베딩 벡터의 크기

#### 3. 순환 신경망 모델의 구조를 확인해보자

```py
model_emb.summary()
```

<img src='./9-2_rnn_with_embedding_summary.png' alt='구조' width='600px' />

- 임베딩 층의 모델 파라미터 개수(8,000) = 500 x 16
- 순환층의 모델 파라미터 개수(200) = 16 x 8 + 8 x 8 + 8

#### 4. 모델을 컴파일하고 훈련하자

```py
model_emb.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-embedding-model.keras', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

history = model_emb.fit(train_seq, train_target, epochs=100, batch_size=64, validation_data=(val_seq, val_target), callbacks=[checkpoint_cb, early_stopping_cb])
```

<img src='./9-2_rnn_embedding_fit_result.png' alt='rnn 훈련 결과' width='800px' />

- 4번째 에포크에서 조기 종료되었고 검증 세트에 대한 정확도는 약 70% 정도임
- 원-핫 인코딩보다 순환층에 주입되는 입력의 크기가 크게 줄었지만 임베딩 벡터는 단어를 잘 표현하는 능력이 있음

#### 5. 훈련 손실과 검증 손실 그래프를 그려보자

```py
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
```

<img src='./9-2_rnn_embedding_loss_graph.png' alt='훈련 손실과 검증 손실 그래프' width='400px' />

## cf) 핵심 패키지와 함수

### Keras

#### `pad_sequence()` 함수

- 시퀀스 길이를 맞추기 위해 패딩을 추가함
- (샘플 개수, 타임스텝 개수) 크기의 2차원 배열을 기대함
- maxlen 매개변수
  - 원하는 시퀀스 길이를 지정
  - 이 값보다 긴 시퀀스는 잘리고 짧은 시퀀스는 패딩됨
  - 이 매개변수를 지정하지 않으면 가장 긴 시퀀스의 길이가 됨
- padding 매개변수
  - 패딩을 추가할 위치를 지정
  - 'pre': 시퀀스 앞에 패딩을 추가
  - 'post': 시퀀스 뒤에 패딩을 추가
  - 기본값: 'pre'
- truncating 매개변수
  - 긴 시퀀스에서 잘라버릴 위치를 지정
  - 'pre': 시퀀스 앞부분을 잘라냄
  - 'post': 시퀀스 뒷부분을 잘라냄
  - 기본값: 'pre'

#### `to_categorical()` 함수

- 정수 시퀀스를 원-핫 인코딩으로 변환함
- 토큰을 원-핫 인코딩하거나 타깃값을 원-핫 인코딩할 때 사용
- num_classes 매개변수
  - 클래스 개수를 지정
  - 지정하지 않으면 데이터에서 자동으로 찾음

#### `SimpleRNN` 클래스

- 케라스의 기본 순환층 클래스
- 첫 번째 매개변수에 뉴런의 개수를 지정
- activation 매개변수
  - 활성화 함수를 지정
  - 기본값: 'tanh' (하이퍼볼릭 탄젠트)
- dropout 매개변수
  - 입력에 대한 드롭아웃 비율을 지정할 수 있음
- return_sequence 매개변수
  - 모든 타임스텝의 은닉 상태를 출력할지 결정함
  - 기본값: False

#### `Embedding` 클래스

- 단어 임베딩을 위한 클래스
- 첫 번째 매개변수에서 어휘 사전의 크기를 지정
- 두 번째 매개변수에서 Embedding 층이 출력할 밀집 벡터의 크기를 지정
