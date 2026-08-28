import pandas as pd


def detect_iqr_outliers(df: pd.DataFrame, columns: list[str], multiplier: float = 1.5) -> pd.DataFrame:
    """Detect IQR outliers and return quartiles, fences, and counts."""
    results = []

    for column in columns:
        values = df[column].dropna()
        q1 = values.quantile(0.25)
        q3 = values.quantile(0.75)
        iqr = q3 - q1
        lower_fence = q1 - multiplier * iqr
        upper_fence = q3 + multiplier * iqr
        outlier_count = int(((values < lower_fence) | (values > upper_fence)).sum())

        results.append({
            "Feature": column,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower Fence": lower_fence,
            "Upper Fence": upper_fence,
            "Outlier Count": outlier_count,
        })

    return pd.DataFrame(results)


def detect_group_iqr_outliers(
    df: pd.DataFrame,
    group_column: str,
    columns: list[str],
    multiplier: float = 1.5,
) -> pd.DataFrame:
    """Detect IQR outliers separately within each group."""
    results = []

    for group in df[group_column].dropna().unique():
        group_df = df[df[group_column] == group]

        for column in columns:
            values = group_df[column].dropna()
            q1 = values.quantile(0.25)
            q3 = values.quantile(0.75)
            iqr = q3 - q1
            lower_fence = q1 - multiplier * iqr
            upper_fence = q3 + multiplier * iqr
            outlier_count = int(((values < lower_fence) | (values > upper_fence)).sum())

            results.append({
                "Group": group,
                "Feature": column,
                "Q1": q1,
                "Q3": q3,
                "IQR": iqr,
                "Lower Fence": lower_fence,
                "Upper Fence": upper_fence,
                "Outlier Count": outlier_count,
            })

    return pd.DataFrame(results)
