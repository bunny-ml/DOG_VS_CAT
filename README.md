# 🐶🐱 Cat vs Dog Image Classifier

A deep-learning project that classifies images as Cat or Dog using a Convolutional Neural Network (CNN).
The model is trained on the Kaggle Cats vs Dogs dataset and deployed with Streamlit for easy image uploads and predictions.

# 🚀 Project Overview

This project builds a CNN from scratch using TensorFlow / Keras, trains it on 25k+ images, saves the best-performing model, and serves it through a Streamlit app where users can upload photos for real-time predictions.

# 📦 Features

- CNN-based classifier

- Training with ImageDataGenerator (augmentation)

- Model checkpointing: saves the best .keras model automatically

- Achieved 84.37% validation accuracy

- Deployed using Streamlit

- Supports JPG/PNG image uploads

# 📊 Training Results
## Epoch Logs
Epoch 1/10
accuracy: 0.5941 - loss: 0.6556 - val_accuracy: 0.7347 - val_loss: 0.5260

Epoch 2/10
accuracy: 0.7634 - loss: 0.4906 - val_accuracy: 0.7970 - val_loss: 0.4568

Epoch 3/10
accuracy: 0.8147 - loss: 0.4102 - val_accuracy: 0.8180 - val_loss: 0.4096

Epoch 4/10
accuracy: 0.8511 - loss: 0.3440 - val_accuracy: 0.8292 - val_loss: 0.3956

Epoch 5/10
accuracy: 0.8821 - loss: 0.2738 - val_accuracy: 0.8332 - val_loss: 0.4169

Epoch 6/10
accuracy: 0.9193 - loss: 0.1984 - val_accuracy: 0.8332 - val_loss: 0.5065

Epoch 7/10
accuracy: 0.9450 - loss: 0.1415 - val_accuracy: 0.8438 - val_loss: 0.5300

Epoch 8/10
accuracy: 0.9640 - loss: 0.1014 - val_accuracy: 0.8334 - val_loss: 0.6567

Epoch 9/10
accuracy: 0.9702 - loss: 0.0789 - val_accuracy: 0.8350 - val_loss: 0.6791

Epoch 10/10
accuracy: 0.9788 - loss: 0.0587 - val_accuracy: 0.8342 - val_loss: 0.7976

Best Validation Accuracy:
84.37%

## 🧠 Model Architecture

The model uses 3 convolutional blocks followed by dense layers.


| Layer (Type)        | Output Shape       | Parameters |
|---------------------|--------------------|------------|
| Conv2D (32 filters) | (126, 126, 32)     | 896        |
| MaxPool2D           | (63, 63, 32)       | 0          |
| Conv2D (64 filters) | (61, 61, 64)       | 18,496     |
| MaxPool2D           | (30, 30, 64)       | 0          |
| Conv2D (128 filters)| (28, 28, 128)      | 73,856     |
| MaxPool2D           | (14, 14, 128)      | 0          |
| Flatten             | (25088)            | 0          |
| Dense (128)         | (128)              | 3,211,392  |
| Dropout (0.1)       | —                  | 0          |
| Dense (64)          | (64)               | 8,256      |
| Dropout (0.1)       | —                  | 0          |
| Dense (1, sigmoid)  | (1)                | 65         |

Total params: **3,312,961**

# 🗂️ Project Structure
```
📁 DOG_VS_CAT
│── model 
|     |_____best_cat_dog_model.keras
|      
│── app.py                   # Streamlit app
│── notebook
|       |___ 01_notebook.ioynb  # Training notebook
|               
│── README.md                # Project documentation
│── requirements.txt
```
# ▶️ How to Run
1. Install dependencies 
```
pip install -r requirements.txt
```
2. Run the Streamlit app
```
streamlit run app.py
```
3. Upload an image

The app will show:
```
➡️ Dog 🐶
or
➡️ Cat 🐱
```