import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_distributions(df: pd.DataFrame, columns: list[str], bins: int = 30) -> None:
    """Plot histograms for selected numeric features."""
    rows = (len(columns) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, 4 * rows))
    axes = axes.flatten() if hasattr(axes, "flatten") else [axes]

    for ax, column in zip(axes, columns):
        sns.histplot(df[column], bins=bins, ax=ax)
        ax.set_title(column)

    for ax in axes[len(columns):]:
        ax.remove()

    plt.tight_layout()
    plt.show()


def plot_boxplots_by_target(df: pd.DataFrame, columns: list[str], target: str) -> None:
    """Plot numeric feature boxplots grouped by a target column."""
    rows = (len(columns) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, 4 * rows))
    axes = axes.flatten() if hasattr(axes, "flatten") else [axes]

    for ax, column in zip(axes, columns):
        sns.boxplot(data=df, x=target, y=column, ax=ax)
        ax.set_title(column)

    for ax in axes[len(columns):]:
        ax.remove()

    plt.tight_layout()
    plt.show()


def plot_outlier_comparison(comparison: pd.DataFrame) -> None:
    """Compare IQR and Z-Score outlier counts."""
    comparison[["IQR Outliers", "Z-Score Outliers"]].set_index(
        comparison["Feature"]
    ).plot(kind="bar", figsize=(12, 6))
    plt.title("IQR vs Z-Score Outlier Detection")
    plt.xlabel("Feature")
    plt.ylabel("Number of Outliers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
