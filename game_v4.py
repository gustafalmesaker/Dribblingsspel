import pyglet
import random
from Read_file import read_csv

class goalCircle:
    def __init__(self, pos, radius):
        self.x, self.y = pos
        self.radius = radius
        self.inner_radius = radius-5
        self.color = (2, 189, 20, 255)
        self.inner_color = (50,205,50)

class cursor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class pointSystem:
    def __init__(self):
        self.points = 0
        self.streak = 0

    def update_points(self):

        points = 1 # Base points for each goal

        if points > 2000:   # Points are calculated based on the number of goals
            points += 10
        elif points > 1000:
            points += 5
        elif points > 300:
            points += 2
        elif points > 100:
            points += 1

        if self.streak > 100:    # Points are calculated based on the streak
            points += 100
        elif self.streak > 50:
            points += 25
        elif self.streak > 25:
            points += 10
        elif self.streak > 15:
            points += 5
        elif self.streak > 10:
            points += 2

        self.points += points

    def update_streak(self):
        self.streak += 1

    def reset_points(self):
        self.points = 0

    def reset_streak(self):
        self.streak = 0


class Game():
    def __init__(self):
        self.new_window = pyglet.window.Window(width=1920, height=1080, caption="Game", resizable=False )
        self.new_window.set_vsync(False)
        self.fps_display = pyglet.window.FPSDisplay(self.new_window)
        self.cursor = cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)
        
        # Read data from the CSV file
        self.exercises, self.positions_from_file = read_csv('exercise_positions.csv')
        self.hash = 0
        self.goalCircles = []


        self.counter = 0    # counts how many goals have been reached, and is used to determine the shrink rate (starts at 0)

        self.point_system = pointSystem() # Create a point system object

        self.new_window.push_handlers(self)

        self.new_window.set_mouse_visible(False)

    def initial_position(self):
         #random number between 1 and 11
        self.hash = random.randint(0, 10)

        print("New hash: ", self.hash)

        pos1 = (150, self.new_window.height-150)
        pos2 = (self.new_window.width//2, self.new_window.height-150)
        pos3 = (self.new_window.width-150, self.new_window.height-150)

        pos4 = (150, 150)
        pos5 = (self.new_window.width//2, 150)
        pos6 = (self.new_window.width-150, 150)

        
        for position in self.positions_from_file[self.hash]:
            #print("entered for loop")
            #print(position)

            if position == "1":
                self.add_new_goal(pos1)
            elif position == "2":
                self.add_new_goal(pos2)
            elif position == "3":
                self.add_new_goal(pos3)
            elif position == "4":
                self.add_new_goal(pos4)
            elif position == "5":
                self.add_new_goal(pos5)
            elif position == "6":
                self.add_new_goal(pos6)
            else:
                pass

            
    def field(self):
        line_width = 15
        dot_radius = 25


        pos1 = (150, self.new_window.height-150)
        pos2 = (self.new_window.width//2, self.new_window.height-150)
        pos3 = (self.new_window.width-150, self.new_window.height-150)

        pos4 = (150, 150)
        pos5 = (self.new_window.width//2, 150)
        pos6 = (self.new_window.width-150, 150)

        #draw outer rectangle
        pyglet.shapes.Rectangle(x=0, y=0, width=self.new_window.width, height=self.new_window.height, color=(2, 189, 20)).draw()
        #draw inner rectangle
        pyglet.shapes.Rectangle(x=10, y=10, width=self.new_window.width-20, height=self.new_window.height-20, color=(0, 0, 0)).draw()

        # Draw lines between the position pos1 and pos3
        pyglet.shapes.Line(x=pos1[0], y=pos1[1], x2=pos3[0], y2=pos3[1], width=line_width, color=(2, 189, 20)).draw()
        # Draw lines between the position pos3 and pos6
        pyglet.shapes.Line(x=pos3[0], y=pos3[1], x2=pos6[0], y2=pos6[1], width=line_width, color=(2, 189, 20)).draw()
        # Draw lines between the position pos6 and pos4
        pyglet.shapes.Line(x=pos6[0], y=pos6[1], x2=pos4[0], y2=pos4[1], width=line_width, color=(2, 189, 20)).draw()
        # Draw lines between the position pos4 and pos1
        pyglet.shapes.Line(x=pos4[0], y=pos4[1], x2=pos1[0], y2=pos1[1], width=line_width, color=(2, 189, 20)).draw()

        #draw lines between the position pos2 and pos5
        pyglet.shapes.Line(x=pos2[0], y=pos2[1], x2=pos5[0], y2=pos5[1], width=line_width, color=(2, 189, 20)).draw()
        
 
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

          

    def draw(self):
        # Draw the field
        self.field()
        # Draw the first goal in the list
        if self.goalCircles:
            goal = self.goalCircles[0]
            # Outer circle of goal
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius, color=goal.color).draw()
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius-5, color=(0, 0, 0)).draw()

            # Inner circle of goal
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.inner_radius, color=goal.inner_color).draw()
            pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.inner_radius-5, color=(0, 0, 0)).draw()
            

        # Cursor
        pyglet.shapes.Circle(x=self.cursor.x, y=self.cursor.y, radius=self.cursor.radius).draw()

        #Points display in top midde of screen
        pyglet.text.Label("Points: " + str(self.point_system.points), font_name= 'Times New Roman', font_size=18, x=self.new_window.width//2 -100, y=self.new_window.height-50, anchor_x='center').draw()

        #Streak display next to points
        pyglet.text.Label("Streak: " + str(self.point_system.streak), font_name= 'Times New Roman', font_size=18, x=self.new_window.width//2 + 100, y=self.new_window.height-50, anchor_x='center').draw()

    def on_draw(self):
        self.new_window.clear()
        self.draw()
        self.fps_display.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.x = x
        self.cursor.y = y

    def update(self, dt):
        #print(self.timer.time_remaining)
        if self.goalCircles:
            goal = self.goalCircles[0]

            # Goal is made smaller when cursor is inside the goal circle

            if (self.cursor.x - goal.x)**2 + (self.cursor.y - goal.y)**2 <= (goal.radius - self.cursor.radius)**2:

                self.goalCircles.remove(goal) # Remove the goal circlel
                self.point_system.update_streak() # Update the streak (needs to be before updating points)
                self.point_system.update_points() # Update the points

                if self.counter <= 12*12:
                   self.counter += 1
                    
            else:
                self.animate_goal(goal,dt)  # Animate the goal circle
        else:
            self.initial_position()

    def add_new_goal(self, pos):
            radius = 100
            goal = goalCircle(pos, radius)
            self.goalCircles.append(goal)
        

    def animate_goal(self,goal,dt):
        shrink_rate = min(self.counter / (12*6), 12)  # Define the shrink rate based on points (max 8)

        # Shrink the goal circle
        goal.inner_radius -= shrink_rate

        # Calculate the ratio of inner radius to outer radius   (goes from 0 to 1 as inner radius decreases)
        ratio = (goal.inner_radius+5) / goal.radius
        print(ratio)

        # Interpolate color gradually from green to red based on the ratio
        goal.inner_color = (
            int(2 + ((1-ratio) * (253))),     # Red component increases
            int(189 - ((1-ratio)*189)),           # Green component decreases
            int(20 - ((1-ratio) *20)),            # Blue component decreases
            255                                 # Alpha remains constant
        )

        # If goal is completely gone, remove it and create a new goal
        if goal.inner_radius <= 0:

            self.point_system.reset_streak() # Reset the streak (reduces points to base value)
            self.goalCircles.remove(goal)    # Remove the goal circle
            self.counter //= 2              # Reset the counter to half of the previous value (rounded down)
            


# if __name__ == "__main__":
#     game = Game()
#     pyglet.app.run(interval=1/120.0)

