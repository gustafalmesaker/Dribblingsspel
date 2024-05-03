import pyglet
from read_file import read_csv
import random


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



def draw_goals(window):
    #random number between 1 and 11
    hash = random.randint(0, 10)
    exercises, positions_from_file = read_csv('exercise_positions.csv')

    print("New hash: ", hash)

    pos1 = (150, window.height-150)
    pos2 = (window.width//2, window.height-150)
    pos3 = (window.width-150, window.height-150)

    pos4 = (150, 150)
    pos5 = (window.width//2, 150)
    pos6 = (window.width-150, 150)


    for position in positions_from_file[hash]:
        #print("entered for loop")
        #print(position)

        if position == "1":
            add_goal(pos1)
        elif position == "2":
            add_goal(pos2)
        elif position == "3":
            add_goal(pos3)
        elif position == "4":
            add_goal(pos4)
        elif position == "5":
            add_goal(pos5)
        elif position == "6":
            add_goal(pos6)
        else:
            pass
    
    goal_circles = []

    if goal_circles:
        goal = goal_circles[0]
        # Outer circle of goal
        pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius, color=goal.color).draw()
        pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius-5, color=(0, 0, 0)).draw()

        # Inner circle of goal
        pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.inner_radius, color=goal.inner_color).draw()
        pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.inner_radius-5, color=(0, 0, 0)).draw()
        

    def add_goal(pos):
        goal = Goal_Circle(pos)
        Goal_Circle.append(goal)

    class Goal_Circle:
        def __init__(self, pos):
            self.x, self.y = pos
            self.radius = 50
            self.inner_radius = self.radius-5
            self.color = (2, 189, 20, 255)
            self.inner_color = (50,205,50)


class Goal:
    def __init__(self):
        self.radius = 25
        self.color = (0, 255, 0)  # Initial color (green)
        self.life_span = 100 
        self.spawn_new_goal()
        
    def spawn_new_goal(self):
        # Randomly choose one of six positions across the screen
        self.x = random.choice([640 // 6 * i for i in range(1, 7)])
        self.y = random.randint(self.radius, 640 - self.radius)
        
        
    def update(self, dt):
        self.life_span = self.life_span - 1
        if self.life_span < 0:
            # If the goal has turned completely red, spawn a new one
            self.spawn_new_goal()
        
        interpolation = min(1, self.life_span / 100)
        red_value = int(255 * interpolation)
        self.color = (255 - red_value, red_value, 0)  # Gradually shifts from green to red

    def draw(self):
        # Draw the goal on the screen
        pyglet.shapes.Circle(self.x, self.y, self.radius, color=self.color).draw()