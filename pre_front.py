from pre_analysis import analyze
import streamlit as st
import requests
import json
import pandas as pd



def analyzer():
# Define the API endpoint
    api_endpoint2 = "http://localhost:8000/preanalyzer"

    # Define Streamlit UI elements
    st.title("Repository Pre-Analyzer")
  
    selected_language = st.selectbox("Select sourceprogramming language", ["java", "c#","plsql"])
    

    # Define source and target directories
    dirname =st.text_input("Enter the source repository's path",key="src")
    
    c1,c2,c3=st.columns([1,1,1])
    translate_button2 = c2.button("Analyze")
    
    def call_api_long():
        response = requests.get(api_endpoint2, params={
            "repo":dirname ,
            "language": selected_language
        })
        if response.status_code == 200:
            try:
                # Convert the JSON response to a pandas DataFrame
                data = json.loads(response.text)

                df = pd.DataFrame(data)
                
                # Define a function to apply formatting to the DataFrame
                def format_dataframe(df):
                    return (
                        df.style
                        .format({"Approximate price in USD": "${:.4f}"}) 
                        .background_gradient(cmap="OrRd", subset=["Number of tokens"])  
                        .highlight_max(subset=["Recommended Translation"])  
                    )
                # Display the formatted DataFrame in Streamlit
                st.write(format_dataframe(df))
            except ValueError:
                st.error("Error reading JSON data.")
        else:
            st.error("Error translating code.")

    # Call the API endpoint when the "Translate" button is clicked

    # Define a function to call the API endpoint
    #df = pd.read_json(response.text, orient='records')
    # Call the API endpoint when the "Translate" button is clicked
    if translate_button2:
        call_api_long()
    