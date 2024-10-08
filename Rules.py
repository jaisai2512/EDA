import pandas as pd

def validate_obj(column):
    if column.isna().all():
        return 'All rows are null'
    unique_values = column.nunique()
    total_values = len(column)
    threshold = 0.05
    return "categorical" if (unique_values / total_values) < threshold else "textual"


def extract_data(data: pd.DataFrame) -> dict:
    num_rows, num_columns = data.shape

    column_data_types = {
        column: validate_obj(data[column]) if data[column].dtype == 'O' else data[column].dtype
        for column in data.columns
    }

    mean = {
        column:round(data[column].mean(),2)  if data[column].dtype in ['int64','float64',int,float] else data[column].dtype
        for column in data.columns
    }

    no_null = {
        column: data[column].isnull().sum() for column in data.columns
    }

    summary = {
        'num_rows': num_rows,
        'num_columns': num_columns,
        'column_names_data_types': column_data_types,
        'mean' : mean,
        'num_of_null' : no_null
    }

    return summary
