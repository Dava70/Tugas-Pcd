import cv2
import numpy as np
from skimage.feature import graycomatrix,graycoprops

#baca citra graysacel
image = cv2.imread('dava.jpg', cv2.IMREAD_GRAYSCALE)

#hitung glcm (gray level co-occurrance matrix)
glcm = graycomatrix(image, distances=[1], angles=[0], levels=256, symmetric=True,
normed=True)

#ekstrak fitur tekstur
contrast = graycoprops(glcm, 'contrast')[0, 0]
energy = graycoprops(glcm, 'energy')[0, 0]
homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
correlation = graycoprops(glcm, 'correlation')[0, 0]

#tampilkan hasi
print(f'Contrast : {contrast}')
print(f'Energy; {energy}')
print(f'Homogeneity: {homogeneity}')
print(f'Correlation: {correlation}')