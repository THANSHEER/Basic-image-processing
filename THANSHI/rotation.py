import cv2 # importing cv
import imutils


# read an image as input using OpenCV
image = cv2.imread("character.jpeg")

Rotated_image = imutils.rotate(image, angle=45)
Rotated1_image = imutils.rotate(image, angle=90)

# display the image using OpenCV of
# angle 45
cv2.imshow("Rotated", Rotated_image)

# display the image using OpenCV of
# angle 90
cv2.imshow("Rotated", Rotated1_image)

# This is used for To Keep On Displaying
# The Image Until Any Key is Pressed
cv2.waitKey(0)

