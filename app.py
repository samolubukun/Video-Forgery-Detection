import streamlit as st
import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image


@st.cache_resource
def load_video_forgery_model():
    return load_model("videoforgerydetection.keras")

# Video Forgery Detection
target_height, target_width = 240, 320  # Define target dimensions (height, width)

def predict_video_forgery(video_path, model):
    vid = []
    sumframes = 0
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Resize frame to target dimensions
        frame = cv2.resize(frame, (target_width, target_height))
        
        sumframes += 1
        vid.append(frame)

    cap.release()
    st.write(f"No. Of Frames in the Video: {sumframes}")

    Xtest = np.array(vid)
    output = model.predict(Xtest)
    output = output.reshape((-1))

    results = []
    for i in output:
        if i>0.5:
            results.append(1)
        else:
            results.append(0)
    #print(len(results))
    #print(results)
    forge_flag = 0
    for i in results:
        if i == 1:
            forge_flag = 1
            break

    forge_flag = any(results)

    if forge_flag == 0:
        return "The video is not forged", 0, sumframes
    else:
        return "The video is forged", sum(results), sumframes


# Main video forgery detection system
st.title("Video Forgery Detection")  # Title added here

# Main video forgery detection system
uploaded_file = st.file_uploader("Upload a video", type=['mp4', 'avi', 'mov', 'mkv'])
if uploaded_file:
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.video("temp_video.mp4")
    model = load_video_forgery_model()
    result_message, forged_frames, total_frames = predict_video_forgery("temp_video.mp4", model)

    if forged_frames == 0:
        st.success(result_message)
    else:
        st.error(result_message)

    st.write(f"Forged Frames: {forged_frames}/{total_frames}")
    os.remove("temp_video.mp4")
