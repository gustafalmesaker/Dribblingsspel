import pyglet
import random
from Read_file import read_csv
from ultralytics import YOLO
import cv2

class Game():
    def __init__(self):
        self.ov_model = YOLO('models\model_v1.1_openvino_model/',task="detect")
        self.cap = cv2.VideoCapture(0)
        self.sound_effect = pyglet.resource.media("soundtrack/meny_music.mp3")
        self.cursor = None
        self.point_system = None
        self.goalCircles = []
        self.counter = 0
        self.tracking = None
        self.new_window = None
        self.fps_display = None
        self.positions_from_file = None
        self.initialize_game()

    def initialize_game(self):
        self.sound_effect.play()
        self.new_window = pyglet.window.Window(width=1420, height=800, caption="Game", vsync=False)
        self.new_window.set_mouse_visible(False)
        self.fps_display = pyglet.window.FPSDisplay(self.new_window)
        self.cursor = Cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)
        self.point_system = PointSystem()
        self.tracking = Tracking(self.ov_model, self.cap)

        self.new_window.push_handlers(self)
        pyglet.clock.schedule_interval(self.update, 1.0/120.0)

    def update(self, dt):
        self.tracking.update_pos()
        self.cursor.update_position(self.tracking.circle_pos_x, self.tracking.circle_pos_y)
        # Add your game logic here

    def on_draw(self):
        self.new_window.clear()
        # Draw game elements here
        self.fps_display.draw()

class Cursor:   
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def update_position(self, x, y):
        self.x = x
        self.y = y

class PointSystem:
    def __init__(self):
        self.points = 0
        self.streak = 0

class Tracking:
    def __init__(self, ov_model, cap):
        self.ov_model = ov_model
        self.cap = cap
        self.circle_pos_x = 600
        self.circle_pos_y = 600

    def update_pos(self):
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, (1420, 800), interpolation=cv2.INTER_LINEAR)
        results = self.ov_model.track(frame, persist=True)
        if results[0] is not None:
            pos = self.center_points(results)
            if pos:
                self.circle_pos_x, self.circle_pos_y = pos[0]

    def center_points(self, results):
        box_list = []
        sports_ball_id = 32
        if results[0].boxes.xyxy is not None:
            for obj in results[0].boxes:
                if obj.cls == sports_ball_id:
                    x_n, y_n, w, h = obj.xywhn[0].tolist()
                    box_list.append([x_n, y_n])
        return box_list

if __name__ == "__main__":
    game = Game()
    pyglet.app.run()


