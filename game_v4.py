import pyglet
import random

class goalCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.inner_radius = radius-5
        self.color = (255, 255, 255, 200)
        self.inner_color = (50,205,50, 200)

class cursor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class pointSystem:
    def __init__(self):
        self.goals = 0
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


class Game:
    def __init__(self):
        self.new_window = pyglet.window.Window(width=1020, height=780)
        self.new_window.set_vsync(False)
        self.fps_display = pyglet.window.FPSDisplay(self.new_window)
        self.cursor = cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)

        self.goalCircles = []
        self.create_goal()

        self.counter = 0    # counts how many goals have been reached, and is used to determine the shrink rate (starts at 0)

        self.point_system = pointSystem() # Create a point system object

        self.new_window.push_handlers(self)

        self.new_window.set_mouse_visible(False)

    def draw(self):
        for goal in self.goalCircles:
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
        for goal in self.goalCircles:
            # Goal is made smaller when cursor is inside the goal circle

            if (self.cursor.x - goal.x)**2 + (self.cursor.y - goal.y)**2 <= (goal.radius - self.cursor.radius)**2:
                self.goalCircles.remove(goal)
                self.add_new_goal(goal) # Create a new goal

                self.point_system.update_streak() # Update the streak (needs to be before updating points)
                self.point_system.update_points() # Update the points

                if self.counter >= 12*12:
                    #do nothing
                    pass
                else:
                    self.counter += 1
                break
            else:
                self.animate_goal(goal,dt)  # Animate the goal circle

    def create_goal(self):
        x = random.randint(50, self.new_window.width-50)
        y = random.randint(50, self.new_window.height-50)
        radius = 100
        goal = goalCircle(x, y, radius)
        self.goalCircles.append(goal)

    def add_new_goal(self, goal):
         #migth be better to just move the goal to a new location instead of creating a new one
        x = random.randint(50, self.new_window.width-50)
        y = random.randint(50, self.new_window.height-50)

        radius = 100
        goal = goalCircle(x, y, radius)
        self.goalCircles.append(goal)

    def animate_goal(self,goal,dt):
        print(self.counter)
        shrink_rate = min(self.counter / 12, 12)  # Define the shrink rate based on points (max 8)

        # Shrink the goal circle
        goal.inner_radius -= shrink_rate

        # Calculate the ratio of inner radius to outer radius   (goes from 0 to 1 as inner radius decreases)
        ratio = goal.inner_radius / goal.radius

        # Interpolate color gradually from green to red based on the ratio
        goal.inner_color = (
            int(254 * (1 - ratio)),             # Red component decreases
            int(180 * ratio),                   # Green component increases
            int(73 * ratio),                    # Blue component increases
            255                                 # Alpha remains constant
        )

        # If goal is completely gone, remove it and create a new goal
        if goal.inner_radius <= 0:
            self.point_system.reset_streak()
            self.goalCircles.remove(goal)
            self.counter //= 2              # Reset the counter to half of the previous value (rounded down)
            self.add_new_goal(goal)
            # self.timer.reset()


# if __name__ == "__main__":
#     game = Game()
#     pyglet.app.run(interval=1/120.0)

