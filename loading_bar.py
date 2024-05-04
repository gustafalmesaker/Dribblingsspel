import pyglet
from survival_mode import Game


class LoadingBar:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.bar_width = 300
        self.bar_height = 20
        self.bar_color = (100, 100, 100, 255)  # Gray color
        self.loading_color = (0, 255, 0, 255)  # Green color
        self.loading_percentage = 0
        self.visible = False

    def draw(self):
        if self.visible:
            pyglet.shapes.Rectangle((self.window_width - self.bar_width) // 2,  100, self.bar_width, self.bar_height, self.bar_color).draw()
            pyglet.shapes.Rectangle((self.window_width - self.bar_width) // 2, 100, (self.loading_percentage * self.bar_width), self.bar_height, self.loading_color).draw()
            self.set_loading_percentage(self.loading_percentage)
            print(self.loading_percentage)
            

    def set_loading_percentage(self, percentage):
        percentage = percentage + 0.01
        self.loading_percentage = min(max(0, percentage), 1)

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False