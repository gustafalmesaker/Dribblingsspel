import cv2

img = cv2.imread('test-images/ball.jpg')
#cv2.imshow('Original Image', img)
#cv2.waitKey(0)

offset = 40

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range = (43-offset, 173-offset, 147-offset)  # Adjust these values as needed
upper_range = (43+offset, 173+offset, 147+offset)  # Adjust these values as needed
mask = cv2.inRange(hsv_img, lower_range, upper_range)
color_image = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Coloured Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
