import pandas as pd


def detect_iqr_outliers(df, columns):
    results = []

    for column in columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        count = ((df[column] < lower) | (df[column] > upper)).sum()

        results.append([column, q1, q3, iqr, lower, upper, count])

    return pd.DataFrame(results, columns=[
        "Feature", "Q1", "Q3", "IQR",
        "Lower Fence", "Upper Fence", "Outlier Count"
    ])
