import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV dataset."""
    return pd.read_csv(path)


def missing_values_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing counts and percentages for columns with missing values."""
    missing = df.isnull().sum()
    result = pd.DataFrame({
        "Missing Values": missing,
        "Percentage": missing / len(df) * 100,
    })
    return result[result["Missing Values"] > 0].sort_values(
        "Missing Values", ascending=False
    )


def numeric_summary(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns."""
    return df[columns].describe().T


def compare_outlier_methods(
    iqr_results: pd.DataFrame,
    zscore_results: pd.DataFrame,
) -> pd.DataFrame:
    """Combine IQR and Z-Score results into one comparison table."""
    iqr = iqr_results[["Feature", "Outlier Count"]].rename(
        columns={"Outlier Count": "IQR Outliers"}
    )
    zscore = zscore_results[["Feature", "Outlier Count"]].rename(
        columns={"Outlier Count": "Z-Score Outliers"}
    )

    comparison = iqr.merge(zscore, on="Feature", how="outer")
    comparison[["IQR Outliers", "Z-Score Outliers"]] = comparison[
        ["IQR Outliers", "Z-Score Outliers"]
    ].fillna(0).astype(int)
    comparison["Total Outliers"] = (
        comparison["IQR Outliers"] + comparison["Z-Score Outliers"]
    )
    return comparison
