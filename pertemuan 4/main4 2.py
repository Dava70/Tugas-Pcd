import cv2
import numpy as np

# Load image
image = cv2.imread('pertemuan4 modul2/naruto.jpg')  

# Get image dimensions
H, W = image.shape[:2]  

# Define affine transformation matrix
M_affine = np.float32([[1, 0, 50], [0, 1, 30]])  

# Apply affine transformation with the correct dsize argument
affine_transformed_image = cv2.warpAffine(image, M_affine, (W, H))  

# Display the result
cv2.imshow('Affine Transformed Image', affine_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
