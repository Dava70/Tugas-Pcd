import cv2
import numpy as np

#baca citra dalam grayscale
image = cv2.imread('macan.jpg', cv2.IMREAD_GRAYSCALE)

#terapkan thresholding global
ret, thresh = cv2.threshold(image, 127, 225, cv2.THRESH_BINARY)

#tampilkan hasil segmentasi
cv2.imshow('Threshold Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()