import cv2
import numpy as np

# Load an image
image = cv2.imread('nature.jpeg')

# Define the translation matrix
tx = 50  # translation in the x-axis
ty = 30  # translation in the y-axis
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the translation to the image
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Display the original and translated images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
