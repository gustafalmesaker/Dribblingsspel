import pyglet 
import random

new_window = pyglet.window.Window(width = 1300, height = 700, caption ='Dribblingsspel', resizable = True)

seconds_played = 0.00
counter = 0

def update(dt):
    global seconds_played
    seconds_played += dt
    #If countdown reaches 0, the game is over
    if seconds_played >= 5:
        countdown_label.text = "Game Over!"
        pyglet.clock.unschedule(update)
        #wait for 2 seconds before closing the window
        pyglet.clock.schedule_once(lambda dt: pyglet.app.exit(), 2)
    else:
        countdown_label.text = str(5.00-seconds_played)[:4]

#pyglet.clock.schedule_interval(update, 0.01)


label = pyglet.text.Label('Real fun begins now!', 
                          font_name ='Times New Roman', 
                          font_size = 16, 
                          x = new_window.width//2,  
                          y = new_window.height//2, 
                          anchor_x ='center',  
                          anchor_y ='center') 

countdown_label = pyglet.text.Label('5.00', 
                          font_name ='Times New Roman', 
                          font_size = 16, 
                          x = new_window.width//2,  
                          y = new_window.height//2 - 50, 
                          anchor_x ='center',  
                          anchor_y ='center')

counter_label = pyglet.text.Label('Points: 0', 
                          font_name ='Times New Roman', 
                          font_size = 16, 
                          x = new_window.width//2,  
                          y = new_window.height- 30, 
                          anchor_x ='center',  
                          anchor_y ='center')



  
@new_window.event
def on_mouse_motion(x, y, dx, dy):
    #if the whole circle is inside the goal circle
    if (circle.x - goalCircle.x)**2 + (circle.y - goalCircle.y)**2 <= (goalCircle.radius - circle.radius)**2:
        goalCircle.x = random.randint(50, new_window.width-50)
        goalCircle.y = random.randint(50, new_window.height-50)
        goalCircle.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        

        #update(-1)

        global counter
        counter += 1
        counter_label.text = "Points: " + str(counter)

    circle.x = x
    circle.y = y


circle = pyglet.shapes.Circle(x=new_window.width//2, y=new_window.height//2, radius=30)
goalCircle = pyglet.shapes.Circle(x=random.randint(50, new_window.width-50), y=random.randint(50, new_window.height-50), radius=50)
goalCircle.color = (255, 105, 180)


@new_window.event
def on_draw():
    new_window.clear()
    goalCircle.draw()
    circle.draw()
    label.draw()
    countdown_label.draw()
    counter_label.draw()


pyglet.app.run() 