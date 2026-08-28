import pandas as pd

from Src.outlier_treatment import keep, trim_iqr, cap_iqr, log_transform


def test_keep_preserves_data():
    df = pd.DataFrame({"value": [1, 2, 3]})
    result = keep(df)
    pd.testing.assert_frame_equal(result, df)
    assert result is not df


def test_trim_iqr_removes_outlier_row():
    df = pd.DataFrame({"value": [1, 2, 3, 4, 100]})
    result = trim_iqr(df, ["value"])
    assert 100 not in result["value"].values


def test_cap_iqr_limits_outlier():
    df = pd.DataFrame({"value": [1, 2, 3, 4, 100]})
    result = cap_iqr(df, ["value"])
    assert result["value"].max() < 100


def test_log_transform():
    df = pd.DataFrame({"value": [0, 1, 9]})
    result = log_transform(df, ["value"])
    assert result.loc[2, "value"] == 2.302585092994046
