import cv2
import numpy as np

#membaca gambar dalam grayscale
image = cv2.imread('macan.jpg', 0)

#menerapkan thresholding
ret, thres_image = cv2.threshold(image, 127, 225, cv2.THRESH_BINARY)

#menampilkan hasil
cv2.imshow('Thresholded Image', thres_image)
cv2.waitKey(0)
cv2.destroyAllWindows()