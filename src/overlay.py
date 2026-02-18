import cv2
import time

class FPSCounter:
    def __init__(self):
        self.last = time.time()
        self.fps = 0.0

    def tick(self):
        now = time.time()
        dt = now - self.last
        self.last = now
        if dt > 0:
            self.fps = 1.0 / dt
        return self.fps

def draw_faces(frame, faces, color=(255, 255, 255)):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

def draw_hud(frame, text_lines):
    y = 24
    for line in text_lines:
        cv2.putText(
            frame,
            line,
            (14, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (220, 220, 220),
            2,
            cv2.LINE_AA,
        )
        y += 22
