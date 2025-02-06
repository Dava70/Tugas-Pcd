import cv2

#baca citra dalam grayscale
image = cv2.imread('naruto.jpg', cv2.IMREAD_GRAYSCALE)

#terapkan deteksi tepi dengan metode canny
edges = cv2.Canny(image, 100, 200)

#tampilkan hasil deteksi teepi
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()