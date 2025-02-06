import cv2
import numpy as np

#membaca gambar
image = cv2.imread('macan.jpg')
Z = image.reshape((-1, 3))

#konversi ke float32
Z = np.float32(Z)

#kriteria k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 3
ret, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

#konversi kembali ke uint8 dan reshape
center = np.uint8(center)
res = center[label.flatten()]
segmented_image = res.reshape((image.shape))

#menampilkan hasil
cv2.imshow('K-Means Segmentation', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()