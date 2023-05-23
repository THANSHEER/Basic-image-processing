import numpy as np
import pandas as pd
import cv2
# Reading the Image
img = cv2.imread('example.jpeg',cv2.IMREAD_UNCHANGED)
domainFilter = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.6)
cv2.imshow('Domain Filter',np.hstack((img,domainFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()
