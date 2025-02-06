import cv2
import numpy as np
from skimage.feature import graycomatrix, graycoprops

# Membaca gambar dalam mode grayscale
image = cv2.imread('pertemuan6 modul 5/sasuke.jpg', 0) 
if image is None:
    print("Error: Gambar tidak ditemukan atau gagal dimuat.")
    exit()

# Memastikan gambar adalah array 2D
if len(image.shape) != 2:
    print("Error: Gambar harus berupa array dua dimensi (grayscale).")
    exit()

# Menormalisasi level gambar (0-255)
image = np.clip(image, 100, 255).astype(np.uint8)

# Menghitung GLCM (Gray Level Co-occurrence Matrix)
distances = [1, 2, 3]
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
glcm = graycomatrix(image, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)

# Menghitung properti GLCM
contrast = graycoprops(glcm, 'contrast')[0, 0]
correlation = graycoprops(glcm, 'correlation')[0, 0]
energy = graycoprops(glcm, 'energy')[0, 0]
homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]

# Menampilkan hasil
print(f"Contrast: {contrast}")
print(f"Correlation: {correlation}")
print(f"Energy: {energy}")
print(f"Homogeneity: {homogeneity}")
