#sports
from ultralytics import YOLO
import cv2

#game
import pyglet

window = pyglet.window.Window(width=640, height=640)


#detection model
#model = YOLO("models\model_v1.1.pt",task="detect") #load created model
ov_model = YOLO('models\model_v1.1_openvino_model/',task="detect") #load openvino model
#model = YOLO("yolov8n.pt") #load pretrained model

cap = cv2.VideoCapture(1)
ret = True