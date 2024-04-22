from huvudmeny import huvudmeny
from chooseGame import chooseGame
import pyglet

def switch_callback(x):
    if x == 1:
        huvudmeny()
    elif x == 2:
        chooseGame()
        
    else:
        return None  # Handle other cases if needed

# Base case
x = 1

# Call the switch_callback function until it returns None
while x is not None:
    x = switch_callback(x)

pyglet.app.run()