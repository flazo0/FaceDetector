import cv2
from .config import DetectorConfig

class FaceDetector:
    def __init__(self, cfg: DetectorConfig):
        self.cfg = cfg
        self.model = cv2.CascadeClassifier(cfg.cascade_path)
        if self.model.empty():
            raise FileNotFoundError(
                f"Could not load Haar cascade at: {cfg.cascade_path}. "
                "Make sure the file exists."
            )

    def detect(self, gray_frame):
        return self.model.detectMultiScale(
            gray_frame,
            scaleFactor=self.cfg.scale_factor,
            minNeighbors=self.cfg.min_neighbors,
            minSize=self.cfg.min_size,
        )
