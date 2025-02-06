import cv2
import numpy as np

#baca citra dalam grayscale
image = cv2.imread('naruto.jpg', cv2.IMREAD_COLOR)

#terapkan harris corner detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

#tingkatkan sudut yang terdeteksi
image[corners > 0.01 * corners.max()] = [0, 0, 255]

#tampilkan hasil deteksi sudut
cv2.imshow('Harris Corner Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()