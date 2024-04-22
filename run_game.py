import pyglet
from game_v4 import Game, cursor, pointSystem, goalCircle
from Read_file import read_csv



# Read data from the CSV file
exercises, positions = read_csv('exercise_positions.csv')



game=Game()

pyglet.clock.schedule_interval(game.update, 1/10.0)

pyglet.app.run(interval=1/120.0)


