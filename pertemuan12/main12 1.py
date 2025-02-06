import cv2

#baca citra dalam format rgb
image = cv2.imread('sasuke.jpg')

#konversi citra dari rgb ke hsv
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#tampilkan citra hasil
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()