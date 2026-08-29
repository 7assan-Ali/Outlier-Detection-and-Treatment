import numpy as np


def keep(df):
    return df.copy()


def trim_iqr(df, columns):
    result = df.copy()

    for column in columns:
        q1 = result[column].quantile(0.25)
        q3 = result[column].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        result = result[
            result[column].isna() |
            result[column].between(lower, upper)
        ]

    return result


def cap_iqr(df, columns):
    result = df.copy()

    for column in columns:
        q1 = result[column].quantile(0.25)
        q3 = result[column].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        result[column] = result[column].clip(lower, upper)

    return result


def log_transform(df, columns):
    result = df.copy()

    for column in columns:
        result[column] = np.log1p(result[column])

    return result
