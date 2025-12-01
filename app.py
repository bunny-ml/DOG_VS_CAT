import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("model/best_cat_dog_model.keras")

st.title("🐱🐶 Cat vs Dog Classifier")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

def preprocess(img):
    img = img.resize((128, 128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image")

    img_array = preprocess(img)

    pred = model.predict(img_array)[0][0]

    if pred >= 0.5:
        st.success("Prediction: **DOG 🐶**")
    else:
        st.success("Prediction: **CAT 🐱**")
