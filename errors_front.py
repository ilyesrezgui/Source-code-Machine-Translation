import requests
import streamlit as st 
import os 
import json
import matplotlib.pyplot as plt
import altair as alt
import pandas as pd
import plotly.graph_objs as go

def errors():
# Define the API endpoint
    api_endpoint2 = "http://localhost:8000/analyzer"

    # Define Streamlit UI elements
    st.title("Repository Analyzer")
  
    selected_language = st.selectbox("Select sourceprogramming language", ["java", "c#","plsql"])
    selected_language2 = st.selectbox("Select target programming language", ["java", "c#","plsql"])

    # Define source and target directories
    dirname =st.text_input("Enter the source repository's path",key="src")
    target_dirname =st.text_input("Enter the target repository's path",key="target")
    
    c1,c2,c3=st.columns([1,1,1])
    translate_button2 = c2.button("Analyze")
    

    # Define a function to call the API endpoint
    def call_api():
        response = requests.get(api_endpoint2, params={
            "repo":dirname,
            "target_repo":target_dirname,
            "language": selected_language
        })
        if response.status_code == 200: 
           
            response_data = json.loads(response.text)
            x_vals=response_data['files']
            error_list = response_data['nb_err_source']
            error_list_target = response_data['nb_err_target']
            
            fig, ax = plt.subplots(figsize=(6, 2))

            # Set the width of each bar
            bar_width = 0.1

            # Set the x positions of the bars
            x_pos = range(len(x_vals))

            # Plot the bars for each integer list
            ax.bar(x_pos, error_list, width=bar_width, label=selected_language ,color='#dc0433')
            ax.bar([x + bar_width for x in x_pos], error_list_target, width=bar_width, label=selected_language2,color='grey')

            # Set the x-axis ticks and labels
            ax.set_xticks([x + bar_width / 2 for x in x_pos])
            ax.set_xticklabels(x_vals,fontsize=5)

            # Add a legend and axis labels
            ax.legend()
            ax.set_xlabel('Files',fontsize=7)
            ax.set_ylabel('Number of Syntactic Errors',fontsize=7)

            # Display the plot in Streamlit
            st.pyplot(fig)

        else:
            st.error("Error translating code.")

    # Call the API endpoint when the "Translate" button is clicked
    if translate_button2:
        call_api()
    
