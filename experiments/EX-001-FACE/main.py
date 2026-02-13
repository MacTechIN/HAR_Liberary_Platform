import cv2
import numpy as np
from core.base.processor import BaseProcessor

class FaceDetector(BaseProcessor):
    """
    Experimental class for face detection using Haar Cascades.
    
    This class demonstrates how to extend BaseProcessor for a specific
    computer vision task.
    """

    def __init__(self, cascade_path: str = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'):
        """
        Initialize the face detector with a Haar Cascade classifier.
        
        Args:
            cascade_path (str): Path to the Haar Cascade XML file.
        """
        super().__init__(name="FaceDetector")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        if self.face_cascade.empty():
            print(f"Error: Could not load cascade from {cascade_path}")

    def process(self, frame: np.ndarray) -> np.ndarray:
        """
        Detect faces in the frame and draw bounding boxes.
        
        Args:
            frame (np.ndarray): The input BGR frame.
            
        Returns:
            np.ndarray: The frame with detected faces highlighted.
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        return frame

def run_experiment():
    """
    Main loop for the face detection experiment.
    """
    detector = FaceDetector()
    cap = cv2.VideoCapture(0) # Open default camera

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting experiment. Press 'q' to quit.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            processed_frame = detector.process(frame)
            detector.display("EX-001-FACE", processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        detector.release()

if __name__ == "__main__":
    run_experiment()
