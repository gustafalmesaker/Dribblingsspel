from ultralytics import YOLO 
import cv2 
import pyglet 

def initialize_variables():
    # Initialize your variables here
    ov_model = YOLO('models\model_v1.1_openvino_model/',task="detect") #load openvino model
    cap = cv2.VideoCapture(1)
    ret = True
    window = pyglet.window.Window(width=640, height=640)
    last_known_pos = [0 , 0]
    return ov_model, cap, ret, window, last_known_pos


def main(ov_model, cap, ret, window, last_known_pos):
    while ret:
        if ret:
            ret, frame = cap.read()
            results = ov_model.track(frame, persist=True)
            frame_ = results[0].plot()
            
            cv2.imshow('frame', frame_)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break 



if __name__ == "__main__":
    ov_model, cap, ret, window, last_known_pos = initialize_variables()
    main(ov_model, cap, ret, window, last_known_pos)