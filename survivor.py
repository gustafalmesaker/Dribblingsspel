import pyglet 
import random

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

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.time_remaining = duration

    def update(self, dt):
        self.time_remaining -= dt
        if self.time_remaining <= 0:
            self.reset()
        #print(self.time_remaining)

    def reset(self):
        self.time_remaining = self.duration

class Game:
    def __init__(self):
        self.new_window = pyglet.window.Window(width=800, height=600)
        self.new_window.set_vsync(False)
        self.fps_display = pyglet.window.FPSDisplay(self.new_window)
        self.cursor = cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)

        self.points = 0
        self.goalCircles = []
        self.create_goal()

        self.new_window.push_handlers(self)
        pyglet.clock.schedule_interval(self.update, 1/10.0)

        self.new_window.set_mouse_visible(False)
        self.timer = Timer(10.0)
        pyglet.clock.schedule_interval(self.timer.update, 1/10.0)
        self.time_rad = 10

    def draw(self):
        for goal in self.goalCircles:
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius, color=goal.color).draw()
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius-5, color=(0, 0, 0)).draw()
        
        pyglet.shapes.Circle(x=self.cursor.x, y=self.cursor.y, radius=self.cursor.radius).draw()

    def on_draw(self):
        self.new_window.clear()
        self.draw()
        self.fps_display.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.x = x
        self.cursor.y = y

    def update(self, dt):
        print(self.timer.time_remaining)
        for goal in self.goalCircles:
            # Goal is made smaller when cursor is inside the goal circle
            
            if (self.cursor.x - goal.x)**2 + (self.cursor.y - goal.y)**2 <= (goal.radius - self.cursor.radius)**2:
                self.goalCircles.remove(goal)
                self.add_new_goal(goal) # Create a new goal
                self.timer.reset() # Reset the timer
                self.points += 1
                break
            else:
                self.animate_goal(dt)

    def create_goal(self):
        x = random.randint(50, self.new_window.width-50)
        y = random.randint(50, self.new_window.height-50)
        radius = 100
        goal = goalCircle(x, y, radius)
        self.goalCircles.append(goal)

    def add_new_goal(self, goal):
        x = random.randint(50, self.new_window.width-50)
        y = random.randint(50, self.new_window.height-50)
        radius = 100-self.time_rad
        goal = goalCircle(x, y, radius)
        self.goalCircles.append(goal)
    
    def animate_goal(self, dt):
        for goal in self.goalCircles:
            if self.points/10 < 8:
                goal.radius -=self.points/10
            else:
                goal.radius -= 8

            if goal.radius <= 0:
                self.goalCircles.remove(goal)
                self.add_new_goal(goal)
                self.timer.reset()
                break


if __name__ == "__main__":
    game = Game()
    pyglet.app.run()
