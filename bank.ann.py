import pandas as pd
import streamlit as st
import keras
import numpy as np
#from tensorflow import keras
from PIL import Image
from keras.models import Sequential
#from keras_preprocessing.sequence import pad_sequences
from keras.utils import pad_sequences

     ##    python -m streamlit run bank.ann.py
    ##    cd C:\Users\yener\OneDrive\Desktop\Datasets with compleated analysis and predictions\GitHub_Banknote_Authentication

##loading the ann model
model = keras.models.load_model("bank_model")

## load the copy of the dataset
df = pd.read_csv("data_banknote_authentication.csv")

## set page configuration
st.set_page_config(page_title = 'forge banknote prediction')

## add page title and content
st.title('forge banknote prediction ')
st.write('Please Enter Set of information requested below:')

## add image
image = Image.open("983.jpg")
st.image(image, use_column_width = True)

#user input 
variance = st.number_input('Enter variance: ')
skewness = st.number_input('Enter skewness: ')
curtosis = st.number_input('Enter curtosis: ')
entrophy = st.number_input('Enter entrophy: ')


a = np.array([[variance,skewness,curtosis,entrophy]])

## convert text to numerical values
##word_index = {word: index for index, word in enumerate(df.columns[:-1])}
##numerical_values = [a]

## pad the numerical values so that it can have a unique shape as the training data 
##padded_value = pad_sequences([numerical_values],maxlen=3000)

## make the prediction
if st.button('Predict'):
    prediction = model.predict(a)

    if prediction > 0.5:
        st.write('it is forged')
    else: 
        st.write('it is not forget')
