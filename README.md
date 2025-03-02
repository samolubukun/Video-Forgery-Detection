# Video Forgery Detection using CNN
This repository provides a deep learning-based solution for detecting forged videos using a Convolutional Neural Network (CNN). 
The system analyzes uploaded videos and predicts whether they contain manipulated frames using a trained ResNet-based model.

![Screenshot (264)](https://github.com/user-attachments/assets/9639a693-57d9-457b-808d-6b2b172b4064)

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

- **Model Download:** Download the trained model file and place it in the same folder as the Streamlit app (e.g., `app.py`) for execution: [videoforgerydetection.keras](https://drive.google.com/file/d/16X6fRYiFargQzyrxmw-IxI2KWREi6z1e/view?usp=sharing)

  
## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/samolubukun/Video-Forgery-Detection.git
   cd Video-Forgery-Detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

