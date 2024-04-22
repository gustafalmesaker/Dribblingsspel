import pyglet 
from pyglet import font

font.add_file('Assets/bebas/Bebas-Regular.ttf')
Bebas = font.load('Bebas', 16)

imgbutton = pyglet.image.load('Assets/150px.png')
imgbutton.anchor_x = imgbutton.width // 2
imgbutton.anchor_y = imgbutton.height // 2

imgbutton.width = imgbutton.width
imgbutton.height = imgbutton.height



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
        #print(self.time_remaining)

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

        #Images

        self.buttons = pyglet.graphics.Batch()
        self.sprites = []
        x_pos = self.new_window.width*(3/10)
        for i in range(2):

            if i == 1:
                x_pos = self.new_window.width*(7/10)

            self.button = pyglet.sprite.Sprite(imgbutton, x_pos, self.new_window.height/2, batch=self.buttons)

            self.sprites.append(self.button)

            

        self.new_window.set_mouse_visible(False)
        self.timer = Timer(10.0)
        pyglet.clock.schedule_interval(self.timer.update, 1/10.0)
        self.time_rad = 10

    def draw(self):

        
        for button in self.circleButtons:

            # outer circle of button
            if (self.cursor.x - button.x)**2 + (self.cursor.y - button.y)**2 <= (button.radius - self.cursor.radius)**2:
                pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.outer_radius, color=button.outer_color).draw()
                pyglet.shapes.Circle(x=button.x, y=button.y, radius=button.outer_radius-5, color=(22,37,33,255)).draw()
         
        
        # Cursor
        pyglet.shapes.Circle(x=self.cursor.x, y=self.cursor.y, radius=self.cursor.radius).draw()

    def on_draw(self):
        self.new_window.clear()
        
        #Bake border for background
        border = pyglet.image.SolidColorImagePattern((2,189,20,255)).create_image(self.new_window.width, self.new_window.height)
        border.blit(0,0)

        #Background color
        background = pyglet.image.SolidColorImagePattern((22,37,33,255)).create_image(self.new_window.width-20, self.new_window.height-20)
        background.blit(10,10)

        
        self.draw()

        #Draw button from png
        
        self.buttons.draw() 

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
        #print(self.timer.time_remaining)
        for button in self.circleButtons:
            # button is made smaller when cursor is inside the button circle
            
            if (self.cursor.x - button.x)**2 + (self.cursor.y - button.y)**2 <= (button.radius - self.cursor.radius)**2:
                self.animate_button(button,dt)  # Animate the button circle
                 # Create a new button
                self.points = 20
            else:
                button.outer_radius = button.radius + 30
                button.outer_color = (2,189,20,255)
                

            
                
    def create_button(self):
        for i in range (2):
            
            x = self.new_window.width*(3/10)    
            
            if i == 1:
                x = self.new_window.width*(7/10)
                

            y = self.new_window.height/2
            radius = 150
            button = circleButton(x, y, radius)
            self.circleButtons.append(button)


        radius = 150
        button = circleButton(x, y, radius)
        self.circleButtons.append(button)
    
    def animate_button(self,button,dt):

        if self.points/10 < 8:
            button.outer_radius -=self.points/10 # button is made smaller every frame
        else:
            button.outer_radius -= 8    

        #if button.outer_radius <= button.radius/4:
            #button.outer_color = (255,0,0, 200)       # Change color of outer circle when it is less than 1/4 of the button circle (red)

        #elif button.outer_radius <= button.radius/2:
            #button.outer_color = (255,165,0, 200)      # Change color of outer circle when it is less than 1/2 of the button circle (orange)


        # if button.radius == button.outer_radius:                # If button is completely gone, remove it and create a new button
        #     self.circleButtons.remove(button)
        #     #self.add_new_button(button)
        #     self.timer.reset()
    



