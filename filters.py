# Python program to explain cv2.imshow() method 

# importing cv2 
import cv2 as cv

# path 
path = r'test-images\ball.jpg'

# Reading an image in default mode 
image = cv.imread(path) 

# Window name in which image is displayed 
window_name = 'image'

# Convert the image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Using cv2.imshow() method 
# Displaying the grayscale image 
cv.imshow(window_name, gray_image) 

# waits for user to press any key 
# (this is necessary to avoid Python kernel from crashing) 
cv.waitKey(0) 

# closing all open windows 
cv.destroyAllWindows()
