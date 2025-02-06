import cv2
import numpy as np

#membaca gambar dalam grayscale
image = cv2.imread('bruno.jpg', 0)

#konversi gambar ke tipe float32
gray = np.float32(image)

#menerapkan harris corner detector
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

#dilasi untuk menonjolkan sudut yang terdeteksi
dst = cv2.dilate(dst, None)

#thresholding untuk menandai sudut
image[dst > 0.01 * dst.max()] = [255]

#menampilkan hasil
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()