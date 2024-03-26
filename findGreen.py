import cv2

def get_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = img_hsv[y, x]
        print("HSV:", pixel)

# Load the image
img = cv2.imread('test-images/ball.jpg')

# Convert image to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display the image
cv2.imshow('Original Image', img)
cv2.setMouseCallback('Original Image', get_hsv)

# Wait for user to select a green pixel
cv2.waitKey(0)
cv2.destroyAllWindows()
