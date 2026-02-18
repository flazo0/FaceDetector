from dataclasses import dataclass

@dataclass
class DetectorConfig:
    cascade_path: str = "models/haarcascade_frontalface_default.xml"
    scale_factor: float = 1.1
    min_neighbors: int = 5
    min_size: tuple[int, int] = (30, 30)

@dataclass
class AppConfig:
    camera_index: int = 0
    width: int | None = 960
    height: int | None = 540
    mirror: bool = True
    show_fps: bool = True
    window_name: str = "Face Detector"
