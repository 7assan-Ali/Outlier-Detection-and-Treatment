# Project Documentation

## 1. About the Project

This project is a practical study of **Outlier Detection and Treatment** using a Heart Disease dataset.

We first explored the data in a Jupyter Notebook, then organized the main calculations into simple Python files. The main goal is to understand the data, detect possible numerical outliers, compare IQR with Z-Score, and understand what can be done when an unusual value is found.

## 2. Team Members

- Hassan Ali Hassan
- Abdelrahman Ahmed Abdelrahman
- Mohamed Hussein Ramadan

---

## 3. Dataset

The dataset is stored in:

```text
Data/raw/heart_disease.csv
```

It contains **10,000 rows and 21 columns**.

The numerical features used for outlier detection are:

```text
Age
Blood Pressure
Cholesterol Level
BMI
Sleep Hours
Triglyceride Level
Fasting Blood Sugar
CRP Level
Homocysteine Level
```

The target column is:

```text
Heart Disease Status
```

We did not use the target column for numerical outlier detection.

---

# 4. Project Workflow

The work was done in this order:

```text
Load Dataset
      ↓
Understand the Data
      ↓
Check Missing Values
      ↓
Select Numerical Columns
      ↓
Descriptive Statistics
      ↓
Histograms
      ↓
Skewness
      ↓
IQR Detection
      ↓
Z-Score Detection
      ↓
Compare Results
      ↓
Decide on Treatment
      ↓
Document the Results
```

---

# 5. Step 1 - Load the Dataset

We loaded the CSV file using Pandas.

The path is kept in `config/config.py` so it does not have to be repeated in different files.

```python
import pandas as pd
from config.config import Data_Path

df = pd.read_csv(Data_Path)
```

We then used:

```python
df.head()
```

to make sure the data was loaded correctly.

---

# 6. Step 2 - Understand the Data

Before applying any method, we checked the basic structure of the dataset.

We used:

```python
df.shape
```

and:

```python
df.info()
```

This showed that the dataset contains:

```text
10,000 rows
21 columns
```

We also checked the column names and data types.

---

# 7. Step 3 - Missing Values

We checked how many values are missing in each column:

```python
df.isnull().sum()
```

Then we calculated the percentage:

```python
missing_percent = df.isnull().sum() / len(df) * 100
```

Most columns had only a small number of missing values. The main exception was:

```text
Alcohol Consumption
Missing = 2,586
Percentage = 25.86%
```

### Mode Imputation Test

We tested replacing the missing values in `Alcohol Consumption` with its mode, which was `Medium`.

Before:

```text
Medium = 2500
Low    = 2488
High   = 2426
```

After:

```text
Medium = 5086
Low    = 2488
High   = 2426
```

The distribution changed noticeably. For that reason, we did not automatically apply this imputation to the final data.

This test helped us understand that a missing-value treatment should be checked instead of applied blindly.

---

# 8. Step 4 - Select Numerical Columns

IQR and Z-Score were applied to numerical features only.

We selected them using:

```python
numeric_columns = df.select_dtypes(include='number').columns
```

This gave us the nine numerical features listed in the Dataset section.

---

# 9. Step 5 - Descriptive Statistics

We used:

```python
df[numeric_columns].describe().T
```

This gave us the count, mean, standard deviation, minimum, quartiles, median, and maximum for each numerical feature.

We also checked the number of unique values:

```python
df[numeric_columns].nunique().sort_values()
```

This was done before outlier detection so we had a basic understanding of the data ranges.

---

# 10. Step 6 - Target Distribution

We checked the target variable separately:

```python
df['Heart Disease Status'].value_counts()
```

The result was:

| Status | Count | Percentage |
|---|---:|---:|
| No | 8,000 | 80% |
| Yes | 2,000 | 20% |

This was only an exploratory step. The target was not included in the outlier calculations.

---

# 11. Step 7 - Histograms

We created histograms for the numerical columns:

```python
df[numeric_columns].hist(figsize=(12, 10), bins=20)
```

The purpose was to visually check the distributions and see whether there were obvious unusual values.

The numerical variables appeared generally spread across their ranges without obvious extreme observations.

The plots were used as a visual check, while IQR and Z-Score were used for the actual statistical detection.

---

# 12. Step 8 - Skewness

We calculated skewness using:

```python
df[numeric_columns].skew()
```

The values were close to zero for the numerical features, so there was no strong skewness.

Some of the values were:

```text
Age                  -0.0068
Blood Pressure        0.0139
Cholesterol Level    -0.0071
BMI                  -0.0213
Sleep Hours           0.0002
Triglyceride Level    0.0061
Fasting Blood Sugar  -0.0089
CRP Level            -0.0041
Homocysteine Level    0.0079
```

This was useful for understanding why Z-Score could also be considered for this dataset.

---

# 13. Step 9 - IQR Outlier Detection

The first method we used was **IQR (Interquartile Range)**.

IQR is based on the middle 50% of the data.

### Q1 and Q3

- Q1 = 25th percentile
- Q3 = 75th percentile

### Formula

```text
IQR = Q3 - Q1
```

### Fences

We used the standard 1.5 × IQR rule:

```text
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

A value below the lower fence or above the upper fence is counted as a potential outlier.

We used the normal lower and upper fences only. **Extreme fences were not used.**

### Example: Age

```text
Q1 = 34
Q3 = 65
IQR = 31

Lower Fence = -12.5
Upper Fence = 111.5
```

The Age values are approximately between 18 and 80, so none of them is outside the calculated fences.

---

# 14. IQR Results

The IQR method found no potential outliers in any of the nine numerical features.

| Feature | Q1 | Q3 | IQR | Lower Fence | Upper Fence | Outliers |
|---|---:|---:|---:|---:|---:|---:|
| Age | 34.00 | 65.00 | 31.00 | -12.50 | 111.50 | 0 |
| Blood Pressure | 134.00 | 165.00 | 31.00 | 87.50 | 211.50 | 0 |
| Cholesterol Level | 187.00 | 263.00 | 76.00 | 73.00 | 377.00 | 0 |
| BMI | 23.658 | 34.520 | 10.862 | 7.365 | 50.813 | 0 |
| Sleep Hours | 5.450 | 8.532 | 3.082 | 0.827 | 13.154 | 0 |
| Triglyceride Level | 176.00 | 326.00 | 150.00 | -49.00 | 551.00 | 0 |
| Fasting Blood Sugar | 99.00 | 141.00 | 42.00 | 36.00 | 204.00 | 0 |
| CRP Level | 3.674 | 11.256 | 7.581 | -7.698 | 22.628 | 0 |
| Homocysteine Level | 8.723 | 16.141 | 7.417 | -2.403 | 27.266 | 0 |

Final IQR result:

```text
IQR Outliers = 0
```

---

# 15. Step 10 - Z-Score Detection

The second method was **Z-Score**.

It measures how far a value is from the mean in standard-deviation units.

### Formula

```text
Z = (X - Mean) / Standard Deviation
```

We used the common rule:

```text
|Z| > 3
```

A value with an absolute Z-Score greater than 3 is counted as a potential outlier.

### Simple Example

If:

```text
Mean = 50
Standard Deviation = 10
X = 80
```

then:

```text
Z = (80 - 50) / 10
Z = 3
```

Because our rule is `|Z| > 3`, a value exactly equal to 3 is not counted.

---

# 16. Z-Score Results

The Z-Score method also found no potential outliers.

| Feature | Z-Score Outliers |
|---|---:|
| Age | 0 |
| Blood Pressure | 0 |
| Cholesterol Level | 0 |
| BMI | 0 |
| Sleep Hours | 0 |
| Triglyceride Level | 0 |
| Fasting Blood Sugar | 0 |
| CRP Level | 0 |
| Homocysteine Level | 0 |

Final Z-Score result:

```text
Z-Score Outliers = 0
```

---

# 17. Step 11 - Comparison Between IQR and Z-Score

After calculating both methods, we compared the results feature by feature.

| Feature | IQR Outliers | Z-Score Outliers | Total |
|---|---:|---:|---:|
| Age | 0 | 0 | 0 |
| Blood Pressure | 0 | 0 | 0 |
| Cholesterol Level | 0 | 0 | 0 |
| BMI | 0 | 0 | 0 |
| Sleep Hours | 0 | 0 | 0 |
| Triglyceride Level | 0 | 0 | 0 |
| Fasting Blood Sugar | 0 | 0 | 0 |
| CRP Level | 0 | 0 | 0 |
| Homocysteine Level | 0 | 0 | 0 |

Both methods produced the same result for this dataset.

### Main Difference

| IQR | Z-Score |
|---|---|
| Based on Q1 and Q3 | Based on mean and standard deviation |
| More resistant to extreme values | More affected by extreme values |
| Does not require normal distribution | More suitable for approximately normal data |
| Common rule: 1.5 × IQR | Common rule: `|Z| > 3` |

There is no single method that is always better. The choice depends on the data and the purpose of the analysis.

---

# 18. Step 12 - Outlier Treatment

After detecting an outlier, we need to decide what to do with it. An unusual value is not automatically a mistake.

The project demonstrates the main treatment options.

### Keep

We keep the value if it is valid and represents a real observation.

### Trimming

Trimming means removing the observation. It can be appropriate when there is a clear reason, such as an obvious data-entry error.

### Capping / Winsorizing

Capping limits an extreme value to a selected boundary instead of deleting the whole row.

### Mathematical Transformation

A transformation such as Log can reduce the effect of large values when the feature is suitable for it.

### Imputation

Imputation is mainly used for missing values rather than normal outliers. The appropriate method depends on the feature and the amount and reason for missing data.

---

# 19. Step 13 - Choosing the Treatment

We should consider several things before changing an outlier:

- Is the value real or a data error?
- What is the distribution of the feature?
- How large is the dataset?
- How much does the value affect the analysis?
- Is the model sensitive to extreme values?
- What is the goal of the analysis?

For our dataset, both detection methods found zero potential numerical outliers. Therefore, there was no reason to trim or cap the numerical features.

---

# 20. Step 14 - Organizing the Project

After testing the analysis in the notebook, we organized the main logic into separate files.

```text
Outlier-Detection-and-Treatment/
│
├── Data/
│   └── raw/
│       └── heart_disease.csv
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── Src/
│   ├── __init__.py
│   ├── iqr_detection.py
│   ├── zscore_detection.py
│   └── outlier_treatment.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── docs/
│   ├── research.md
│   └── documentation.md
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 21. Explanation of the Project Files

### `Data/raw/heart_disease.csv`

The dataset used in the analysis.

### `config/config.py`

Stores the dataset path in one place.

### `Src/iqr_detection.py`

Contains the IQR outlier detection function. It calculates Q1, Q3, IQR, the lower and upper fences, and the number of potential outliers.

### `Src/zscore_detection.py`

Contains the Z-Score calculation and counts values where `|Z| > 3`.

### `Src/outlier_treatment.py`

Contains simple examples of Keep, Trimming, Capping, and Log Transformation.

### `notebooks/exploratory_analysis.ipynb`

This was the testing area. We used it to explore the data and check every step before organizing the code.

### `main.py`

Runs the main IQR and Z-Score analysis from the project root.

### `docs/research.md`

Contains the research explanation, comparison, treatment methods, results, and references.

### `docs/documentation.md`

Explains the complete work done in the project step by step.

### `README.md`

Gives a short overview of the project.

### `requirements.txt`

Contains the Python packages needed to run the project.

---

# 22. Running the Project

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the requirements:

```powershell
python -m pip install -r requirements.txt
```

Run the main program from the project root:

```powershell
python main.py
```

For the notebook, open:

```text
notebooks/exploratory_analysis.ipynb
```

and run the cells from top to bottom.

---

# 23. Final Results

The final outlier comparison was:

```text
IQR Outliers     = 0
Z-Score Outliers = 0
```

Therefore:

```text
No numerical rows were removed.
No numerical values were capped.
```

The main preprocessing issue found in the dataset was:

```text
Alcohol Consumption
2,586 missing values
25.86%
```

We tested mode imputation and observed a noticeable change in the distribution, so we did not automatically apply it.

---

# 24. What We Learned

The main point of the project is that outlier detection is not just about finding unusual numbers.

We need to:

1. Understand the dataset first.
2. Check whether the unusual value is valid.
3. Use an appropriate detection method.
4. Compare the results when useful.
5. Choose a treatment based on the data.
6. Avoid changing data without a clear reason.

In our case, the correct decision was to **keep the numerical data unchanged** because neither IQR nor Z-Score detected potential outliers.

---

# 25. Conclusion

We followed a complete but simple workflow starting from data exploration and ending with outlier detection and treatment decisions.

The two methods used in the project, IQR and Z-Score, both returned zero potential outliers for the nine numerical features. Therefore, no trimming or capping was applied.

The project also showed that missing values need separate attention. The `Alcohol Consumption` column had 25.86% missing values, and the mode-imputation test changed its distribution noticeably.

The final decision was based on the actual analysis rather than applying a preprocessing technique automatically.

---

# 26. References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
3. NIST/SEMATECH. *e-Handbook of Statistical Methods*.

---

## Quick Summary

```text
Heart Disease Dataset
        ↓
Data Exploration
        ↓
Missing Values
        ↓
Numerical Features
        ↓
Statistics + Histograms + Skewness
        ↓
IQR → 0 Outliers
        ↓
Z-Score → 0 Outliers
        ↓
Comparison
        ↓
No Trimming / No Capping
        ↓
Final Documentation
```
