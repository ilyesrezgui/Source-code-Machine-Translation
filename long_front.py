import requests
import streamlit as st 
import os 
import tkinter as tk
from tkinter import filedialog

def long_repo():
# Define the API endpoint
    api_endpoint = "http://localhost:8000/translator"

    # Define Streamlit UI elements
    st.title("Long repositories code translator")
    

    root = tk.Tk()
    root.withdraw()

    # Define source and target directories
    selected_source = st.selectbox("Select source programming language", ["java", "c#","plsql"])
    selected_target = st.selectbox("Select target programming language", ["java", "c#","plsql"])
    source_dirname =st.text_input("Enter source repository's path",key="src")
    target_dirname =st.text_input("Enter target repository's path",key="target")
    
    c1,c2,c3=st.columns([1,1,1])
    translate_button = c2.button("Translate")

    # Define a function to call the API endpoint
    def call_api_long():
        response = requests.get(api_endpoint, params={
            "src_repo":source_dirname ,
            "target_repo": target_dirname,
            "selected_source": selected_source,
            "selected_target": selected_target
        })
        if response.status_code == 200:
            st.write("Translation is done Check the target repository")
        else:
            st.error("Error translating code.")

    # Call the API endpoint when the "Translate" button is clicked
    if translate_button:
        if selected_source==selected_target:
            c2.write("""<div align='text-align:center'>Source & target languages should be different</div>""", unsafe_allow_html=True)
        else:
            call_api_long()
