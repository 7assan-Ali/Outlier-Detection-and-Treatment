import pandas as pd
from scipy.stats import zscore


def detect_zscore_outliers(
    df: pd.DataFrame,
    columns: list[str],
    threshold: float = 3.0,
) -> pd.DataFrame:
    """Detect potential outliers using the absolute standard Z-Score."""
    results = []

    for column in columns:
        values = df[column].dropna()
        if values.empty:
            results.append({
                "Feature": column,
                "Mean": float("nan"),
                "Std": float("nan"),
                "Z-Score Threshold": threshold,
                "Outlier Count": 0,
            })
            continue

        scores = zscore(values, ddof=1)
        outlier_count = int((abs(scores) > threshold).sum())

        results.append({
            "Feature": column,
            "Mean": values.mean(),
            "Std": values.std(ddof=1),
            "Z-Score Threshold": threshold,
            "Outlier Count": outlier_count,
        })

    return pd.DataFrame(results)
