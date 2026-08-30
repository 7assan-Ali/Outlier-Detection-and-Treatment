# Project Documentation

## About the Project

This project is a practical study of **outlier detection and treatment** using a Heart Disease dataset.

We started the work in the notebook to understand the data first, then moved the main calculations into simple Python files.

The main goal is to compare two common methods:

- IQR
- Z-Score

and understand what we should do when unusual values are found.

## Team Members

- Hassan Ali Hassan
- Abdelrahman Ahmed Abdelrahman
- Mohamed Hussein Ramadan

## Dataset

The dataset contains **10,000 rows and 21 columns**.

For the outlier analysis, we used the numerical columns only:

- Age
- Blood Pressure
- Cholesterol Level
- BMI
- Sleep Hours
- Triglyceride Level
- Fasting Blood Sugar
- CRP Level
- Homocysteine Level

We did not use `Heart Disease Status` for outlier detection because it is the target column.

## What We Did

### 1. Loaded the data

We loaded `heart_disease.csv` and checked its shape, columns, data types, and first few rows.

### 2. Checked missing values

We counted missing values in every column and calculated their percentages.

Most columns had only a small number of missing values. The main problem was `Alcohol Consumption`, which had **2,586 missing values (25.86%)**.

We also tested filling these missing values with the mode. The result changed the distribution noticeably, so we decided not to apply this automatically.

### 3. Explored the numerical data

We used:

- `describe()` for summary statistics
- `nunique()` to see the number of different values
- Histograms to look at distributions
- Skewness to get a simple idea about the shape of the data

### 4. Detected outliers using IQR

For every numerical feature, we calculated Q1, Q3 and IQR.

```text
IQR = Q3 - Q1

Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

Any value below the lower fence or above the upper fence was counted as an outlier.

We used the normal **1.5 × IQR rule** and did not use extreme fences.

### 5. Detected outliers using Z-Score

We calculated the Z-Score for every numerical feature using:

```text
Z = (X - Mean) / Standard Deviation
```

We used:

```text
|Z| > 3
```

as the outlier rule.

### 6. Compared the two methods

After running both methods, we compared the number of detected outliers for every numerical feature.

The result was:

```text
IQR Outliers     = 0
Z-Score Outliers = 0
```

So, both methods gave the same result on our dataset.

## Outlier Treatment

Because no potential numerical outliers were detected, we did not remove or cap any rows in the final dataset.

We still included simple treatment functions in the project to demonstrate the main approaches:

- **Keep:** leave valid unusual values as they are.
- **Trimming:** remove observations when there is a valid reason to do so.
- **Capping:** replace extreme values with selected limits.
- **Log transformation:** reduce the effect of large values when the data is suitable for it.

An important point from the research is that an outlier is not automatically an error. We should understand the data before deciding to remove or change it.

## Project Structure

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

## What Each File Does

### `main.py`

Runs the main analysis and shows the IQR and Z-Score results.

### `config/config.py`

Contains the path of the dataset so we do not have to write the path in different files.

### `Src/iqr_detection.py`

Contains the function used to detect outliers using IQR.

### `Src/zscore_detection.py`

Contains the function used to detect outliers using Z-Score.

### `Src/outlier_treatment.py`

Contains simple examples of possible outlier treatment methods.

### `notebooks/exploratory_analysis.ipynb`

This was our testing area. We used it to explore the dataset, check missing values, visualize distributions, calculate skewness, and test IQR and Z-Score before organizing the code.

### `docs/research.md`

Contains the research part of the project, including the explanation of IQR, Z-Score, treatment methods, comparison, results, and references.

## How to Run

Create the environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the libraries:

```powershell
python -m pip install -r requirements.txt
```

Then run:

```powershell
python main.py
```

## Final Result

The main finding of the project is simple: **we did not find potential numerical outliers using either IQR or Z-Score with the selected rules.**

Therefore, there was no need to trim or cap the numerical data.

The most noticeable preprocessing issue was missing data in `Alcohol Consumption`, which we investigated separately instead of changing the data automatically.

## References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
3. NIST/SEMATECH. *e-Handbook of Statistical Methods*.
