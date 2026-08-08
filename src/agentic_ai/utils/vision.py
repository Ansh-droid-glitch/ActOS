from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("image.jpg")

for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        label = model.names[class_id]

        print(label, confidence, center_x, center_y)