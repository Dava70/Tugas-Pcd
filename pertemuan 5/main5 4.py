import cv2
import numpy as np

#membaca gambar
image = cv2.imread('macan.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#thresholding
ret, thresh = cv2.threshold(gray, 0, 225, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

#dilasi untuk menonjolkan latar belakang
sure_bg = cv2.dilate(opening, kernel, iterations=3)

#menghitung jarak dari foreground
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

#menandai area yang tidak jelas (unknown region)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

#memamdai komponen yang terhubung
ret, markers = cv2.connectedComponents(sure_fg)

#menambahkan satu untuk memastikan latar belakang tidak 0
markers = markers + 1
markers[unknown == 255] = 0

#menerapkan algoritma watershed
markers = cv2.watershed(image, markers)
image[markers == -1] = [255, 0, 0]

#menampilkan hasil
cv2.imshow('Watershed Sementation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()