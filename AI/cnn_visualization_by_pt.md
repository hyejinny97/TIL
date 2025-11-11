# ✔ 파이토치로 합성곱 신경망 시각화하기

> ['파이토치로 합성곱 신경망 시각화하기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/08-3.pytorch.ipynb)

## 1️⃣ 가중치 시각화

#### 1. 합성곱 신경망 모델을 만든 후, 'best-cnn-model.pt'에 저장된 가중치를 로드하자

```py
import torch.nn as nn

model = nn.Sequential()
model.add_module('conv1', nn.Conv2d(1, 32, kernel_size=3, padding='same'))
model.add_module('relu1', nn.ReLU())
model.add_module('pool1', nn.MaxPool2d(2))
model.add_module('conv2', nn.Conv2d(32, 64, kernel_size=3, padding='same'))
model.add_module('relu2', nn.ReLU())
model.add_module('pool2', nn.MaxPool2d(2))
model.add_module('flatten', nn.Flatten())
model.add_module('dense1', nn.Linear(3136, 100))
model.add_module('relu3', nn.ReLU())
model.add_module('dropout', nn.Dropout(0.3))
model.add_module('dense2', nn.Linear(100, 10))

model.load_state_dict(torch.load('best_cnn_model.pt', weights_only=True))
```

- 'best-cnn-model.pt' 파일에는 가중치만 저장되어 있기 때문에, 이전에 만든 것과 동일한 모델을 생성한 후 이 가중치를 로드해야 함

#### 2. 첫 번째 합성곱 층을 가져오자

##### 방법1) model 객체의 `children()` 메서드 사용

```py
layers = [layer for layer in model.children()]
print(layers[0])
# Conv2d(1, 32, kernel_size=(3, 3), stride=(1, 1), padding=same)
```

- `children()` 메서드: 모델에 추가된 층을 반환하는 파이썬 제너레이터 객체를 반환함

##### 방법2) model 객체의 `named_children()` 메서드 사용

```py
for name, layer in model.named_children():
    print(f"{name:10s}", layer)

"""
conv1      Conv2d(1, 32, kernel_size=(3, 3), stride=(1, 1), padding=same)
relu1      ReLU()
pool1      MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
conv2      Conv2d(32, 64, kernel_size=(3, 3), stride=(1, 1), padding=same)
relu2      ReLU()
pool2      MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
flatten    Flatten(start_dim=1, end_dim=-1)
dense1     Linear(in_features=3136, out_features=100, bias=True)
relu3      ReLU()
dropout    Dropout(p=0.3, inplace=False)
dense2     Linear(in_features=100, out_features=10, bias=True)
"""
```

- `named_children()` 메서드: 층의 이름과 층 객체를 반환함

##### 방법3) model 객체의 속성을 이용

```py
model[0]
# Conv2d(1, 32, kernel_size=(3, 3), stride=(1, 1), padding=same)
```

- Sequential 클래스로 만든 모델은 정수 인덱스로 하위 층을 참조할 수 있음

```py
model.conv1
# Conv2d(1, 32, kernel_size=(3, 3), stride=(1, 1), padding=same)
```

- 파이토치 모델은 층의 이름을 모델의 속성처럼 사용해 층을 참조할 수 있음

#### 3. 첫 번째 합성곱 층 가중치의 평균과 표준편차를 계산해보자

```py
conv_weights = model.conv1.weight.

print(conv_weights.shape)
# torch.Size([32, 1, 3, 3])
print(conv_weights.mean(), conv_weights.std())
# tensor(-0.0550) tensor(0.3589)
```

- `weight` 속성: 파이토치 층의 가중치를 저장
  - 파이토치의 Parameter 클래스의 객체
  - 실제 가중치 텐서는 `data` 속성에 저장됨
- `bias` 속성: 파이토치 층의 절편을 저장
  - 파이토치의 Parameter 클래스의 객체
  - 실제 절편 텐서는 `data` 속성에 저장됨
- 역시 평균은 0에 가깝고 표준편차는 약 0.3 정도임
- 케라스는 기본적으로 가중치를 (높이, 너비, 채널, 필터 개수)로 나타내지만, 파이토치는 (필터 개수, 채널, 높이, 너비)로 나타냄

#### 4. 가중치를 히스토그램으로 그려보자

```py
import matplotlib.pyplot as plt

plt.hist(conv_weights.reshape(-1, 1))
plt.xlabel('weight')
plt.ylabel('count')
plt.show()
```

<img src='./8-3_weights_histogram_pt.png' alt='가중치 히스토그램' width='350px' />

- 케라스 모델과 비슷하게 약간 한쪽으로 치우쳐져 있지만 종모양 형태를 띄고 있음

#### 5. 32개의 필터를 이미지로 출력해보자

```py
fig, axs = plt.subplots(2, 16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i, j].imshow(conv_weights[i*16 + j,0,:,:], vmin=-0.5, vmax=0.5)
        axs[i, j].axis('off')
plt.show()
```

<img src='./8-3_weights_subplot_pt.png' alt='필터 이미지' width='700px' />

## 2️⃣ 특성 맵 시각화

### 첫 번째 합성곱 층의 특성 맵 시각화

#### 1. 패션 MNIST 데이터셋을 읽은 후 훈련 세트에 있는 첫 번쨰 샘플을 그려보자

```py
from torchvision.datasets import FashionMNIST

fm_train = FashionMNIST(root='.', train=True, download=True)
train_input = fm_train.data

plt.imshow(train_input[0], cmap='gray_r')
plt.show()
```

<img src='./8-3_sample_img.png' alt='첫 번째 샘플' width='250px' />

#### 2. 샘플을 첫 번째 합성곱 층과 렐루 층에 전달한 후 특성 맵을 만들어보자

```py
ankle_boot = train_input[0:1].reshape(1, 1, 28, 28) / 255.0

model.eval()
with torch.no_grad():
    feature_maps = model.conv1(ankle_boot)
    feature_maps = model.relu1(feature_maps)

print(feature_maps.shape)
# torch.Size([1, 32, 28, 28])
```

- 파이토치의 경우, 렐루 함수가 별도의 층으로 분리되어 있기 때문에 합성곱 층이 반환한 결과를 다시 렐루 층에 전달하여 최종 결과를 얻어야 함

#### 3. 32개의 특성 맵을 이미지로 출력해보자

```py
fig, axs = plt.subplots(4, 8, figsize=(15,8))
for i in range(4):
    for j in range(8):
        axs[i, j].imshow(feature_maps[0,i*8 + j,:,:])
        axs[i, j].axis('off')
plt.show()
```

<img src='./8-3_feature_maps_pt.png' alt='특성 맵' width='500px' />

- 케라스 모델과 비슷하게 이 합성곱 층은 이미지의 경계와 모서리, 전경, 배경 등을 감지하는 것 같음

### 두 번째 합성곱 층의 특성 맵 시각화

#### 1. 두 번째 합성곱 층까지 거쳐 특성 맵을 만들어보자

```py
# 방법1
model.eval()
with torch.no_grad():
    feature_maps = model.conv1(ankle_boot)
    feature_maps = model.relu1(feature_maps)
    feature_maps = model.pool1(feature_maps)
    feature_maps = model.conv2(feature_maps)
    feature_maps = model.relu2(feature_maps)
```

```py
# 방법2
model.eval()
x = ankle_boot
with torch.no_grad():
    for name, layer in model.named_children():
        x = layer(x)
        if name == 'relu2':
            break
feature_maps = x
```

#### 2. 32개의 특성 맵을 이미지로 출력해보자

```py
fig, axs = plt.subplots(8, 8, figsize=(12,12))
for i in range(8):
    for j in range(8):
        axs[i, j].imshow(feature_maps[0,i*8 + j,:,:])
        axs[i, j].axis('off')
plt.show()
```

<img src='./8-3_feature_maps_second_pt.png' alt='특성 맵' width='500px' />

- 두 번째 합성곱 층이 출력한 특성 맵도 케라스 모델이 만든 것과 비슷한 것 같음
