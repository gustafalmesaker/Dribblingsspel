#sports
from ultralytics import YOLO
import cv2

ov_model = YOLO('models\model_v1.1_openvino_model/',task="detect") #load openvino model

cap = cv2.VideoCapture(1)
ret = True

class tracking:
    def __init__(self):
        self.circle_points = []

    #find where sports balls are located (id 32)
    def center_points(results):
        box_list = []
        sports_ball_id = 32

        if results[0].boxes.xyxy is not None:
            for obj in results[0].boxes:
                if obj.cls == sports_ball_id:
                    x_n, y_n, w, h = obj.xywhn[0].tolist()
                    box_list.append([x_n, y_n])
        return box_list
        

    def update_pos(dt):
        ret, frame = cap.read()

        frame = cv2.resize(frame , (1420 , 800), interpolation=cv2.INTER_LINEAR)
        results = ov_model.track(frame, persist=True)
        if results[0] is not None:
            self.circle_centers = center_points(results=results) 

