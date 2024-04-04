import pyglet 
import random
import math

class goalCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 255, 255, 200)

class cursor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class Game:
    def __init__(self):
        self.new_window = pyglet.window.Window(width=800, height=600)
        self.new_window.set_vsync(False)
        self.fps_display = pyglet.window.FPSDisplay(self.new_window)
        self.cursor = cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)
       
        self.goalCircles = []

        for _ in range(3):
            x = random.randint(50, self.new_window.width-50)
            y = random.randint(50, self.new_window.height-50)
            radius = 50
            goal = goalCircle(x, y, radius)
            self.goalCircles.append(goal)
    

        self.new_window.push_handlers(self)
        pyglet.clock.schedule_interval(self.update, 1/10.0)
        self.new_window.set_mouse_visible(False)
    
    def draw(self):
        goalIndex = 1
        for goal in self.goalCircles:
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius, color=goal.color).draw()
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius-5, color=(0, 0, 0)).draw()
            pyglet.text.Label(str(goalIndex), font_name= 'Times New Roman', font_size=18, x=goal.x, y=goal.y).draw()
            goalIndex += 1
        pyglet.shapes.Circle(x=self.cursor.x, y=self.cursor.y, radius=self.cursor.radius).draw()

    def on_draw(self):
        self.new_window.clear()
        self.draw()
        self.fps_display.draw()


    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.x = x
        self.cursor.y = y
    
    
    def update(self, dt):
        for goal in self.goalCircles:
            if (self.cursor.x - goal.x)**2 + (self.cursor.y - goal.y)**2 <= (goal.radius - self.cursor.radius)**2:
                
                self.goalCircles.remove(goal)
                self.add_new_goal(goal)
                break

        #print(len(self.goalCircles))
        
    def add_new_goal(self, goal):
        x = random.randint(50, self.new_window.width-50)
        y = random.randint(50, self.new_window.height-50)
        radius = 50
        goal.x = x
        goal.y = y
        goal.radius = radius
        goal.color = (255, 255, 255, 200)
        
        self.goalCircles.append(goal)

    
if __name__ == "__main__":
    game = Game()
    pyglet.app.run(interval=1/120.0)
