import Rules
from API import api
import streamlit as st
import pandas as pd
import json
from execute import execute_code_safely
import seaborn as sns
import matplotlib.pyplot as plt 
import io
from Summary import summary_gen
 
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

    var_dict = {'df':df}

    summary = summary_gen(df)
    st.write(summary)
    prompt_qa = f'''You are  a data analyst with expertise in interpreting data summaries, your task is to generate insightful questions that help identify patterns based on the provided data using visualizations. Focus specifically on distribution and correlation patterns. Please adhere to the following instructions:

	Instruction:	
	1. Do not generate any code.
	2. Only use information obtained from the dictionary provided.
	3. Only Generate 5 questions.
	4. Don't generate any comment or anything apart from the json format list.
	5.The Visualization should not be complex.

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
        prompt_vis = f'''You are a data analyst with coding skills and you are tasked to write a visualization code based on the provided question, visualization, reason and summary of the data

Instructions:
    1.The data is provided in a DataFrame named df.
    2.Generate only Python code without any explanations or comments.
    3.Do not modify any part of the provided code structure below 
Here are the details:

Question, visualization, and reason:
“”"
{i}
“”"

Summary of the data:
“”"
{summary}
“”"

 
The visualization code should be generated in the <<stub>> part in the below code.

```python
import altair as alt
import io
def plot_and_save(df):
    
    <<stub>>
    # Save the figure to a buffer instead of a file
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)  # Move the cursor to the start of the stream
    return buf
'''     

        with st.spinner("Executing code..."):
         generated_code = api(prompt_vis)
         #st.code(generated_code,language='Python')
         local_vars = {}
         exec(generated_code.replace('```python','').replace('```',''), globals(), local_vars) 
         plot_and_save = local_vars['plot_and_save']  
         plot_buffer = plot_and_save(df)  
        if plot_buffer:
         st.image(plot_buffer, caption="Age Chart", use_column_width=True)
else:
    st.write("Please upload a CSV file to proceed.")




