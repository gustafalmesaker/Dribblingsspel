import pyglet

class CircleButton(pyglet.shapes.Circle):
    def __init__(self, x, y, radius, color=(255, 255, 255)):
        super().__init__(x, y, radius, color=color)

class Game:
    def __init__(self):
        self.new_window = pyglet.window.Window(width=800, height=600)
        self.button = CircleButton(400, 300, 50)

        @self.new_window.event
        def on_draw():
            self.new_window.clear()
            self.button.draw()

if __name__ == "__main__":
    game = Game()
    pyglet.app.run()
