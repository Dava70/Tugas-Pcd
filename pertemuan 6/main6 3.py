import cv2

# Inisialisasi ORB detector
orb = cv2.ORB_create()

# Membaca gambar
image_path = 'pertemuan6 modul 3\dava.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Periksa apakah gambar berhasil dimuat
if image is None:
    print(f"Error: Gambar '{image_path}' tidak ditemukan atau gagal dimuat.")
else:
    # Ubah ukuran gambar
    resized_image = cv2.resize(image, (500, 800))  # Contoh dimensi

    # Mendeteksi keypoints dan menghitung deskriptor
    keypoints, descriptor = orb.detectAndCompute(resized_image, None)

    # Menggambar keypoints pada gambar yang diubah ukurannya
    orb_image = cv2.drawKeypoints(resized_image, keypoints, None)

    # Menampilkan hasil
    cv2.imshow('ORB', orb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
