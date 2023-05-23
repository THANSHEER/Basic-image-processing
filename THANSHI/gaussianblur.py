import cv2

# Load an image from file
image = cv2.imread('trees.jpg')

# Display the image
cv2.imshow('Image', image)


# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the blurred image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
