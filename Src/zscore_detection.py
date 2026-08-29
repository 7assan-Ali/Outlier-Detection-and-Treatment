import pandas as pd


def detect_zscore_outliers(df, columns, threshold=3):
    results = []

    for column in columns:
        values = df[column].dropna()
        mean = values.mean()
        std = values.std()

        z = (values - mean) / std
        count = (abs(z) > threshold).sum()

        results.append([column, mean, std, count])

    return pd.DataFrame(results, columns=[
        "Feature", "Mean", "Std", "Outlier Count"
    ])
