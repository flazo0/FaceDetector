import argparse
import cv2

from src.config import DetectorConfig, AppConfig
from src.detector import FaceDetector
from src.camera import Camera
from src.overlay import FPSCounter, draw_faces, draw_hud
from src.utils import save_screenshot, VideoRecorder

def parse_args():
    p = argparse.ArgumentParser(description="Real-time face detector (Haar Cascade)")
    p.add_argument("--camera", type=int, default=0, help="Camera index (default: 0)")
    p.add_argument("--width", type=int, default=960, help="Capture width")
    p.add_argument("--height", type=int, default=540, help="Capture height")
    p.add_argument("--cascade", type=str, default="models/haarcascade_frontalface_default.xml", help="Path to Haar cascade XML")
    p.add_argument("--scale", type=float, default=1.1, help="detectMultiScale scaleFactor")
    p.add_argument("--neighbors", type=int, default=5, help="detectMultiScale minNeighbors")
    p.add_argument("--minsize", type=int, nargs=2, default=[30, 30], help="Minimum face size (w h)")
    p.add_argument("--no-mirror", action="store_true", help="Disable mirror mode")
    p.add_argument("--no-fps", action="store_true", help="Disable FPS display")
    p.add_argument("--strict", action="store_true", help="Stricter detection (reduces false positives)")
    return p.parse_args()

def main():
    args = parse_args()

    det_cfg = DetectorConfig(
        cascade_path=args.cascade,
        scale_factor=args.scale,
        min_neighbors=args.neighbors,
        min_size=(args.minsize[0], args.minsize[1]),
    )

    if args.strict:
        det_cfg.min_neighbors = max(det_cfg.min_neighbors, 7)
        det_cfg.min_size = (max(det_cfg.min_size[0], 40), max(det_cfg.min_size[1], 40))

    app_cfg = AppConfig(
        camera_index=args.camera,
        width=args.width,
        height=args.height,
        mirror=not args.no_mirror,
        show_fps=not args.no_fps,
        window_name="Face Detector",
    )

    detector = FaceDetector(det_cfg)
    cam = Camera(app_cfg.camera_index, width=app_cfg.width, height=app_cfg.height)
    fps = FPSCounter()
    recorder = VideoRecorder()

    cv2.namedWindow(app_cfg.window_name, cv2.WINDOW_NORMAL)

    show_hud = True
    camera_index = app_cfg.camera_index

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        if app_cfg.mirror:
            frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detect(gray)

        draw_faces(frame, faces, color=(240, 240, 240))

        fps_val = fps.tick()
        if show_hud:
            hud = [
                f"Faces: {len(faces)}",
                f"FPS: {fps_val:.1f}" if app_cfg.show_fps else "FPS: off",
                f"Mirror: {'on' if app_cfg.mirror else 'off'}",
                f"Recording: {'on' if recorder.active else 'off'}",
                "Keys: q quit | s shot | r rec | m mirror | c cam | h hud",
            ]
            draw_hud(frame, hud)

        if recorder.active:
            recorder.write(frame)

        cv2.imshow(app_cfg.window_name, frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("h"):
            show_hud = not show_hud
        elif key == ord("m"):
            app_cfg.mirror = not app_cfg.mirror
        elif key == ord("s"):
            path = save_screenshot(frame)
            print(f"[screenshot] saved: {path}")
        elif key == ord("r"):
            if recorder.active:
                out = recorder.stop()
                print(f"[recording] saved: {out}")
            else:
                out = recorder.start(frame.shape, fps=25.0)
                print(f"[recording] started: {out}")
        elif key == ord("c"):
            camera_index = (camera_index + 1) % 3
            try:
                cam.switch(camera_index, width=app_cfg.width, height=app_cfg.height)
                print(f"[camera] switched to index {camera_index}")
            except Exception as e:
                print(f"[camera] failed to switch: {e}")
                camera_index = app_cfg.camera_index
                cam.switch(camera_index, width=app_cfg.width, height=app_cfg.height)

    if recorder.active:
        recorder.stop()

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()