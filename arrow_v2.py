import pyglet
from pyglet import app, shapes
import math


#--- WINDOW ---#
height = 720
width = 1080
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
#----------------------------------------------------------------------------#



# --- BOOLS --- #
entered_correctly = True
inside = True
# ------------- #




# --- ARROWS --- #
# Start
start_x, start_y = 100, 560
# End
end_x, end_y = 500, 560 

# Arrow
x3, y3 = end_x-100, end_y-75
x4, y4 = end_x-100, end_y+75

# point1 = pyglet.shapes.Circle(x1, y1, 10, None, RED, batch=point_batch)
# point2 = pyglet.shapes.Circle(x2, y2, 10, None, RED, batch=point_batch)
# point3 = pyglet.shapes.Circle(x3, y3, 10, None, RED, batch=point_batch)
# point4 = pyglet.shapes.Circle(x4, y4, 10, None, RED, batch=point_batch)

# line1 = pyglet.shapes.Line(x1, y1, x2, y2, 30, BLUE, batch=line_batch) 
# line2 = pyglet.shapes.Line(x2-8, y2, x3, y3, 30, BLUE, batch=line_batch) 
# line3 = pyglet.shapes.Line(x2-8, y2, x4, y4, 30, BLUE, batch=line_batch) 
#loading_bar = pyglet.shapes.Line(start_x, start_y, start_x, start_y, 30, GREEN, batch=line_batch) 
# -------------- #


# -------------------------------- ROTATION -------------------------------- #
# Anchor point #
ox, oy = end_x, end_y

#rot_angle = math.radians(0) # RIGHT
#rot_angle = math.radians(180) # LEFT
rot_angle = math.radians(90) # UP
#rot_angle = math.radians(-90) # DOWN

#rot_angle = math.radians(45) # UP RIGHT
#rot_angle = math.radians(135) # UP LEFT
#rot_angle = math.radians(-45) # DOWN RIGHT
#rot_angle = math.radians(-135) # DOWN LEFT


# Rotation #
start_x_r, start_y_r = ox + math.cos(rot_angle) * (start_x - ox) - math.sin(rot_angle) * (start_y - oy), oy + math.sin(rot_angle) * (start_x - ox) + math.cos(rot_angle) * (start_y - oy)
end_x_r, end_y_r = ox + math.cos(rot_angle) * (end_x - ox) - math.sin(rot_angle) * (end_y - oy), oy + math.sin(rot_angle) * (end_x - ox) + math.cos(rot_angle) * (end_y - oy)
x3_r, y3_r = ox + math.cos(rot_angle) * (x3 - ox) - math.sin(rot_angle) * (y3 - oy), oy + math.sin(rot_angle) * (x3 - ox) + math.cos(rot_angle) * (y3 - oy)
x4_r, y4_r = ox + math.cos(rot_angle) * (x4 - ox) - math.sin(rot_angle) * (y4 - oy), oy + math.sin(rot_angle) * (x4 - ox) + math.cos(rot_angle) * (y4 - oy)

point = pyglet.shapes.Circle(end_x_r, end_y_r, 15, None, RED, batch=point_batch)

point1 = pyglet.shapes.Circle(start_x_r, start_y_r, 3, None, BLACK, batch=point_batch)
point2 = pyglet.shapes.Circle(end_x_r, end_y_r, 3, None, BLACK, batch=point_batch)
point3 = pyglet.shapes.Circle(x3_r, y3_r, 3, None, BLACK, batch=point_batch)
point4 = pyglet.shapes.Circle(x4_r, y4_r, 3, None, BLACK, batch=point_batch)

line1 = pyglet.shapes.Line(start_x_r, start_y_r, end_x_r, end_y_r, 30, RED, batch=line_batch) 
line2 = pyglet.shapes.Line(end_x_r, end_y_r, x3_r, y3_r, 30, RED, batch=line_batch) 
line3 = pyglet.shapes.Line(end_x_r, end_y_r, x4_r, y4_r, 30, RED, batch=line_batch) 

angle1 = math.atan2(y3 - end_y, x3 - end_x) * 180 / math.pi
angle2 = math.atan2(y4 - end_y, x4 - end_x) * 180 / math.pi

rect_size = 35
# --- ARROW STRAIGHT RIGHT --- #
if rot_angle == math.radians(0): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r, start_y_r-18, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r-12, y3_r+14, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(angle1))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+10, y4_r+14, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(angle2))
# ---------------------------- #

# --- ARROW STRAIGHT LEFT --- #
if rot_angle == math.radians(180): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r, start_y_r+18, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r-11, y3_r+14, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(angle1))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+11, y4_r+14, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(angle2))
# --------------------------- #

# --- ARROW STRAIGHT UP --- #
if rot_angle == math.radians(90): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r+18, start_y_r, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r+14, y3_r+10, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(126))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+13, y4_r-10, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(53))
# ------------------------- #

# --- ARROW STRAIGHT DOWN --- #
if rot_angle == math.radians(-90): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r-18, start_y_r, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r+14, y3_r+12, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(127))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+14, y4_r-10, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(53))
# --------------------------- #

# --- ARROW UP TO THE RIGHT --- #
if rot_angle == math.radians(45): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r+11, start_y_r-11, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r+15, y3_r-3, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(81))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+2, y4_r-15, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(8))
# ----------------------------- #

# --- ARROW UP TO THE LEFT --- #
if rot_angle == math.radians(135): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r+13, start_y_r+12, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r+3, y3_r+15, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(171))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+17, y4_r+1, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(98))
# ---------------------------- #

# --- ARROW DOWN TO THE RIGHT --- #
if rot_angle == math.radians(-45): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r-12, start_y_r-9, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r+1, y3_r+16, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(172))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+15, y4_r+2, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(98))
# ------------------------------- #

# --- ARROW DOWN TO THE LEFT --- #
if rot_angle == math.radians(-135): 
    loading_bar = pyglet.shapes.Rectangle(start_x_r-12, start_y_r+14, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar.rotation = -math.degrees(rot_angle)

    loading_bar2 = pyglet.shapes.Rectangle(x3_r+15, y3_r-1, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar2.rotation = -math.degrees(math.radians(83))

    loading_bar3 = pyglet.shapes.Rectangle(x4_r+3, y4_r-18, 0, rect_size, GREEN, batch=line_batch) 
    loading_bar3.rotation = -math.degrees(math.radians(8))
# ------------------------------ #

#----------------------------------------------------------------------------#


def update_loading_bar(x,y):
    global start_x, end_x, start_y, end_y

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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = 128
            loading_bar3.width = 128
            point.radius = 18
            point.color = GREEN
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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
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

        print('loading_bar2.width: ', loading_bar2.width)
        if prog > 99:
            loading_bar.width = 400
            loading_bar2.width = -128
            loading_bar3.width = -128
            point.radius = 18
            point.color = GREEN
    # ----------------- #
    



# --- MOUSE ROATION --- #
@window.event
def on_mouse_motion(x, y, dx, dy):
    update_cursor_position_text(x, y)  # Update cursor position text


    # --- UPDATE LOADING BAR --- #

    if entered_correctly and inside:
        update_loading_bar(x, y)
        
    #else:
    #    entered_corr(x, y)
        
     # -/- UPDATE LOADING BAR -/- #
        
# -/- MOUSE ROATION -/- #


#####################################################################################
##                                       APP                                       ##
#####################################################################################
@window.event
def on_draw():
    pyglet.gl.glClearColor(1, 1, 1, 1)
    window.clear()
    line_batch.draw()
    point_batch.draw()
    text_batch.draw()



pyglet.app.run()
#---///-------------///---#
