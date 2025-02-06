import cv2
import numpy as np 

#membaca gambar biner
image = cv2.imread('bruno.jpg', 0)

#mendefinisikan kernel
kernel = np.ones((5, 5), np.uint8)

#melakukan dilasi dan erosi
dilated_image = cv2.dilate(image, kernel, iterations=1)
eroded_image = cv2.erode(image, kernel, iterations=1)

#menampilkan hasil
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()