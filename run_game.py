import pyglet
import cv2

#from ultralytics import YOLO

from game_v4 import Game, cursor, pointSystem, goalCircle
#from tracking import tracking



game=Game()



pyglet.clock.schedule_interval(game.update, 1/60.0)
pyglet.clock.schedule_interval(game.ball_position, 2)


pyglet.app.run(interval=1/120.0)