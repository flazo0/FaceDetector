import os
import time
import cv2

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def timestamp():
    return time.strftime("%Y%m%d-%H%M%S")

def save_screenshot(frame, out_dir="outputs/screenshots"):
    ensure_dir(out_dir)
    file_path = os.path.join(out_dir, f"shot-{timestamp()}.png")
    cv2.imwrite(file_path, frame)
    return file_path

class VideoRecorder:
    def __init__(self):
        self.writer = None
        self.active = False
        self.path = None

    def start(self, frame_shape, fps=25.0, out_dir="outputs/recordings"):
        ensure_dir(out_dir)
        h, w = frame_shape[:2]
        self.path = os.path.join(out_dir, f"rec-{timestamp()}.mp4")

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.writer = cv2.VideoWriter(self.path, fourcc, fps, (w, h))
        if not self.writer.isOpened():
            raise RuntimeError("Could not start video writer")

        self.active = True
        return self.path

    def write(self, frame):
        if self.active and self.writer is not None:
            self.writer.write(frame)

    def stop(self):
        if self.writer is not None:
            self.writer.release()
        self.writer = None
        self.active = False
        return self.path
