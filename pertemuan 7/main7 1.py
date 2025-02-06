import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Membaca dataset dari CSV
data = pd.read_csv('sample_dataset.csv')

# Mengonversi label menjadi numerik
label_encoder = LabelEncoder()
data['label'] = label_encoder.fit_transform(data['label'])  # Konversi ClassA, ClassB ke numerik

# membaca dataset citra
x = data.iloc[:, :-1].values  # Semua kolom kecuali kolom terakhir
y = data.iloc[:, -1].values   # Kolom terakhir

# Split data untuk pelatihan dan pengujian
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Inisialisasi model SVM
clf = svm.SVC(kernel='linear')

# Latih model menggunakan data pelatihan
clf.fit(x_train, y_train)

# Prediksi menggunakan data uji
y_pred = clf.predict(x_test)

# Hitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi: {accuracy * 100:}%')