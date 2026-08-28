# Outlier Detection and Treatment

A practical Python project for **exploring, detecting, comparing, and treating potential outliers** using the Interquartile Range (IQR) and standard Z-Score methods. The project combines a reproducible research notebook, reusable analysis modules, automated tests, and a Tkinter GUI.

## 👥 Team

- **Hassan Ali Hassan**
- **Abdelrahman Ahmed Abdelrahman**
- **Mohamed Hussein Ramadan**

## 🎯 Project Goal

The project investigates how IQR can be used to identify potential outliers through Q1, Q3, IQR, and lower/upper fences, how detected observations should be treated, and when IQR is more appropriate than Z-Score.

> **Important:** an outlier is not automatically an error. Detection is a statistical screening step; treatment must be justified by the data, domain context, and analysis objective.

## 🔬 Research

The full research paper is available here:

**[docs/research.md](docs/research.md)**

It covers:

- IQR and Z-Score theory
- Q1, Q3, IQR, lower and upper fences
- IQR vs Z-Score comparison
- Keep, trimming, capping, winsorization
- Missing-value imputation
- Log, Box-Cox, and Yeo-Johnson transformations
- Treatment-selection criteria
- Experimental results on the Heart Disease dataset
- Limitations and scientific references

## ❤️ Dataset

The main practical analysis uses a Heart Disease dataset with:

- **10,000 rows**
- **21 columns**
- **9 numerical features** for the main outlier analysis
- **12 categorical features**
- `Heart Disease Status` as the target

### Numerical Features

- Age
- Blood Pressure
- Cholesterol Level
- BMI
- Sleep Hours
- Triglyceride Level
- Fasting Blood Sugar
- CRP Level
- Homocysteine Level

## 📊 Main Findings

### IQR

Using the standard rule:

```text
IQR = Q3 - Q1
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

All nine numerical features produced **0 potential IQR outliers**.

### Z-Score

Using:

```text
Z = (X - mean) / standard deviation
```

and the screening threshold:

```text
|Z| > 3
```

all nine numerical features also produced **0 potential Z-Score outliers**.

### Missing Values

The major missing-data issue was `Alcohol Consumption`:

```text
Missing = 2,586
Percentage = 25.86%
```

A mode-imputation experiment changed `Medium` from **33.72% to 50.86%**, demonstrating that simple mode imputation can substantially distort a categorical distribution when the missing proportion is high.

## ⚖️ IQR vs Z-Score

| Aspect | IQR | Z-Score |
|---|---|---|
| Basis | Q1, Q3, IQR | Mean, Standard Deviation |
| Normality required | No | More appropriate for approximately normal data |
| Robustness | More robust to extreme values | More sensitive to extremes |
| Typical rule | 1.5 × IQR fences | `|Z| > 3` |
| Useful for skewed data | Yes | Less suitable without additional checks |

The project uses both methods as complementary diagnostic tools rather than assuming one method is universally better.

## 🛠️ Outlier Treatments

Implemented reusable treatment functions include:

- **Keep** — retain observations unchanged.
- **Trimming** — remove rows containing IQR outliers.
- **Capping** — clip values to IQR fences.
- **Winsorization** — limit extreme values without removing rows.
- **Log transformation** — reduce the influence of large non-negative values.
- **Yeo-Johnson transformation** — transform numerical variables while allowing zero and negative values.

Missing-value imputation is handled separately because imputation is primarily a missing-data treatment, not an outlier treatment.

## 🖥️ GUI

The project includes a Tkinter application for interactive analysis.

Current GUI workflow:

```text
Load CSV
   ↓
Preview Data
   ↓
Choose IQR or Z-Score
   ↓
Set threshold / multiplier
   ↓
Run Detection
   ↓
Review Results
   ↓
Apply IQR-based Treatment when appropriate
   ↓
Export CSV
```

### Important GUI behavior

When **Z-Score** is selected, the application performs Z-Score detection. The current treatment functions are IQR-based, so the GUI does **not silently apply an IQR treatment after a Z-Score analysis**. It keeps the dataset unchanged unless `Keep` is selected.

## 📁 Project Structure

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
│   ├── __init__.py
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
├── docs/
│   └── research.md
│
├── main.py
├── requirements.txt
└── README.md
```

## 🧰 Technologies

- Python
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Matplotlib
- Seaborn
- Tkinter
- Pytest

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/7assan-Ali/Outlier-Detection-and-Treatment.git
cd Outlier-Detection-and-Treatment
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, activate the environment from Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python main.py
```

### 5. Run the GUI

```bash
python gui/app.py
```

### 6. Run tests

```bash
pytest
```

## 🧪 Testing

The test suite covers:

- IQR outlier detection
- Z-Score outlier detection
- Keep treatment
- IQR trimming
- IQR capping
- Log transformation

Tests use small controlled datasets because the real Heart Disease dataset contains no detected numerical outliers under the selected rules.

## 📚 Scientific References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
3. National Institute of Standards and Technology (NIST/SEMATECH). *e-Handbook of Statistical Methods: Detection of Outliers*.
4. National Institute of Standards and Technology (NIST/SEMATECH). *e-Handbook of Statistical Methods: Exploratory Data Analysis*.

## 📌 Final Result

The analysis found **no potential numerical outliers using either IQR or standard Z-Score** in the selected Heart Disease features. Therefore, the project does not force trimming or capping where there is no statistical evidence for doing so.

The strongest preprocessing finding was instead the high missingness in `Alcohol Consumption`, showing why preprocessing decisions must be validated against the resulting data distribution.

## 👨‍💻 Authors

**Hassan Ali Hassan · Abdelrahman Ahmed Abdelrahman · Mohamed Hussein Ramadan**
