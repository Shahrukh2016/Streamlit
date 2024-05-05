import streamlit as st
import pandas as pd
import time as ts
from datetime import time
import matplotlib.pyplot as plt
import numpy as np 
import pyshortner

# s = pyst.Shortener()
st.markdown("<h1 style= 'text-align:center'> URL Shorner </h1>", unsafe_allow_html=True)
form = st.form(key="Page", clear_on_submit=True)
url = form.text_input(label="URL HERE")
s_button = form.form_submit_button("Submit")

# if url and s_button:
#     short_url = s.tinyurl.short("https://pyshorteners.readthedocs.io/en/latest/")
    
# print(short_url)