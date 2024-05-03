import pyglet
import cv2

#from ultralytics import YOLO

from game_v4 import Game, cursor, pointSystem, goalCircle
from tracking import tracking




game=Game()

#tracking = tracking()



# def main(dt):
#     tracking.update_pos(dt)
#     game.ball_position(tracking.circle_pos_x,tracking.circle_pos_y)

pyglet.clock.schedule_interval(game.update, 1.0/ 120.0)


#pyglet.clock.schedule_interval(main, 1/30.0)


pyglet.app.run()