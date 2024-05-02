from cgitb import reset
from lib2to3.pgen2.token import BACKQUOTE
from re import X
import pyglet
from pyglet import app, shapes
from pyglet.window import key
import time
import random
import math
from pyglet import image

#--- WINDOW ---#
height = 720
width = 1080
window = pyglet.window.Window(width, height)
#--------------#

#--- COLORS ---#
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)  
GRAY = (130, 130, 130, 255)
RED = (200, 0, 0, 255)
GREEN = (0, 200, 0, 255)
BLUE = (20, 100, 255, 255)
ORANGE = (255, 140, 0, 255)
#--------------#


# pic = pyglet.image.load('arrow.png')
# pic_sprite = pyglet.sprite.Sprite(pic, 540, 360)
# pic_sprite.rotation = 45



#----------------------------------- TEXT -----------------------------------#
label = pyglet.text.Label('Follow the Arrow',
                            font_name='Arial',
                            font_size=36,
                            x=window.width//2, y=window.height-30,
                            anchor_x='center', anchor_y='center',
                            color=(0, 0, 0, 255))
                            
entered_corr_text = pyglet.text.Label('Entered correctly',
                            font_name='Arial',
                            font_size=18,
                            x=window.width // 2, y=window.height-70,
                            anchor_x='center', anchor_y='center',
                            color=(255, 0, 0, 255))

inside_text = pyglet.text.Label('Inside',
                            font_name='Arial',
                            font_size=18,
                            x=window.width // 2, y=window.height-100,
                            anchor_x='center', anchor_y='center',
                            color=(255, 0, 0, 255))

done_text = pyglet.text.Label('DONE',
                            font_name='Arial',
                            font_size=30,
                            x=window.width // 2, y=window.height-150,
                            anchor_x='center', anchor_y='center',
                            color=(0, 255, 0, 255))
#----------------------------------------------------------------------------#
line_batch = pyglet.graphics.Batch()
temp = pyglet.graphics.Batch()



#--------------------------------- ARROWS -----------------------------------#
#--- START ARROW ---#
# LEFTIE
# x1, y1 = width-640, height//2     # P1
# x2, y2 = x1+150, y1-100           # P2
# x3, y3 = x1+150, y1+100           # P3
# x4, y4 = x1+150, y1-50            # P4
# x5, y5 = x1+150, y1+50            # P5
# x6, y6 = x1+450, y1-50            # P6
# x7, y7 = x1+450, y1+50            # P7
# direction = "left"
# triangle_progress = x4
# triangle = pyglet.shapes.Triangle(x2, y2, triangle_progress, y1, x3, y3, color=(255, 0, 0, 100), batch=line_batch)


#RIGHTIE
x1, y1 = width-200, height//2   # P1
x2, y2 = x1-150, y1+100         # P2
x3, y3 = x1-150, y1-100         # P3
x4, y4 = x1-150, y1-50          # P4    
x5, y5 = x1-150, y1+50          # P5
x6, y6 = x1-450, y1-50          # P6
x7, y7 = x1-450, y1+50          # P7
direction = "right"
triangle_progress = x4
triangle = pyglet.shapes.Triangle(x2, y2, triangle_progress, y1, x3, y3, color=(255, 0, 0, 100), batch=temp)

# UP
# x1, y1 = width//2, height-150 # P1
# x2, y2 = x1-100, y1-150       # P2
# x3, y3 = x1+100, y1-150       # P3
# x4, y4 = x1-50, y1-150        # P4
# x5, y5 = x1+50, y1-150        # P5
# x6, y6 = x1-50, y1-450        # P6
# x7, y7 = x1+50, y1-450        # P7
# direction = "up"
# triangle_progress = y4
# triangle = pyglet.shapes.Triangle(x2, y2, x1, triangle_progress, x3, y3, color=(255, 0, 0, 100), batch=line_batch)


# DOWN
# x1, y1 = width//2, height-600   # P1
# x2, y2 = x1-100, y1+150         # P2
# x3, y3 = x1+100, y1+150         # P3
# x4, y4 = x1-50, y1+150          # P4
# x5, y5 = x1+50, y1+150          # P5
# x6, y6 = x1-50, y1+450          # P6
# x7, y7 = x1+50, y1+450          # P7
# direction = "down"
# triangle_progress = y4
# triangle = pyglet.shapes.Triangle(x2, y2, x1, triangle_progress, x3, y3, color=(255, 0, 0, 100), batch=line_batch)

line1 = shapes.Line(x1, y1, x2, y2, 5, GREEN, batch=line_batch)  # Left diagonal
line2 = shapes.Line(x1, y1, x3, y3, 5, GREEN, batch=line_batch)  # Righ diagonal
line3 = shapes.Line(x2, y2, x3, y3, 5, GREEN, batch=line_batch) # Triangle bottom 
line4 = shapes.Line(x4, y4, x6, y6, 5, GREEN, batch=line_batch)  # Left side rect
line5 = shapes.Line(x5, y5, x7, y7, 5, GREEN, batch=line_batch)  # Right side rect
line6 = shapes.Line(x6, y6, x7, y7, 5, ORANGE, batch=line_batch)  # Entry line
loading_bar = pyglet.shapes.Rectangle(x6, y6, 0, 100, color=(255, 0, 0, 100), batch=line_batch)  # Horizontal arrow
# loading_bar = pyglet.shapes.Rectangle(x6, y6, 100, 0, color=(255, 0, 0, 100), batch=line_batch)  # Vertical arrow

# #-------------------#

# line1_t = shapes.Line(x1_t, y1_t, x2_t, y2_t, 5, GREEN, batch=line_batch)  # Left diagonal
# line2_t = shapes.Line(x1_t, y1_t, x3_t, y3_t, 5, GREEN, batch=line_batch)  # Righ diagonal
# line3_t = shapes.Line(x2_t, y2_t, x3_t, y3_t, 5, GREEN, batch=line_batch) # Triangle bottom 
# line4_t = shapes.Line(x4_t, y4_t, x6_t, y6_t, 5, GREEN, batch=line_batch)  # Left side rect
# line5_t = shapes.Line(x5_t, y5_t, x7_t, y7_t, 5, GREEN, batch=line_batch)  # Right side rect
# line6_t = shapes.Line(x6_t, y6_t, x7_t, y7_t, 5, ORANGE, batch=line_batch)  # Entry line
# #loading_bar = pyglet.shapes.Rectangle(x6, y6, 0, 100, color=(255, 0, 0, 100), batch=line_batch)  # Horizontal arrow
# loading_bar = pyglet.shapes.Rectangle(x6_t, y6_t, 100, 0, color=(255, 0, 0, 100), batch=line_batch)  # Vertical arrow

#loading_bar = pyglet.shapes.Line(x1, y6, x1, y6, 100, color=(255, 0, 0, 100), batch=line_batch) # Line for diagonal

# hit_box_line1 = pyglet.shapes.Line(x6, y6, x1, y6, 2, RED, batch=line_batch)
# hit_box_line2 = pyglet.shapes.Line(x7, y7, x1, y7, 2, RED, batch=line_batch)
# hit_box_line3 = pyglet.shapes.Line(x1, y6, x1, y7, 2, RED, batch=line_batch)    

last_progressed_position_x = x6
last_progressed_position_y = y6


# box

box = pyglet.shapes.BorderedRectangle(x6, y6, 300, 100, 10, border_color=GREEN, batch=temp)
box.rotation = 45

#--- ARROWS DEFINITIONS ---#
# LEFT 
def left_arrow(x_start, y_start):
    global x1, x2, x3, x4, x5, x6, x7, y1, y2, y3, y4, y5, y6, y7
    global last_progressed_position_x, last_progressed_position_y
    x1, y1 = x_start, y_start   # P1
    x2, y2 = x1+150, y1-100     # P2
    x3, y3 = x1+150, y1+100     # P3
    x4, y4 = x1+150, y1-50      # P4
    x5, y5 = x1+150, y1+50      # P5
    x6, y6 = x1+450, y1-50      # P6
    x7, y7 = x1+450, y1+50      # P7
    last_progressed_position_x = x6
    last_progressed_position_y = y6 
    return "left"

# RIGHT 
def right_arrow(x_start, y_start):
    global x1, x2, x3, x4, x5, x6, x7, y1, y2, y3, y4, y5, y6, y7
    global last_progressed_position_x, last_progressed_position_y
    x1, y1 = x_start, y_start   # P1
    x2, y2 = x1-150, y1+100     # P2
    x3, y3 = x1-150, y1-100     # P3
    x4, y4 = x1-150, y1-50      # P4    
    x5, y5 = x1-150, y1+50      # P5
    x6, y6 = x1-450, y1-50      # P6
    x7, y7 = x1-450, y1+50      # P7
    last_progressed_position_x = x6
    last_progressed_position_y = y6 
    return "right"

# UP 
def up_arrow(x_start, y_start):
    global x1, x2, x3, x4, x5, x6, x7, y1, y2, y3, y4, y5, y6, y7
    global last_progressed_position_x, last_progressed_position_y
    x1, y1 = x_start, y_start   # P1
    x2, y2 = x1-100, y1-150     # P2
    x3, y3 = x1+100, y1-150     # P3
    x4, y4 = x1-50, y1-150      # P4
    x5, y5 = x1+50, y1-150      # P5
    x6, y6 = x1-50, y1-450      # P6
    x7, y7 = x1+50, y1-450      # P7
    last_progressed_position_x = x6
    last_progressed_position_y = y6 
    return "up"

# DOWN 
def down_arrow(x_start, y_start):
    global x1, x2, x3, x4, x5, x6, x7, y1, y2, y3, y4, y5, y6, y7
    global last_progressed_position_x, last_progressed_position_y
    x1, y1 = x_start, y_start   # P1
    x2, y2 = x1-100, y1+150     # P2
    x3, y3 = x1+100, y1+150     # P3
    x4, y4 = x1-50, y1+150      # P4
    x5, y5 = x1+50, y1+150      # P5
    x6, y6 = x1-50, y1+450      # P6
    x7, y7 = x1+50, y1+450      # P7
    last_progressed_position_x = x6
    last_progressed_position_y = y6 
    return "down"
#--------------------------#

#--- POINTS ---#
point_batch = pyglet.graphics.Batch()
point1 = pyglet.text.Label('P1', font_name='Arial', font_size=12, x=x1, y=y1, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point2 = pyglet.text.Label('P2', font_name='Arial', font_size=12, x=x2, y=y2, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point3 = pyglet.text.Label('P3', font_name='Arial', font_size=12, x=x3, y=y3, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point4 = pyglet.text.Label('P4', font_name='Arial', font_size=12, x=x4, y=y4, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point5 = pyglet.text.Label('P5', font_name='Arial', font_size=12, x=x5, y=y5, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point6 = pyglet.text.Label('P6', font_name='Arial', font_size=12, x=x6, y=y6, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point7 = pyglet.text.Label('P7', font_name='Arial', font_size=12, x=x7, y=y7, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
#--------------#
#----------------------------------------------------------------------------#

#------------------------------- DRAW FIGURE --------------------------------#
def draw_figure():
    global line1, line2, line3, line4, line5, line6, loading_bar, circle, triangle, triangle_progress
    global hit_box_line1, hit_box_line2, hit_box_line3

    line1 = shapes.Line(x1, y1, x2, y2, 5, GREEN, batch=line_batch)     # Left diagonal
    line2 = shapes.Line(x1, y1, x3, y3, 5, GREEN, batch=line_batch)     # Right diagonal
    line3 = shapes.Line(x2, y2, x3, y3, 5, GREEN, batch=line_batch)     # Triangle base 
    line4 = shapes.Line(x4, y4, x6, y6, 5, GREEN, batch=line_batch)     # Left side rect
    line5 = shapes.Line(x5, y5, x7, y7, 5, GREEN, batch=line_batch)     # Right side rect
    line6 = shapes.Line(x6, y6, x7, y7, 5, ORANGE, batch=line_batch)    # Entry line

    # hit_box_line1 = pyglet.shapes.Line(x6, y6, x1, y6, 2, RED, batch=line_batch)
    # hit_box_line2 = pyglet.shapes.Line(x7, y7, x1, y7, 2, RED, batch=line_batch)
    # hit_box_line3 = pyglet.shapes.Line(x1, y6, x1, y7, 2, RED, batch=line_batch)    
 
    if (direction == "right" or direction == "left"):
        loading_bar = pyglet.shapes.Rectangle(x6, y6, 0, 100, color=(255, 0, 0, 100), batch=line_batch)
        triangle = pyglet.shapes.Triangle(x2, y2, x4, y1, x3, y3, color=(255, 0, 0, 100), batch=line_batch)

    else: 
        loading_bar = pyglet.shapes.Rectangle(x6, y6, 100, 0, color=(255, 0, 0, 100), batch=line_batch)
        triangle = pyglet.shapes.Triangle(x2, y4, x1, y4, x3, y3, color=(255, 0, 0, 100), batch=line_batch)

#----------------------------------------------------------------------------#

#--- BOOLS ---#
entered_correctly = False
inside = False
done = False
#-------------#

#---------------------------------- UPDATE ----------------------------------#
#----- INSIDE -----#
def check_inside(x, y):
    global inside
    if (direction == "right" or direction == "left") and (x >= min(x1, x6) and x <= max(x1, x6)) and (y >= min(y6, y7) and y <= max(y6, y7)):
        inside = True
    elif (direction == "up" or direction == "down") and (x >= min(x6, x7) and x <= max(x6, x7)) and (y >= min(y1, y6) and y <= max(y1, y6)):
        inside = True
    else:
        inside = False

#------------------#

#----- ENTERED CORRECTLY -----#
def entered_corr(x, y):
    global entered_correctly
    if not entered_correctly:
        if (direction == "right" or direction == "left") and x >= x6-10 and x <= x6+10 and y >= y6 and y <= y7 and loading_bar.width == 0:  
                entered_correctly = True
        elif (direction == "up" or direction == "down") and x >= x6 and x <= x7 and y <= y6+10 and y >= y6-10 and loading_bar.height == 0:  
                entered_correctly = True

        elif (direction == "right" or direction == "left") and inside and x >= last_progressed_position_x-5 and x <= last_progressed_position_x+5:
            entered_correctly = True

        elif (direction == "up" or direction == "down") and inside and y >= last_progressed_position_y-5 and y <= last_progressed_position_y+5:
            entered_correctly = True
    else: 
        entered_correctly = False
#-----------------------------#

#------LOADING BAR -----#
def update_loading_bar(x, y, direction):
    global inside, last_progressed_position_x, last_progressed_position_y, entered_correctly, done, triangle_progress
    progress = 0

    # FILL IN THE ARROW BASED ON CURSOR POSITION
    if entered_correctly and inside:
        #--- LEFT ---#
        if direction == "left" and x <= last_progressed_position_x:
            loading_bar.width = min(0, max(x - x6, -300))
            last_progressed_position_x = x

            # TEXT #
            progress = abs(last_progressed_position_x - x6)/3
            loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(progress)
            # ---- #
      
            if x > x4:
                triangle_progress = x4
            else:
                triangle_progress = x
            triangle.x2 = triangle_progress

            if triangle_progress <= x1 + 5:
                done = True
        #-------------#
        
        #--- RIGHT ---#
        if direction == "right" and x >= last_progressed_position_x:
            loading_bar.width = max(0, min(x - x6, 300))
            last_progressed_position_x = x 

            # TEXT #
            progress = abs(last_progressed_position_x - x6)/3
            loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(progress)
            # ---- #

            if x < x4:
                triangle_progress = x4
            else: 
                triangle_progress = x
            triangle.x2 = triangle_progress

            if triangle_progress >= x1 - 5:
                done = True
            #print("triangle_progress: ", triangle_progress)
        #----------#

        #--- UP ---#
        if direction == "up" and y >= last_progressed_position_y:
            loading_bar.height = max(0, min(y - y6, 300))
            last_progressed_position_y = y

            # TEXT #
            progress = abs(last_progressed_position_y - y6)/3
            loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(progress)
            # ---- #

            if y < y4:
                triangle_progress = y4
            else: 
                triangle_progress = y
            triangle.y2 = triangle_progress

            if triangle_progress >= y1 - 5:
                done = True
        #------------#

        #--- DOWN ---#
        if direction == "down" and y <= last_progressed_position_y:
            loading_bar.height = min(0, max(y - y6, -300))
            #loading_bar.y2 = min(0, max(y - y6, -300))
            last_progressed_position_y = y
            
            # TEXT #
            progress = abs(last_progressed_position_y - y6)/3
            loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(progress)
            # ---- #

            if y > y4:
                triangle_progress = y4
            else:
                triangle_progress = y
            triangle.y2 = triangle_progress

            if triangle_progress <= y1 + 5:
                done = True
        #------------#

    elif not inside:
        loading_bar.width = max(0, last_progressed_position_x)
        loading_bar.height = max(0, last_progressed_position_y)
        triangle.y = max(0, triangle_progress)
    

#-----------------------#

#--- CURSOR ---#
def update_cursor(x, y):
    global inside, entered_correctly
    # Check if cursor is inside the lines
    if entered_correctly and inside:
        window.set_mouse_cursor(window.get_system_mouse_cursor(window.CURSOR_HAND))
    else:
        window.set_mouse_cursor(window.get_system_mouse_cursor(window.CURSOR_DEFAULT))
#--------------#
#----------------------------------------------------------------------------#

#----------------------------------- RESET ----------------------------------#


#--- RESET GAME ---#
@window.event
def reset_game():
    global loading_bar, entered_correctly, done, last_progressed_position_x, last_progressed_position_y, direction 
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7
    global line1, line2, line3, line4, line5, line6
    global point1, point2, point3, point4, point5, point6, point7 
    global direction_text

    update_points()

    # Randomly choose arrow direction
    direction = random.choice(["right", "left", "up", "down"])

    # Set arrow points based on the chosen direction
    if direction == "right":
        x1 = random.randint(500, width - 50)
        y1 = random.randint(200, height - 200)
        direction = right_arrow(x1, y1)
        loading_bar.width = 0
        loading_bar.height = 100
        draw_figure()

    elif direction == "left":
        x1 = random.randint(50, width-500)
        y1 = random.randint(200, height - 200)
        direction = left_arrow(x1, y1)
        loading_bar.width = 0
        loading_bar.height = 100
        draw_figure()
        
    elif direction == "up":
        x1 = random.randint(150, width - 150)
        y1 = random.randint(500, height - 50)
        direction = up_arrow(x1, y1)
        loading_bar.width = 100
        loading_bar.height = 0
        draw_figure()

    elif direction == "down":
        x1 = random.randint(150, width - 150)
        y1 = random.randint(100, height - 500)
        direction = down_arrow(x1, y1)
        loading_bar.width = 100
        loading_bar.height = 0
        draw_figure()

    progress = 0
    entered_correctly = False
    done = False
    loading_bar_width_text.text = ('PROGRESS: 0.0')

    direction_text = pyglet.text.Label('Direction: {}'.format(direction),
                                           font_name='Arial',
                                           font_size=14,
                                           x=10, y=height - 200,
                                           anchor_x='left', anchor_y='center',
                                           color=GREEN)       
    update_points_label()


#------------------#

#--- COORDINATES ---#
    point1 = pyglet.text.Label('P1', font_name='Arial', font_size=12, x=x1, y=y1, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point2 = pyglet.text.Label('P2', font_name='Arial', font_size=12, x=x2, y=y2, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point3 = pyglet.text.Label('P3', font_name='Arial', font_size=12, x=x3, y=y3, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point4 = pyglet.text.Label('P4', font_name='Arial', font_size=12, x=x4, y=y4, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point5 = pyglet.text.Label('P5', font_name='Arial', font_size=12, x=x5, y=y5, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point6 = pyglet.text.Label('P6', font_name='Arial', font_size=12, x=x6, y=y6, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point7 = pyglet.text.Label('P7', font_name='Arial', font_size=12, x=x7, y=y7, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
#-------------------#

#--- RESET BUTTON ---#
button_x = 50
button_y = 600
button_width = 100
button_height = 50
button_shape = pyglet.shapes.Rectangle(button_x, button_y, button_width, button_height, color=BLUE)

def is_mouse_inside_button(x, y):
    return button_x < x < button_x + button_width and button_y < y < button_y + button_height

@window.event
def on_mouse_press(x, y, button, modifiers):
    if is_mouse_inside_button(x, y):
        window.set_mouse_cursor(window.get_system_mouse_cursor(window.CURSOR_HAND))
        if button == pyglet.window.mouse.LEFT:     
            reset_game()
            
    else:
        window.set_mouse_cursor(window.get_system_mouse_cursor(window.CURSOR_DEFAULT))
reset_text = pyglet.text.Label('Reset', font_name='Arial', font_size=18, x=button_x + button_width // 2, y=button_y + button_height // 2, anchor_x='center', anchor_y='center')
#--------------------#
#----------------------------------------------------------------------------#

points = 0
points_label = pyglet.text.Label('Points: {}'.format(points),
                                 font_name='Valken',
                                 font_size=24,
                                 x=window.width - 100,
                                 y=window.height - 40,
                                 anchor_x='center',
                                 anchor_y='center',
                                 color=(0, 0, 0, 255))

def update_points():
    global points
    points += 1

def update_points_label():
    points_label.text = 'Points: {}'.format(points)

#---------------------------------- DEBUG -----------------------------------#
cursor_position_text = pyglet.text.Label('Cursor Position: (0, 0)',
                                        font_name='Arial',
                                        font_size=14,
                                        x=10, y=height - 20,
                                        anchor_x='left', anchor_y='center',
                                        color=(0, 0, 0, 255))

loading_bar_width_text = pyglet.text.Label('PROGRESS: {}'.format((last_progressed_position_x-x6)/3),
                                           font_name='Arial',
                                           font_size=14,
                                           x=10, y=height - 40,
                                           anchor_x='left', anchor_y='center',
                                           color=(0, 0, 0, 255))

direction_text = pyglet.text.Label('Direction: {}'.format(direction),
                                           font_name='Arial',
                                           font_size=14,
                                           x=10, y=height - 200,
                                           anchor_x='left', anchor_y='center',
                                           color=GREEN)                                          

def update_cursor_position_text(x, y):
    cursor_position_text.text = 'Cursor Position: ({}, {})'.format(x, y)
#----------------------------------------------------------------------------#



#####################################################################################
##                                       APP                                       ##
#####################################################################################

circle = pyglet.shapes.Circle(width//2, height//2, 5, color=BLACK, batch=line_batch)


@window.event
def on_mouse_motion(x, y, dx, dy):
    global entered_correctly, direction
    update_cursor(x, y)
    update_cursor_position_text(x, y)  # Update cursor position text
    check_inside(x, y)

    #--- UPDATE LOADING BAR ---#
    if entered_correctly and inside:
        update_loading_bar(x, y, direction)
        entered_correctly = True
    else:
        entered_corr(x, y)
    #--------------------------#

    #--- MOVE CIRCLE ---#
    circle.x = x
    circle.y = y
    #-------------------# 

#---/// GAME WINDOW ///---#
@window.event
def on_draw():
    pyglet.gl.glClearColor(1, 1, 1, 1)
    window.clear()

    label.draw() # LABEL
    #line_batch.draw()
    loading_bar.draw()
    points_label.draw() 
    #pic_sprite.draw()
    temp.draw()

    #--- DEBUG ---#
    # RESET BUTTON
    button_shape.draw()
    reset_text.draw()
    #direction_text.draw()

    cursor_position_text.draw()
    #loading_bar_width_text.draw()
    point_batch.draw()

    if entered_correctly:
        entered_corr_text.draw()
    
    if inside:
        inside_text.draw()
    #-------------#

    #--- RESET ---#
    if done:
        done_text.draw()
        reset_game()
    #-------------#

pyglet.app.run()
#---///-------------///---#
