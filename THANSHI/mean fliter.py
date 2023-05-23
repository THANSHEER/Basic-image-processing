import numpy as np
import pandas as pd
import cv2
# Reading the Image
img = cv2.imread('example1.jpeg',cv2.IMREAD_UNCHANGED)
kernel = np.ones((10,10),np.float32)/25
meanFilter = cv2.filter2D(img,-1,kernel)
cv2.imshow("Mean Filtered Image",np.hstack((img, meanFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()