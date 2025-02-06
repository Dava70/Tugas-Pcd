import cv2
import numpy as np
from skimage.feature import local_binary_pattern

import os
print("Direktori kerja saat ini:", os.getcwd())

# Membaca gambar dalam mode grayscale
image = cv2.imread('pertemuan6 modul 4\dava.jpg', 0)

# Periksa apakah gambar berhasil dimuat
if image is None:
    print("Error: Gambar 'pertemuan6 modul 4\dava.jpg.jpg tidak ditemukan atau gagal dimuat.")
else:
    # Parameter untuk LBP
    radius = 1
    n_points = 8 * radius

    # Menerapkan Local Binary Pattern (LBP)
    lbp = local_binary_pattern(image, n_points, radius, method='uniform')

    # Menampilkan hasil
    cv2.imshow('Local Binary Pattern', lbp.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
