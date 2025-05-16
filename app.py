import streamlit as st
from PIL import Image
import numpy as np
import easyocr

st.title("OCR - Image to Text with EasyOCR")
st.markdown("Upload an image and extract text using EasyOCR.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to numpy array (EasyOCR input)
    img_array = np.array(image.convert('RGB'))

    # Initialize EasyOCR Reader (English)
    reader = easyocr.Reader(['en'])

    # Perform OCR
    result = reader.readtext(img_array, detail=0)

    # Show extracted text
    st.subheader("Extracted Text")
    st.text_area("Text Output", '\n'.join(result), height=200)
