import cv2
from ultralytics import YOLO

# Load YOLOv8 model (YOLOv8n is the nano version, faster for real-time detection)
model = YOLO('yolov8n.pt')  # You can use other models like 'yolov8s.pt', 'yolov8m.pt', etc.

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Perform object detection using YOLOv8
    results = model(frame)

    # Draw bounding boxes and labels on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame with bounding boxes and labels
    cv2.imshow('YOLOv8 Object Detection', annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()