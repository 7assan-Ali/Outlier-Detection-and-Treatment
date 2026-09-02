# 📊 Outlier Detection & Treatment

A practical Python project that investigates statistical outliers using **IQR** and **Z-Score** methods on a Heart Disease dataset.

## 🎯 Project Objective

Compare two common statistical approaches for detecting unusual observations, evaluate their results, and discuss appropriate treatment strategies without blindly removing valid data.

## 📦 Dataset

- 10,000 rows
- 21 columns
- 9 numerical features analyzed for outliers
- Target: `Heart Disease Status`

## 🔬 Methodology

1. Explore the dataset
2. Inspect missing values
3. Detect outliers using IQR
4. Detect outliers using Z-Score
5. Compare detection results
6. Evaluate treatment options
7. Document findings

## 📈 Results

For the nine numerical features evaluated:

- **IQR outliers: 0**
- **Z-Score outliers: 0**

No observations were removed or capped based on these tests.

The main data-quality issue identified was missing `Alcohol Consumption` data. Because simple mode imputation noticeably changed the distribution, the project avoids treating that method as automatically appropriate and recommends further investigation.

## 🧮 Detection Methods

### IQR

```text
IQR = Q3 - Q1
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

### Z-Score

```text
Z = (X - mean) / standard deviation
```

A common screening threshold is `|Z| > 3`.

## 🛠️ Treatment Strategies

Depending on context, outliers may be:

- Kept when they represent valid observations
- Trimmed when justified
- Capped / Winsorized
- Investigated for data-entry errors
- Transformed using an appropriate mathematical transformation

## 📁 Project Structure

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

## 🚀 Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## 👥 Team

- Hassan Ali Hassan
- Abdelrahman Ahmed Abdelrahman
- Mohamed Hussein Ramadan

## 📚 References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*.
3. NIST/SEMATECH. *e-Handbook of Statistical Methods*.

## 👨‍💻 Author / Team Project

Developed as a collaborative data analysis project.
