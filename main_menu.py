import pyglet
from loading_bar import LoadingBar
from survival_mode import Game
from run_game import run_game
# Load images
practice = pyglet.image.load('assets/practice.png')  # 150 x 150 px
survival = pyglet.image.load('assets/survival.png')  # 150 x 150 px

# Window size
window_width = 640
window_height = 640

# Calculate positions for images
padding_between_images = 20
total_width_of_images = practice.width + padding_between_images + survival.width
starting_x = (window_width - total_width_of_images) // 2
practice_x = starting_x
survival_x = practice_x + practice.width + padding_between_images

# Center vertically
image_y = (window_height - practice.height) // 2

# Create window
window = pyglet.window.Window(width=window_width, height=window_height)
window.game_started = False


class Cursor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.hovering = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y

        # Check if mouse is hovering over images
        if (x >= practice_x and x <= practice_x + practice.width and y >= image_y and y <= image_y + practice.height):
            self.hovering = "practice"
        elif (x >= survival_x and x <= survival_x + survival.width and y >= image_y and y <= image_y + survival.height):
            self.hovering = "survival"
        else:
            self.hovering = None

    def draw_cursor(self):
        pyglet.shapes.Circle(x=self.x, y=self.y, radius=self.radius, color=(255, 255, 255)).draw()

cursor = Cursor(x=starting_x, y=image_y, radius=10)
loading_bar = LoadingBar(window_width=window_height, window_height=window_height)

@window.event
def on_draw():
    window.clear()
    
    if cursor.hovering == "survival" and window.game_started is False:
        loading_bar.show()
        if loading_bar.loading_percentage >= 1:
            game_started = True
            run_game()
            
    elif cursor.hovering == "practice":
        loading_bar.show()
        if loading_bar.loading_percentage >= 1:
            pass
    else: 
        loading_bar.hide()
        loading_bar.loading_percentage = 0

    practice.blit(practice_x, image_y)
    survival.blit(survival_x, image_y)
    cursor.draw_cursor()
    loading_bar.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    cursor.on_mouse_motion(x, y, dx, dy)
    
pyglet.app.run()
