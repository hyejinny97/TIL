# ✔ 합성곱 신경망의 시각화

> ['합성곱 신경망의 시각화' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/8-3.ipynb)

## 1️⃣ 가중치 시각화

- 합성곱 층은 여러 개의 필터를 사용해 이미지에서 특징을 학습함
- 가중치는 입력 이미지의 2차원 영역에 적용되어 어떤 특징을 크게 두드러지게 표현하는 역할을 함

### 훈련한 모델의 가중치 시각화

#### 1. 'best-cnn-model.keras' 모델을 로드하자

```py
model = keras.models.load_model('best-cnn-model.keras')
```

```py
model.layers
"""
[<Conv2D name=conv2d, built=True>,
 <MaxPooling2D name=max_pooling2d, built=True>,
 <Conv2D name=conv2d_1, built=True>,
 <MaxPooling2D name=max_pooling2d_1, built=True>,
 <Flatten name=flatten, built=True>,
 <Dense name=dense, built=True>,
 <Dropout name=dropout, built=True>,
 <Dense name=dense_1, built=True>]
"""
```

- `layers` 속성: 케라스 모델에 추가한 층이 저장됨

#### 2. 첫 번째 합성곱 층의 가중치를 확인해보자

```py
conv = model.layers[0]

print(conv.weights[0].shape, conv.weights[1].shape)
# (3, 3, 1, 32) (32,)
```

- `weights` 속성: 층의 가중치와 절편이 저장됨
  - 첫 번째 원소: 가중치
  - 두 번째 원소: 절편
- (3, 3, 1, 32): 커널 크기가 (3, 3, 1)인 필터 32개
- (32,): 필터마다 절편 하나씩 총 32개

#### 3. 가중치 배열의 평균과 표준편차를 계산해보자

```py
conv_weights = conv.weights[0].numpy()

print(conv_weights.mean(), conv_weights.std())
# -0.014383553 0.23351653
```

- weights 속성은 텐서플로의 다차원 배열인 Tensor 클래스의 객체이므로, 다루기 쉽도록 넘파이 배열로 변환함
- 가중치의 평균값은 0에 가깝고 표준편차는 0.23 정도임

#### 4. 가중치를 히스토그램으로 그려보자

```py
import matplotlib.pyplot as plt

plt.hist(conv_weights.reshape(-1, 1))
plt.xlabel('weight')
plt.ylabel('count')
plt.show()
```

<img src='./8-3_weights_histogram.png' alt='가중치 히스토그램' width='350px' />

- 히스토그램을 보면 0을 중심으로 종 모양 분포를 띠고 있는 것을 알 수 있음

#### 5. 32개의 필터를 이미지로 출력해보자

```py
fig, axs = plt.subplots(2, 16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i, j].imshow(conv_weights[:,:,0,i*16 + j], vmin=-0.5, vmax=0.5)
        axs[i, j].axis('off')
plt.show()
```

<img src='./8-3_weights_subplot.png' alt='가중치 히스토그램' width='700px' />

- 결과 그래프를 보면 가중치 값이 무작위로 나열된 것이 아닌 어떤 패턴을 볼 수 있음
- 가중치 값이 낮을수록 검은색에 가깝고, 높을수록 노란색에 가까움
- `imshow()` 함수: 배열에 있는 최댓값과 최솟값을 사용해 픽셀의 강도를 표현함
  - 하지만, 어떤 절댓값으로 기준을 정해서 픽셀의 강도를 나타내야 비교하기 좋음
  - `vmin`과 `vmax` 매개변수를 통해 컬러맵으로 표현할 범위 지정 가능

### 훈련하지 않은 모델의 가중치 시각화

#### 1. 새로운 합성곱 신경망 모델을 하나 만들자

```py
no_training_model = keras.Sequential()
no_training_model.add(keras.layers.Input(shape=(28,28,1)))
no_training_model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same'))
```

#### 2. 합성곱 층의 가중치를 확인해보자

```py
no_training_conv = no_training_model.layers[0]
print(no_training_conv.weights[0].shape)
# (3, 3, 1, 32)
```

#### 3. 가중치 배열의 평균과 표준편차를 계산해보자

```py
no_training_weights = no_training_conv.weights[0].numpy()
print(no_training_weights.mean(), no_training_weights.std())
# 0.0053191613 0.08463709
```

- 평균은 이전과 동일하게 0에 가깝지만 표준편차는 이전과 달리 매우 작음

#### 4. 가중치를 히스토그램으로 그려보자

```py
plt.hist(no_training_weights.reshape(-1, 1))
plt.xlabel('weight')
plt.ylabel('count')
plt.show()
```

<img src='./8-3_weights_histogram_no_trained.png' alt='가중치 히스토그램' width='350px' />

- 대부분의 가중치가 -0.15 ~ 0.15 사이에 있고 비교적 고른 분포를 보임
- 이런 이유는 케라스가 신경망의 가중치를 처음 초기화할 때 균등 분포에서 랜덤하게 값을 선택하기 때문

#### 5. 32개의 필터를 이미지로 출력해보자

```py
fig, axs = plt.subplots(2, 16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i, j].imshow(no_training_weights[:,:,0,i*16 + j], vmin=-0.5, vmax=0.5)
        axs[i, j].axis('off')
plt.show()
```

<img src='./8-3_weights_subplot_no_trained.png' alt='가중치 히스토그램' width='700px' />

- 전체적으로 가중치가 밋밋하게 초기화된 것을 볼 수 있음
- 훈련한 모델의 가중치를 시각화한 이미지와 비교해봤을 때, 합성곱 신경망이 패션 MNIST 데이터셋의 분류 정확도를 높이기 위해 유용한 패턴을 학습했다는 사실을 알 수 있음

## 2️⃣ 함수형 API

- 케라스 Sequential 클래스는 층을 차례대로 쌓은 모델을 만듦
  - 단점: 입력이 2개이거나 출력이 2개인 복잡한 모델은 만들 수 없음
- 함수형 API를 사용하면 복잡한 조합의 모델을 자유롭게 구성할 수 있음
  - 함수형 API는 케라스의 Model 클래스를 사용해 모델을 만듦
- model 객체의 predict() 메서드를 호출하면 입력부터 마지막 층까지 모든 계산을 수행한 후 최종 출력을 반환함
  - 따라서, 특정 합성곱 층의 특성 맵을 얻으려면 함수형 API를 사용해야 함

#### 완전 연결 신경망을 함수형 API로 구현해보자

```py
inputs = keras.Input(shape=(784,))
dense1 = keras.layers.Dense(100, activation='relu')
dense2 = keras.layers.Dense(10, activation='sortmax')

hidden = dense1(inputs)
outputs = dense2(hidden)
func_model = keras.Model(inputs, outputs)
```

- 케라스의 층은 객체를 함수처럼 호출했을 때 적절히 동작할 수 있도록 미리 준비해 놓았음
- 체인처럼 입력에서 출력까지 연결하고 마지막에 Model 클래스에 입력과 출력을 지정하여 모델을 만듦
- 이렇게 모델을 만들게 되면 중간에 다양한 형태로 층을 연결할 수 있음

#### 합성곱 신경망 첫 번째 합성곱 층의 특성 멥을 출력하는 모델을 만들자

```py
print(model.inputs)
# [<KerasTensor shape=(None, 28, 28, 1), dtype=float32, sparse=False, name=input_layer>]
```

- `inputs` 속성: 모델의 입력을 저장

```py
conv_acti = keras.Model(model.inputs[0], model.layers[0].output)
```

- `output` 속성: 층의 출력을 저장
- model.inputs의 첫 번째 원소와 model.layers[0].output을 연결하는 새로운 conv_acti 모델을 만들었음
- model 객체의 predict() 메서드를 호출하면 최종 출력층의 확률을 반환하지만, conv_acti의 predict() 메서드를 호출하면 첫 번쨰 Conv2D의 출력을 반환할 것임

## 3️⃣ 특성 맵 시각화

### 첫 번째 합성곱 층의 특성 맵 시각화

#### 1. 패션 MNIST 데이터셋을 읽은 후 훈련 세트에 있는 첫 번쨰 샘플을 그려보자

```py
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()

plt.imshow(train_input[0], cmap='gray_r')
plt.show()
```

<img src='./8-3_sample_img.png' alt='첫 번째 샘플' width='250px' />

- 앵클 부츠인 것을 확인할 수 있음

#### 2. 샘플을 conv_acti 모델에 주입해 특성 맵을 출력해보자

```py
inputs = train_input[0:1].reshape(-1, 28, 28, 1) / 255.0

feature_maps = conv_acti.predict(inputs)
print(feature_maps.shape)  # (1, 28, 28, 32)
```

- predict() 메서드는 항상 입력의 첫 번째 차원이 배치 차원일 것으로 기대하므로 슬라이싱 연산자를 사용했음
- (1, 28, 28, 32) == (배치, 너비, 높이, 필터 개수 또는 특성 맵 개수)

#### 3. 32개의 특성 맵을 이미지로 출력해보자

```py
fig, axs = plt.subplots(4, 8, figsize=(15,8))
for i in range(4):
    for j in range(8):
        axs[i, j].imshow(feature_maps[0,:,:,i*8 + j])
        axs[i, j].axis('off')
plt.show()
```

<img src='./8-3_feature_maps.png' alt='특성 맵' width='500px' />

- 위 특성 맵은 32개의 필터로 인해 입력 이미지에서 강하게 활성화된 부분을 보여 줌
- 일곱 번째 필터는 전체적으로 밝은 색이므로, 전면이 모두 칠해진 영역을 감지함
- 스물 네 번째 필터는 수직선을 감지하므로, 특성 맵에서 수직선이 강하게 활성화되었음

### 두 번째 합성곱 층의 특성 맵 시각화

#### 1. 합성곱 신경망 두 번째 합성곱 층의 특성 멥을 출력하는 모델을 만들자

```py
conv2_acti = keras.Model(model.inputs, model.layers[2].output)
```

#### 2. 샘플을 conv2_acti 모델에 주입해 특성 맵을 출력해보자

```py
inputs = train_input[0:1].reshape(-1, 28, 28, 1) / 255.0

feature_maps = conv2_acti.predict(inputs)
print(feature_maps.shape)  # (1, 14, 14, 64)
```

- (1, 14, 14, 64) == (배치, 너비, 높이, 필터 개수 또는 특성 맵 개수)

#### 3. 64개의 특성 맵을 이미지로 출력해보자

```py
fig, axs = plt.subplots(8, 8, figsize=(12,12))
for i in range(8):
    for j in range(8):
        axs[i, j].imshow(feature_maps[0,:,:,i*8 + j])
        axs[i, j].axis('off')
plt.show()
```

<img src='./8-3_feature_maps_second.png' alt='특성 맵' width='500px' />

- 위 특성 맵은 직관적으로 이해하기 어려운데, 이런 현상은 합성곱 층을 많이 쌓을수록 심해짐
- 합성곱 신경망의 앞부분에 있는 합성곱 층은 이미지의 시각적인 정보를 감지하고 뒤쪽에 있는 합성곱 층은 앞쪽에서 감지한 시각적인 정보를 바탕으로 추상적인 정보를 학습함

## cf) 핵심 패키지와 함수

### Keras

#### `Model` 클래스

- 케라스 모델을 만드는 클래스
- 첫 번째 매개변수인 inputs에 모델의 입력 또는 입력의 리스트를 지정함
- 두 번째 매개변수인 outputs에 모델의 출력 또는 출력의 리스트를 지정함
- name 매개변수
  - 모델의 이름 지정
