import cv2
import numpy as np

#membaca gambar
image = cv2.imread('pertemuan4 modul3/naruto.jpg')

#mendefinisikan empat titik sudut citra asli
points1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

#mendefinisikan empat titik sudut baru
points1 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

#mendapatkan matriks transformasi perspektif
M_perspective = cv2.getPerspectiveTransform(points1, points1)

#melakukan transformasi perspektif
perspective_transformed_image = cv2.warpPerspective(image, M_perspective, (300, 300))

#menampilkan hasil 
cv2.imshow('Perspective Transformed Image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows