import streamlit as st
import pandas as pd
import time as ts
from datetime import time
import matplotlib.pyplot as plt
import numpy as np

## Lecture 12
st.markdown("""
<style>
               .st-emotion-cache-6q9sum.ef3psqc4  
            {visibility: hidden},
</style>
""", unsafe_allow_html= True)
st.markdown("<h1> User Registeration Form </h1>", unsafe_allow_html=True)

form = st.form("Form 1")
form.text_input(label="First Name:")
form.form_submit_button(label="Submit")

with st.form("Form 2"):
    st.text_input(label="Last Name:")
    st.form_submit_button(label="Submit")

with st.form("Form 3"):
    col1, col2 = st.columns(2)
    col1.text_input(label="First Name:")
    col2.text_input(label="Last Name:")
    st.text_input(label="Password:")
    st.text_input(label="Confirm Password:")
    st.form_submit_button(label="Submit")
st.markdown("---")

## Lecture 12  
st.markdown("<h1 style = 'text-align:center'> Registeration Form </h1>", unsafe_allow_html=True)
with st.form("Form 4", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input(label="First Name:")
    l_name = col2.text_input(label="Last Name:")
    pwd = st.text_input(label="Password:")
    c_pwd = st.text_input(label="Confirm Password:")
    date, month, year = st.columns(3)
    date.text_input(label="Date:")
    month.text_input(label="Month:")
    year.text_input(label="Year:")
    s_state = st.form_submit_button(label="Submit")

    if s_state:
        if pwd != c_pwd:
            st.write("Password did not match")
        elif len(pwd) == 0 or len(c_pwd) == 0:
            st.warning("Please enter password")
        elif f_name == "" or l_name == "":
            st.warning("Please enter first and last name")
        else:
            st.success("Form submitted successfully")

    print(f"pwd: {pwd}, c_pwd: {c_pwd}")

st.markdown("---")

## Lecture 13
st.sidebar.write("Hello, this is sidebar")














