import pandas as pd
from scipy.stats import zscore


def detect_zscore_outliers(
    df: pd.DataFrame,
    columns: list[str],
    threshold: float = 3.0,
) -> pd.DataFrame:
    """Detect outliers using the absolute Z-score threshold."""
    results = []

    for column in columns:
        values = df[column].dropna()
        scores = zscore(values)
        outlier_count = int((abs(scores) > threshold).sum())

        results.append({
            "Feature": column,
            "Mean": values.mean(),
            "Std": values.std(),
            "Z-Score Threshold": threshold,
            "Outlier Count": outlier_count,
        })

    return pd.DataFrame(results)
