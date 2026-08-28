from config.config import Data_Path
from Src.utils import load_data, missing_values_summary
from Src.preprocessing import get_feature_types
from Src.iqr_detection import detect_iqr_outliers
from Src.zscore_detection import detect_zscore_outliers
from Src.utils import compare_outlier_methods


def main():
    df = load_data(Data_Path)

    numeric_columns, _ = get_feature_types(
        df,
        target_column="Heart Disease Status",
    )

    print(f"Dataset shape: {df.shape}")
    print("\nMissing values:")
    print(missing_values_summary(df))

    iqr_results = detect_iqr_outliers(df, numeric_columns)
    zscore_results = detect_zscore_outliers(df, numeric_columns)

    comparison = compare_outlier_methods(iqr_results, zscore_results)

    print("\nIQR vs Z-Score:")
    print(comparison)


if __name__ == "__main__":
    main()
