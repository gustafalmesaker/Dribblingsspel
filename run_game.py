import pyglet
from game_v4 import Game, cursor, pointSystem, goalCircle
from Read_file import read_csv



# Read data from the CSV file
exercises, positions = read_csv('exercise_positions.csv')

# Find the index of exercise "B"
index_of_b = exercises.index('A')

# Print positions for exercise "B"
print("Positions for exercise B:", positions[index_of_b])

game=Game()

game.initial_position(positions[index_of_b])

pyglet.clock.schedule_interval(game.update, 1/10.0)

pyglet.app.run(interval=1/120.0)


