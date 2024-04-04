import pyglet 
import random
import math

class goalCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 255, 255, 200)

    def draw(self):
        pyglet.shapes.Circle(x=self.x, y=self.y, radius=self.radius, color=self.color).draw()
        pyglet.shapes.Circle(x=self.x, y=self.y, radius=self.radius-5, color=(0, 0, 0)).draw()


class cursor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pyglet.shapes.Circle(x=self.x, y=self.y, radius=self.radius).draw()


class Game:
    def __init__(self):
        self.new_window = pyglet.window.Window(width=800, height=600)
        self.font = 'Times New Roman'
        self.font_size = 16
        self.counter_label = pyglet.text.Label('Points: 0', font_name=self.font, font_size=self.font_size, x=self.new_window.width//2, y=self.new_window.height- 30, anchor_x='center', anchor_y='center')
        
        self.cursor = cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)
        self.goalCircle = goalCircle(x=random.randint(50, self.new_window.width-50), y=random.randint(50, self.new_window.height-50), radius=50)
        self.innerGoalCircle = goalCircle(x=self.goalCircle.x, y=self.goalCircle.y, radius=45)
        self.innerGoalCircle.color = (0, 0, 0)
        
        self.counter = 0
        self.new_window.event(self.on_mouse_motion)
        self.new_window.event(self.on_draw)
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def on_mouse_motion(self, x, y, dx, dy):
        if (self.cursor.x - self.goalCircle.x)**2 + (self.cursor.y - self.goalCircle.y)**2 <= (self.goalCircle.radius - self.cursor.radius)**2:
            self.add_new_goal()
            self.counter += 1
            self.counter_label.text = "Points: " + str(self.counter)
        self.cursor.x = x
        self.cursor.y = y

    def add_new_goal(self):
        self.goalCircle.x = random.randint(50, self.new_window.width-50)
        self.goalCircle.y = random.randint(50, self.new_window.height-50)
        self.innerGoalCircle.x = self.goalCircle.x
        self.innerGoalCircle.y = self.goalCircle.y

    def on_draw(self):
        self.new_window.clear()
        self.goalCircle.draw()
        self.cursor.draw()
        self.counter_label.draw()

    def update(self, dt):
        pass

if __name__ == '__main__':
    game = Game()
    pyglet.app.run()

