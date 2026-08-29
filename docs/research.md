# Research: Outlier Detection and Treatment

## Team Members

- Hassan Ali Hassan
- Abdelrahman Ahmed Abdelrahman
- Mohamed Hussein Ramadan

## 1. Introduction

An outlier is an observation that is noticeably different from most observations in a dataset. It can be caused by an error, but it can also be a real and important observation. For this reason, detecting an outlier does not mean that it should automatically be removed.

This research focuses on two common methods for detecting numerical outliers: **Interquartile Range (IQR)** and **Z-Score**. It also discusses common ways of dealing with unusual observations.

## 2. Research Question

How can IQR and Z-Score be used to detect outliers, and how should the treatment of detected observations depend on the data and the goal of the analysis?

## 3. Dataset

The analysis uses a Heart Disease dataset containing 10,000 rows and 21 columns. Nine numerical features were used for outlier detection:

- Age
- Blood Pressure
- Cholesterol Level
- BMI
- Sleep Hours
- Triglyceride Level
- Fasting Blood Sugar
- CRP Level
- Homocysteine Level

## 4. Exploratory Analysis

The first step was to inspect the shape, data types, missing values, descriptive statistics, unique values, target distribution, histograms, and skewness.

The target contains:

| Heart Disease Status | Count | Percentage |
|---|---:|---:|
| No | 8,000 | 80% |
| Yes | 2,000 | 20% |

The numerical features had skewness values close to zero in our analysis, and no strong univariate skewness was observed.

## 5. Missing Values

Most features had a small amount of missing data (around 0.2%–0.3%). The main exception was `Alcohol Consumption`, with 2,586 missing values (25.86%).

A mode-imputation test changed the distribution considerably:

| Category | Before | After | Before % | After % |
|---|---:|---:|---:|---:|
| Medium | 2,500 | 5,086 | 33.72% | 50.86% |
| Low | 2,488 | 2,488 | 33.56% | 24.88% |
| High | 2,426 | 2,426 | 32.72% | 24.26% |

This result shows why missing values should not always be filled automatically with the mode, especially when the missing percentage is high.

## 6. IQR Method

The IQR method uses the middle 50% of the data and is relatively resistant to extreme observations.

### Q1 and Q3

- **Q1** = 25th percentile.
- **Q3** = 75th percentile.

### IQR

```text
IQR = Q3 - Q1
```

### Fences

```text
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

A value below the lower fence or above the upper fence is considered a potential outlier.

We use only the lower and upper fences in this project; extreme fences are not required.

### Example: Age

```text
Q1 = 34
Q3 = 65
IQR = 31
Lower Fence = -12.5
Upper Fence = 111.5
```

There were no observations outside these limits.

## 7. IQR Results

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

**Result: 0 IQR outliers.**

## 8. Z-Score Method

The standard Z-Score shows how far a value is from the mean in standard-deviation units.

```text
Z = (X - mean) / standard deviation
```

A common screening rule is:

```text
|Z| > 3
```

This method is more sensitive to extreme observations because the mean and standard deviation can themselves be affected by extreme values. It is generally easier to interpret when the data are approximately normally distributed.

## 9. Z-Score Results

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

**Result: 0 Z-Score outliers.**

## 10. IQR vs Z-Score

| Point | IQR | Z-Score |
|---|---|---|
| Based on | Q1 and Q3 | Mean and standard deviation |
| Normal distribution required | No | More suitable for approximately normal data |
| Effect of extreme values | More robust | More sensitive |
| Common rule | 1.5 × IQR | `|Z| > 3` |
| Good choice | Skewed or non-normal data | Approximately normal data |

Neither method is always better. The choice depends on the distribution and the purpose of the analysis.

## 11. Treatment of Outliers

### Keep

Keep the observation when it is valid and represents real variation in the population.

### Trimming

Remove the observation when there is a good reason to believe that it is an error or should not be part of the analysis. Removing observations can reduce the sample size and may introduce bias.

### Capping / Winsorization

Limit extreme values to selected boundaries instead of removing the entire row. This can reduce the influence of extreme values while keeping the observation in the dataset.

### Imputation

Imputation is mainly a **missing-value treatment**, not an outlier treatment. It can be used for missing values when an appropriate strategy is available.

### Mathematical Transformations

Transformations such as Log, Box-Cox, and Yeo-Johnson can reduce skewness and decrease the influence of very large values while keeping the observations.

## 12. Choosing the Treatment

The treatment should depend on:

- **Reason for the value:** an obvious data-entry error may be removed or corrected.
- **Validity:** a real unusual observation should not be removed just because it is unusual.
- **Distribution:** skewed data may benefit from robust methods or transformations.
- **Sample size:** deleting rows can be problematic in small datasets.
- **Analysis goal:** descriptive and predictive analyses may require different decisions.
- **Model sensitivity:** some models are more affected by extreme values than others.

## 13. Findings

Both methods found **zero potential numerical outliers** in the Heart Disease dataset under the selected rules. Therefore, there was no statistical reason to trim or cap the nine numerical features.

The more important preprocessing issue was missing data, especially `Alcohol Consumption`. The mode-imputation experiment changed its distribution substantially, showing that preprocessing decisions should be checked after they are applied.

## 14. Limitations

- IQR and standard Z-Score are mainly univariate methods.
- A statistical outlier is not necessarily an error.
- Z-Score can be affected by extreme observations.
- The thresholds used are common rules, not universal laws.
- The analysis does not determine the actual cause of missing values.

## 15. Conclusion

IQR is a simple and robust method for detecting potential outliers using quartiles and fences. Z-Score measures the distance from the mean and is especially useful when the data are approximately normally distributed.

In this dataset, both methods produced zero potential outliers. Therefore, no trimming, capping, or winsorization was applied. The analysis instead highlighted the importance of handling missing data carefully, particularly for `Alcohol Consumption`.

The main conclusion is that outlier detection should support a preprocessing decision rather than automatically determine it.

## 16. References

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. Iglewicz, B., & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
3. National Institute of Standards and Technology (NIST/SEMATECH). *e-Handbook of Statistical Methods*.

## 17. Implementation

The analysis was implemented in Python using Pandas, NumPy, SciPy, and related libraries. The main calculations were first tested in `notebooks/exploratory_analysis.ipynb` and then organized into simple reusable Python files.

Repository: https://github.com/7assan-Ali/Outlier-Detection-and-Treatment
