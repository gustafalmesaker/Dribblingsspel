import pyglet

def draw_game_field(window):
    line_width = 15
    dot_radius = 25


    pos1 = (150, window.height-150)
    pos2 = (window.width//2, window.height-150)
    pos3 = (window.width-150, window.height-150)

    pos4 = (150, 150)
    pos5 = (window.width//2, 150)
    pos6 = (window.width-150, 150)

    #draw outer rectangle
    pyglet.shapes.Rectangle(x=0, y=0, width=window.width, height=window.height, color=(2, 189, 20)).draw()
    #draw inner rectangle
    pyglet.shapes.Rectangle(x=10, y=10, width=window.width-20, height=window.height-20, color=(0, 0, 0)).draw()

    # Draw lines between the position pos1 and pos3
    pyglet.shapes.Line(x=pos1[0], y=pos1[1], x2=pos3[0], y2=pos3[1], width=line_width, color=(2, 189, 20)).draw()
    # Draw lines between the position pos3 and pos6
    pyglet.shapes.Line(x=pos3[0], y=pos3[1], x2=pos6[0], y2=pos6[1], width=line_width, color=(2, 189, 20)).draw()
    # Draw lines between the position pos6 and pos4
    pyglet.shapes.Line(x=pos6[0], y=pos6[1], x2=pos4[0], y2=pos4[1], width=line_width, color=(2, 189, 20)).draw()
    # Draw lines between the position pos4 and pos1
    pyglet.shapes.Line(x=pos4[0], y=pos4[1], x2=pos1[0], y2=pos1[1], width=line_width, color=(2, 189, 20)).draw()

    #draw lines between the position pos2 and pos5
    pyglet.shapes.Line(x=pos2[0]-8, y=pos2[1], x2=pos5[0]-8, y2=pos5[1], width=line_width, color=(2, 189, 20)).draw()
    

    # Draw lines between the position pos1 and pos5
    pyglet.shapes.Line(x=pos1[0], y=pos1[1], x2=pos5[0], y2=pos5[1], width=line_width, color=(2, 189, 20)).draw()
    # Draw lines between the position pos5 and pos3
    pyglet.shapes.Line(x=pos5[0], y=pos5[1], x2=pos3[0], y2=pos3[1], width=line_width, color=(2, 189, 20)).draw()

    #draw dots at the positions
    pyglet.shapes.Circle(x=pos1[0], y=pos1[1], radius=dot_radius, color=(2, 189, 20)).draw()
    pyglet.shapes.Circle(x=pos2[0], y=pos2[1], radius=dot_radius, color=(2, 189, 20)).draw()
    pyglet.shapes.Circle(x=pos3[0], y=pos3[1], radius=dot_radius, color=(2, 189, 20)).draw()
    pyglet.shapes.Circle(x=pos4[0], y=pos4[1], radius=dot_radius, color=(2, 189, 20)).draw()
    pyglet.shapes.Circle(x=pos5[0], y=pos5[1], radius=dot_radius, color=(2, 189, 20)).draw()
    pyglet.shapes.Circle(x=pos6[0], y=pos6[1], radius=dot_radius, color=(2, 189, 20)).draw()