import streamlit as st
import cv2
import numpy as np
st.title('Convert image into pencil sketch')
st.subheader('Real Image')
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    # Check the shape of cv2_img:
    #converted_img = np.array(bytes_data.convert('RGB')) 
    gray_scale = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
    inv_gray = 255 - gray_scale
    slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
    blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
    sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
    st.subheader('Converted Image')
    st.image(sketch) 
