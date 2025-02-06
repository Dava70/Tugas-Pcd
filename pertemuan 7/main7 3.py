import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

#membaca dataset
data = pd.read_csv('sample_dataset.csv')

#encoding label menjadi numerik
label_encoder = LabelEncoder()
data['label'] = label_encoder.fit_transform(data['label'])

# Memisahkan fitur x dan y
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

#reshape data untuk CNN (misal: 3 fitur dianggap sebagai gambar 1x3)
x = x.reshape(-1, 1, 3, 1) #(samples, height, width, channels)
y = to_categorical(y) #One-hot encoding label

# Memisahkan data menjadi data latih dan uji
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Membangun model CNN
model = Sequential([Conv2D(32, (1, 2), activation='relu', input_shape=(1, 3, 1)), Flatten(), Dense(64, activation='relu'), Dense(y.shape[1], activation='softmax')])

#complile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#latih model
model.fit(x_train, y_train, epochs=10, batch_size=32) 

#evaluasi model
loos, accuracy = model.evaluate(x_test, y_test)
print(f'Akurasi CNN: {accuracy *100:.2f}%')
