import openai
import pandas as pd
import streamlit as st
from transformers import GPT2Tokenizer
import long_front as lf

import simple_front as tsf
from transformers import GPT2Tokenizer
import errors_front as ef
import pre_front as p1
# Your Streamlit app code goes here

st.set_page_config(layout="wide")
st.write("""
    <style>
        .stButton>button {
            width: 300px;
            height: 45px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
st.sidebar.image("Linedata_Logo.png")

def page1():
    lf.long_repo()

def page3():
    tsf.translate_simple_f()

def page4():
    ef.errors()
def page5():
    p1.analyzer()
pages = {
    "Repo Pre-Analysis": page5,
    "Long Repositories": page1,
    "Short Code": page3,
    "Repo Post-Analysis": page4
}
# Define a function to render the pages
def render_page():
    st.sidebar.title("Operations")
    selection = st.sidebar.selectbox("Check: ", list(pages.keys()))
    page = pages[selection]
    page()

# Call the function to render the selected page
render_page()