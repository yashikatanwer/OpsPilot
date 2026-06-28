import pandas as pd


def analyze_dataset(df):

    rows = len(df)
    columns = len(df.columns)

    missing_values = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())
    empty_columns = int(df.isnull().all().sum())

    completeness = round(
        ((df.notna().sum().sum()) / (rows * columns)) * 100,
        2
    )

    numeric_columns = list(
        df.select_dtypes(include="number").columns
    )

    text_columns = list(
        df.select_dtypes(include="object").columns
    )

    date_columns = []

    for column in df.columns:

        try:

            converted = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            if converted.notna().sum() > len(df) * 0.7:

                date_columns.append(column)

        except:

            pass

    unique_values = {}

    for column in df.columns:
        unique_values[column] = df[column].nunique()

    return {

        "rows": rows,
        "columns": columns,
        "missing": missing_values,
        "duplicates": duplicate_rows,
        "empty_columns": empty_columns,
        "completeness": completeness,
        "numeric_columns": numeric_columns,
        "text_columns": text_columns,
        "date_columns": date_columns,
        "unique_values": unique_values

    }