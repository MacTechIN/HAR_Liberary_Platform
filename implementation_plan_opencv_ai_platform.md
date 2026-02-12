# OpenCV + AI Modular Platform Implementation Plan

## 1. 개요 (Overview)
OpenCV와 Deep Learning 기술을 체계적으로 실험, 보관 및 재사용하기 위한 모듈형 플랫폼 설계안입니다. 이 플랫폼은 신규 프로젝트에 기술을 신속하게 도입할 수 있도록 **확장성, 개방성, 재사용성**을 핵심 가치로 합니다.

---

## 2. 핵심 설계 원칙 (Core Principles)
- **Modularization (모듈화)**: 기능별로 코드를 분리하여 다른 프로젝트로의 이식이 용이함.
- **Traceability (추적성)**: 실험 환경, 데이터, 결과(메트릭)를 한눈에 파악할 수 있도록 기록.
- **Interchangeability (교체성)**: 인터페이스 추상화를 통해 모델(YOLO, MediaPipe, SSD 등)을 쉽게 교체 가능.

---

## 3. 디렉토리 구조 (Directory Structure)
```bash
VisionAI-Platform/
├── core/                # 재사용 가능한 핵심 모듈 (Library)
│   ├── base/            # 인터페이스 및 추상 클래스
│   │   ├── processor.py # 모든 영상 처리의 공통 부모 클래스
│   │   └── model_wrapper.py
│   ├── processing/      # 전처리 및 후처리 (Filter, ROI, Augmentation)
│   └── models/          # 개별 엔진 래퍼 (YOLOv8, MediaPipe, etc.)
├── experiments/         # 기술 검증 및 실험 로깅
│   ├── EX-001-FACE/     # 얼굴 인식 테스트 폴더
│   │   ├── main.py      # 실험 실행 코드
│   │   ├── results/     # 로그, 스크린샷, 벤치마킹 데이터
│   │   └── report.md    # 실험 결과 분석 및 특이사항
├── assets/              # 공유 자원
│   ├── weights/         # 모델 가중치 파일 (.onnx, .pt, .pb)
│   └── configs/         # 모델 설정 파일 (.yaml, .json)
├── examples/            # 신규 프로젝트 적용을 위한 레퍼런스 코드
└── docs/                # 기술 검색을 위한 문서화 (Tags, How-to)
```

---

## 4. 상세 구현 전략

### ① 추상화 계층 구축 (Core Library)
객체 지향 프로그래밍(OOP)을 활용하여 표준 인터페이스를 정의합니다.
- `BaseComputerVision`: 이미지 읽기, 쓰기, 결과 렌더링을 담당.
- `DeepLearningModel`: 다양한 프레임워크(PyTorch, TensorFlow, ONNX)의 모델을 동일한 방식으로 호출.

### ② 실험 규격화 (Standardized Experiments)
모든 실험은 `report.md`를 포함하며 다음 내용을 기록합니다.
- **Environment**: OS, GPU, OpenCV/Framework 버전
- **Performance**: FPS, Latency, Accuracy
- **Tags**: `#ObjectDetection`, `#Face`, `#Realtime`, `#LowMemory`

### ③ 검색 및 지식 축적 (Knowledge Management)
- **마크다운 기반 문서화**: `grep` 또는 문서 검색 도구를 통해 필요한 코드를 즉시 검색.
- **코드 스니펫 관리**: 자주 쓰이는 `OpenCV` 유틸리티(예: 투영 변환, 투명 오버레이 레이어 등)를 `core/processing`에 정규화.

---

## 5. 단계별 실행 로드맵 (Roadmap)
1. **Phase 1: Foundation (기초 구축)**
   - 디렉토리 구조 설정 및 `Base` 인터페이스 정의.
2. **Phase 2: Core Module (핵심 구현)**
   - OpenCV DNN 모듈을 활용한 범용 추론 엔진 구현.
3. **Phase 3: Experiment & Logging (축적)**
   - 기존 진행했던 기술들을 `experiments/` 폴더로 이관 및 규격화.
4. **Phase 4: Optimization (고도화)**
   - 멀티스레딩, 가속기(TensorRT, OpenVINO) 지원 추가.
