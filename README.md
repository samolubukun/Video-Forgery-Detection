# Video Forgery Detection using CNN
This repository provides a deep learning-based solution for detecting forged videos using a Convolutional Neural Network (CNN). 
The system analyzes uploaded videos and predicts whether they contain manipulated frames using a trained ResNet-based model.

![Uploading Screenshot (264).png…]()


## Features
- **Streamlit Web App:** A user-friendly interface for uploading and analyzing videos.
- **Trained CNN Model:** Detects video forgery by analyzing individual frames.
- **Frame-wise Analysis:** Reports the total number of frames and forged frames.

## Model Summary
The CNN model is trained to classify video frames as real or forged:
- **Architecture:** ResNet-based CNN.
- **Input Shape:**  320x240 RGB frames.
- **Performance Metrics:**
  - Accuracy: 81.0%

- **Access Training Notebook:** [Notebook](https://github.com/samolubukun/Video-Forgery-Detection/tree/main/Notebook)
- **Dataset Used:** [REWIND 3D Dataset]([https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces](https://data.mendeley.com/datasets/2b28sr4mm3/2/files/a931d246-f383-46ee-803c-1242a1df6b1b))
