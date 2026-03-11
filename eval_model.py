
from ultralytics import YOLO

model = YOLO("C:/Dhanya/PythonCourse2526/MachineLearning/10Mar2026/yolo-lab/runs/detect/train9/weights/best.pt")
model.predict(source=0, show=True)
model.val(data="data/annotated/data.yaml")