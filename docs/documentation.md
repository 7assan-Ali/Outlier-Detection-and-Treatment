# Project Documentation

## 1. Project Overview

This project detects numerical outliers in a Heart Disease dataset using two common methods:

- IQR (Interquartile Range)
- Z-Score

The project also explains common ways to treat outliers and missing values.

## 2. Dataset

The dataset contains 10,000 records and 21 columns.

The numerical columns used in the outlier analysis are:

- Age
- Blood Pressure
- Cholesterol Level
- BMI
- Sleep Hours
- Triglyceride Level
- Fasting Blood Sugar
- CRP Level
- Homocysteine Level

`Heart Disease Status` is the target column and is not used for numerical outlier detection.

## 3. Project Structure

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

## 4. Installation

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required libraries:

```powershell
python -m pip install -r requirements.txt
```

## 5. Running the Project

Run the main program from the project root:

```powershell
python main.py
```

The notebook can be opened from:

```text
notebooks/exploratory_analysis.ipynb
```

If the notebook cannot import `config`, run it with the project root as the working directory or use the relative dataset path inside the notebook.

## 6. IQR Detection

The IQR method is implemented in:

```text
Src/iqr_detection.py
```

The calculation is:

```text
IQR = Q3 - Q1
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

A value outside the lower or upper fence is counted as an outlier.

## 7. Z-Score Detection

The Z-Score method is implemented in:

```text
Src/zscore_detection.py
```

The formula is:

```text
Z = (X - Mean) / Standard Deviation
```

The project uses the common rule:

```text
|Z| > 3
```

## 8. Outlier Treatment

The treatment functions are in:

```text
Src/outlier_treatment.py
```

The project demonstrates simple treatment options:

- Keep the values.
- Remove extreme rows (Trimming).
- Limit values to selected boundaries (Capping).
- Apply a logarithmic transformation when appropriate.

Treatment should not be applied automatically. First, check whether the unusual value is a real observation or a data error.

## 9. Missing Values

Missing values are checked during exploratory analysis.

Most numerical and categorical columns have a small number of missing values. `Alcohol Consumption` has the largest number of missing values: 2,586 records (25.86%).

A mode-imputation test was performed, but it changed the distribution of the feature considerably. Therefore, the project does not automatically apply mode imputation to this column.

## 10. Results

For the nine numerical features analyzed:

```text
IQR Outliers     = 0
Z-Score Outliers = 0
```

Because both methods found no potential numerical outliers, no trimming or capping was applied.

## 11. Main Files

### `main.py`

Runs the basic analysis from the command line.

### `config/config.py`

Stores the path to the raw dataset.

### `Src/iqr_detection.py`

Contains the IQR outlier detection function.

### `Src/zscore_detection.py`

Contains the Z-Score outlier detection function.

### `Src/outlier_treatment.py`

Contains simple functions for possible outlier treatments.

### `notebooks/exploratory_analysis.ipynb`

Used to explore and test the analysis step by step before organizing the code into Python files.

### `docs/research.md`

Contains the research explanation, comparison, findings, and references.

## 12. References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
3. NIST/SEMATECH. *e-Handbook of Statistical Methods*.

## 13. Team Members

- Hassan Ali Hassan
- Abdelrahman Ahmed Abdelrahman
- Mohamed Hussein Ramadan
