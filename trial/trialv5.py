import cv2
import torch

# Load YOLOv5 model (you can choose other versions like 'yolov5s', 'yolov5m', 'yolov5l', etc.)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

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

    # Perform object detection using YOLOv5
    results = model(frame)  # YOLOv5 model inference

    # Extract results
    labels, coords = results.xyxy[0][:, -1], results.xyxy[0][:, :-1]  # labels and bounding boxes

    # Annotate the frame with bounding boxes and labels
    for label, box in zip(labels, coords):
        x1, y1, x2, y2, conf = box  # Unpack bounding box coordinates and confidence
        # Convert to int for pixel values
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        # Draw the rectangle and label on the frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'{model.names[int(label)]} {conf:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Display the resulting frame
    cv2.imshow('YOLOv5 Object Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
