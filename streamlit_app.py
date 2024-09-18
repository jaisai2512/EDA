import Rules
from API import api
import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title("EDA Report Generator")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the content of the CSV file
    st.write("Summary of the CSV file:")
    summary = Rules.extract_data(df)


    prompt = f'''You are a data analyst with expertise in data interpretation using pandas dataframe. You are provided with a dataframe represented as a dictionary. Thoroughly analyze this data and provide a comprehensive summary in a single paragraph. The summary should be rich, compact, and concise, capturing all key information and insights from the data. Ensure that no critical details are omitted while keeping the text engaging.

  Please adhere to the following instructions:
    1.Do not generate any code.
    2.Do not generate tabular columns.
    3.Only use information obtained from the dictionary provided.
    
  Here is the dictionary for analysis:{summary}
    '''
    prompt_qa = f'''You are a data analyst with expertise in interpreting data summaries and generating questions for visualizations. Please adhere to the following instructions:

1. Do not generate any code.
2. Do not generate tabular columns.
3. Only use information obtained from the dictionary provided.
4. Only Generate 5 questions.
5. The visualization should be a single graph, not a combination or multiple graphs.

The output should be in valid JSON format as follows:

[
    {{
        "question": "...",
        "visualization": "...",
        "reason": "..."
    }},
    ...
]
Here is the summary of the data:
{summary}
'''

    # Display basic information about the CSV
    st.write("Basic Information:")
    st.write(api(promp_qa))
else:
    st.write("Please upload a CSV file to proceed.")




