# Python program to explain cv2.imshow() method 

# importing cv2 
import cv2 as cv

# path 
path = r'test-images\ball.jpg'

# Reading an image in default mode 
image = cv.imread(path) 

if image is not None:
    # Split the image into its color channels (BGR)
    b, g, r = cv.split(image)

    # Calculate mean values for each channel
    mean_b = cv.mean(b)[0]
    mean_g = cv.mean(g)[0]
    mean_r = cv.mean(r)[0]

    # Subtract mean from each pixel for each channel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            #b[i][j] -= mean_b
            g[i][j] -= mean_g
            #r[i][j] -= mean_r
    
    # Merge the modified channels back into an image
    modified_image = cv.merge((b, g, r))
    
    # Display the modified image
    cv.imshow("Modified Image", modified_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Error: Unable to read the image.")

# Convert the image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
mod_gray_image = cv.cvtColor(modified_image, cv.COLOR_BGR2GRAY)


# Using cv2.imshow() method 
# Displaying the grayscale image 
cv.imshow('original2gray', gray_image) 
cv.imshow('modded', mod_gray_image)
# waits for user to press any key 
# (this is necessary to avoid Python kernel from crashing) 
cv.waitKey(0) 

# closing all open windows 
cv.destroyAllWindows()
