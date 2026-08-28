import pandas as pd

from Src.zscore_detection import detect_zscore_outliers


def test_zscore_detects_outlier():
    df = pd.DataFrame({"value": [10, 10, 10, 10, 10, 100]})
    result = detect_zscore_outliers(df, ["value"])
    assert result.loc[0, "Outlier Count"] == 1


def test_zscore_no_outliers():
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5]})
    result = detect_zscore_outliers(df, ["value"])
    assert result.loc[0, "Outlier Count"] == 0
