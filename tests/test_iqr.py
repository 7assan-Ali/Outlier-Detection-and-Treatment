import pandas as pd

from Src.iqr_detection import detect_iqr_outliers


def test_iqr_detects_outlier():
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 100]})
    result = detect_iqr_outliers(df, ["value"])
    assert result.loc[0, "Outlier Count"] == 1


def test_iqr_no_outliers():
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5]})
    result = detect_iqr_outliers(df, ["value"])
    assert result.loc[0, "Outlier Count"] == 0
