import pytest
import numpy as np
import cv2

@pytest.fixture
def sample_bgr_frame():
    """
    Generate a sample 100x100 BGR frame (all blue).
    """
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame[:, :, 0] = 255 # Set blue channel
    return frame

@pytest.fixture
def face_frame():
    """
    Generate a frame with a white rectangle that could be interpreted
    as a simple face-like object for basic processing verification.
    """
    frame = np.zeros((200, 200, 3), dtype=np.uint8)
    # Draw a white rectangle in the middle
    cv2.rectangle(frame, (50, 50), (150, 150), (255, 255, 255), -1)
    return frame
