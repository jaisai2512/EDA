import Rules
from API import api
import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title("CSV File Uploader")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the content of the CSV file
    st.write("Summary of the CSV file:")
    summary = Rules.extract_data(df)


    prompt = f'''You are an English teacher with expertise in data interpretation with pandas dataframe.You are provided with a dataframe represented as a dictionary. Your task is to analyze the data thoroughly and provide a comprehensive summary in paragraph form. The summary should be rich, compact, and concise, capturing all key information and insights from the data. Ensure that no critical details are omitted while keeping the text engaging.
    
    Instruction:
    1.No code should be generated
    2.No tabular columns should be generrated
    3.No information apart from the information obtained from the dictionary.
    Dictionary: {summary}
    '''

    # Display basic information about the CSV
    st.write("Basic Information:")
    st.write(api(prompt))
else:
    st.write("Please upload a CSV file to proceed.")




