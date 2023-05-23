import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)

# Perform Fourier Transform
f = np.fft.fft2(image)
f_shift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(f_shift))

# Display the original and magnitude spectrum images
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()