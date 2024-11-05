from ultralytics import YOLO

model = YOLO("yolo11n.pt")
results = model('./explorer.jpg', save=True)