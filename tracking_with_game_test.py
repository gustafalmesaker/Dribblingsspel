# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import pyglet
import random
import math
from Read_file import read_csv

#=======================Tracking==============================
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args()) 

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
blueLower = (87, 54, 78)
blueUpper = (104, 252, 255)

colorLower = blueLower
colorUpper = blueUpper
pts = deque(maxlen=args["buffer"])

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    vs = VideoStream(src=1).start()
# otherwise, grab a reference to the video file
else:
    print("Video not found")

# allow the camera or video file to warm up
time.sleep(2.0)

#================ Sounds =================
audioPlayer = pyglet.media.Player()
audioPlayer.volume = 0.4
audioPlayer.loop = True
sound_music = pyglet.resource.media("soundtrack/meny_music.mp3")
audioPlayer.queue(sound_music)
sound_goal = pyglet.resource.media("soundtrack/goal.mp3")
sound_goal2 = pyglet.resource.media("soundtrack/goal.mp3")
sound_streak = pyglet.resource.media("soundtrack/streak.mp3")
sound_miss = pyglet.resource.media("soundtrack/miss.mp3") 

audioPlayer.play()
#================animations===================
animation = pyglet.image.load_animation('images/explosion.gif')
sprite = pyglet.sprite.Sprite(animation)




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
        if self.streak % 2 == 0: 
            sound_goal.play()   
        else:                       # sound does not play everytime if to fast (quickfix)
            sound_goal2.play()


    def reset_points(self):
        self.points = 0

    def reset_streak(self):
        self.streak = 0
        sound_miss.play()


class Game():
    def __init__(self):
        config = pyglet.gl.Config(double_buffer=True, depth_size=24)
        self.new_window = pyglet.window.Window(width=1920, height=1080,style =pyglet.window.Window.WINDOW_STYLE_BORDERLESS, caption="Game", vsync=False, config=config )
        #self.new_window.set_vsync(False)
        self.fps_display = pyglet.window.FPSDisplay(self.new_window)
        self.cursor = cursor(x=self.new_window.width//2, y=self.new_window.height//2, radius=20)

        self.new_window.push_handlers(self)
        self.new_window.set_mouse_visible(False)
        

        # Read data from the CSV file
        self.exercises, self.positions_from_file = read_csv('exercise_positions.csv')
        self.hash = 0
        self.goalCircles = []

        self.is_goal = False

        self.counter = 0    # counts how many goals have been reached, and is used to determine the shrink rate (starts at 0)
        self.point_system = pointSystem() # Create a point system object

        self.trackcounter = 0

        self.ball_center = (self.new_window.width, self.new_window.height)



    def initial_position(self):
         #random number between 1 and 11
        self.hash = random.randint(0, 10)

        #print("New hash: ", self.hash)

        pos1 = (150, self.new_window.height-150)
        pos2 = (self.new_window.width//2, self.new_window.height-150)
        pos3 = (self.new_window.width-150, self.new_window.height-150)

        pos4 = (150, 150)
        pos5 = (self.new_window.width//2, 150)
        pos6 = (self.new_window.width-150, 150)

        
        for position in self.positions_from_file[self.hash]:
            position = int(position)

            if position == 1:
                self.add_new_goal(pos1)
            elif position == 2:
                self.add_new_goal(pos2)
            elif position == 3:
                self.add_new_goal(pos3)
            elif position == 4:
                self.add_new_goal(pos4)
            elif position == 5:
                self.add_new_goal(pos5)
            elif position == 6:
                self.add_new_goal(pos6)
            else:
                pass


    def tracking(self):
        # Read the current frame
        frame = vs.read()

        # Preprocess the frame
        frame = frame[1] if args.get("video", False) else frame
        frame = imutils.resize(frame, width=640)
        x0 = 200 # 400px left of center
        y0 = 250 # 400px above center
        x1 = 510 # 400px right of center
        y1 = 420 # 400px below center
        frame = frame[y0:y1, x0:x1] # slicing	    

	        
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # Create a mask to isolate the ball color
        mask = cv2.inRange(hsv, colorLower, colorUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # Find contours in the mask
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # Initialize variables to store the center of the ball
        new_center = self.ball_center

        # Only proceed if at least one contour was found
        if len(cnts) > 0:
            # Find the largest contour in the mask
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # Compute the area of the contour
            area = cv2.contourArea(c)

            # Set a threshold for the minimum contour area to consider
            min_area_threshold = 50

            # If the contour area is above the threshold, consider it as the ball
            if area > min_area_threshold:
                # Compute the centroid of the contour
                M = cv2.moments(c)
                new_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            

        # Smooth movement: Linear interpolation between previous and current positions
        if new_center is not None:
            # Define the smoothing factor (how much influence the new position has)
            smoothing_factor = 0.5
            # Compute the interpolated position
            interpolated_center = (int((1 - smoothing_factor) * self.ball_center[0] + smoothing_factor * new_center[0]),
                                int((1 - smoothing_factor) * self.ball_center[1] + smoothing_factor * new_center[1]))
            # Update the ball center
            self.ball_center = interpolated_center
            # Return the center of the ball
            self.ball_position(interpolated_center[0], interpolated_center[1])



    def field(self):
        line_width = 15
        dot_radius = 25

        fieldL = []
        fieldB = pyglet.graphics.Batch()

        color_default = (125, 125, 130)
        color_active = (2, 189, 20)
        #find what find unique values in self.positions_from_file[self.hash]
        unique_positions = set(self.positions_from_file[self.hash])
        color_field = [color_default, color_default, color_default, color_default, color_default, color_default, color_default, color_default, color_default, color_default, color_default, color_default]

        #change color lines based on if they are connected between the positions in unique_positions
        if '1' in unique_positions and '2' in unique_positions:
            color_field[0] = color_active
        if '2' in unique_positions and '3' in unique_positions:
            color_field[2] = color_active
        if '3' in unique_positions and '6' in unique_positions:
            color_field[3] = color_active
        if '6' in unique_positions and '5' in unique_positions:
            color_field[4] = color_active
        if '5' in unique_positions and '4' in unique_positions:
            color_field[5] = color_active
        if '4' in unique_positions and '1' in unique_positions:
            color_field[6] = color_active
        if '2' in unique_positions and '5' in unique_positions:
            color_field[7] = color_active
        if '1' in unique_positions and '5' in unique_positions:
            color_field[8] = color_active
        if '5' in unique_positions and '3' in unique_positions:
            color_field[9] = color_active

        #color of the dots
        dot_color = [color_default, color_default, color_default, color_default, color_default, color_default]
        if '1' in unique_positions:
            dot_color[0] = color_active
        if '2' in unique_positions:
            dot_color[1] = color_active
        if '3' in unique_positions:
            dot_color[2] = color_active
        if '4' in unique_positions:
            dot_color[3] = color_active
        if '5' in unique_positions:
            dot_color[4] = color_active
        if '6' in unique_positions:
            dot_color[5] = color_active

        pos1 = (150, self.new_window.height-150)
        pos2 = (self.new_window.width//2, self.new_window.height-150)
        pos3 = (self.new_window.width-150, self.new_window.height-150)

        pos4 = (150, 150)
        pos5 = (self.new_window.width//2, 150)
        pos6 = (self.new_window.width-150, 150)

        #draw outer rectangle
        fieldL.append(pyglet.shapes.Rectangle(x=0, y=0, width=self.new_window.width, height=self.new_window.height, color=(2, 189, 20), batch = fieldB))
        #draw inner rectangle
        fieldL.append(pyglet.shapes.Rectangle(x=10, y=10, width=self.new_window.width-20, height=self.new_window.height-20, color=(0, 0, 0),batch=fieldB))
    
        # Draw lines between the position pos1 and pos2
        fieldL.append(pyglet.shapes.Line(x=pos1[0], y=pos1[1], x2=pos2[0], y2=pos2[1], width=line_width, color=color_field[0], batch=fieldB))

        # Draw lines between the position pos2 and pos3
        fieldL.append(pyglet.shapes.Line(x=pos2[0], y=pos2[1], x2=pos3[0], y2=pos3[1], width=line_width, color=color_field[2], batch=fieldB))

        # Draw lines between the position pos3 and pos6
        fieldL.append(pyglet.shapes.Line(x=pos3[0], y=pos3[1], x2=pos6[0], y2=pos6[1], width=line_width, color=color_field[3], batch=fieldB))

        #Draw lines between the position pos6 and pos5
        fieldL.append(pyglet.shapes.Line(x=pos6[0], y=pos6[1], x2=pos5[0], y2=pos5[1], width=line_width, color=color_field[4], batch=fieldB))

        # Draw lines between the position pos5 and pos4
        fieldL.append(pyglet.shapes.Line(x=pos5[0], y=pos5[1], x2=pos4[0], y2=pos4[1], width=line_width, color=color_field[5], batch=fieldB))

        # Draw lines between the position pos4 and pos1
        fieldL.append(pyglet.shapes.Line(x=pos4[0], y=pos4[1], x2=pos1[0], y2=pos1[1], width=line_width, color=color_field[6], batch=fieldB))


        #draw lines between the position pos2 and pos5
        fieldL.append(pyglet.shapes.Line(x=pos2[0]-(line_width/2), y=pos2[1], x2=pos5[0]-(line_width/2), y2=pos5[1], width=line_width, color=color_field[7], batch=fieldB))
        # Draw lines between the position pos1 and pos5
        fieldL.append(pyglet.shapes.Line(x=pos1[0]-(line_width/2), y=pos1[1], x2=pos5[0]-(line_width/2), y2=pos5[1], width=line_width, color=color_field[8], batch=fieldB))
        # Draw lines between the position pos5 and pos3
        fieldL.append(pyglet.shapes.Line(x=pos5[0]+(line_width/2), y=pos5[1], x2=pos3[0]+(line_width/2), y2=pos3[1], width=line_width, color=color_field[9], batch=fieldB))

        #draw dots at the positions
        fieldL.append(pyglet.shapes.Circle(x=pos1[0], y=pos1[1], radius=dot_radius, color=dot_color[0],batch=fieldB))
        fieldL.append(pyglet.shapes.Circle(x=pos2[0], y=pos2[1], radius=dot_radius, color=dot_color[1],batch=fieldB))
        fieldL.append(pyglet.shapes.Circle(x=pos3[0], y=pos3[1], radius=dot_radius, color=dot_color[2],batch=fieldB))
        fieldL.append(pyglet.shapes.Circle(x=pos4[0], y=pos4[1], radius=dot_radius, color=dot_color[3],batch=fieldB))
        fieldL.append(pyglet.shapes.Circle(x=pos5[0], y=pos5[1], radius=dot_radius, color=dot_color[4],batch=fieldB))
        fieldL.append(pyglet.shapes.Circle(x=pos6[0], y=pos6[1], radius=dot_radius, color=dot_color[5],batch=fieldB))
        fieldB.draw()   

    def draw(self):
        # Draw the field
        self.field()
        drawL= []
        drawB = pyglet.graphics.Batch()

        # Draw the first goal in the list
        if self.goalCircles:
            goal = self.goalCircles[0]
            # Outer circle of goal
            drawL.append(pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius, color=goal.color, batch=drawB))
            drawL.append(pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.radius-5, color=(0, 0, 0),batch=drawB))

            # Inner circle of goal
            drawL.append(pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.inner_radius, color=goal.inner_color, batch=drawB))
            drawL.append(pyglet.shapes.Circle(x=goal.x, y=goal.y, radius=goal.inner_radius-5, color=(0, 0, 0), batch=drawB))
            

        # Cursor
        #drawL.append(pyglet.shapes.Circle(x=self.cursor.x, y=self.cursor.y, radius=self.cursor.radius, batch=drawB))

        #Points display in top midde of screen
        drawL.append(pyglet.text.Label("Points: " + str(self.point_system.points), font_name= 'Times New Roman', font_size=18, x=self.new_window.width//2 -100, y=self.new_window.height-50, anchor_x='center', batch=drawB))

        #Streak display next to points
        drawL.append(pyglet.text.Label("Streak: " + str(self.point_system.streak), font_name= 'Times New Roman', font_size=18, x=self.new_window.width//2 + 100, y=self.new_window.height-50, anchor_x='center', batch=drawB))
        drawB.draw()
        self.animation_effect()


    def on_draw(self):
        self.new_window.clear()
        self.draw()
        self.fps_display.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.x = x
        self.cursor.y = y

    def ball_position(self, x, y):
        #normalize the position of the ball 170x310 to 1920x1080
        x = x*5.8
        y = y*7.2
       

        #Scale the position of the ball to the window size ,left_down: (500, 260), left_up : (500,420), right_down: (240, 260), right_up: (240, 420)

        # if x > 500 and y > 260 and y < 420:
        #     self.cursor.x = 150
        #     self.cursor.y = 150
        # elif x < 500 and x > 240 and y > 260 and y < 420:
        #     self.cursor.x = self.new_window.width//2
        #     self.cursor.y = 150
        # elif x < 240 and y > 260 and y < 420:
        #     self.cursor.x = self.new_window.width-150
        #     self.cursor.y = 150
        # elif x > 500 and y > 420:
        #     self.cursor.x = 150
        #     self.cursor.y = self.new_window.height-150
        # elif x < 500 and x > 240 and y > 420:
        #     self.cursor.x = self.new_window.width//2
        #     self.cursor.y = self.new_window.height-150  
        # elif x < 240 and y > 420:
        #     self.cursor.x = self.new_window.width-150
        #     self.cursor.y = self.new_window.height-150
        # else:
        #     self.cursor.x = x
        #     self.cursor.y = y

       
        self.cursor.x = (self.new_window.width - (x))
        self.cursor.y = y


    def update(self, dt):

        self.tracking()

        self.trackcounter += 1

        if self.goalCircles:
            goal = self.goalCircles[0]

            # Goal is made smaller when cursor is inside the goal circle

            if (self.cursor.x - goal.x)**2 + (self.cursor.y - goal.y)**2 <= (goal.radius - self.cursor.radius)**2:
                
                self.is_goal = True
                
                sprite.x = goal.x-225
                sprite.y = goal.y-250

                self.goalCircles.remove(goal) # Remove the goal circlel
                self.point_system.update_streak() # Update the streak (needs to be before updating points)
                self.point_system.update_points() # Update the points

                if self.counter <= 12*12:
                   self.counter += 1
                    
            else:
                self.animate_goal(goal,dt)  # Animate the goal circle
        else:
            if self.point_system.streak > 0:
                sound_streak.play()
            self.initial_position()

    def add_new_goal(self, pos):
            radius = 150
            goal = goalCircle(pos, radius)
            self.goalCircles.append(goal)
        

    def animate_goal(self,goal,dt):
        shrink_rate = min(self.counter / (12*6), 12)  # Define the shrink rate based on points (max 8)

        # Shrink the goal circle
        goal.inner_radius -= shrink_rate

        # Calculate the ratio of inner radius to outer radius   (goes from 0 to 1 as inner radius decreases)
        ratio = (goal.inner_radius+5) / goal.radius
        #print(ratio)

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
            self.goalCircles = []    # Remove the goal circle
            self.counter //= 2              # Reset the counter to half of the previous value (rounded down)
            
    def animation_effect(self):
        if self.is_goal == True:
            sprite.draw()
            #if sprite has played the gif once, then set is_goal to False
            if sprite._frame_index == len(sprite._animation.frames)-1:
                self.is_goal = False
                sprite._frame_index = 0

if __name__ == "__main__":
    game = Game()
    pyglet.clock.schedule_interval(game.update, 1.0/ 60.0)
    pyglet.app.run()