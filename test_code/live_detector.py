from ultralytics import YOLO
import cv2


import openvino.properties as props
import openvino.properties.hint as hints


model = YOLO("models\model_v1.1.pt",task="detect") #load created model
ov_model = YOLO('models\model_v1.1_openvino_model/',task="detect") #load openvino model
#model = YOLO("yolov8n.pt") #load pretrained model

#config = {hints.performance_mode: hints.PerformanceMode.THROUGHPUT}
#compiled_model = core.compile_model(model, "GPU", config)


video_path = "videos\Test_ball_detection_2.mp4"
#video_path = "videos\Test_ball_detection.gif"

cap = cv2.VideoCapture(1)

#cap = cv2.VideoCapture(0) #test with live camera
#cap = cv2.VideoCapture(1) #test with live webcamera
ret = True

while ret:
    if ret:
        ret, frame = cap.read()
        frame = cv2.resize(frame , (640 , 640), interpolation=cv2.INTER_LINEAR)
        #results = compiled_model.track(frame, persist=True)
        results = ov_model.track(frame, persist=True)
        #results = model.track(frame, persist=True)

        frame_ = results[0].plot()


        
        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# After the loop release the cap object 
cap.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 