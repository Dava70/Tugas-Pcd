import cv2

#membaca gambar dalam grayscale
image = cv2.imread('macan.jpg', 0)

#menarapkan adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(image, 225, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY, 11, 2)

#menampilkan hasil
cv2.imshow('Adaptive Thresholding', adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()