
import streamlit as st
from PIL import Image
import numpy as np
import pytesseract


st.title("OCR - Image to Text")
st.markdown("Upload an image and extract text using Tesseract OCR.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    gray = np.array(image.convert("L"))  # Convert to grayscale
    thresh = np.where(gray > 150, 255, 0).astype('uint8')  # Threshold manually


    # OCR
    text = pytesseract.image_to_string(thresh)

    st.subheader("Extracted Text")
    st.text_area("Text Output", text, height=200)

