import pytest
import numpy as np
import cv2
import os
from experiments.EX_001_FACE.main import FaceDetector

# Note: The directory name in the file path was EX-001-FACE, 
# but python imports usually prefer underscores. 
# Checking current directory structure and adjusting as needed.

def test_face_detector_initialization():
    """
    Test if any error occurs when initializing FaceDetector.
    """
    try:
        detector = FaceDetector()
        assert detector.name == "FaceDetector"
        # Verify if cascade is loaded (might be empty if path is wrong, but shouldn't crash)
        assert hasattr(detector, 'face_cascade')
    except Exception as e:
        pytest.fail(f"Initialization failed: {e}")

def test_face_detector_process(face_frame):
    """
    Test the process method with a sample frame.
    We check if the output is still an image of the same shape.
    """
    detector = FaceDetector()
    processed_frame = detector.process(face_frame)
    
    assert processed_frame is not None
    assert processed_frame.shape == face_frame.shape
    assert isinstance(processed_frame, np.ndarray)

def test_face_detector_logic_with_blank_image():
    """
    Ensure the detector doesn't crash on an empty (black) image.
    """
    blank = np.zeros((100, 100, 3), dtype=np.uint8)
    detector = FaceDetector()
    try:
        processed = detector.process(blank)
        assert np.array_equal(processed, blank) # Should be unchanged if no faces
    except Exception as e:
        pytest.fail(f"Process failed on blank image: {e}")
