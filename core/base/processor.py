from abc import ABC, abstractmethod
import cv2
import numpy as np

class BaseProcessor(ABC):
    """
    Abstract base class for all image and video processors.
    
    This class defines the standard interface for processing frames
    in the VisionAI platform.
    """

    def __init__(self, name: str = "BaseProcessor"):
        """
        Initialize the processor.
        
        Args:
            name (str): The name of the processor instance.
        """
        self.name = name

    @abstractmethod
    def process(self, frame: np.ndarray) -> np.ndarray:
        """
        Process a single frame.
        
        Args:
            frame (np.ndarray): The input image frame (BGR format).
            
        Returns:
            np.ndarray: The processed image frame.
        """
        pass

    def display(self, window_name: str, frame: np.ndarray):
        """
        Display the frame in a window.
        
        Args:
            window_name (str): The name of the display window.
            frame (np.ndarray): The image frame to display.
        """
        cv2.imshow(window_name, frame)

    def release(self):
        """
        Release any resources held by the processor.
        """
        cv2.destroyAllWindows()
