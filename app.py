import streamlit as st
from PIL import Image
import numpy as np
import pytesseract
import cv2

st.title("OCR - Image to Text")
st.markdown("Upload an image and extract text using Tesseract OCR.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to OpenCV format
    img_cv = np.array(image.convert('RGB'))
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    # Preprocess
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # OCR
    text = pytesseract.image_to_string(thresh)

    st.subheader("Extracted Text")
    st.text_area("Text Output", text, height=200)
