import cv2

class Camera:
    def __init__(self, index: int = 0, width=None, height=None):
        self.index = index
        self.cap = cv2.VideoCapture(index)
        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open camera index {index}")

        if width is not None:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(width))
        if height is not None:
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height))

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()

    def switch(self, new_index: int, width=None, height=None):
        self.release()
        self.index = new_index
        self.cap = cv2.VideoCapture(new_index)
        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open camera index {new_index}")

        if width is not None:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(width))
        if height is not None:
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height))
