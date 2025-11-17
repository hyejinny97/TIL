# ✔ 파이토치로 순환 신경망 만들기

> ['파이토치로 순환 신경망 만들기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/09-2.pytorch.ipynb)

#### 1. IMDB 리뷰 데이터셋을 로드한 후, 각 샘플의 길이를 100으로 맞추자

```py
from keras.datasets import imdb
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences

(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)

print(train_seq.shape, train_target.shape)
# (20000, 100) (20000,)
```

#### 2. 입력 데이터와 타깃 데이터를 파이토치 텐서로 바꾸자

```py
train_seq = torch.tensor(train_seq)
val_seq = torch.tensor(val_seq)
```

- 케라스로 준비한 입력 데이터는 넘파이 배열임
- 파이토치의 데이터로더에 사용하려면 이를 파이토치 텐서로 변환해야 함
- `torch.tensor()` 함수: 리스트나 튜플 같은 파이썬 데이터 타입을 파이토치 텐서로 바꿔줌

```py
print(train_target.dtype)  # int64

train_target = torch.tensor(train_target, dtype=torch.float32)
val_target = torch.tensor(val_target, dtype=torch.float32)

print(train_target.dtype)  # torch.float32
```

- 타깃값은 긍정 또는 부정을 나타내는 64비트 정수 1과 0으로 채워져 있음
- 파이토치 손실 함수는 입력으로 실숫값을 기대하기 때문에 32비트 부동소수점으로 변환함

#### 3. 데이터 로더로 훈련 세트와 검증 세트를 준비하자

```py
from torch.utils.data import TensorDataset, DataLoader

train_dataset = TensorDataset(train_seq, train_target)
val_dataset = TensorDataset(val_seq, val_target)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)
```

#### 4. 순환 신경망 모델을 만들자

```py
import torch.nn as nn

class IMDBRnn(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(500, 16)
        self.rnn = nn.RNN(16, 8, batch_first=True)
        self.dense = nn.Linear(8, 1)
        self.sigmoid = nn.Sigmoid()
    def forward(self, x):
        x = self.embedding(x)
        _, hidden = self.rnn(x)
        outputs = self.dense(hidden[-1])
        return self.sigmoid(outputs)

model = IMDBRnn()
```

- 파이토치의 RNN 층은 모든 타임스텝의 출력과 최종 은닉 상태 두 가지 값을 반환하기 때문에, Sequential 클래스를 사용하여 모델을 구현하기에는 어려움이 있음
- 대신, nn.Module의 서브 클래스를 만들어 모델을 구현하면 손쉽게 RNN 모델을 만들 수 있음
- \_\_init\_\_() 메서드에서 부모 클래스의 생성자를 호출한 다음, IMDBRnn 모델이 사용할 층을 생성함
- forward() 메서드에서는 \_\_init\_\_() 메서드에서 정의한 층을 사용해 입력에서 출력까지 층 객체를 호출함
- `nn.Embedding` 클래스: 임베딩 층
  - 첫 번쨰 매개변수에 어휘 사전의 크기를 지정
  - 두 번째 매개변수에 임베딩 벡터의 크기를 지정
  - (배치 크기, 시퀀스 길이) 크기의 입력을 전달하면 (배치 크기, 시퀀스 길이, 임베딩 크기)의 출력을 만듦
- `nnRNN` 클래스: 기본 순환층
  - 첫 번쨰 매개변수에 입력 크기(임베딩 벡터의 크기)를 지정
  - 두 번쨰 매개변수에 출력 크기(뉴런 개수)를 지정
  - 파이토치 순환층은 기본적으로 입력 차원의 순서가 (시퀀스 길이, 배치 크기, 임베딩 크기)라고 가정함
  - batch_first 매개변수를 True로 지정하면 배치 차원이 맨 앞이라는 것을 알릴 수 있음
- 케라스와 달리 파이토치는 여러 개의 순환층을 쌓기 위해 nn.RNN 클래스의 객체를 여러 개 만들 필요가 없이 num_layers 매개변수에서 층 개수를 지정하면 됨 (기본값: 1)
- nn.RNN 클래스는 마지막 층에서 나온 각 타임스텝의 은닉 상태와 모든 층의 최종 은닉 상태 두 개를 반환함
  - 각 타임 스텝의 은닉 상태는 batch_first=True로 지정된 경우 (배치 크기, 시퀀스 길이, 뉴런 개수)이고, False로 지정된 경우 (시퀀스 길이, 배치 크기, 뉴런 개수)임
  - 최종 은닉 상태의 크기는 (층 개수, 배치 크기, 뉴런 개수)임
- `nn.Linear` 클래스: 밀집층
- `nn.Sigmoid` 클래스: 시그모이드 활성화 함수

#### 5. 모델을 GPU로 적재한 후, 손실 함수와 옵티마이저를 준비하자

```py
import torch
import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=2e-4)
```

- 위에서 모델의 마지막 층으로 시그모이드 함수를 추가했기 때문에 `nn.BCELoss`를 사용했음
- 만약, 모델이 마지막 출력을 만들기 위해 시그모이드 함수를 사용하지 않았다면 `nn.BCEWithLogisticLoss`을 손실 함수로 사용해야 함

#### 6. 조기 종료를 사용해 신경망 모델을 훈련하자

```py
train_hist = []  # 훈련 손실
val_hist = []    # 검증 손실
patience = 2
best_loss = -1
early_stopping_counter = 0

epochs = 100
for epoch in range(epochs):
    # 훈련
    model.train()
    train_loss = 0
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), targets)
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
            loss = criterion(outputs.squeeze(), targets)
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
        torch.save(model.state_dict(), 'best_rnn_model.pt')
    else:
        early_stopping_counter += 1
        if early_stopping_counter >= patience:
            print(f"{epoch+1}번째 에포크에서 조기 종료되었습니다.")
            break
```

<img src='./9-2_pt_rnn_loss.png' alt='파이토치로 훈련한 모델의 각 에포크마다 손실 값' width='350px' />

- 이 모델은 (64, 100) 크기의 배치 입력을 받아 마지막 시그모이드 함수를 통과한 (64, 1) 크기의 값을 출력하는데, 이 값은 각 샘플이 양성 클래스에 속할 확률을 나타냄
- 하지만, 위에서 준비한 타깃의 크기는 (64,)로 1차원 배열임
- 손실 함수에서 이 두 값을 사용하려면 차원이 같아야 하므로, 파이토치 텐서의 `squeeze()` 메서드를 사용해 크기가 1인 차원을 삭제한 후 criterion 객체에 전달했음
- 49번째 에포크가 최상의 성능을 기록했으며, 51번째 에포크에서 조기 종료됨

#### 7. 훈련 손실과 검증 손실을 그래프로 그려보자

```py
import matplotlib.pyplot as plt

plt.plot(train_hist, label='train')
plt.plot(val_hist, label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
```

<img src='./9-2_pt_rnn_loss_graph.png' alt='훈련 손실과 검증 손실 그래프' width='400px' />

#### 8. 'best_rnn_model.pt' 파일을 로드하여 검증 세트에 대한 정확도를 확인해보자

```py
model.load_state_dict(torch.load('best_rnn_model.pt', weights_only=True))

model.eval()
corrects = 0
with torch.no_grad():
    for inputs, targets in val_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs)
        predicts = outputs > 0.5
        corrects += (predicts.squeeze() == targets).sum().item()

accuracy = corrects / len(val_dataset)
print(f"검증 정확도: {accuracy:.4f}")  # 검증 정확도: 0.7272
```

- 검증 정확도는 73% 정도임
