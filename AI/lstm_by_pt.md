# ✔ 파이토치로 LSTM 모델 훈련하기

> ['파이토치로 LSTM 모델 훈련하기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/09-3.pytorch.ipynb)

#### 1. IMDB 리뷰 데이터셋을 로드한 후, 각 샘플의 길이를 100으로 맞추자

```py
from keras.datasets import imdb
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences

(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)
```

#### 2. 데이터를 파이토치 텐서로 바꾼 후, 데이터 로더로 훈련 세트와 검증 세트를 준비하자

```py
from torch.utils.data import TensorDataset, DataLoader

train_seq = torch.tensor(train_seq)
val_seq = torch.tensor(val_seq)
train_target = torch.tensor(train_target, dtype=torch.float32)
val_target = torch.tensor(val_target, dtype=torch.float32)

train_dataset = TensorDataset(train_seq, train_target)
val_dataset = TensorDataset(val_seq, val_target)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)
```

#### 3. LSTM 모델을 만들자

```py
import torch.nn as nn

class IMDBLstm(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(500, 16)
        self.lstm = nn.LSTM(16, 8, batch_first=True, num_layers=2, dropout=0.2)
        self.dense = nn.Linear(8, 1)
        self.sigmoid = nn.Sigmoid()
    def forward(self, x):
        x = self.embedding(x)
        _, (hidden, _) = self.lstm(x)
        outputs = self.dense(hidden[-1])
        return self.sigmoid(outputs)

model = IMDBLstm()
```

- `nn.LSTM` 클래스: LSTM 층
  - num_layers 매개변수: 층의 개수
  - dropout 매개변수: 드롭아웃 비율
- `nn.LSTM` 클래스는 순서대로 아래 세 개의 값을 반환함
  1. 마지막 층의 타임스텝별 은닉 상태
  2. 모든 층의 마지막 은닉 상태
  3. 모든 층의 마지막 셀 상태
- `nn.LSTM` 클래스의 두 번째 반환값인 hidden 값의 크기는 (2, 64, 8)이므로, 두 번째 층의 마지막 값을 선택해서 밀집층에 전달해야 함

#### 4. 모델을 GPU로 적재한 후, 손실 함수와 옵티마이저를 준비하자

```py
import torch
import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters())
```

#### 5. 조기 종료를 사용해 LSTM 모델을 훈련하자

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
        torch.save(model.state_dict(), 'best_2lstm_model.pt')
    else:
        early_stopping_counter += 1
        if early_stopping_counter >= patience:
            print(f"{epoch+1}번째 에포크에서 조기 종료되었습니다.")
            break
```

<img src='./9-3_lstm_pt_fit.png' alt='파이토치로 훈련한 모델의 각 에포크마다 손실 값' width='350px' />

#### 6. 훈련 손실과 검증 손실을 그래프로 그려보자

```py
import matplotlib.pyplot as plt

plt.plot(train_hist, label='train')
plt.plot(val_hist, label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
```

<img src='./9-3_lstm_pt_loss_graph.png' alt='훈련 손실과 검증 손실 그래프' width='400px' />

#### 7. 'best_2lstm_model.pt' 파일을 로드하여 검증 세트에 대한 정확도를 확인해보자

```py
model.load_state_dict(torch.load('best_2lstm_model.pt', weights_only=True))

model.eval()
corrects = 0
with torch.no_grad():
    for inputs, targets in val_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs)
        predicts = outputs > 0.5
        corrects += (predicts.squeeze() == targets).sum().item()

accuracy = corrects / len(val_dataset)
print(f"검증 정확도: {accuracy:.4f}")  # 검증 정확도: 0.8014
```

#### 8. 테스트 세트에 대한 정확도를 확인해보자

```py
test_seq = pad_sequences(test_input, maxlen=100)
test_seq = torch.tensor(test_seq)
test_target = torch.tensor(test_target, dtype=torch.float32)

test_dataset = TensorDataset(test_seq, test_target)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

model.eval()
corrects = 0
with torch.no_grad():
    for inputs, targets in test_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs)
        predicts = outputs > 0.5
        corrects += (predicts.squeeze() == targets).sum().item()

accuracy = corrects / len(test_dataset)
print(f"테스트 정확도: {accuracy:.4f}")  # 테스트 정확도: 0.8072
```
