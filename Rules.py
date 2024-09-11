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

    # Extracting data types of each column
    column_data_types = {
        column: validate_obj(data[column]) if data[column].dtype == 'O' else data[column].dtype
        for column in data.columns
    }

    summary = {
        'num_rows': num_rows,
        'num_columns': num_columns,
        'column_names_data_types': column_data_types,
    }

    return summary
