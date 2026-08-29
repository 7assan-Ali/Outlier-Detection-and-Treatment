# Outlier Detection and Treatment

A simple Python project for studying outliers using **IQR** and **Z-Score** on a Heart Disease dataset.

## Team Members

- Hassan Ali Hassan
- Abdelrahman Ahmed Abdelrahman
- Mohamed Hussein Ramadan

## Dataset

- 10,000 rows
- 21 columns
- 9 numerical features used for outlier detection
- Target: `Heart Disease Status`

## Project Steps

1. Explore the dataset.
2. Check missing values.
3. Detect outliers using IQR.
4. Detect outliers using Z-Score.
5. Compare the results.
6. Discuss possible treatment methods.

## Results

For all nine numerical features:

- **IQR outliers: 0**
- **Z-Score outliers: 0**

Therefore, no rows were removed or capped because the analysis did not find statistical outliers.

The main missing-data issue was `Alcohol Consumption` with **2,586 missing values (25.86%)**. A simple mode-imputation test changed the distribution noticeably, so this method was not considered suitable without further investigation.

## IQR

```text
IQR = Q3 - Q1
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

## Z-Score

```text
Z = (X - mean) / standard deviation
```

A common screening rule is `|Z| > 3`.

## Treatment Methods

The research discusses:

- Keep
- Trimming
- Capping / Winsorization
- Imputation
- Mathematical transformations

The choice depends on the data, the reason for the unusual value, and the goal of the analysis.

## Project Structure

```text
Data/raw/heart_disease.csv
config/config.py
Src/iqr_detection.py
Src/zscore_detection.py
Src/outlier_treatment.py
notebooks/exploratory_analysis.ipynb
docs/research.md
main.py
requirements.txt
README.md
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the analysis:

```powershell
python main.py
```

## Research

The detailed research is available in [`docs/research.md`](docs/research.md).

## References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
3. NIST/SEMATECH. *e-Handbook of Statistical Methods*.
