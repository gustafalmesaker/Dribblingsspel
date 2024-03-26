import cv2 as cv
import numpy as np
import time
from collections import deque

VideoCapture = cv.VideoCapture(0)

prevCircles = deque(maxlen=24)  # Queue to store previous circles
dist = lambda x1, y1, x2, y2: (x1 - x2)**2 + (y1 - y2)**2

# Variables for FPS calculation
frame_count = 0
start_time = time.time()

while True:
    ret, frame = VideoCapture.read()
    if not ret:
        break

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (17, 17), 0)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=75, maxRadius=400)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            if prevCircles:
                prevCircle = prevCircles[-1]
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircles.append(chosen)

        # Draw previous circles with decreasing opacity
        for idx, circle in enumerate(prevCircles):
            opacity = 0.5 - (idx + 1) / (2 * len(prevCircles))  # Adjust opacity based on position in queue
            overlay = frame.copy()
            cv.circle(overlay, (circle[0], circle[1]), circle[2], (255, 0, 255), -1)  # Draw filled circle
            frame = cv.addWeighted(overlay, opacity, frame, 1 - opacity, 0)

    cv.imshow("circles", cv.flip(frame, 1))
    cv.imshow("blur", cv.flip(blurFrame, 1))
    frame_count += 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    # Calculate FPS
    if time.time() - start_time >= 1:
        fps = frame_count / (time.time() - start_time)
        print(f"FPS: {fps:.2f}")
        # Reset variables for the next FPS calculation
        frame_count = 0
        start_time = time.time()

VideoCapture.release()
cv.destroyAllWindows()
