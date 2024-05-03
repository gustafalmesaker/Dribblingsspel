import pyglet 
from pyglet import font

font.add_file('Assets/bebas/Bebas-Regular.ttf')
Bebas = font.load('Bebas', 16)

imgbutton = pyglet.image.load('Assets/150px.png')
imgbutton.anchor_x = imgbutton.width // 2
imgbutton.anchor_y = imgbutton.height // 2

imgbutton2 = pyglet.image.load('Assets/backbutton.png')
imgbutton2.anchor_x = imgbutton.width // 2
imgbutton2.anchor_y = imgbutton.height // 2



class circleButton:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.outer_radius = radius-5
        self.color = (22,37,33,255)
        self.outer_color = (22,37,33,255)

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

    def reset(self):
        self.time_remaining = self.duration

class chooseGame:
    def __init__(self):
        self.new_window = pyglet.window.Window(width=1200, height=600)
        self.new_window.set_vsync(False)
        self.fps_display = pyglet.window.FPSDisplay(self.new_window)
        self.cursor = cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)

        self.points = 0
        self.circleButtons = []
        self.create_button()

        self.new_window.push_handlers(self)
        pyglet.clock.schedule_interval(self.update, 1/10.0)

        # Images
        self.buttons = pyglet.graphics.Batch()
        self.sprites = []
        x_pos = self.new_window.width*(3/10)
        for i in range(3):
            if i == 1:
                x_pos = self.new_window.width*(7/10)

            self.button = pyglet.sprite.Sprite(imgbutton, x_pos, self.new_window.height*0.4, batch=self.buttons)
            self.sprites.append(self.button)

            if i == 2:
                x_pos = self.new_window.width*(3/20)
                self.button = pyglet.sprite.Sprite(imgbutton2, x_pos, self.new_window.height*(24/25), batch=self.buttons)
                self.sprites.append(self.button)
            
           



            

        

        

        self.new_window.set_mouse_visible(False)
        self.timer = Timer(10.0)
        pyglet.clock.schedule_interval(self.timer.update, 1/10.0)
        self.time_rad = 10

    def draw(self):
        for button in self.circleButtons:
            # Outer circle of button
            if (self.cursor.x - button.x)**2 + (self.cursor.y - button.y)**2 <= (button.radius - self.cursor.radius)**2:
                pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.outer_radius, color=button.outer_color).draw()
                pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.outer_radius-5, color=(22,37,33,255)).draw()
            
        # Draw other buttons
        self.buttons.draw() 

        # Cursor
        pyglet.shapes.Circle(x=self.cursor.x, y=self.cursor.y, radius=self.cursor.radius).draw()


    def on_draw(self):
        self.new_window.clear()
        
        # Background
        border = pyglet.image.SolidColorImagePattern((2,189,20,255)).create_image(self.new_window.width, self.new_window.height)
        border.blit(0,0)

        # Background color
        background = pyglet.image.SolidColorImagePattern((22,37,33,255)).create_image(self.new_window.width-20, self.new_window.height-20)
        background.blit(10,10)

        # Draw buttons
        self.draw()

        # Title
        titel = pyglet.text.Label('Välj spel',
                          font_name='Bebas',
                          font_size=75,
                          x=self.new_window.width//2, y=self.new_window.height*(0.85),
                          anchor_x='center', anchor_y='center')
        titel.draw()
        
        self.fps_display.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.x = x
        self.cursor.y = y

    def update(self, dt):
        for button in self.circleButtons:
            # Button is made smaller when cursor is inside the button circle
            if (self.cursor.x - button.x)**2 + (self.cursor.y - button.y)**2 <= (button.radius - self.cursor.radius)**2:
                self.animate_button(button,dt)  # Animate the button circle
                # Create a new button
                self.points = 20
            else:
                button.outer_radius = button.radius + 30
                button.outer_color = (2,189,20,255)
        
                
    def create_button(self):
        for i in range (3):

            if i == 0:
                x = self.new_window.width*(3/10)
                y = self.new_window.height
                radius = 2*150

            elif i == 1:
                x = self.new_window.width*(7/10)
                y = self.new_window.height
                radius = 2*150

            elif i == 2:
                x = self.new_window.width*(3/34)
                y = self.new_window.height*(0.835/0.4)
                radius = 150


            y = y*0.4
            radius = radius/2
            button = circleButton(x, y, radius)
            self.circleButtons.append(button)
        

        

    
    def animate_button(self,button,dt):
        if self.points/10 < 8:
            button.outer_radius -=self.points/10 # Button is made smaller every frame
        else:
            button.outer_radius -= 8

if __name__ == "__main__":
    chooseGame = chooseGame()
    pyglet.app.run()
