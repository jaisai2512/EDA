import Rules
import pandas as pd
from API import api

data = pd.read_csv('mtcars.csv')

summary = Rules.extract_data(data)

prompt = f'''You are given a dictionary containing statistical information about a dataframe (e.g., mean of each row, total number of rows, column statistics, etc.). Your task is to generate a concise summary that captures all key details from the dictionary in a natural language format.

Instructions:
1. Ensure the summary is written in natural language and easy to understand.
2. Keep the summary within 500 tokens.
3. Include all relevant insights derived from the dataframe without omitting any important information.

Example summary:
The fruit dataset contains information about various fruits, featuring 5 fields: Fruit_Name, Color, Weight_in_grams, Sweetness_Level, and Country_of_Origin. Fruit_Name identifies the type of fruit, while Color indicates its appearance. Weight_in_grams provides the weight, Sweetness_Level rates the taste on a scale, and Country_of_Origin shows where the fruit is typically grown. This dataset can be used for classification and analysis tasks related to fruit characteristics.
Dictionary: {summary}
'''


print(api(prompt))


