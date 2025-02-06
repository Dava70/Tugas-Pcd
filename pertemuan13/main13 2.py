import cv2

#baca citra dalam grayscale
image = cv2.imread('macan.jpg', cv2.IMREAD_GRAYSCALE)

#menerapkan outsu's thresholding
ret, otsu_thresh = cv2.threshold(image, 0, 225, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#tampilkan hasil segmentasi
cv2.imshow('Otsu Thresholding', otsu_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()