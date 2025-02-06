import cv2

#membaca citra grayscale
image = cv2.imread('naruto.jpg', cv2.IMREAD_GRAYSCALE)

#deteksi tapi menggunakan canny
edges = cv2.Canny(image, 100, 200)

#tampilkan hasil
cv2.imshow('Edges Detected', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()