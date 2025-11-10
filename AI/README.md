# 📚 AI

## 📃 목록

### 1. 나의 첫 머신러닝

- [인공지능과 머신러닝, 딥러닝](./ai.md)
  - 인공지능이란
  - 머신러닝이란
  - 딥러닝이란
- [코랩과 주피터 노트북](./colab.md)
  - 구글 코랩
  - 텍스트 셀
  - 코드 셀
  - 노트북
- [마켓과 머신러닝](./machine_learing.md)
  - 생선 분류 문제
  - 첫 번째 머신러닝 프로그램
  - cf) 핵심 패키지와 함수
    - matplotlib
    - scikit-learn

### 2. 데이터 다루기

- [훈련 세트와 테스트 세트](./train_test_set.md)
  - 지도 학습과 비지도 학습
  - 훈련 세트와 테스트 세트
  - 샘플링 편향
  - 넘파이
  - 두 번째 머신러닝 프로그램
  - cf) 핵심 패키지와 함수
    - numpy
- [데이터 전처리](./data-preprocessing.md)
  - 넘파이로 데이터 준비하기
  - 사이킷런으로 훈련 세트와 테스트 세트 나누기
  - 수상한 도미 한 마리
  - 기준을 맞춰라
  - 전처리 데이터로 모델 훈련하기
  - cf) 핵심 패키지와 함수
    - scikit-learn

### 3. 회귀 알고리즘과 모델 규제

- [k-최근접 이웃 회귀](./k-neighbors-regression.md)
  - k-최근접 이웃 회귀
  - 데이터 준비
  - 결정계수(R²)
  - 과대적합 vs 과소적합
  - cf) 핵심 패키지와 함수
    - scikit-learn
    - numpy
- [선형 회귀](./linear_regression.md)
  - k-최근접 이웃의 한계
  - 선형 회귀
  - 다항 회귀
  - cf) 핵심 패키지와 함수
    - scikit-learn
- [특성 공학과 규제](./feature.md)
  - 다중 회귀
  - 데이터 준비
  - 사이킷런의 변환기
  - 다중 회귀 모델 훈련하기
  - 규제
  - 릿지 회귀
  - 라쏘 회귀
  - cf) 핵심 패키지와 함수
    - pandas
    - scikit-learn

### 4. 다양한 분류 알고리즘

- [로지스틱 회귀](./logistic_regression.md)
  - 럭키백의 확률
  - 로지스틱 회귀
  - cf) 핵심 패키지와 함수
    - scikit-learn
- [확률적 경사 하강법](./gradient_descent.md)
  - 점진적인 학습
  - SGDClassifier
  - 에포크와 과대/과소적합
  - cf) 핵심 패키지와 함수
    - scikit-learn

### 5. 트리 알고리즘

- [결정 트리](./decision_tree.md)
  - 로지스틱 회귀로 와인 분류하기
  - 결정 트리
  - cf) 핵심 패키지와 함수
    - pandas
    - scikit-learn
- [교차 검증과 그리드 서치](./cross_validation.md)
  - 검증 세트
  - 교차 검증
  - 하이퍼파라미터 튜닝
  - cf) 핵심 패키지와 함수
    - scikit-learn
- [트리의 앙상블](./tree_ensemble.md)
  - 정형 데이터와 비정형 데이터
  - 랜덤 포레스트
  - 엑스트라 트리
  - 그레디언트 부스팅
  - 히스토그램 기반 그레디언트 부스팅
  - cf) 핵심 패키지와 함수
    - scikit-learn

### 6. 비지도 학습

- [군집 알고리즘](./cluster.md)
  - 타깃을 모르는 비지도 학습
  - 과일 사진 데이터 준비하기
  - 픽셀값 분석하기
  - 평균값과 가까운 사진 고르기
- [k-평균](./k_mean.md)
  - k-평균 알고리즘 소개
  - kMeans 클래스
  - 클러스터 중심
  - 최적의 k 찾기
  - cf) 핵심 패키지와 함수
    - scikit-learn
- [주성분 분석](./principle_component.md)
  - 차원과 차원 축소
  - 주성분 분석 소개
  - PCA 클래스
  - 원본 데이터 재구성
  - 설명된 분산
  - 다른 알고리즘과 함께 사용하기
  - cf) 핵심 패키지와 함수
    - scikit-learn

### 7. 딥러닝

- [인공 신경망](./ann.md)
  - 패션 MNIST
  - 로지스틱 회귀로 패션 아이템 분류하기
  - 인공 신경망
  - 인공 신경망으로 모델 만들기
  - 인공 신경망으로 패션 아이템 분류하기
  - cf) 핵심 패키지와 함수
    - Keras
- [심층 신경망](./dnn.md)
  - 2개의 층
  - 심층 신경망 만들기
  - 층을 추가하는 다른 방법
  - 렐루 함수
  - 옵티마이저
  - cf) 핵심 패키지와 함수
    - Keras
- [➕ 파이토치로 신경망 모델 만들기](./ann_made_by_pytorch.md)
- [신경망 모델 훈련](./fit_neural_network.md)
  - 손실 곡선
  - 검증 손실
  - 드롭아웃
  - 모델 저장과 복원
  - 콜백
  - cf) 핵심 패키지와 함수
    - Keras
    - NumPy
- [➕ 파이토치로 신경망 모델 훈련하기](./ann_fit_by_pytorch.md)

### 8. 합성곱 신경망

- [합성곱 신경망의 구성 요소](./cnn.md)
  - 합성곱
  - 케라스 합성곱 층
  - 합성곱 신경망의 전체 구조
- [합성곱 신경망을 사용한 이미지 분류](./classification_by_cnn.md)
  - 패션 MNIST 데이터 불러오기
  - 합성곱 신경망 만들기
  - 모델 컴파일과 훈련
  - cf) 핵심 패키지와 함수
    - Keras
    - matplotlib
- [➕ 파이토치로 합성곱 신경망 모델 훈련하기](./cnn_by_pytorch.md)
- [합성곱 신경망의 시각화](./cnn_visualization.md)
  - 가중치 시각화
  - 함수형 API
  - 특성 맵 시각화
  - cf) 핵심 패키지와 함수
    - Keras

## 🔎 참고자료

- 혼자 공부하는 머신러닝+딥러닝
