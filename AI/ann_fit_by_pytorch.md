# ✔ 파이토치로 신경망 모델 훈련하기

> ['파이토치로 신경망 모델 훈련하기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/07-3.pytorch.ipynb)

#### 1. 패션 MNIST 데이터를 로드하고, 훈련 세트와 검증 세트를 준비하자

```py
from torchvision.datasets import FashionMNIST

fm_train = FashionMNIST(root='.', train=True, download=True)
fm_test = FashionMNIST(root='.', train=False, download=True)

train_input = fm_train.data
train_target = fm_train.targets

train_scaled = train_input / 255.0
```

```py
from sklearn.model_selection import train_test_split

train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)
```

#### 2. 신경망 모델을 만들고, GPU에 적재하자

```py
import torch.nn as nn

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 100),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(100, 10)
)
```

```py
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

#### 3. 손실 함수와 옵티마이저를 준비하자

```py
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())
```

#### 4. 조기 종료를 사용해 신경망 모델을 훈련하자

```py
train_hist = []  # 훈련 손실
val_hist = []    # 검증 손실
patience = 2
best_loss = -1
early_stopping_counter = 0

epochs = 20
batches = int(len(train_scaled)/32)
for epoch in range(epochs):
    model.train()
    train_loss = 0
    for i in range(batches):
        inputs = train_scaled[i*32:(i+1)*32].to(device)
        targets = train_target[i*32:(i+1)*32].to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    model.eval()
    val_loss = 0
    with torch.no_grad():
        val_scaled = val_scaled.to(device)
        val_target = val_target.to(device)
        outputs = model(val_scaled)
        loss = criterion(outputs, val_target)
        val_loss = loss.item()

    # 훈련 손실과 검증 손실 기록
    train_hist.append(train_loss/batches)
    val_hist.append(val_loss)
    print(f"에포크:{epoch+1},",
          f"훈련 손실:{train_loss/batches:.4f}, 검증 손실:{val_loss:.4f}")

    # 조기 종료
    if best_loss == -1 or val_loss < best_loss:
        best_loss = val_loss
        early_stopping_counter = 0
        torch.save(model.state_dict(), 'best_model.pt')
    else:
        early_stopping_counter += 1
        if early_stopping_counter >= patience:
            print(f"{epoch+1}번째 에포크에서 조기 종료되었습니다.")
            break
```

<img src='./7-3)_pytorch_loss_by_epoch.png' alt='파이토치로 훈련한 모델의 각 에포크마다 손실 값' width='350px' />

- `torch.save()` 함수: 모델을 저장
  - 모델 객체와 파일 이름을 지정하면 모델 구조와 모델 파라미터가 모두 저장됨
- `state_dict()` 메서드: 모델 파라미터와 훈련하는 동안 기록된 다른 값(층 정규화의 파라미터 등)을 반환함

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

<img src='./7-3_pytorch_loss_graph.png' alt='훈련 손실과 검증 손실 그래프' width='400px' />

- 8번째 에포크에서 검증 점수가 가장 좋고 그 이후에 과대적합되어 10번째 에포크에서 멈춘 것을 확인할 수 있음

#### 6. 'best_model.pt' 파일에 저장한 모델 파라미터를 읽어 모델을 복원해보자

```py
model.load_state_dict(torch.load('best_model.pt', weights_only=True))
```

- `torch.load()` 함수: torch.save()로 저장한 모델이나 텐서를 불러옴
- `load_state_dict()` 메서드: state_dict()로 저장한 데이터를 다시 모델에 복원해줌

#### 7. 검증 세트에 대한 정확도를 확인해보자

```py
model.eval()
with torch.no_grad():
    val_scaled = val_scaled.to(device)
    val_target = val_target.to(device)
    outputs = model(val_scaled)
    predicts = torch.argmax(outputs, 1)
    corrects = (predicts == val_target).sum().item()

accuracy = corrects / len(val_target)
print(f"검증 정확도: {accuracy:.4f}")
# 검증 정확도: 0.8798
```
