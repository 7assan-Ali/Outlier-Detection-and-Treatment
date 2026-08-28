# Research: Outlier Detection and Treatment Using IQR and Z-Score

## Team Members
- Hassan Ali Hassan
- Abdelrahman Ahmed Abdelrahman
- Mohamed Hussein Ramadan

## 1. Introduction
Outliers are observations that appear to deviate markedly from the other observations in a dataset. They may result from measurement or data-entry errors, unusual but valid observations, natural variation, or scientifically important cases. Therefore, detecting an outlier does not automatically mean that it should be deleted. The appropriate treatment depends on the data-generating process, feature distribution, amount of contamination, and analysis objective.

This research investigates two common univariate approaches for detecting potential outliers: the Interquartile Range (IQR) method and the Z-Score method. It also discusses keeping, trimming, capping/winsorizing, imputation where appropriate, and mathematical transformations.

## 2. Research Question
How can the IQR method identify potential outliers through Q1, Q3, IQR, and lower and upper fences? How should unusual observations be treated, and how does treatment depend on the data and analysis goal? When is IQR more suitable than Z-Score, and vice versa?

## 3. Objectives
1. Explain IQR-based outlier detection.
2. Calculate Q1, Q3, IQR, lower fence, and upper fence.
3. Detect potential outliers in the Heart Disease dataset.
4. Explain common outlier-treatment strategies.
5. Explain standard Z-Score and compare it with IQR.
6. Evaluate both methods on the same numerical features.
7. Document practical preprocessing decisions.

## 4. Dataset
The analysis uses a Heart Disease dataset containing 10,000 observations and 21 variables. The target variable is `Heart Disease Status`.

Numerical features used for outlier analysis:
- Age
- Blood Pressure
- Cholesterol Level
- BMI
- Sleep Hours
- Triglyceride Level
- Fasting Blood Sugar
- CRP Level
- Homocysteine Level

The dataset also contains categorical health and lifestyle variables.

## 5. Exploratory Data Analysis
The exploratory stage inspected shape, data types, missing values, descriptive statistics, unique values, target distribution, histograms, and skewness.

Target distribution:

| Heart Disease Status | Count | Percentage |
|---|---:|---:|
| No | 8,000 | 80% |
| Yes | 2,000 | 20% |

The numerical features showed skewness values close to zero in the analysis, with no strong univariate skewness.

## 6. Missing Values
Missing values were found in numerical and categorical variables. The most important case was `Alcohol Consumption`, with 2,586 missing values (25.86%). Other missing-value percentages were approximately 0.2%–0.3% per feature.

A test of simple mode imputation for `Alcohol Consumption` substantially changed its observed distribution:

| Category | Before Count | After Count | Before %* | After % |
|---|---:|---:|---:|---:|
| Medium | 2,500 | 5,086 | 33.72% | 50.86% |
| Low | 2,488 | 2,488 | 33.56% | 24.88% |
| High | 2,426 | 2,426 | 32.72% | 24.26% |

`*` Before percentages are calculated among non-missing observations.

Because replacing 2,586 missing values with the mode substantially changes the distribution, simple mode imputation should not be applied automatically. In this project, the missing category can instead be represented explicitly as `Unknown` when appropriate.

## 7. IQR Method
The Interquartile Range is a robust measure of spread based on the middle 50% of observations.

### 7.1 Q1
Q1 is the 25th percentile.

### 7.2 Q3
Q3 is the 75th percentile.

### 7.3 IQR
`IQR = Q3 - Q1`

### 7.4 Lower and Upper Fences
Using the standard 1.5 × IQR rule:

`Lower Fence = Q1 - 1.5 × IQR`

`Upper Fence = Q3 + 1.5 × IQR`

Values below the lower fence or above the upper fence are labeled potential outliers. This project uses lower and upper fences only; extreme fences are not required.

### 7.5 Example: Age
- Q1 = 34
- Q3 = 65
- IQR = 31
- Lower Fence = -12.5
- Upper Fence = 111.5

All observed ages fall inside these fences, so Age has zero potential outliers.

## 8. IQR Results
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

The IQR analysis found **no potential outliers** among the nine numerical features using the standard 1.5 × IQR rule.

## 9. Z-Score Method
The standard Z-Score measures how far an observation is from the sample mean in standard-deviation units:

`Z = (x - mean) / standard deviation`

A commonly used screening rule flags observations with absolute Z-Score greater than 3. This is a practical convention, not a universal law. Z-Score can be affected by skewness and by extreme observations because the mean and standard deviation are themselves sensitive to unusual values.

NIST also discusses the modified Z-Score based on the median and MAD and notes the commonly recommended 3.5 threshold for that robust statistic. The current project uses the standard Z-Score for the requested IQR-versus-Z-Score comparison.

## 10. Z-Score Results
Using |Z| > 3, the analysis found zero potential outliers for all nine numerical features:

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

## 11. IQR vs Z-Score
| Criterion | IQR | Z-Score |
|---|---|---|
| Basis | Quartiles and middle 50% | Mean and standard deviation |
| Distribution assumption | Does not require normality | Most interpretable for approximately normal data |
| Robustness | Relatively robust to extremes | Sensitive because mean and SD can be affected |
| Typical rule | 1.5 × IQR | Often |Z| > 3 |
| Suitable for | Skewed, non-normal, or uncertain distributions | Approximately normal numerical variables |
| Interpretation | Distance from quartile-based fences | Distance from mean in SD units |

The methods are complementary. Applying both can provide a useful diagnostic comparison, but disagreement should be investigated rather than resolved automatically.

## 12. Treatment of Outliers
### 12.1 Keep
Keep a potential outlier when it is valid and represents real population variation. Removing meaningful observations can introduce bias.

### 12.2 Trimming
Trimming removes observations considered invalid or inappropriate. It is most defensible when there is evidence of data-entry, measurement, or collection error.

### 12.3 Capping / Winsorizing
Capping replaces values beyond selected boundaries with boundary values. Winsorization similarly limits the influence of extremes without deleting rows. It can be useful when extreme values are valid but have excessive influence on a downstream model.

### 12.4 Imputation
Imputation is primarily a missing-data treatment, not an outlier treatment. Mean or median imputation may be considered for missing numerical values, while mode imputation can be considered for categorical variables with very small missing proportions. It should not be used simply to hide valid extreme observations.

The `Alcohol Consumption` experiment shows why blindly applying mode imputation can distort a feature distribution when missingness is high.

### 12.5 Mathematical Transformations
Transformations can reduce skewness and compress the influence of large values while preserving observations. Examples include log/log1p, Box-Cox, and Yeo-Johnson. A transformation should be motivated by the distribution and downstream analysis requirements.

## 13. How to Choose a Treatment
The decision depends on:

- **Nature of the observation:** correct/remove clear errors; preserve valid unusual observations.
- **Distribution:** IQR and robust approaches are useful when data are skewed or non-normal.
- **Sample size:** deletion can be costly in small datasets.
- **Analysis objective:** descriptive analysis may require retaining valid extremes; predictive modeling may benefit from reducing their influence depending on the model.
- **Model sensitivity:** regression, distance-based methods, and squared-error objectives can react strongly to extreme values; some tree-based models are less sensitive.

## 14. Findings from This Dataset
The Heart Disease dataset contains **no potential numerical outliers according to either the standard IQR rule or the standard Z-Score threshold used in this project**. Therefore, trimming, capping, and winsorization are not justified for these numerical variables based on the current detection results.

The main preprocessing issue was missing data, especially `Alcohol Consumption`. The mode-imputation experiment demonstrated that preprocessing can substantially alter a feature distribution even when no numerical outliers exist.

The main principle is therefore: statistical rules should provide evidence for a preprocessing decision, not automatically force modification of every unusual or incomplete observation.

## 15. Limitations
1. IQR and standard Z-Score are primarily univariate and may miss multivariate anomalies.
2. A statistically unusual value is not necessarily erroneous.
3. Standard Z-Score is sensitive to the mean and standard deviation.
4. The 1.5 × IQR and |Z| > 3 thresholds are practical conventions, not universal definitions.
5. The analysis does not establish the cause of missingness.
6. Outlier detection here focuses on numerical features.

## 16. Conclusion
IQR provides a simple and robust approach for identifying potential outliers using quartiles and fences. Z-Score provides a standardized measure of distance from the mean and is particularly useful when the distribution is approximately normal.

For this Heart Disease dataset, both approaches identified zero potential outliers across the nine numerical features. Consequently, no trimming, capping, or winsorization was required for these features.

The analysis also showed that preprocessing choices must be evaluated empirically. Mode imputation of `Alcohol Consumption` changed its observed distribution substantially because 25.86% of its values were missing. Treatment decisions should therefore consider missingness rate, feature type, distribution, validity of observations, and the objective of the analysis.

## 17. References
1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
3. National Institute of Standards and Technology (NIST/SEMATECH). *e-Handbook of Statistical Methods: Detection of Outliers*.
4. National Institute of Standards and Technology (NIST/SEMATECH). *e-Handbook of Statistical Methods: Exploratory Data Analysis*.

## 18. Project Implementation
The research is implemented in Python using Pandas, NumPy, SciPy, scikit-learn, Matplotlib, Seaborn, and Tkinter. The repository separates detection, treatment, preprocessing, visualization, testing, and GUI components so the analysis can be reproduced and reused on other CSV datasets.

Repository: https://github.com/7assan-Ali/Outlier-Detection-and-Treatment
