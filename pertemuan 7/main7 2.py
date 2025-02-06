import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

#membaca dataset
data = pd.read_csv('sample_dataset.csv')

#encoding lebel menjadi numerik
label_encoder = LabelEncoder()
data['label'] = label_encoder.fit_transform(data['label'])

#memishkan fitur x dan y
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

##split data untuk pelatihan dan penjualan
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#membuat dan melatih knn
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

#prediksi pada data uji 
y_pred = knn.predict(x_test)

#hitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy KNN: {accuracy * 100:.2f}%')