import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.subheader('Upload Menu Hari ini')

# kode sekolah di backend

df = pd.DataFrame({"DM": ['almonds', 'apple', 'avocado', 'banana', 'beer', 'biscuits',
       'boisson-au-glucose-50g', 'bread-french-white-flour', 'bread-sourdough',
       'bread-white', 'bread-whole-wheat', 'bread-wholemeal', 'broccoli',
       'butter', 'carrot', 'cheese', 'chicken', 'chips-french-fries',
       'coffee-with-caffeine', 'corn', 'croissant', 'cucumber',
       'dark-chocolate', 'egg', 'espresso-with-caffeine', 'french-beans',
       'gruyere', 'ham-raw', 'hard-cheese', 'honey', 'jam', 'leaf-spinach',
       'mandarine', 'mayonnaise', 'mixed-nuts',
       'mixed-salad-chopped-without-sauce', 'mixed-vegetables', 'onion',
       'parmesan', 'pasta-spaghetti', 'pickle', 'pizza-margherita-baked',
       'potatoes-steamed', 'rice', 'salad-leaf-salad-green', 'salami',
       'salmon', 'sauce-savoury', 'soft-cheese', 'strawberries',
       'sweet-pepper', 'tea', 'tea-green', 'tomato', 'tomato-sauce', 'water',
       'water-mineral', 'white-coffee-with-caffeine', 'wine-red', 'wine-white',
       'zucchini']})
with st.popover("Daftar makanan yang bisa dideteksi", help='ini hanya konsep, perlu di latih lagi dengan makanan Indonesia untuk bisa mendeteksi jenis makanan indonesia,serta menilai kelayakan porsi yang disajikan dan menghitung harganya'):
    st.write(df)


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import *
from tensorflow.keras import preprocessing
from PIL import Image

  
def predict(image):
    classifier_model = "food_model.h5"
      
    model = load_model(classifier_model)
    test_image = image.resize((256,256))
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    predictions = model.predict(test_image)
    scores = tf.nn.softmax(predictions[0])
    scores = scores.numpy()
    unique_classes = df["DM"].unique()
    class_labels = unique_classes
    predicted_classes = np.argmax(predictions, axis=1)
    result = [class_labels[i] for i in predicted_classes]

    return result

file_uploaded = st.file_uploader("Upload File", type=["png","jpg","jpeg"])
if file_uploaded is not None:    
        image = Image.open(file_uploaded)
        st.image(image, caption='Gambar yang diunggah', use_column_width=True)

class_btn = st.button("Submit")

if class_btn:
    with st.spinner('Kerja.. Kerja.. Tipes..'):
            plt.imshow(image)
            plt.axis("off")
            predictions = predict(image)
            time.sleep(1)
            st.write('contoh penggunaan computer vision')
            st.success(predictions)