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

cap = cv2.VideoCapture(0)
ret = True

def on_draw(circle_centers):
    window.clear()
    for x , y in circle_centers:
         x = int(window.width * x)
         y = int(window.height * y)
         pyglet.shapes.Circle(x=x, y=y, radius=10, color=(255,255,0)).draw()
         

def exit_game():
    cap.release()  # Release the camera capture device
    pyglet.app.exit()  # Terminate the Pyglet application


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
    

def update(dt):
    ret, frame = cap.read()
    if ret is False:
        exit_game()
    frame = cv2.resize(frame , (640 , 640), interpolation=cv2.INTER_LINEAR)
    results = ov_model.track(frame, persist=True)
    if results[0] is not None:
            circle_centers = center_points(results=results)
            if circle_centers != []:
                x,y = circle_centers[0]
                print(x,y)
            on_draw(circle_centers=circle_centers)
    


# Schedule the update function to be called regularly
pyglet.clock.schedule_interval(update, 1/30.0)

# Start the game loop
pyglet.app.run()
        
    