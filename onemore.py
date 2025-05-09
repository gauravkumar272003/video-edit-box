import cv2
import random
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

input_path = "2024.mp4"       # input video name
output_path = "d.mp4"     # Output video with name

# Open the input video
cap = cv2.VideoCapture(input_path)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

# Process each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]  # Perform detection on the frame

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        shape = random.choice(["rectangle", "circle", "triangle"])
        color = [random.randint(0, 255) for _ in range(3)]
        thickness = 2

        if shape == "rectangle":
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

        elif shape == "circle":
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            radius = min((x2 - x1) // 2, (y2 - y1) // 2)
            cv2.circle(frame, center, radius, color, thickness)

        elif shape == "triangle":
            pt1 = (x1, y2)
            pt2 = (x2, y2)
            pt3 = ((x1 + x2) // 2, y1)
            pts = [pt1, pt2, pt3]
            cv2.polylines(frame, [np.array(pts, dtype=np.int32)], isClosed=True, color=color, thickness=thickness)

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
