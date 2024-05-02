import cv2
from ultralytics import YOLO
import supervision as sv

# load a pre-trained or custom-trained model
model = YOLO('models\model_v1.1.pt')

# read an image
image = cv2.imread("images\IMG_0171.JPEG")
result = model(image)[0]



for result in model.track(source=0, show=True, stream=True):
    frame = result.orig_image

    # parse detections
    detections = sv.Detections.from_yolov8(result)

    if result.boxes.id is not None:
        detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)

    detections = detections[detections.class_id == 0]

    cv2.imshow('yolov8', frame)


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break