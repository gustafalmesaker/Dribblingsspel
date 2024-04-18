import pyglet 
import random

class circleButton:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.inner_radius = radius-5
        self.color = (50,205,50, 200)
        self.inner_color = (50,205,50, 200)

    

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
        self.circleButtons = []
        self.create_button()

        self.new_window.push_handlers(self)
        pyglet.clock.schedule_interval(self.update, 1/10.0)

        self.new_window.set_mouse_visible(False)
        self.timer = Timer(10.0)
        pyglet.clock.schedule_interval(self.timer.update, 1/10.0)
        self.time_rad = 10

    def draw(self):
        for button in self.circleButtons:

            # Inner circle of button
            if (self.cursor.x - button.x)**2 + (self.cursor.y - button.y)**2 <= (button.radius - self.cursor.radius)**2:
                pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.inner_radius, color=button.inner_color).draw()
                pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.inner_radius-5, color=(0, 0, 0)).draw()

            # Outer circle of button
            pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.radius, color=button.color).draw()
            pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.radius-5, color=(0, 0, 0)).draw()

            
        
        # Cursor
        pyglet.shapes.Circle(x=self.cursor.x, y=self.cursor.y, radius=self.cursor.radius).draw()

    def on_draw(self):
        self.new_window.clear()
        self.draw()
        self.fps_display.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.x = x
        self.cursor.y = y

    def update(self, dt):
        #print(self.timer.time_remaining)
        for button in self.circleButtons:
            # button is made smaller when cursor is inside the button circle
            
            if (self.cursor.x - button.x)**2 + (self.cursor.y - button.y)**2 <= (button.radius - self.cursor.radius)**2:
                self.animate_button(button,dt)  # Animate the button circle
                 # Create a new button
                self.points = 20
            else:
                button.inner_radius = button.radius + 30
                button.inner_color = (255, 255, 255, 200)
                

            
                
    def create_button(self):
        for i in range (2):
            x = self.new_window.width*(3/10)    

            if i == 1:
                x = self.new_window.width*(7/10)
                

            y = self.new_window.height/2
            radius = 100
            button = circleButton(x, y, radius)
            self.circleButtons.append(button)


        radius = 100
        button = circleButton(x, y, radius)
        self.circleButtons.append(button)
    
    def animate_button(self,button,dt):

        if self.points/10 < 8:
            button.inner_radius -=self.points/10 # button is made smaller every frame
        else:
            button.inner_radius -= 8    

        #if button.inner_radius <= button.radius/4:
            #button.inner_color = (255,0,0, 200)       # Change color of inner circle when it is less than 1/4 of the button circle (red)

        #elif button.inner_radius <= button.radius/2:
            #button.inner_color = (255,165,0, 200)      # Change color of inner circle when it is less than 1/2 of the button circle (orange)


        if button.radius == button.inner_radius:                # If button is completely gone, remove it and create a new button
            self.circleButtons.remove(button)
            #self.add_new_button(button)
            self.timer.reset()
    


if __name__ == "__main__":
    game = Game()
    pyglet.app.run()

