from ultralytics import YOLO
import cv2

model = YOLO("..\models\model_v1.1.pt",task="detect") #load created model
ov_model = YOLO("..\models\model_v1.1_openvino_model/",task="detect") #load openvino model
#model = YOLO("yolov8n.pt") #load pretrained model

cap = cv2.VideoCapture(0) #test with live camera
#cap = cv2.VideoCapture(1) #test with live webcamera
ret = True

while ret:
    ret, frame = cap.read()
    results = model.track(frame, persist=True)
    frame_ = results[0].plot()

    cv2.imshow('frame', frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# After the loop release the cap object 
cap.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 