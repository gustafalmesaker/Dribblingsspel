import pyglet
from huvudmeny import huvudmeny
from chooseGame import chooseGame

class AppState:
    def __init__(self):
        self.current_state = 'menu'  # Initial state

    def run(self):
        while self.current_state is not None:
            if self.current_state == 'menu':
                menu = huvudmeny()
                self.current_state = menu.run()
            elif self.current_state == 'game':
                game = chooseGame()
                self.current_state = game.run()
            else:
                self.current_state = None

if __name__ == "__main__":
    app = AppState()
    app.run()
    pyglet.app.run()
