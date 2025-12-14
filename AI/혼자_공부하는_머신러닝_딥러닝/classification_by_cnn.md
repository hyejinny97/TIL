# ✔ 합성곱 신경망을 사용한 이미지 분류

> ['합성곱 신경망을 사용한 이미지 분류' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl/blob/master/8-2.ipynb)

## 1️⃣ 패션 MNIST 데이터 불러오기

#### 1. 패션 MNIST 데이터를 다운로드하고 전처리한 후, 훈련 세트와 검증 세트로 나누자

```py
from tensorflow import keras
from sklearn.model_selection import train_test_split

(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()

train_scaled = train_input.reshape(-1, 28, 28, 1) / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)
```

- 입력 이미지는 항상 깊이(채널) 차원이 있어야 함
- 흑백 이미지의 경우 채널 차원이 없는 2차원 배열이지만 Conv2D층을 사용하기 위해 마지막에 채널 차원을 추가해야 함

## 2️⃣ 합성곱 신경망 만들기

- 전형적인 합성곱 신경망 구조는 합성곱 층으로 이미지에서 특징을 감지한 후 밀집층으로 클래스에 따른 분류 확률을 계산함

#### 1. 합성곱 신경망 모델을 만들자

```py
model = keras.Sequential()
model.add(keras.layers.Input(shape=(28,28,1)))
model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))
```

- 필터 개수가 32개인 첫 번째 합성곱-풀링 층을 만듦

```py
model.add(keras.layers.Conv2D(64, kernel_size=(3,3), activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))
```

- 필터 개수가 64개인 두 번째 합성곱-풀링 층을 만듦

```py
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(10, activation='softmax'))
```

- 특성 맵을 일렬로 펼쳐서 Dense 은닉층, Dense 출력층에 순서대로 전달했음

#### 2. 모델의 구조를 확인해보자

```py
model.summary()
```

<img src='./image/8-2_cnn_summary.png' alt='신경망 모델 정보' width='550px' />

- 첫 번째 합성곱층의 파라미터 개수: 3 x 3 x 1 x 32 + 32 = 320개
- 두 번째 합성곱층의 파라미터 개수: 3 x 3 x 32 x 64 + 64 = 18,496개

#### 3. 층의 구성을 그림으로 확인해보자

```py
keras.utils.plot_model(model)
keras.utils.plot_model(model, show_shapes=True)
```

<img src='./image/8-2_cnn_plot.png' alt='층의 구성 그림' width='100px' />
<img src='./image/8-2_cnn_plot_shapes.png' alt='층의 구성과 입력 및 출력' width='300px' />

- `plot_model()` 함수: 층의 구성을 그림으로 표현해줌
  - 기본적으로 'model.png' 파일에 출력된 이미지를 저장해줌
- show_shape 매개변수: True로 설정하면 그림에 입력과 출력의 크기를 표시해줌
- to_file 매개변수: 원하는 파일 이름을 지정
- dpi 매개변수: 해상도를 지정
  - 기본값: 200

## 3️⃣ 모델 컴파일과 훈련

#### 1. 모델을 컴파일하고 훈련하자

```py
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.keras', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)

history = model.fit(train_scaled, train_target, epochs=20, validation_data=(val_scaled, val_target), callbacks=[checkpoint_cb, early_stopping_cb])
```

<img src='./image/8-2_cnn_fit_result.png' alt='모델 훈련 결과' width='750px' />

- 훈련 세트의 정확도가 이전에는 80%대였는데 90%대로 올랐음

#### 2. 훈련 손실과 검증 손실의 그래프를 그려보자

```py
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
```

<img src='./image/8-2_cnn_loss_graph.png' alt='훈련 손실과 검증 손실의 그래프' width='400px' />

- 여섯 번째 에포크가 최적임

#### 3. 검증 세트에 대한 성능을 평가해보자

```py
model.evaluate(val_scaled, val_target)
```

<img src='./image/8-2_cnn_val_accuracy.png' alt='검증 세트에 대한 성능' width='550px' />

#### 4. 검증 세트의 첫 번째 샘플 이미지를 확인해보자

```py
plt.imshow(val_scaled[0].reshape(28, 28), cmap='gray_r')
plt.show()
```

<img src='./image/8-2_sample_img.png' alt='첫 번째 샘플 이미지' width='300px' />

- 맷플롯립에서는 흑백 이미지에 깊이 차원은 없기 때문에, (28, 28, 1) 크기를 (28, 28)로 바꾸어 출력해야 함

#### 5. 검증 세트의 첫 번째 샘플 이미지에 대한 예측 확률을 출력해보자

```py
preds = model.predict(val_scaled[0:1])
print(preds)
```

<img src='./image/8-2_predict_sample.png' alt='첫 번째 샘플 이미지에 대한 예측 확률' width='500px' />

- 케라스의 fit(), predict(), evaluate() 메서드는 모두 입력의 첫 번째 차원이 배치 차원이라고 기대함
  - 따라서, 인덱싱이 아닌 배열 슬라이싱을 사용했음
- 결과를 보면 아홉 번째 값이 1이고 다른 값은 거의 0에 가까움
  - 즉, 위 샘플은 아홉 번째 클래스일 확률이 높음

#### 6. 첫 번째 샘플 이미지에 대한 예측 확률을 막대 그래프로 그려보자

```py
plt.bar(range(1, 11), preds[0])
plt.xlabel('class')
plt.ylabel('prob.')
plt.show()
```

<img src='./image/8-2_sample_bar.png' alt='첫 번째 샘플 이미지의 예측 확률에 대한 막대 그래프' width='350px' />

```py
import numpy as np

classes = ['티셔츠', '바지', '스웨터', '드레스', '코트', '샌달', '셔츠', '스니커즈', '가방', '앵클 부츠']
print(classes[np.argmax(preds)])  # 가방
```

- 샘플을 '가방'으로 잘 예측했음

#### 7. 테스트 세트에 대한 성능을 평가해보자

```py
test_scaled = test_input.reshape(-1, 28, 28, 1) / 255.0
model.evaluate(test_scaled, test_target)
```

<img src='./image/8-2_cnn_test_accuracy.png' alt='테스트 세트에 대한 성능' width='550px' />

- 테스트 세트에서의 점수는 검증 세트보다 조금 더 작지만, 약 91%의 성능을 보임

## cf) 핵심 패키지와 함수

### Keras

#### `Conv2D` 클래스

- 입력의 너비와 높이 방향의 합성곱 연산을 구현한 클래스
- 첫 번째 매개변수는 합성곱 필터의 개수임
- kernel_size 매개변수
  - 필터의 커널 크기를 지정
  - 가로세로 크기가 같은 경우 정수 하나로, 다른 경우 (높이, 너비)로 구성된 정수 튜플을 지정할 수 있음
  - 일반적으로 커널의 가로세로 크기는 동일함
  - 커널의 깊이는 입력의 깊이와 동일하기 때문에 따로 지정하지 않음
- strides 매개변수
  - 필터의 이동 간격을 지정
  - 가로세로 크기가 같은 경우 정수 하나로, 다른 경우 정수 튜플을 지정할 수 있음
  - 일반적으로 스트라이드의 가로세로 크기는 동일함
  - 기본값: 1
- padding 매개변수
  - 입력의 패딩 타입을 지정
  - 'valid': 패딩을 하지 않음
  - 'same': 합성곱 층의 출력의 가로세로 크기를 입력과 동일하게 맞추도록 입력에 패딩을 추가함
  - 기본값: 'valid'
- activation 매개변수
  - 합성곱 층에 적용할 활성화 함수를 지정

#### `MaxPooling2D` 클래스

- 입력의 너비와 높이를 줄이는 풀링 연산을 구현한 클래스
- 첫 번째 매개변수는 풀링의 크기를 지정
  - 가로세로 크기가 같은 경우 정수 하나로, 다른 경우 정수 튜플을 지정할 수 있음
  - 일반적으로 풀링의 가로세로 크기는 동일함
- strides 매개변수
  - 풀링의 이동 간격을 지정
  - 기본값: 풀링의 크기와 동일 (즉, 입력 위를 겹쳐서 풀링하지 않음)
- padding 매개변수
  - 입력의 패딩 타입을 지정
  - 'valid': 패딩을 하지 않음
  - 'same': 합성곱 층의 출력의 가로세로 크기를 입력과 동일하게 맞추도록 입력에 패딩을 추가함
  - 기본값: 'valid'

#### `plot_model()` 함수

- 케라스 모델 구조를 주피터 노트북에 그리거나 파일로 저장함
- 첫 번째 매개변수에 케라스 모델 객체를 전달함
- to_file 매개변수
  - 파일 이름을 지정하면 그림을 파일로 저장함
- show_shapes 매개변수
  - True로 지정하면 층의 입력, 출력 크기를 표시함
  - 기본값: False
- show_layer_names 매개변수
  - True로 지정하면 층 이름을 출력함
  - 기본값: False

### matplotlib

#### `bar()` 함수

- 막대그래프를 출력함
- 첫 번째 매개변수에 x축의 값을 리스트나 넘파이 배열로 전달함
- 두 번째 매개변수에 막대의 y축 값을 리스트나 넘파이 배열로 전달함
- width 매개변수
  - 막대의 두께를 지정
  - 기본값: 0.8
