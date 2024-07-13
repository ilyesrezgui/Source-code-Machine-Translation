import os
import streamlit as st
from calc_tokens import number_tokens
import pandas as pd


def list_files(path, extension):
    """List all files with the given extension in the given path"""
    with os.scandir(path) as entries:
        files = [entry.name for entry in entries if entry.is_file() and entry.name.endswith(f'.{extension}')]
    return files


def count_tokens(filepath):
    """Count the number of lines in the given file"""
    with open(filepath, 'r') as f:
        lines = f.read()
    if len(lines)>0:
        x=number_tokens(lines)
        
    else:
        x=0
    return x

def analyze(repo_path, language):
    """
    Given a path to a local repository and a source language, returns a Pandas
    DataFrame containing information about the files in the repository.
    """
    if language == "java":
        extension = "java"
    elif language == "c#":
        extension = "cs"
    elif language == "plsql":
        extension = "sql"
    else:
        extension = None

    if extension is None:
        st.warning("Please select a valid language.")
        return None

    if not repo_path:
        st.warning("Please enter a path to your local repo.")
        return None

    if not os.path.isdir(repo_path):
        st.warning(f"{repo_path} is not a valid directory.")
        return None

    files = list_files(repo_path, extension)
    data = []

    for file in files:
        filepath = os.path.join(repo_path, file)
        num_tokens = count_tokens(filepath)
        price = 0.00002*num_tokens*2
        if num_tokens <= 2000:
            type = "No decomposing needed"
        else: 
            type = "Decomposing needed"
        data.append((file, num_tokens, price, type))

    if not data:
        st.write(f"No {language} files found.")
        return None

    df=pd.DataFrame(pd.DataFrame(data, columns=['Filename', 'Number of tokens',"Approximate price in USD","Recommended Translation"]))
    return df    

