import cv2
import numpy as np
from matplotlib import pyplot as plt
#baca citra gray
image = cv2.imread('lutfi.jpg', cv2.IMREAD_GRAYSCALE)

#deteksi tepi menggunakan sobel
scharr_X = cv2.Scharr(image, cv2.CV_64F, 1, 0) 
scharr_X_abs = np.uint8(np.absolute(scharr_X)) 


scharr_Y = cv2.Scharr(image, cv2.CV_64F,0, 1) 
scharr_Y_abs = np.uint8(np.absolute(scharr_Y)) 

scahrr_XY_combined = cv2.bitwise_or(scharr_Y_abs,scharr_X_abs)

#tamilkan hasil
cv2.imshow('scharr_Y', scahrr_XY_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()