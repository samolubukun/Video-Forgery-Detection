# Video Forgery Detection using CNN
This repository provides a deep learning-based solution for detecting forged videos using a Convolutional Neural Network (CNN). 
The system analyzes uploaded videos and predicts whether they contain manipulated frames using a trained ResNet-based model.

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
