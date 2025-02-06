import cv2
import numpy as np

#baca citra
image = cv2.imread('macan.jpg')

#ubah format citra ke dalam satu dimensi
Z = image.reshape((-1,3))

#ubah tipe data ke float32
Z = np.float32(Z)

#tentukan kriteria dan jumlah cluster
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3 #Misalnya, 3 cluster

#terapkan k-means clustering
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

#konversi hasil kembali ke format citra
center = np.uint8(center)
res = center[label.flatten()]
segmented_image = res.reshape((image.shape))

#tampilkan hasil segmentasi
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()