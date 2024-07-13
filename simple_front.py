import requests
import streamlit as st 
import os 
import json


def translate_simple_f():
# Define the API endpoint
    api_endpoint2 = "http://localhost:8000/translate_simple"

    # Define Streamlit UI elements
    st.title("Chunks of code translator")
    code=st.text_area("Enter your code here")

    # Define source and target directories
    selected_source0 = st.selectbox("Select source programming language", ["java", "c#","plsql"])
    selected_target0 = st.selectbox("Select target programming language", ["java", "c#"])
    c1,c2,c3=st.columns([1,1,1])
    translate_button0 = c2.button("Translate")

    # Define a function to call the API endpoint
    def call_api2():
        response = requests.get(api_endpoint2, params={
            "input_code": code,
            "selected_source": selected_source0,
            "selected_target": selected_target0
                            })
        if response.status_code == 200:
            response_data = json.loads(response.text)
            x_vals=response_data['translation']
            st.write(x_vals)
        else:
            st.error("Error translating code.")

    # Call the API endpoint when the "Translate" button is clicked
    if translate_button0:
        if selected_source0==selected_target0:
            c2.write("""<div align='text-align:center'>Source & target languages should be different</div>""", unsafe_allow_html=True)
        else:
            call_api2()
