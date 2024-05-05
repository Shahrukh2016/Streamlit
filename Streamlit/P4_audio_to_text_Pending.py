import streamlit as st
import pandas as pd
import numpy as np 
from pydub import AudioSegment

st.markdown("<h1 style= 'text-align:center'> Audio to Text Convertor </h1>", unsafe_allow_html=True)
audio = st.file_uploader(label="Upload Your Audio File:", type=["mp3", "wav"])


