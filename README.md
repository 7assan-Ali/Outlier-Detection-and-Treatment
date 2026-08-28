# Outlier Detection and Treatment

A practical data-analysis project for detecting, comparing, and treating outliers using the **Interquartile Range (IQR)** and **Z-Score** methods. The project also demonstrates several treatment strategies and provides a reusable Python backend with a GUI-oriented structure.

## Team Members

- **Hassan Ali Hassan**
- **Abdelrahman Ahmed Abdelrahman**
- **Mohamed Hussein Ramadan**

## Project Overview

Outliers are observations that differ substantially from the majority of observations in a dataset. They may result from measurement errors, data-entry problems, unusual but valid observations, or genuine variation in the population. Therefore, an outlier should not automatically be deleted; the appropriate treatment depends on the data-generating process and the objective of the analysis.

This project applies the research question to a **Heart Disease** dataset containing 10,000 observations and 21 variables. The analysis focuses on numerical features such as Age, Blood Pressure, Cholesterol Level, BMI, Sleep Hours, Triglyceride Level, Fasting Blood Sugar, CRP Level, and Homocysteine Level.

## Research Question

How can the IQR method be used to identify outliers, how should detected outliers be treated, and when is IQR more appropriate than the Z-Score approach?

## Research Objectives

1. Explore and understand the dataset before detecting outliers.
2. Identify missing values and describe their distribution.
3. Detect potential outliers using the IQR method.
4. Detect potential outliers using the Z-Score method.
5. Compare the results of IQR and Z-Score.
6. Explain and implement common outlier-treatment strategies.
7. Select treatment methods according to the characteristics and purpose of the data.
8. Provide reusable Python functions and a GUI-ready project structure.

# Research Background

## 1. What is an Outlier?

An outlier is an observation that appears to be unusually far from the other observations in a sample. An unusual observation can represent a data-quality problem, but it can also represent genuine variation or an interesting phenomenon. Consequently, detecting an outlier is not equivalent to proving that the observation is incorrect.

NIST emphasizes that possible causes should be investigated before observations are rejected. In particular, an outlier may be caused by incorrect coding or experimental problems, while in other cases it may be a legitimate observation.

## 2. IQR Method

The Interquartile Range measures the spread of the middle 50% of the observations.

### Step 1: Calculate Q1

Q1 is the 25th percentile.

### Step 2: Calculate Q3

Q3 is the 75th percentile.

### Step 3: Calculate IQR

```text
IQR = Q3 - Q1
```

### Step 4: Calculate the fences

```text
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

Observations below the lower fence or above the upper fence are commonly flagged as potential outliers.

The IQR approach is based on quartiles and is therefore less dependent on the mean and standard deviation than the ordinary Z-Score approach. This makes it particularly useful when the distribution is skewed or when extreme observations may influence the mean and standard deviation.

## 3. Z-Score Method

The standard Z-Score expresses an observation in units of standard deviations from the sample mean.

```text
Z = (X - mean) / standard deviation
```

A commonly used rule is to flag observations whose absolute Z-Score is greater than 3:

```text
|Z| > 3
```

The threshold should not be treated as a universal law. Its suitability depends on the distribution, sample size, and analytical context. NIST also notes that ordinary Z-Scores can be misleading in some situations, especially when the data are not well represented by the assumptions behind mean and standard deviation.

## 4. IQR vs Z-Score

| Aspect | IQR | Z-Score |
|---|---|---|
| Main statistics | Q1, Q3, IQR | Mean, Standard Deviation |
| Distribution assumption | No normality assumption required | More suitable when distribution is approximately normal |
| Sensitivity to extreme values | Relatively robust | More sensitive because mean and SD can be affected |
| Typical rule | Outside Q1 ± 1.5×IQR | Usually |Z| > 3 |
| Useful for skewed data | Yes | Less suitable without additional checks |
| Interpretation | Distance from quartile-based fences | Distance from the mean in SD units |

### When should IQR be preferred?

IQR is generally a strong choice when the distribution is skewed, when extreme values may affect the mean and standard deviation, or when a robust exploratory rule is desired.

### When should Z-Score be preferred?

Z-Score can be useful when the numerical feature is approximately normally distributed and the analyst wants to express unusual observations relative to the mean and standard deviation.

## 5. Outlier Treatment

Detecting an outlier does not automatically determine what should happen to it. Common approaches include:

### Keep

The observation is retained when it is considered valid and meaningful.

### Trimming

The observation is removed from the analysis. This can be appropriate when there is strong evidence that an observation is erroneous, but deleting valid observations can introduce bias and reduce sample size.

### Capping

Values beyond selected boundaries are replaced by the boundary values. In this project, IQR fences can be used as the boundaries.

### Winsorization

Extreme values are replaced by less extreme values rather than deleting the corresponding observations. The exact winsorization rule should be reported because different thresholds can produce different results.

### Imputation

Imputation replaces missing values with estimated values. It is primarily a missing-data treatment rather than a direct outlier treatment. In this project, missing categorical values were investigated separately from outlier detection.

### Mathematical Transformation

Transformations such as logarithmic or Yeo-Johnson transformations can reduce skewness and decrease the influence of very large or very small values while retaining observations.

## 6. How to Choose a Treatment

The treatment should be selected after considering:

- **Cause of the observation:** measurement error, data-entry error, or genuine observation.
- **Distribution:** symmetric, skewed, heavy-tailed, or approximately normal.
- **Sample size:** removing observations has a greater impact in small datasets.
- **Feature meaning:** extreme values may have real scientific or medical meaning.
- **Analysis objective:** descriptive statistics, statistical inference, or machine learning may require different decisions.
- **Model sensitivity:** some models are more sensitive to extreme observations than others.
- **Robustness:** results should ideally be checked under reasonable alternative treatments.

A treatment should therefore be justified rather than selected only because it improves a metric.

# Dataset Analysis

The project uses a Heart Disease dataset with:

- **10,000 rows**
- **21 columns**
- **9 numerical features** used for the main outlier analysis
- **12 categorical features**
- **Heart Disease Status** as the target variable

## Missing Values

Most features contain a very small proportion of missing values. The major exception is `Alcohol Consumption`, with 2,586 missing observations (**25.86%**).

A test of simple mode imputation showed that replacing all missing `Alcohol Consumption` values with `Medium` changed the observed proportion of `Medium` from approximately **33.72% to 50.86%**. This demonstrates why the missing-data mechanism and the amount of missingness should be considered before blindly applying mode imputation.

For the remaining categorical variables, missingness was approximately 0.2–0.3%, so mode imputation has a much smaller effect on the overall distribution. The project keeps missing-value treatment conceptually separate from outlier treatment.

## Outlier Detection Results

For the nine numerical features analyzed in the Heart Disease dataset:

| Feature | IQR Outliers | Z-Score Outliers |
|---|---:|---:|
| Age | 0 | 0 |
| Blood Pressure | 0 | 0 |
| Cholesterol Level | 0 | 0 |
| BMI | 0 | 0 |
| Sleep Hours | 0 | 0 |
| Triglyceride Level | 0 | 0 |
| Fasting Blood Sugar | 0 | 0 |
| CRP Level | 0 | 0 |
| Homocysteine Level | 0 | 0 |

Both methods identified **zero potential outliers** using the selected standard thresholds.

This result is itself an important finding. The project does not force an outlier treatment when the detection methods do not identify observations as outliers.

## Skewness Findings

The calculated skewness values were close to zero for the numerical features, indicating that the features were broadly symmetric rather than strongly skewed.

Examples:

```text
Age                   -0.006789
Blood Pressure         0.013907
Cholesterol Level     -0.007120
BMI                   -0.021342
Sleep Hours            0.000172
Triglyceride Level     0.006142
Fasting Blood Sugar   -0.008915
CRP Level             -0.004069
Homocysteine Level     0.007886
```

These values support the observation that the numerical distributions are not strongly skewed in this dataset.

# Project Implementation

```text
Outlier-Detection-and-Treatment/
│
├── Data/
│   └── raw/
│       └── heart_disease.csv
│
├── config/
│   └── config.py
│
├── Src/
│   ├── iqr_detection.py
│   ├── zscore_detection.py
│   ├── preprocessing.py
│   ├── outlier_treatment.py
│   ├── visualization.py
│   └── utils.py
│
├── gui/
│   ├── app.py
│   ├── components.py
│   └── dashboard.py
│
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   └── test.ipynb
│
├── tests/
│   ├── test_iqr.py
│   ├── test_zscore.py
│   └── test_treatment.py
│
├── main.py
└── README.md
```

## Main Technologies

- Python
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Matplotlib
- Seaborn
- Tkinter
- Pytest

## Treatment Functions Implemented

The backend includes reusable functions for:

- Keep
- IQR trimming
- IQR capping
- Winsorization
- Log transformation
- Yeo-Johnson transformation

## Running the Project

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the main analysis:

```bash
python main.py
```

Run tests:

```bash
pytest
```

## Scientific References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. NIST/SEMATECH. *e-Handbook of Statistical Methods — Detection of Outliers*. National Institute of Standards and Technology.
3. Iglewicz, B., & Hoaglin, D. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
4. Hawkins, D. M. (1980). *Identification of Outliers*. Chapman and Hall.
5. Gollin, D., & Udry, C. (2021). Heterogeneity in productivity: evidence from African production. *Econometrica*, 89(6), 2939–2978.
6. Musillo, G. (2026). *Winsorizing and trimming in RCTs*. Journal of Development Economics, 182, 103815. https://doi.org/10.1016/j.jdeveco.2026.103815

## Important Note

Outlier detection is a statistical screening step, not proof that an observation is wrong. The final treatment should be justified by domain knowledge, data quality, distributional characteristics, and the objective of the analysis.

## Authors

**Hassan Ali Hassan — Abdelrahman Ahmed Abdelrahman — Mohamed Hussein Ramadan**
