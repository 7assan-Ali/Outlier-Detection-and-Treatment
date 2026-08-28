import pandas as pd


def get_feature_types(df: pd.DataFrame, target_column: str | None = None):
    """Return numerical and categorical column names."""
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

    if target_column in numeric_columns:
        numeric_columns.remove(target_column)
    if target_column in categorical_columns:
        categorical_columns.remove(target_column)

    return numeric_columns, categorical_columns


def impute_missing_values(
    df: pd.DataFrame,
    numeric_strategy: str = "mean",
    categorical_strategy: str = "mode",
    unknown_category: str | None = None,
    exclude_columns: list[str] | None = None,
) -> pd.DataFrame:
    """Return a copy with missing numerical/categorical values imputed."""
    result = df.copy()
    exclude = set(exclude_columns or [])

    numeric_columns, categorical_columns = get_feature_types(result)

    for column in numeric_columns:
        if column in exclude:
            continue
        if numeric_strategy == "mean":
            value = result[column].mean()
        elif numeric_strategy == "median":
            value = result[column].median()
        else:
            raise ValueError("numeric_strategy must be 'mean' or 'median'")
        result[column] = result[column].fillna(value)

    for column in categorical_columns:
        if column in exclude:
            continue
        if column == "Alcohol Consumption" and unknown_category is not None:
            result[column] = result[column].fillna(unknown_category)
        elif categorical_strategy == "mode":
            mode = result[column].mode()
            if not mode.empty:
                result[column] = result[column].fillna(mode.iloc[0])
        else:
            raise ValueError("categorical_strategy must be 'mode'")

    return result
