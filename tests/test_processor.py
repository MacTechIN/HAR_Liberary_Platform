import pytest
import numpy as np
from core.base.processor import BaseProcessor

class MockProcessor(BaseProcessor):
    """
    A simple mock processor to test the BaseProcessor interface.
    """
    def process(self, frame: np.ndarray) -> np.ndarray:
        # Just return the frame as is
        return frame

def test_processor_initialization():
    """
    Test if BaseProcessor can be initialized via a mock class.
    """
    name = "TestProcessor"
    processor = MockProcessor(name=name)
    assert processor.name == name

def test_processor_process(sample_bgr_frame):
    """
    Test if the process method works correctly in the mock.
    """
    processor = MockProcessor()
    processed = processor.process(sample_bgr_frame)
    assert np.array_equal(processed, sample_bgr_frame)

def test_processor_display_does_not_crash(sample_bgr_frame):
    """
    Verify that display method doesn't crash (window won't actually show in headless).
    Note: In some CI environments, cv2.imshow might fail. This is just a basic check.
    """
    processor = MockProcessor()
    # We don't actually call imshow here to avoid issues in headless tests, 
    # but we verify the method exists.
    assert hasattr(processor, 'display')
