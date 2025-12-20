# ✔ 강아지와 고양이 사진 분류하기

> ['강아지와 고양이 사진 분류하기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hm-dl/blob/main/02-2.ipynb)

## 1️⃣ VGGNet 모델 로드하기

- 이미지넷 데이터셋에는 다양한 품종의 강아지와 고양이도 포함되어 있기 때문에, 강아지와 고양이 사진을 분류하기 위해 사전 훈련된 모델을 바로 사용할 수 있음
- 케라스에서는 VGGNet을 비롯한 여러 가지 모델을 제공함
- 모델의 구조뿐만 아니라 이미지넷 데이터셋에서 훈련한 모델의 가중치까지 포함되어 있음

### 사전 훈련

- 구체적인 작업에 딥러닝 모델을 적용하기 전에 대규모 데이터셋에서 일반적인 특성을 학습하는 과정
- 컴퓨터 비전에서는 이미지넷 데이터셋, COCO 등과 같은 대규모 데이터셋을 사용해 신경망을 사전 훈련함
- 자연어 처리에서는 인터넷에서 수집한 텍스트 등을 활용해 트랜스포머와 같은 대규모 언어 모델을 사전 훈련함

#### 1. 케라스에서 VGG16 모델을 로드하자

```py
import keras

vggnet = keras.applications.VGG16()
```

- `keras.applications` 모듈: 컴퓨터 비전 문제에 활용할 수 있는 다양한 사전 훈련된 모델을 제공함
  - 이 모듈에서 제공하는 컴퓨터 비전 모델은 이미지넷 데이터셋에서 사전 훈련된 가중치를 기본으로 제공함
- 자연어 처리 분야에서 사용할 수 있는 사전 훈련된 모델은 `KerasNLP` 패키지로 제공함
- `VGG16()` 함수: VGG16 모델
- `weights` 매개변수: 가중치
  - 'imagenet': 이미지넷 데이터셋으로 사전 훈련된 가중치를 로드함
  - None: 랜덤하게 초기화된 가중치가 할당됨
  - 기본값: 'imagenet'

#### 2. 강아지와 고양이 이미지를 구글 드라이브에서 다운로드하고 압축을 해제하자

```
!gdown 1xGkTT3uwYt4myj6eJJeYtdEFgTi2Sj8C
!unzip cat-dog-images.zip
```

- 구글 코랩에서는 셸 명령을 실행하기 위해 `!` 기호를 사요함

#### 3. 강아지 사진을 로드한 후, 이미지를 출력해보자

```py
from PIL import Image

dog_png = Image.open('images/dog.png')
display(dog_png)
```

<img src='./image/2-2_dog_image.png' alt='강아지 사진' width='150px' />

- `Image.open()` 함수: 사진을 로드함
  - PIL.Image.Image 클래스의 객체를 반환함
- `display()` 함수: 이미지를 출력함

#### 4. 샘플 이미지를 넘파이 배열로 변환하자

```py
import numpy as np

dog_array = np.array(dog_png)
print(dog_array.shape)  # (224, 224, 3)
```

- predict() 메서드를 사용해 샘플 이미지를 예측할 수 있음
- 이때, predict() 메서드는 넘파이 배열을 입력값으로 받기 때문에 샘플 이미지를 변환해줘야 함
- VGG16 모델의 이미지 입력 크기와 동일하게 (244, 244, 3) 크기의 넘파이 배열이 준비됨
  - 입력 크기가 달라지면 합성곱층과 풀링층의 출력 크기도 달라지기 때문에, 첫 번째 밀집층에 입력으로 사용할 수 없음
  - 따라서, VGG16 모델에서 밀집층만 새로 만들어 추가한다면 다른 크기의 입력 이미지를 사용할 수 있음

## 2️⃣ 강아지와 고양이 사진 분류하기

### 이미지 전처리

- 사전 훈련된 합성곱 신경망을 사용해 예측을 만들기 전에 수행해야 하는 필수 작업임
- 신경망 모델마다 기대하는 입력의 크기와 값의 범위가 다름
- 경우에 따라서는 컬러 채널의 순서가 다를 수도 있음
- 다행히, 케라스에서는 각 모델의 이미지 전처리 방법을 함께 제공함

#### VGGNet 모델의 이미지 전처리

1. 컬러 이미지의 RGB 채널을 BGR 순서로 바꿈
2. 각 채널에서 이미지넷 데이터셋의 채널 평균값인 (103.939, 116.779, 123.68)을 뺌

### 강아지 사진 분류하기

#### 1. 샘플 이미지를 전처리하자

```py
from keras.applications import vgg16

vgg_prep_dog = vgg16.preprocess_input(dog_array)
```

- `preprocess_input()` 함수: VGGNet에 필요한 이미지 전처리 과정을 수행함

#### 2. VGG16 모델을 사용해 샘플 이미지의 클래스를 예측해보자

```py
predictions = vggnet.predict(vgg_prep_dog[np.newaxis,:])
```

- predict() 메서드는 항상 첫 번째 차원이 배치 차원이어야 함
- 따라서, 늘리고 싶은 차원에 `np.newaxis`를 작성해, (1, 244, 244, 3)과 같이 4차원 배열을 만들어 입력해 줌
- 아래처럼 `reshape()` 메서드나 `expand_dims()` 함수를 사용해 차원을 늘릴 수도 있음

  ```py
  new_prep_dog = vgg_prep_dog.reshape((1, 244, 244, 3))
  ```

  ```py
  new_prep_dog = vgg_prep_dog.reshape((1,) + vgg_prep_dog.shape)
  ```

  ```py
  new_prep_dog = np.expand_dims(vgg_prep_dog, axis=0)
  ```

#### 3. 클래스에 대한 예측 확률 값을 확인해보자

```py
max_index = np.argmax(predictions[0])
print(max_index, predictions[0][max_index])  # 208 0.35698113
```

- predictions는 배치 차원에 해당하는 각 행마다 1,000개의 클래스에 대한 확률 값을 담고 있음
- `argmax()` 함수: 배열에서 가장 큰 값을 가진 인덱스를 반환함
- 실행 결과를 보면, 인덱스가 208(즉, 209번째)인 클래스가 약 35.7%의 확률로 예측됨을 알 수 있음

### 모델 출력 디코딩하기

- 구글 클라우드 스토리지(Google Cloud Storage, GCS)에 이미지넷의 클래스에 대한 정보가 공개되어 있음

#### 1. 구글 클라우드 스토리지에 저장된 이미지넷 클래스 파일을 다운로드하고 디코딩해보자

```py
import requests

url = "https://storage.googleapis.com/download.tensorflow.org/" + \
      "data/imagenet_class_index.json"
json_data = requests.get(url).json()

print(json_data[str(max_index)])
# ['n02099712', 'Labrador_retriever']
```

- 인덱스가 208인 클래스는 래브라도 리트리버인 것을 알 수 있음
- 'n02099712': 이미지넷 클래스에 대한 고유 ID 값

#### 2. decode_predictions() 함수를 사용해 높은 확률을 가진 클래스 정보를 손쉽게 얻어보자

```py
vgg16.decode_predictions(predictions)
```

<img src='./image/2-2_decode_predictions.png' alt='예측 확률 디코딩 결과' width='700px' />

- `decode_predictions()` 함수: predict() 메서드의 반환 값인 predictions를 전달하면 높은 확률을 가진 클래스를 얻을 수 있음
- 실행 결과, 약 35.7%의 확률로 '래브라도 리트리버'가 예측되었고, 그 다음 약 14.5%의 확률로 '골든 리트리버'가 예측됨

```py
vgg16.decode_predictions(predictions, top=1)
# [[('n02099712', 'Labrador_retriever', np.float32(0.35698113))]]
```

- `top` 매개변수: 출력하고 싶은 최상위 클래스의 개수
  - 기본값: 5 (가장 높은 확률을 가진 5개의 클래스를 반환)

### 고양이 사진 분류하기

#### 1. 고양이 사진을 로드한 후, 이미지를 출력해보자

```py
cat_png = Image.open('images/cat.png')
display(cat_png)
```

<img src='./image/2-2_cat_image.png' alt='고양이 이미지' width='150px' />

#### 2. 이미지를 전처리한 후 예측해보자

```py
vgg_prep_cat = vgg16.preprocess_input(np.array(cat_png))
predictions = vggnet.predict(vgg_prep_cat[np.newaxis,:])
vgg16.decode_predictions(predictions)
"""
[[('n02123045', 'tabby', np.float32(0.43275326)),
  ('n02124075', 'Egyptian_cat', np.float32(0.3112799)),
  ('n02123159', 'tiger_cat', np.float32(0.21606496)),
  ('n02971356', 'carton', np.float32(0.0035795611)),
  ('n03223299', 'doormat', np.float32(0.0031308222))]]
"""
```

- 실행 결과, 약 43.3%의 확률로 '얼룩 고양이'를 예측했고, 31.3%의 확률로 '이집트 고양이'를 예측했음
