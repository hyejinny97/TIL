## 📕 도서 [혼자 만들면서 공부하는 딥러닝]

### 1. 합성곱 신경망(CNN)으로 패션 상품 이미지 분류하기

- [딥러닝 개발환경 구축하기](./start.md)
  - 딥러닝을 위한 준비물, 구글 코랩
  - 코랩의 화면 구성
  - 코랩으로 실습 준비하기
- [합성곱 신경망(CNN) 모델 이해하기](./cnn.md)
  - 최초의 CNN 모델 - LeNet
  - 합성곱층 - Conv2D
  - 풀링층과 밀집층 - AveragePooling2D, Dense
- [패션 상품 이미지 분류하기](./classify_fashion_product.md)
  - LeNet 모델 만들기
  - LeNet 모델 훈련하기

### 2. 사전 훈련된 CNN 모델로 강아지와 고양이 사진 분류하기

- [이미지 분류 CNN 모델 만들기](./cnn_iamge_classification.md)
  - 이미지넷 대회에서 우승한 최초의 CNN 모델 - AlexNet
  - 사전 훈련된 CNN 모델 - VGGNet
- [강아지와 고양이 사진 분류하기](./classify_cat_dog.md)
  - VGGNet 모델 로드하기
  - 강아지와 고양이 사진 분류하기
- [강아지와 고양이 사진 분류 모델의 성능 개선하기](./improve_performance.md)
  - 훈련 성능을 높이는 CNN 모델 - ResNet
  - ResNet 모델 만들기
  - 강아지와 고양이 사진 분류하기
  - cf) GoogLeNet

### 3. 고급 CNN 모델과 전이 학습으로 이미지 분류하기

- [이미지 분류 모델의 효율성 최적화하기](./cnn_optimization.md)
  - ResNet의 확장 모델 - DenseNet
  - 모바일 환경(경량) 모델 - MobileNet
- [이미지 분류 모델의 성능 최적화하기](./cnn_performance_optimization.md)
  - 가장 높은 성능을 내는 모델 - EfficientNet
  - EfficientNet 모델 만들기
  - EfficientNet 모델로 강아지 사진 분류하기
- [전이 학습으로 피스타치오 이미지 분류하기](./classfy_pistachio.md)
  - 텐서플로 허브로 강아지 사진 분류하기
  - 허깅페이스로 강아지 사진 분류하기
  - 전이 학습으로 피스타치오 품종 분류하기
  - cf) 캐글 모델로 피스타치오 품종 분류하기

### 4. 트랜스포머 인코더 모델로 텍스트 감성 분류하기

- [트랜스포머 인코더 모델 이해하기](./encoder.md)
  - 어텐션 메커니즘
  - 위치 인코딩과 층 정규화
  - 트랜스포머 인코더 모델 만들기
- [전이 학습으로 영화 리뷰 텍스트의 감성 분류하기](./classify_movie_review.md)
  - 트랜스포머 인코더 기반 언어 이해 모델 - BERT
  - KerasNLP로 영화 리뷰 텍스트의 감성 분류하기
  - 허깅페이스로 영화 리뷰 텍스트의 감성 분류하기
  - cf) 미세 튜닝된 모델로 감성 분석하기
- [BERT 후속 모델로 영화 리뷰 텍스트의 감성 분류하기](./roberta_distilbert.md)
  - BERT의 성능 개선 모델 - RoBERTa
  - BERT의 경량화 모델 - DistilBERT
  - cf) KerasNLP로 DistilBERT 모델 만들기
