import cv2

# Load an image from file
image = cv2.imread('trees.jpg')

# Display the image
cv2.imshow('Image', image)


# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)


# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the blurred image
cv2.imshow('Blurred Image', blurred_image)

# Convert the grayscale image to binary using a threshold value of 128
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow('Binary Image', binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()