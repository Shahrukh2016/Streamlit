import streamlit as st
import pandas as pd
import time as ts
from datetime import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align:center;'> Image Editor </h1>", unsafe_allow_html=True)
st.markdown("---")
image = st.file_uploader(label="Upload your image:", type=["png", "jpg", "jpeg"])
st.image(image)

info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

with st.form(key="Form1"):
    if image:
        img = Image.open(image)
        info.markdown("<h2 style='text-align:center;'> Information </h2>", unsafe_allow_html=True)
        st.markdown(f"<h6> Size: {img.size} </h6>", unsafe_allow_html=True)
        st.markdown(f"<h6> Mode: {img.mode} </h6>", unsafe_allow_html=True)
        st.markdown(f"<h6> Format: {img.format} </h6>", unsafe_allow_html=True)

        st.markdown("<h2 style='text-align:center;'> Resizing </h2>", unsafe_allow_html=True)
        width = st.number_input(label="Width", value=img.width)
        height = st.number_input(label="Height", value=img.height)

        st.markdown("<h2 style='text-align:center;'> Rotation </h2>", unsafe_allow_html=True)
        degree = st.number_input(label="Degree")

        st.markdown("<h2 style='text-align:center;'> Filters </h2>", unsafe_allow_html=True)
        filters = st.selectbox(label="Filters", options=('None','Blur', 'Contour', 'Detail', 'Edge Enhance', 'Edge Enhance More', 'Emboss', 'Find Edges', 'Sharpen', 'Smooth', 'Smooth More'))

        s_button = st.form_submit_button(label="Submit")

        if s_button:
            edited = img.resize(size=(width, height)).rotate(angle=degree)
            filtered = edited
            if filters != "None":
                if filters == "Blur":
                    filtered = edited.filter(filter=BLUR)
                elif filters == "Contour":
                    filtered = edited.filter(filter=CONTOUR)
                elif filters == "Detail":
                    filtered = edited.filter(filter=DETAIL)
                elif filters == "Edge Enhance":
                    filtered = edited.filter(filter=EDGE_ENHANCE)
                elif filters == "Edge Enhance More":
                    filtered = edited.filter(filter=EDGE_ENHANCE_MORE)
                elif filters == "Emboss":
                    filtered = edited.filter(filter=EMBOSS)
                elif filters == "Find Edges":
                    filtered = edited.filter(filter=FIND_EDGES)
                elif filters == "Sharpen":
                    filtered = edited.filter(filter=SHARPEN)
                elif filters == "Smooth":
                    filtered = edited.filter(filter=SMOOTH)
                elif filters == "Smooth More":
                    filtered = edited.filter(filter=SMOOTH_MORE)
            st.image(filtered)

                


