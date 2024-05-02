#from msilib.schema import ProgId
from re import X
from turtle import position
import pyglet
from pyglet import clock, shapes
import math


#--- WINDOW ---#
height = 720
width = 1280
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

points_arr = []

#--- FOOTBALL ---#
batch = pyglet.graphics.Batch()
circle = pyglet.shapes.Circle(width//2, height//2, 30, color=BLACK, batch=batch)
circle_red = pyglet.shapes.Circle(width//2, height//2, 30, color=RED)
#----------------#

# Timer to control update rate

cursor_position_text = pyglet.text.Label('Cursor Position: (0, 0)',
                                        font_name='Arial',
                                        font_size=14,
                                        x=10, y=height - 20,
                                        anchor_x='left', anchor_y='center',
                                        color=(0, 0, 0, 255))
def update_cursor_position_text(mouse_x, mouse_y):
    cursor_position_text.text = 'Cursor Position: ({}, {})'.format(mouse_x, mouse_y)

points_label = pyglet.text.Label('Points: 0',
                                 font_name='Valken',
                                 font_size=24,
                                 x=window.width//2,
                                 y=window.height - 40,
                                 anchor_x='center',
                                 anchor_y='center',
                                 color=(0, 0, 0, 255))

counter = 0
mouse_x, mouse_y = 0, 0
inside_bool = False

line_length_text =  pyglet.text.Label('Length: 0',
                                    font_name='Arial',
                                    font_size=14,
                                    x=10, y=height - 40,
                                    anchor_x='left', anchor_y='center',
                                    color=(0, 0, 0, 255))
line_length = 0

angle_text =  pyglet.text.Label('Angle: 0 degrees',
                                    font_name='Arial',
                                    font_size=14,
                                    x=10, y=height - 60,
                                    anchor_x='left', anchor_y='center',
                                    color=(0, 0, 0, 255))

inner_r_text =  pyglet.text.Label('Inner radius: ',
                                    font_name='Arial',
                                    font_size=14,
                                    x=10, y=height - 80,
                                    anchor_x='left', anchor_y='center',
                                    color=(0, 0, 0, 255))
                                    
outer_r_text =  pyglet.text.Label('Outer radius: ',
                                    font_name='Arial',
                                    font_size=14,
                                    x=10, y=height - 100,
                                    anchor_x='left', anchor_y='center',
                                    color=(0, 0, 0, 255))
                                    

@window.event
def on_mouse_motion(x, y, dx, dy):
    global mouse_x, mouse_y, inside_bool, line, line_length, triangle
    mouse_x, mouse_y = x, y

    #--- MOVE CIRCLE ---#
    circle.x = x
    circle.y = y
    #-------------------# 
    update_cursor_position_text(mouse_x, mouse_y)  # Update cursor position text

    if is_point_in_arc(x, y, center_x, center_y, radius, thickness, start_angle, end_angle):
        inside_bool = True
    else:
        inside_bool = False

    line = pyglet.shapes.Line(center_x, center_y, x, y, 2, BLACK, batch=batch)
    line_length = math.sqrt((x-center_x)*(x-center_x) + (y-center_y)*(y-center_y))
    line_length_text.text = ('Length: {:.3f}'.format(line_length))


    angle = math.atan2(y - center_y, x - center_x) * (180 / math.pi)
    angle = math.radians(angle)
    if angle < 0:
            angle += 2 * math.pi

    angle_text.text = ('Angle: {:.1f} radians'.format(angle))

@window.event
def addPoints():
    global counter, mouse_x, mouse_y, points_arr
    points_arr.append((mouse_x, mouse_y))
    counter += 1
    points_label.text = 'Points: {}'.format(counter)

    if len(points_arr) > 500:
        points_arr = []
        counter = 0

def callback_addPoints(dt):
    addPoints()

clock.schedule_interval(callback_addPoints, 0.0001)   # called once a second

point1 = float(100), float(100)
point2 = float(130), float(150)
point3 = float(140), float(120)
point4 = float(160), float(180)

arr = [point1, point2, point3, point4]


center_x, center_y = width//2,  height//2-20
radius = 300
thickness = 40
start_angle = 0
end_angle = 5
progression = 0
segments = 10

arc = pyglet.shapes.Arc(center_x, center_y, radius, None, end_angle, start_angle, False, thickness, (0, 0, 255, 80), batch=batch)
arc_loading = pyglet.shapes.Arc(center_x, center_y, radius, None, progression, start_angle, False, thickness, (0, 255, 0, 200), batch=batch)
arc2 = pyglet.shapes.Arc(center_x, center_y, radius, None, end_angle, start_angle, False, 1, (255, 0, 0, 255), batch=batch)
#circle = pyglet.shapes.Circle(width//2, height//2, 50, segments, GREEN, batch=batch)


def is_point_in_arc(x, y, center_x, center_y, radius, thickness, start_angle, end_angle):
    global progression

    # Calculate distance between cursor and center of the arc
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    
    # Check if distance is within the inner and outer radii of the arc
    inner_radius = radius - (thickness / 2)
    outer_radius = radius + (thickness / 2)
    
    inner_r_text.text = ('Inner radius: {:.1f}'.format(inner_radius))
    outer_r_text.text = ('Outer radius: {:.1f}'.format(outer_radius))

    if inner_radius <= distance <= outer_radius:
        # Calculate angle between center and point
        angle = math.atan2(y - center_y, x - center_x) * (180 / math.pi)
        angle = math.radians(angle)
        if angle < 0:
            angle += 2 * math.pi
        
        # Check if angle is within the angular range of the arc
        if start_angle <= end_angle:
            progression = angle
            arc_loading.angle = progression
            return start_angle <= angle <= end_angle
        else:
            # Handle cases where the arc wraps around
            return angle >= start_angle or angle <= end_angle
    return False

inside_label = pyglet.text.Label('Inside',
                                 font_name='Valken',
                                 font_size=24,
                                 x=window.width//2,
                                 y=window.height - 480,
                                 anchor_x='center',
                                 anchor_y='center',
                                 color=(200, 0, 0, 255))      



#####################################################################################
##                                       APP                                       ##
#####################################################################################
@window.event
def on_draw():
    pyglet.gl.glClearColor(1, 1, 1, 1)
    window.clear()

    for point in points_arr: 
        x, y = point
        circle_red = pyglet.shapes.Circle(x, y, 10, color=(200, 0, 0, 100), batch=batch)
        circle_red.draw()

    
    batch.draw()
    points_label.draw()
    cursor_position_text.draw()
    line_length_text.draw()
    angle_text.draw()
    outer_r_text.draw()
    inner_r_text.draw()

    if inside_bool:
        inside_label.draw()


pyglet.app.run()