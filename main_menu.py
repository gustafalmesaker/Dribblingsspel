import pyglet

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

@window.event
def on_draw():
    window.clear()
    practice.blit(practice_x, image_y)
    survival.blit(survival_x, image_y)

pyglet.app.run()
