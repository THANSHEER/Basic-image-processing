import numpy as np
import pandas as pd
import cv2
# Reading the Image
img = cv2.imread('example.jpeg',cv2.IMREAD_UNCHANGED)
gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Gaussian Smoothing",np.hstack((img,gaussBlur)))
cv2.waitKey(0)
cv2.destroyAllWindows()