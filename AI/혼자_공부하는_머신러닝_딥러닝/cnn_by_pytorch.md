# ✔ 파이토치로 합성곱 신경망 모델 훈련하기

> ['파이토치로 합성곱 신경망 모델 훈련하기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/08-2.pytorch.ipynb)

#### 1. 패션 MNIST 데이터를 로드하고 표준화한 후, 훈련 세트와 검증 세트를 준비하자

```py
from torchvision.datasets import FashionMNIST
from sklearn.model_selection import train_test_split

fm_train = FashionMNIST(root='.', train=True, download=True)
fm_test = FashionMNIST(root='.', train=False, download=True)

train_input = fm_train.data
train_target = fm_train.targets
train_scaled = train_input.reshape(-1, 1, 28, 28) / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)
```

- 파이토치는 이미지의 채널 차원이 배치 차원 바로 다음에 올 것이라 기대함
- 따라서, 기존 (28, 28) 크기의 이미지를 (1, 28, 28) 크기로 변환해야 함

#### 2. 합성곱 신경망 모델을 만들자

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
```

- `add_module()` 메서드: 모델 객체에 층을 하나씩 추가함
  - 첫 번째 매개변수로 층 이름을 전달
  - 두 번째 매개변수로 층 객체를 전달
- `Cov2d` 클래스: 합성곱 층
  - 첫 번쨰 매개변수로 입력 채널 개수를 지정
  - 두 번째 매개변수로 출력 채널 개수(=필터 개수)를 지정
  - kernel_size 매개변수: 커널 크기를 정수 하나 또는 정수의 튜플로 지정
  - padding 매개변수
- `MaxPool2d` 클래스: 최대 풀링층
  - 첫 번째 매개변수는 풀링 크기를 지정(정수 하나 또는 정수 튜플로 지정)

```py
outputs = model(torch.ones(1, 1, 28, 28))
print(outputs.shape)  # torch.Size([1, 3136])
```

- 다음에 올 Linear 층을 사용할 때는 입력 크기를 첫 번째 매개변수로 전달해야 함
- 위 모델에서 Flatten 층으로 펼친 입력의 크기는 3136개인 것을 알 수 있음
  - 7 x 7 x 64 = 3136개

```py
model.add_module('dense1', nn.Linear(3136, 100))
model.add_module('relu3', nn.ReLU())
model.add_module('dropout', nn.Dropout(0.3))
model.add_module('dense2', nn.Linear(100, 10))
```

#### 3. 모델을 GPU로 적재한 후, 손실 함수와 옵티마이저를 준비하자

```py
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

```py
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())
```

#### 4. 조기 종료를 사용해 신경망 모델을 훈련하자

```py
from torch.utils.data import TensorDataset, DataLoader

train_dataset = TensorDataset(train_scaled, train_target)
val_dataset = TensorDataset(val_scaled, val_target)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
```

- 이전 장에서는 훈련 세트를 직접 배치 크기로 나누어 모델을 훈련함
  - 단점1) 훈련 세트의 크기가 배치 크기의 정수배가 아닌 경우에는 이를 적절히 처리해야 하는 문제가 있음
  - 단점2) 에포크마다 훈련 세트를 섞지 않았음
- 에포크가 시작할 때마가 훈련 샘플을 섞어주면, 모델이 샘플 순서에서 발생할 수 있는 편향을 학습하지 않고 무작위성 덕분에 손실 함수의 최솟값을 더 잘 찾을 수 있음
- `TensorDataset` 클래스: 여러 텐서를 결합아여 하나의 데이터셋으로 관리해줌
  - 데이터를 섞을 때 입력과 타깃이 같은 순서로 섞여야 하기 때문에, 배치를 만들기 전 입력과 타깃을 묶어주는 것이 좋음
- `DataLoader` 클래스: 배치를 생성
  - batch_size 매개변수: 배치 크기
  - shuffle 매개변수: 데이터를 섞을 지 여부

```py
train_hist = []  # 훈련 손실
val_hist = []    # 검증 손실
patience = 2
best_loss = -1
early_stopping_counter = 0

epochs = 20
for epoch in range(epochs):
    # 훈련
    model.train()
    train_loss = 0
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    # 검증
    model.eval()
    val_loss = 0
    with torch.no_grad():
        for inputs, targets in val_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            val_loss += loss.item()

    # 훈련 손실과 검증 손실 기록
    train_loss = train_loss/len(train_loader)
    val_loss = val_loss/len(val_loader)
    train_hist.append(train_loss)
    val_hist.append(val_loss)
    print(f"에포크:{epoch+1},",
          f"훈련 손실:{train_loss:.4f}, 검증 손실:{val_loss:.4f}")

    # 조기 종료
    if best_loss == -1 or val_loss < best_loss:
        best_loss = val_loss
        early_stopping_counter = 0
        torch.save(model.state_dict(), 'best_cnn_model.pt')
    else:
        early_stopping_counter += 1
        if early_stopping_counter >= patience:
            print(f"{epoch+1}번째 에포크에서 조기 종료되었습니다.")
            break
```

<img src='./image/8-2_pytorch_loss_by_epoch.png' alt='파이토치로 훈련한 모델의 각 에포크마다 손실 값' width='350px' />

#### 5. 훈련 손실과 검증 손실을 그래프로 그려보자

```py
import matplotlib.pyplot as plt

plt.plot(train_hist, label='train')
plt.plot(val_hist, label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
```

<img src='./image/8-2_pytorch_loss_graph.png' alt='훈련 손실과 검증 손실 그래프' width='400px' />

#### 6. 'best_cnn_model.pt' 파일을 로드하여 검증 세트에 대한 정확도를 확인해보자

```py
model.load_state_dict(torch.load('best_cnn_model.pt', weights_only=True))

model.eval()
corrects = 0
with torch.no_grad():
    for inputs, targets in val_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs)
        predicts = torch.argmax(outputs, 1)
        corrects += (predicts == targets).sum().item()

accuracy = corrects / len(val_dataset)
print(f"검증 정확도: {accuracy:.4f}")
# 검증 정확도: 0.9216
```

- 케라스 모델과 거의 비슷한 정확도를 얻었음

#### 7. 테스트 세트에 대한 정확도를 확인해보자

```py
test_scaled = fm_test.data.reshape(-1, 1, 28, 28) / 255.0
test_target = fm_test.targets

test_dataset = TensorDataset(test_scaled, test_target)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

model.eval()
corrects = 0
with torch.no_grad():
    for inputs, targets in test_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs)
        predicts = torch.argmax(outputs, 1)
        corrects += (predicts == targets).sum().item()

accuracy = corrects / len(test_dataset)
print(f"테스트 정확도: {accuracy:.4f}")
# 테스트 정확도: 0.9165
```

- 테스트 세트의 정확도는 검증 세트보다 약간 낮음
