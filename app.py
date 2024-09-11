import Rules
import pandas as pd

data = pd.read_csv('mtcars.csv')

summary = Rules.extract_data(data)



