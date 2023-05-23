import cv2

# Load an image
image = cv2.imread('character.jpeg')

# Flip the image horizontally
flipped_horizontally = cv2.flip(image, 1)

# Flip the image vertically
flipped_vertically = cv2.flip(image, 0)

# Display the original and flipped images
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Horizontally', flipped_horizontally)
cv2.imshow('Flipped Vertically', flipped_vertically)
cv2.waitKey(0)
cv2.destroyAllWindows()
