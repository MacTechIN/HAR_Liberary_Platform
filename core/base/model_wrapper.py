from abc import ABC, abstractmethod
import numpy as np
from typing import Any, List, Dict

class BaseModelWrapper(ABC):
    """
    Abstract base class for all Deep Learning model wrappers.
    
    Provides a standardized interface for loading models and
    performing inference across different frameworks (PyTorch, ONNX, etc.).
    """

    def __init__(self, model_path: str, config: Dict[str, Any] = None):
        """
        Initialize the model wrapper.
        
        Args:
            model_path (str): Path to the model weights file.
            config (Dict[str, Any], optional): Configuration parameters for the model.
        """
        self.model_path = model_path
        self.config = config or {}
        self.model = None
        self.load_model()

    @abstractmethod
    def load_model(self):
        """
        Load the model from the specified model_path.
        """
        pass

    @abstractmethod
    def predict(self, input_data: np.ndarray) -> Any:
        """
        Perform inference on the input data.
        
        Args:
            input_data (np.ndarray): The data to be processed by the model.
            
        Returns:
            Any: The raw prediction results from the model.
        """
        pass

    @abstractmethod
    def preprocess(self, frame: np.ndarray) -> np.ndarray:
        """
        Prepare the input frame for model inference.
        
        Args:
            frame (np.ndarray): The raw input frame.
            
        Returns:
            np.ndarray: The preprocessed data.
        """
        pass

    @abstractmethod
    def postprocess(self, prediction: Any) -> List[Dict[str, Any]]:
        """
        Convert raw predictions into a standardized format.
        
        Args:
            prediction (Any): The raw prediction results.
            
        Returns:
            List[Dict[str, Any]]: List of detection results (e.g., boxes, labels, scores).
        """
        pass
