import numpy as np
import pandas as pd
from scipy.stats.mstats import winsorize


def keep(df: pd.DataFrame) -> pd.DataFrame:
    """Return the data unchanged."""
    return df.copy()


def trim_iqr(df: pd.DataFrame, columns: list[str], multiplier: float = 1.5) -> pd.DataFrame:
    """Remove rows containing an IQR outlier in any selected numeric column."""
    result = df.copy()
    mask = pd.Series(True, index=result.index)

    for column in columns:
        values = result[column]
        q1 = values.quantile(0.25)
        q3 = values.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - multiplier * iqr
        upper = q3 + multiplier * iqr
        mask &= values.isna() | values.between(lower, upper)

    return result.loc[mask].copy()


def cap_iqr(df: pd.DataFrame, columns: list[str], multiplier: float = 1.5) -> pd.DataFrame:
    """Cap IQR outliers at the lower and upper fences."""
    result = df.copy()

    for column in columns:
        values = result[column]
        q1 = values.quantile(0.25)
        q3 = values.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - multiplier * iqr
        upper = q3 + multiplier * iqr
        result[column] = values.clip(lower=lower, upper=upper)

    return result


def winsorize_iqr(df: pd.DataFrame, columns: list[str], multiplier: float = 1.5) -> pd.DataFrame:
    """Winsorize values outside IQR fences to the corresponding fence."""
    return cap_iqr(df, columns, multiplier)


def log_transform(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Apply log1p transformation to selected non-negative numeric columns."""
    result = df.copy()

    for column in columns:
        if (result[column].dropna() < 0).any():
            raise ValueError(f"Log transformation requires non-negative values: {column}")
        result[column] = np.log1p(result[column])

    return result


def yeo_johnson_transform(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Apply Yeo-Johnson transformation to selected numeric columns."""
    from sklearn.preprocessing import PowerTransformer

    result = df.copy()
    transformer = PowerTransformer(method="yeo-johnson", standardize=False)

    for column in columns:
        non_null = result[[column]].dropna()
        transformed = transformer.fit_transform(non_null).ravel()
        result.loc[non_null.index, column] = transformed

    return result
