from ultralytics import YOLO
import cv2


model = YOLO("models\model_v1.1.pt") #load created model
#model = YOLO("yolov8n.pt") #load pretrained model

#video_path = "videos\Test_ball_detection_2.mp4"
#video_path = "videos\Test_ball_detection.gif"

#cap = cv2.VideoCapture(video_path)

cap = cv2.VideoCapture(0) #test with live camera
ret = True

while ret:
    if ret:
        ret, frame = cap.read()

        results = model.track(frame, persist=True)
        frame_ = results[0].plot()


        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

