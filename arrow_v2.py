import pyglet
from pyglet import app, shapes
import math
import random


#--- WINDOW ---#
height = 1080
width = 1920
window = pyglet.window.Window(width, height)
#--------------#

#--- COLORS ---#
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)  
GRAY = (130, 130, 130, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 200, 0, 255)
BLUE = (20, 100, 255, 255)
ORANGE = (255, 140, 0, 255)
#--------------#

line_batch = pyglet.graphics.Batch()
point_batch = pyglet.graphics.Batch()
text_batch = pyglet.graphics.Batch()
game_batch = pyglet.graphics.Batch()

direction = "R"

#----------------------------------- TEXT -----------------------------------#
inside_text = pyglet.text.Label('Inside',
                            font_name='Arial',
                            font_size=18,
                            x=window.width // 2, y=window.height-100,
                            anchor_x='center', anchor_y='center',
                            color=(255, 0, 0, 255)) #, batch=text_batch)

cursor_position_text = pyglet.text.Label('Cursor Position: (0, 0)',
                                        font_name='Arial',
                                        font_size=14,
                                        x=10, y=height - 20,
                                        anchor_x='left', anchor_y='center',
                                        color=(0, 0, 0, 255), batch=text_batch)

def update_cursor_position_text(x, y):
    cursor_position_text.text = 'Cursor Position: ({}, {})'.format(x, y)

loading_bar_width_text = pyglet.text.Label('PROGRESS: {}'.format(0),
                                        font_name='Arial',
                                        font_size=14,
                                        x=10, y=height - 40,
                                        anchor_x='left', anchor_y='center',
                                        color=(0, 0, 0, 255),  batch=text_batch)

rotation_text = pyglet.text.Label('ROTATION: {}'.format(0),
                                        font_name='Arial',
                                        font_size=14,
                                        x=10, y=height - 80,
                                        anchor_x='left', anchor_y='center',
                                        color=(0, 0, 0, 255),  batch=text_batch)

direction_text = pyglet.text.Label('Direction: {}'.format(direction),
                                        font_name='Arial',
                                        font_size=14,
                                        x=300, y=height - 80,
                                        anchor_x='left', anchor_y='center',
                                        color=(0, 0, 0, 255),  batch=text_batch)



point_batch = pyglet.graphics.Batch()
point1 = pyglet.text.Label('P1', font_name='Arial', font_size=12, x=0, y=0, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point2 = pyglet.text.Label('P2', font_name='Arial', font_size=12, x=0, y=0, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point3 = pyglet.text.Label('P3', font_name='Arial', font_size=12, x=0, y=0, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
point4 = pyglet.text.Label('P4', font_name='Arial', font_size=12, x=0, y=0, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch) 
#----------------------------------------------------------------------------#



# --- BOOLS --- #
entered_correctly = True
inside = False
done = True
# ------------- #

prog = 0
rect_size = 35



# -------------------------------- DRAW ARROW -------------------------------- #
@window.event
def draw_arrow(arrow_x, arrow_y, dir):
    global start_x, start_y, end_x, end_y, x3, y3, x4, y4
    global start_x_r, start_y_r, end_x_r, end_y_r, x3_r, y3_r, x4_r, y4_r
    global rot_angle, ox, oy, angle1, angle2
    global point, point1, point2, point3, point4, line1, line2, line3, line_batch, point_batch
    global loading_bar, loading_bar2, loading_bar3, rect_size
    global done, prog, direction

    # --- RESET VALUES --- #
    line1 = pyglet.shapes.Line(0, 0, 0, 0, 30, RED, batch=line_batch) 
    line2 = pyglet.shapes.Line(0, 0, 0, 0, 30, RED, batch=line_batch) 
    line3 = pyglet.shapes.Line(0, 0, 0, 0, 30, RED, batch=line_batch)

    line_batch = pyglet.graphics.Batch()
    point_batch = pyglet.graphics.Batch()

    done = False
    prog = 0
    loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)
    # -------------------- #

    # --- Start & End point --- #
    end_x = arrow_x
    end_y = arrow_y

    start_y = end_y
    start_x = end_x - 400

    # Arrow
    x3, y3 = end_x-100, end_y-75
    x4, y4 = end_x-100, end_y+75

    ox = end_x
    oy = end_y
    # ------------------------- #

    # --- rot_angle --- #
    # random
    # rot_angle = random.choice([math.radians(0), math.radians(90), math.radians(180), math.radians(-90), math.radians(45), math.radians(135), math.radians(-45), math.radians(-135)])
    direction = dir

    if direction == "R": 
        rot_angle = math.radians(0)
    elif direction == "L":
        rot_angle = math.radians(180)
    elif direction == "U":
        rot_angle = math.radians(90)
    elif direction == "D":
        rot_angle = math.radians(-90)
    
    elif direction == "UR":
        rot_angle = math.radians(45)
    elif direction == "DR":
        rot_angle = math.radians(-45)
    elif direction == "UL":
        rot_angle = math.radians(135)
    elif direction == "DL":
        rot_angle = math.radians(-135)
    
    rotation_text.text = 'ROTATION: {:.1f}'.format(math.degrees(rot_angle))
    # ----------------- #

    # --- RE-CALCULATE --- #
    start_x_r = ox + math.cos(rot_angle) * (start_x - ox) - math.sin(rot_angle) * (start_y - oy) 
    start_y_r = oy + math.sin(rot_angle) * (start_x - ox) + math.cos(rot_angle) * (start_y - oy)
    end_x_r = ox + math.cos(rot_angle) * (end_x - ox) - math.sin(rot_angle) * (end_y - oy)
    end_y_r = oy + math.sin(rot_angle) * (end_x - ox) + math.cos(rot_angle) * (end_y - oy)

    x3_r, y3_r = ox + math.cos(rot_angle) * (x3 - ox) - math.sin(rot_angle) * (y3 - oy), oy + math.sin(rot_angle) * (x3 - ox) + math.cos(rot_angle) * (y3 - oy)
    x4_r, y4_r = ox + math.cos(rot_angle) * (x4 - ox) - math.sin(rot_angle) * (y4 - oy), oy + math.sin(rot_angle) * (x4 - ox) + math.cos(rot_angle) * (y4 - oy)
    
    point = pyglet.shapes.Circle(end_x_r, end_y_r, 15, None, RED, batch=line_batch)

    angle1 = math.atan2(y3 - end_y, x3 - end_x) * 180 / math.pi
    angle2 = math.atan2(y4 - end_y, x4 - end_x) * 180 / math.pi
    # -------------------- #

    line1 = pyglet.shapes.Line(start_x_r, start_y_r, end_x_r, end_y_r, 30, RED, batch=line_batch) 
    line2 = pyglet.shapes.Line(x3_r, y3_r, end_x_r, end_y_r, 30, RED, batch=line_batch) 
    line3 = pyglet.shapes.Line(x4_r, y4_r, end_x_r, end_y_r, 30, RED, batch=line_batch)

    # --- DEBUG --- #
    point1 = pyglet.shapes.Circle(start_x_r, start_y_r, 3, None, BLACK, batch=point_batch)
    point2 = pyglet.shapes.Circle(end_x_r, end_y_r, 3, None, BLACK, batch=point_batch)
    point3 = pyglet.shapes.Circle(x3_r, y3_r, 3, None, BLACK, batch=point_batch)
    point4 = pyglet.shapes.Circle(x4_r, y4_r, 3, None, BLACK, batch=point_batch)

    point1 = pyglet.text.Label('P1', font_name='Arial', font_size=12, x=start_x_r, y=start_y_r, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point2 = pyglet.text.Label('P2', font_name='Arial', font_size=12, x=end_x_r, y=end_y_r, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point3 = pyglet.text.Label('P3', font_name='Arial', font_size=12, x=x3_r, y=y3_r, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch)    
    point4 = pyglet.text.Label('P4', font_name='Arial', font_size=12, x=x4_r, y=y4_r, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=point_batch) 
    # ------------- #

    #############################################
    #       DRAW DIFFERENT TYPE OF ARROW        #
    #############################################

    # --- ARROW STRAIGHT RIGHT --- #
    if direction == "R": 
        loading_bar = pyglet.shapes.Rectangle(start_x_r, start_y_r-18, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r-12, y3_r+14, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(angle1))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+10, y4_r+14, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(angle2))
    # ---------------------------- #
        
    # --- ARROW STRAIGHT LEFT --- #
    if direction == "L":
        loading_bar = pyglet.shapes.Rectangle(start_x_r, start_y_r+18, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r-11, y3_r+14, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(angle1))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+11, y4_r+14, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(angle2))
    # --------------------------- #

    # --- ARROW STRAIGHT UP --- #
    if direction == "U": 
        loading_bar = pyglet.shapes.Rectangle(start_x_r+18, start_y_r, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r+14, y3_r+10, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(126))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+13, y4_r-10, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(53))
    # ------------------------- #

    # --- ARROW STRAIGHT DOWN --- #
    if direction == "D": 
        loading_bar = pyglet.shapes.Rectangle(start_x_r-18, start_y_r, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r+14, y3_r+12, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(127))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+14, y4_r-10, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(53))
    # --------------------------- #
        
    # --- ARROW UP TO THE RIGHT --- #
    if direction == "UR": 
        loading_bar = pyglet.shapes.Rectangle(start_x_r+11, start_y_r-11, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r+15, y3_r-3, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(81))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+2, y4_r-15, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(8))
    # ----------------------------- #
        
    # --- ARROW UP TO THE LEFT --- #
    if direction == "UL": 
        loading_bar = pyglet.shapes.Rectangle(start_x_r+13, start_y_r+12, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r+3, y3_r+15, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(171))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+17, y4_r+1, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(98))
    # ---------------------------- #
        
    # --- ARROW DOWN TO THE RIGHT --- #
    if direction == "DR":
        loading_bar = pyglet.shapes.Rectangle(start_x_r-12, start_y_r-9, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r+1, y3_r+16, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(172))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+15, y4_r+2, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(98))
    # ------------------------------- #

    # --- ARROW DOWN TO THE LEFT --- #
    if direction == "DL":
        loading_bar = pyglet.shapes.Rectangle(start_x_r-12, start_y_r+14, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar.rotation = -math.degrees(rot_angle)

        loading_bar2 = pyglet.shapes.Rectangle(x3_r+15, y3_r-1, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar2.rotation = -math.degrees(math.radians(83))

        loading_bar3 = pyglet.shapes.Rectangle(x4_r+3, y4_r-18, 0, rect_size, GREEN, batch=line_batch) 
        loading_bar3.rotation = -math.degrees(math.radians(8))
    # ------------------------------ #
        
    direction_text.text = ('Direction: {}'.format(direction))
# ------------------------------------------------------------------------------- #
    
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
            draw_arrow()
            
    else:
        window.set_mouse_cursor(window.get_system_mouse_cursor(window.CURSOR_DEFAULT))
reset_text = pyglet.text.Label('Reset', font_name='Arial', font_size=18, x=button_x + button_width // 2, y=button_y + button_height // 2, anchor_x='center', anchor_y='center', batch=text_batch)
#--------------------#

# ------------------------------ CHECK INSIDE -------------------------------- #
def check_inside(x, y):
    global inside
    #box = pyglet.shapes.BorderedRectangle(start_x_r,start_y_r, 400, 30, 5, ORANGE, batch=line_batch)
    if (direction == "R" or direction == "L") and (x >= min(start_x_r, end_x_r) and x <= max(start_x_r, end_x_r)) and (y >= min(start_y_r-15, start_y_r+15) and y <= max(start_y_r-15, start_y_r+15)):
        inside = True
        print(f"Conditions for inside: {min(start_x_r, end_x_r)} < x < {max(start_x_r, end_x_r)} and {min(start_y_r-15, start_y_r+15)} < y < {max(start_y_r-15, start_y_r+15)}")

    elif (direction == "U" or direction == "D") and (x >= min(start_x_r-15, start_x_r+15) and x <= max(start_x_r-15, start_x_r+15)) and (y >= min(start_y_r, end_y_r) and y <= max(start_y_r, end_y_r)):
        inside = True
        print(f"Conditions for inside: {min(start_x_r-15, start_x_r+15)} < x < {max(start_x_r-15, start_x_r+15)} and {min(start_y_r, end_y_r)} < y < {max(start_y_r, end_y_r)}")

    elif (direction == "UR" or direction == "UL" or direction == "DR" or direction == "DL")  and (x >= min(start_x_r, end_x_r) and x <= max(start_x_r, end_x_r)) and (y >= min(start_y_r, end_y_r) and y <= max(start_y_r, end_y_r)):
        inside = True
        print('*** IM HERE ***')
        print(f"Conditions for inside: {min(start_x_r, end_x_r)} < x < {max(start_x_r, end_x_r)} and {min(start_y_r-15, start_y_r+15)} < y < {max(start_y_r-15, start_y_r+15)}")

    else:
        inside = False

# ---------------------------------------------------------------------------- #

# ------------------------------- LOADING BAR -------------------------------- #
def update_loading_bar(x,y):
    global start_x, end_x, start_y, end_y, done, prog, rot_angle

    x_new = x - start_x_r
    y_new = y - start_y_r

    # --- STRAIGHT RIGHT --- #
    if (rot_angle ==  math.radians(0) and x_new > 0):
        scaling = abs(x_new)
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = min(0, -(prog-75)*4)
            loading_bar3.width = min(0, -(prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
            done = True
    # ---------------------- #
            
    # --- STRAIGHT LEFT --- #
    if (rot_angle ==  math.radians(180) and x_new < 0):
        scaling = abs(x_new)
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = max(0, (prog-75)*4)
            loading_bar3.width = max(0, (prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
            done = True
    # --------------------- #
            
    # --- STRAIGHT UP --- #
    if (rot_angle ==  math.radians(90) and y_new > 0):
        scaling = abs(y_new)
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = max(0, (prog-75)*4)
            loading_bar3.width = max(0, (prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
            done = True
    # ------------------- #            
            
            
    # --- STRAIGHT DOWN --- #
    if (rot_angle ==  math.radians(-90) and y_new < 0):
        scaling = abs(y_new)
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = min(0, -(prog-75)*4)
            loading_bar3.width = min(0, -(prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
            done = True
    # --------------------- #

    # --- UP RIGHT --- #
    if (rot_angle ==  math.radians(45) and x_new > 0):
        scaling = abs(x_new)*1.45
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = max(0, (prog-75)*4)
            loading_bar3.width = max(0, (prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
            done = True
    # ---------------- #

    # --- UP LEFT --- #
    if (rot_angle ==  math.radians(135) and x_new < 0):
        scaling = abs(x_new)*1.45
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = max(0, (prog-75)*4)
            loading_bar3.width = max(0, (prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
            done = True
    # --------------- #

    # --- DOWN RIGHT --- #
    if (rot_angle ==  math.radians(-45) and x_new > 0):
        scaling = abs(x_new)*1.45
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = min(0, -(prog-75)*4)
            loading_bar3.width = min(0, -(prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
            done = True
    # ------------------ #

    # --- DOWN LEFT --- #
    if (rot_angle ==  math.radians(-135) and x_new < 0):
        scaling = abs(x_new)*1.45
        loading_bar.width = max(0, scaling)
        prog = loading_bar.width/4
        loading_bar_width_text.text = 'PROGRESS: {:.1f}'.format(prog)

        if prog > 75: 
            loading_bar2.width = min(0, -(prog-75)*4)
            loading_bar3.width = min(0, -(prog-75)*4)

        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
            done = True
    # ----------------- #
# ---------------------------------------------------------------------------- #

    
ball = pyglet.shapes.Circle(width//2, height//2, 80, None, BLACK, batch=game_batch)

# --- MOUSE MOTION --- #
@window.event
def on_mouse_motion(x, y, dx, dy):
    update_cursor_position_text(x, y)  # Update cursor position text

    check_inside(x, y)

    # Update ball position to follow the mouse cursor
    ball.x = x
    ball.y = y

    # --- UPDATE LOADING BAR --- #
    if entered_correctly and inside:
        update_loading_bar(x, y)
# -------------------- #
  
# -------- FAKE GAME for pictures -------- #
gline1 = pyglet.shapes.Line(width//2, 220, width//2, 750, 20, color=(0, 255, 0, 100), batch=game_batch)
gcircle1 = pyglet.shapes.Circle(width//2, 125, 100, None, color=(0, 255, 0, 100), batch=game_batch)
wcircle1 = pyglet.shapes.Circle(width//2, 125, 85, None, WHITE, batch=game_batch)

gline2 = pyglet.shapes.Line(width//2, 220, width//2, 750, 20, color=(0, 255, 0, 100), batch=game_batch)
gcircle2 = pyglet.shapes.Circle(width//2, 750, 100, None, color=(0, 255, 0, 100), batch=game_batch)
wcircle2 = pyglet.shapes.Circle(width//2, 750, 85, None, WHITE, batch=game_batch)

gline3 = pyglet.shapes.Line(385, 130, width//2-95, 130, 20, color=(0, 255, 0, 100), batch=game_batch)
gcircle3 = pyglet.shapes.Circle(290, 130, 100, None, color=(0, 255, 0, 100), batch=game_batch)
wcircle3 = pyglet.shapes.Circle(290, 130, 85, None, WHITE, batch=game_batch)

gline4 = pyglet.shapes.Line(340, 210, width//2-80, 710, 20, color=(0, 255, 0, 100), batch=game_batch)
# ---------------------------------------- #

counter = 1
#####################################################################################
##                                       APP                                       ##
#####################################################################################
@window.event
def on_draw():
    global counter
    pyglet.gl.glClearColor(1, 1, 1, 1)
    
    window.clear()

    game_batch.draw()
    line_batch.draw()
    #point_batch.draw()
    #text_batch.draw()
    #button_shape.draw()

    if inside:
        inside_text.draw()

    if done and counter == 0:
        draw_arrow(width//2-100, 125, "R")
        counter = counter+1

    if done and counter == 1:
        draw_arrow(width//2, 650, "U")
        counter = counter+1
    
    if done and counter == 2:
        draw_arrow(355, 210, "DL")
        counter = 0

pyglet.app.run()
#---///-------------///---#
