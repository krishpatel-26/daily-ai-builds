from pathlib import Path
from typing import Any
import numpy as np
from PIL import Image
from app.policy import Detection

def load_image_rgb(uploaded_file: Any) -> np.ndarray:
    return np.asarray(Image.open(uploaded_file).convert("RGB"))

def run_yolo_inference(image_rgb: np.ndarray, model_path: str, confidence: float):
    path = Path(model_path)
    if not path.is_file():
        raise FileNotFoundError(
            f"Model weights not found at '{model_path}'. Train or provide a custom defect model."
        )
    from ultralytics import YOLO
    result = YOLO(str(path)).predict(source=image_rgb, conf=confidence, verbose=False)[0]
    names = result.names
    detections = []
    if result.boxes is not None:
        for box in result.boxes:
            cls_id = int(box.cls.item())
            x1, y1, x2, y2 = [float(v) for v in box.xyxy[0].tolist()]
            detections.append(Detection(str(names.get(cls_id, cls_id)), float(box.conf.item()),
                                         x1, y1, x2, y2))
    return detections, result.plot()[:, :, ::-1].copy()
