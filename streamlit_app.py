import Rules
from API import api
import streamlit as st
import pandas as pd
import json
from Inject import inject_variables

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

    var_dict = {'df':df}

    prompt = f'''You are a data analyst with expertise in data interpretation using pandas dataframe. You are provided with a dataframe represented as a dictionary. Thoroughly analyze this data and provide a comprehensive summary in a single paragraph. The summary should be rich, compact, and concise, capturing all key information and insights from the data. Ensure that no critical details are omitted while keeping the text engaging.

  Please adhere to the following instructions:
    1.Do not generate any code.
    2.Do not generate tabular columns.
    3.Only use information obtained from the dictionary provided.
    
  Here is the dictionary for analysis:{summary}
    '''
    prompt_qa = f'''You are a data analyst with expertise in interpreting data summaries and generating insightful questions to identify patterns in data. Use visualizations to support your analysis and provide meaningful interpretations of the trends. Please adhere to the following instructions:

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
    data = json.loads(api(prompt_qa))
    for i in data:
        prompt_vis = f'''You are a data analyst with coding skills and you are tasked to write a visualization code based on the provided question, visualization, and reason, given a summary of the data.

Instructions:
    1.Use only Seaborn for visualization.
    2.The data is provided in a DataFrame named df.
    3.Generate Python code only, without explanations.
Here are the details:

Question, visualization, and reason:
“”"
{i}
“”"

Summary of the data:
“”"
{summary}
“”"

Please generate the Seaborn code according to the guidelines above.
'''     
        full_code = inject_variables(api(prompt_vis),var_dict)
        st.write(full_code))
        break
else:
    st.write("Please upload a CSV file to proceed.")




