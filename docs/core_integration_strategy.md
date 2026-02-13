# Core Module Integration & Environment Setup Strategy

이 문서는 OpenCV 및 Deep Learning 실험 환경에서 공통 모듈(`core/`)을 효율적으로 활용하고 각 실험의 독립성을 유지하기 위한 전략을 기술합니다.

---

## 1. 개조 가능한 설치 아키텍처 (Editable Install Architecture)

### 1단계: 가상환경별 의존성 설치
각 실험 폴더(`experiments/`) 내부의 가상환경에 필요한 패키지를 독립적으로 설치합니다.
- **명령어**: `pip install opencv-python pillow`
- **목적**: 실험 단위별로 최적화된 엔진 버전을 유지하여 시스템 전체의 안정성을 보장합니다.

### 2단계: 프로젝트 '개발 모드(Editable Mode)' 설정
프로젝트 루트에 `pyproject.toml`을 설정하여 `core` 폴더를 로컬 패키지로 등록합니다.
- **설정 파일**: `pyproject.toml`
- **적용 방법**: `pip install -e .`
- **이점**: `sys.path.append()`와 같은 불필요한 코드 없이 어디서든 `import core` 호출이 가능해집니다.

### 3단계: 공통 모듈 패키지화 (Package Initialization)
파이썬이 폴더를 패키지로 인식할 수 있도록 각 디렉토리에 `__init__.py`를 구성합니다.
- `core/__init__.py`
- `core/base/__init__.py`
- `core/processing/__init__.py`

---

## 2. 코드 활용 가이드 (Usage Guide)

`core/` 폴더에 작성된 로직을 실험 코드에서 불러올 때의 표준 규격입니다.

```python
# experiments/some-experiment/main.py

import cv2
from core.base.processor import BaseProcessor  # 공통 모듈 호출

class CustomDetector(BaseProcessor):
    def process(self, frame):
        # core의 기능을 상속받아 고유 로직 구현
        pass
```

---

## 3. 기대 효과 (Expected Benefits)

1. **환경 독립성**: 실험 A의 요구사항이 실험 B의 환경을 파괴하지 않음.
2. **코드 재사용성**: 검증된 OpenCV 전처리 로직을 `core/`에서 중앙 관리.
3. **배포 용이성**: `requirements.txt`와 `pyproject.toml`만으로 동일 환경 즉시 구축 가능.

---

## 업데이트 기록
- 2026-02-12 21:18: 통합 전략 문서 초안 작성 및 저장
