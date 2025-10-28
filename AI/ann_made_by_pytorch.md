# ✔ 파이토치로 신경망 모델 만들기

> ['파이토치로 신경망 모델 만들기' 구글 코랩](https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/07-2.pytorch.ipynb)

#### 1. 패션 MNIST 데이터를 가져오자

```py
from torchvision.datasets import FashionMNIST

fm_train = FashionMNIST(root='.', train=True, download=True)
fm_test = FashionMNIST(root='.', train=False, download=True)
```

- 파이토치의 컴퓨터 비전 라이브러리인 torchvision을 통해 패션 MNIST 데이터셋을 불러올 수 있음
- `root` 매개변수: 다운로드된 데이터가 저장될 위치
- `train` 매개변수: 훈련 데이터를 다운로드할지, 테스트 데이터를 다운로드할지를 결정
  - True이면 훈련 데이터를, False이면 테스트 데이터를 다운로드함
  - 기본값: True
- `download` 매개변수: True로 지정하면 원격에 저장된 데이터를 다운로드하여 로컬에 저장함
  - 기본값: False

```py
type(fm_train.data)  # torch.Tensor
print(fm_train.data.shape, fm_test.data.shape)
# torch.Size([60000, 28, 28]) torch.Size([10000, 28, 28])
```

- 입력 데이터는 fm_train, fm_test 객체의 `data` 속성에 파이토치 텐서(PyTorch Tensor)로 저장됨
  - 텐서(Tensor): 파이토치의 기본 데이터 구조로 넘파이 배열과 비슷한 인터페이스를 제공함
- torch.Size: 텐서의 크기를 나타내는 튜플과 유사한 객체

```py
print(fm_train.targets.shape, fm_test.targets.shape)
# torch.Size([60000]) torch.Size([10000])
```

- 타깃 데이터는 fm_train, fm_test 객체의 `targets` 속성에 저장됨
- 타깃이 1차원 배열이므로 원-핫 인코딩이 아니라 정숫값이라는 것을 짐작할 수 있음

#### 2. 입력 데이터와 타깃 데이터를 준비한 후 표준화하자

```py
train_input = fm_train.data
train_target = fm_train.targets

train_scaled = train_input / 255.0
```

- 파이토치 텐서도 넘파이 배열처럼 브로드캐스팅을 지원함

#### 3. 훈련 세트에서 검증 세트를 나누자

```py
from sklearn.model_selection import train_test_split

train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)

print(train_scaled.shape, val_scaled.shape)
# torch.Size([48000, 28, 28]) torch.Size([12000, 28, 28])
```

#### 4. 심층 신경망 모델을 만들자

```py
import torch.nn as nn

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 100),
    nn.ReLU(),
    nn.Linear(100, 10)
)
```

- Sequential 클래스를 호출할 때 필요한 층을 차례로 나열하면 됨

##### 🔹 케라스 모델과 파이토치 모델의 차이점

1. 파이토치에서는 모델의 입력 크기를 사전에 지정할 필요가 없음

   - 따라서, 케라스의 Input()과 같은 별도의 입력 정의 함수가 없음

2. 파이토치의 Linear 층이 케라스의 Dense 층과 동일한 역할을 함

   - Linear 층을 사용할 때는 입력 크기와 출력 크기(뉴런 개수)를 매개변수로 전달해야 함

3. 파이토치에서는 활성화 함수를 별도의 층으로 추가해야 함
4. 출력층에 해당하는 두 번째 Linear 층 다음에는 활성화 함수가 없음

#### 5. 모델의 정보를 확인해보자

```py
from torchinfo import summary

summary(model, input_size=(32, 28, 28))
```

<img src='./pytorch_dnn_summary.png' alt='파이토치로 만든 심층 신경망 모델에 대한 정보' width='550px' />

- 파이토치는 케라스의 summary() 메서드와 같이 전체 구조를 확인하는 도구를 제공하지 않음
- 대신, `torchinfo` 패키지의 summary() 함수를 사용하면 비슷한 결과를 얻을 수 있음
- `input_size` 매개변수: 입력 크기 지정

#### 6. 모델을 GPU에 적재하자

```py
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

- 케라스의 경우 GPU가 감지되면 자동으로 모델을 GPU에서 훈련하지만, 파이토치는 명시적으로 GPU로 모델을 이동해야 함
  - 그렇지 않으면 CPU를 사용하게 되어 훈련 속도가 느려질 수 있음
- `torch.cuda.is_available()` 함수: 시스템에 GPU가 있는 경우 True, 그렇지 않으면 False를 반환함

#### 7. 심층 신경망 모델을 컴파일하자

```py
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())
```

- `CrossEntropyLoss` 클래스: 다중 분류를 위한 크로스 엔트로피 손실 함수
- torch.optim 패키지 아래 Adam을 비롯한 다양한 옵티마이저 클래스가 있음
- CrossEntropyLoss 클래스에 소프트맥스 함수가 포함되어 있음
  - CrossEntropyLoss 클래스는 소프트맥스 함수 계산과 크로스 엔트로피 계산을 하나의 연산으로 합쳐 효율적으로 계산함
  - 따라서, 다중 분류 문제를 다룰 때 파이토치 모델의 마지막에 소프트맥스 함수를 추가할 필요가 없음

```py
for params in model.parameters():
    print(params.shape)
"""
torch.Size([100, 784]) 👈 첫 번째 Linear 층의 가중치
torch.Size([100])      👈 첫 번째 Linear 층의 절편
torch.Size([10, 100])  👈 두 번째 Linear 층의 가중치
torch.Size([10])       👈 두 번째 Linear 층의 절편
"""
```

- 옵티마이저를 만들 때 훈련 과정에서 최적화시킬 파이토치 텐서를 전달해야 함
- `parameters()` 메서드: 훈련 가능한 모든 모델 파라미터를 전달

#### 8. 심층 신경망 모델을 훈련하자

```
for 에포크 반복
    에포크 손실 초기화
    for 배치 반복
        배치 입력과 타깃 준비
        옵티마이저 그레이디언트 초기화
        모델에 입력 전달
        모델 출력과 타깃으로 손실 계산
        손실 역전파
        모델 파라미터 업데이트
        에포크 손실 기록
    에포크 손실 출력
```

- 파이토치에는 케라스와 같은 fit() 메서드가 없기 때문에, 에포크와 배치 경사 하강법을 위한 for문을 직접 구현해야 함
- 그레이디언트는 손실 함수라는 산에서 내려가야 할 방향과 크기를 알려주는 값임
- 순전파(forward propagation, 정방향 계산): 배치를 모델에 전달하여 출력을 생성하고 출력과 타깃을 손실 함수에 전달해 손실을 계산하는 과정
- 역전파(backward propagation): 손실을 모델의 출력층에서부터 입력층 방향으로 거꾸로 전달하여 각 층의 모델 파라미터에 대한 그레이디언트를 계산하는 과정
- 옵티마이저 객체는 계산된 그레이디언트를 사용해 손실 함수가 감소되는 방향으로 모델 파라미터를 업데이트함

```py
epochs = 5
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
    print(f"에포크:{epoch + 1}, 손실:{train_loss/batches:.4f}")

"""
에포크:1, 손실:0.5428
에포크:2, 손실:0.4004
에포크:3, 손실:0.3594
에포크:4, 손실:0.3320
에포크:5, 손실:0.3119
"""
```

- `train()` 메서드: 모델을 훈련 모드로 설정함
- criterion이 반환하는 값은 배치에 있는 샘플에 대한 손실의 합이 아니라 평균임
- `backward()` 메서드: 모델 파라미터에 대한 그레이디언트를 계산
- `step()` 메서드: 그레이디언트를 기반으로 모델 파라미터를 업데이트
- `item()` 메서드: 텐서가 배열이 아니라 단일값(스칼라)을 가진 경우 이를 파이썬 타입으로 변환해줌

#### 9. 검증 세트를 통해 모델을 평가해보자

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
# 검증 정확도: 0.8719
```

- `eval()` 메서드: 모델을 평가 모드로 설정함
- 파이썬 with 문으로 `torch.no_grad()`를 호출해 그레이디언트 계산을 하지 않는다고 알려줌
- 각 샘플마다 가장 큰 값의 인덱스를 추출하면 이것이 예측 클래스가 됨
- 케라스로 만든 모델과 비슷하게 87% 정도의 정확도를 얻음
