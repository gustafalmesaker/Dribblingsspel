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
       
        self.goalCircles = []
        for _ in range(3):
            x = random.randint(50, self.new_window.width-50)
            y = random.randint(50, self.new_window.height-50)
            radius = 50
            goal = goalCircle(x, y, radius)
            self.goalCircles.append(goal)
    
        self.goalCircles[0].color = (255, 255, 255, 200)

        self.points = 0
        self.goal = self.goalCircles[0]
        self.goal_index = 0
        self.goal_radius = self.goal.radius
        self.goal_x = self.goal.x
        self.goal_y = self.goal.y
        self.goal_color = self.goal.color

        self.new_window.push_handlers(self)
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        self.new_window.set_mouse_visible(False)
        #self.new_window.set_exclusive_mouse(True)

    def on_draw(self):
        self.new_window.clear()
        self.counter_label.draw()
        for goal in self.goalCircles:
            goal.draw()

        self.cursor.draw()
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.x = x
        self.cursor.y = y
    

    def update(self, dt):
        if (self.cursor.x - self.goal.x)**2 + (self.cursor.y - self.goal.y)**2 <= (self.goal.radius - self.cursor.radius)**2:
            self.points += 1
            self.counter_label.text = "Points: " + str(self.points)
            
            # if self.goal_index == len(self.goalCircles):
            #     self.goal_index = 0
            
            # self.goal = self.goalCircles[self.goal_index]

            self.goal_x = self.goal.x
            self.goal_y = self.goal.y
            self.goal_radius = self.goal.radius
            self.goal_color = self.goal.color

            self.goalCircles.pop(self.goal_index)
            self.goal_index += 1
            
            self.goalCircles.insert(self.goal_index, goalCircle(x=random.randint(50, self.new_window.width-50), y=random.randint(50, self.new_window.height-50), radius=50))

        
        self.goal.x = self.goal_x
        self.goal.y = self.goal_y
        self.goal.radius = self.goal_radius
        self.goal.color = self.goal_color
    



if __name__ == '__main__':
    game = Game()
    pyglet.app.run()

