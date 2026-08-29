import pandas as pd

from config.config import Data_Path
from Src.iqr_detection import detect_iqr_outliers
from Src.zscore_detection import detect_zscore_outliers


def main():
    df = pd.read_csv(Data_Path)

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    # Remove the target if it is numeric
    if "Heart Disease Status" in numeric_columns:
        numeric_columns.remove("Heart Disease Status")

    print("Dataset shape:", df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    print("\nIQR Results:")
    iqr_results = detect_iqr_outliers(df, numeric_columns)
    print(iqr_results)

    print("\nZ-Score Results:")
    zscore_results = detect_zscore_outliers(df, numeric_columns)
    print(zscore_results)

    print("\nComparison:")
    comparison = iqr_results[["Feature", "Outlier Count"]].rename(
        columns={"Outlier Count": "IQR Outliers"}
    )
    comparison["Z-Score Outliers"] = zscore_results["Outlier Count"].values
    print(comparison)


if __name__ == "__main__":
    main()
