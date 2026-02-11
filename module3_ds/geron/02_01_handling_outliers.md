# Handling Outliers in Data Science

## Introduction

Outliers are data points that significantly deviate from the majority of the data in a dataset. 

## Mathematical Definition of Outliers

### 1. Standard Deviation Method
A data point is considered an outlier if it lies beyond a certain number of standard deviations from the mean:

$$|x - μ| > kσ$$

Where:
- x is the data point
- μ is the mean
- σ is the standard deviation
- k is typically 2 or 3 (based on the empirical rule)

### 2. Interquartile Range (IQR) Method

- $Q1$ is the first quartile (25th percentile)
- $Q3$ is the third quartile (75th percentile)
- $IQR = Q3 - Q1$

Using quartiles, outliers are defined as observations that fall outside the range:
- Lower bound = $Q1 - 1.5 × IQR$
- Upper bound = $Q3 + 1.5 × IQR$

Extreme outliers are defined as:
- Lower extreme = $Q1 - 3.0 × IQR$
- Upper extreme = $Q3 + 3.0 × IQR$

### 3. Modified Z-Score
- $\tilde{x}$ is the median
- $MED = median(\{|x_i - \tilde{x}| : i = 1, 2, ..., n\})$

The modified z-score uses the median absolute deviation (MAD) instead of the standard deviation:

$$M_i = 0.6745(x_i - x̃) / MAD$$

An observation is considered an outlier if $|M_i| > 3.5$

## Types of Outliers

### 1. Point Outliers (Global Outliers)
Individual data points that are significantly different from the rest of the dataset.

### 2. Contextual Outliers (Conditional Outliers)
Data points that are outliers in a specific context but not globally. For example, temperature readings that are normal in winter but outliers in summer.

### 3. Collective Outliers
A subset of data points that are collectively different from the rest of the dataset, even though individual points may not be outliers.

## Impact of Outliers on Statistical Measures

### Effect on Central Tendency
- **Mean**: Highly sensitive to outliers
- **Median**: Robust to outliers
- **Mode**: Generally unaffected by outliers

### Effect on Dispersion
- **Variance/Standard Deviation**: Significantly affected by outliers
- **Interquartile Range**: More robust to outliers
- **Range**: Extremely sensitive to outliers

### Effect on Correlation
Outliers can dramatically change correlation coefficients:
- Positive outliers can increase correlation
- Negative outliers can decrease correlation
- Single outliers can create spurious correlations

## Detection Methods

### 1. Univariate Outlier Detection

#### Box Plot Method
Based on the IQR method, box plots visually represent outliers as points beyond the whiskers.

#### Z-Score Method
Calculates how many standard deviations a data point is from the mean:
$$z = (x - μ) / σ$$

### 2. Multivariate Outlier Detection

#### Mahalanobis Distance
Measures the distance of a point from the center of the distribution, accounting for correlations between variables:

$$D² = (x - μ)ᵀ Σ⁻¹ (x - μ)$$

Where:
- x is the vector of observations
- μ is the vector of means
- Σ is the covariance matrix

#### Isolation Forest
An ensemble method that isolates outliers by randomly selecting features and split values.

#### Local Outlier Factor (LOF)
Compares the local density of a point to the local densities of its neighbors.

## Approaches to Handle Outliers

### 1. Removal
Completely remove outlier observations from the dataset.

- Removes extreme influence
- Risk of removing genuine rare events

### 2. Transformation
Apply mathematical transformations to reduce the impact of outliers:

#### Log Transformation
$$y = log(x)$$
compresses the scale, reducing the effect of large values

#### Square Root Transformation
$$y = √x$$
also compresses the scale but less aggressively than log

#### Box-Cox Transformation
for λ ≠ 0:
$$y = (x^λ - 1) / λ$$
for λ = 0:
$$y = log(x)$$

### 3. Winsorization
Replace extreme values with percentiles rather than removing them:

- Replace top 1% of values with the 99th percentile
- Replace bottom 1% of values with the 1st percentile

### 4. Robust Statistical Methods
Use statistical methods that are inherently resistant to outliers:

- Median instead of mean
- Median Absolute Deviation (MAD) instead of standard deviation
- Robust regression techniques

## Coding Implementation with Scikit-Learn

Scikit-learn provides several tools for detecting and handling outliers. Contamination is a hyperparameter defining the expected proportion of outliers (anomalies) in the dataset. A higher value marks more data points as outliers, while a lower value marks fewer.

### 1. Isolation Forest

Isolation Forest isolates anomalies by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature.

```python
import numpy as np
import pandas as pd

# Sample data with outliers
np.random.seed(42)
X_inliers = np.random.normal(0, 1, (100, 2))
X_outliers = np.random.uniform(low=-4, high=4, size=(10, 2))
X = np.vstack([X_inliers, X_outliers])
```

```python
from sklearn.ensemble import IsolationForest

# Isolation Forest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
outlier_labels = iso_forest.fit_predict(X)  # -1 for outliers, 1 for inliers

# Separate inliers and outliers
inlier_mask = outlier_labels == 1
outlier_mask = outlier_labels == -1
```

```python
# Visualize results
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(X[inlier_mask, 0], X[inlier_mask, 1], c='blue', label='Inliers', alpha=0.6)
plt.scatter(X[outlier_mask, 0], X[outlier_mask, 1], c='red', label='Outliers', alpha=0.8)
plt.title('Isolation Forest Outlier Detection')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 2. Local Outlier Factor (LOF)

LOF measures the local deviation of density of a given sample with respect to its neighbors.

```python
from sklearn.neighbors import LocalOutlierFactor

# Using the same sample data
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
outlier_labels = lof.fit_predict(X)  # -1 for outliers, 1 for inliers
lof_scores = lof.negative_outlier_factor_
```

### 3. Elliptic Envelope (Assumes Gaussian Distribution)

Elliptic Envelope assumes the data is normally distributed and fits an ellipse around the data.

```python
from sklearn.covariance import EllipticEnvelope

# Elliptic Envelope (assumes Gaussian distribution)
ell_envelope = EllipticEnvelope(contamination=0.1, random_state=42)
outlier_labels = ell_envelope.fit_predict(X)

# Separate inliers and outliers
inlier_mask = outlier_labels == 1
outlier_mask = outlier_labels == -1
```

### 4. One-Class SVM

One-Class SVM learns a rough, close frontier delimiting the region where most of the training data lies.

```python
from sklearn.svm import OneClassSVM

# One-Class SVM
oc_svm = OneClassSVM(gamma='auto', nu=0.1)
outlier_labels = oc_svm.fit_predict(X)

# Separate inliers and outliers
inlier_mask = outlier_labels == 1
outlier_mask = outlier_labels == -1
```

### 5. Standard Deviation Method

The standard deviation method identifies outliers as data points that lie beyond a certain number of standard deviations from the mean.

```python
import pandas as pd
import numpy as np

def detect_outliers_std(df, threshold=3):
    """
    Detect outliers using the standard deviation method
    
    Parameters:
    df: pandas DataFrame
    threshold: number of standard deviations to consider as outlier (default 3)
    
    Returns:
    DataFrame with boolean mask indicating outliers
    """
    outlier_mask = pd.DataFrame(index=df.index, columns=df.columns)
    
    for col in df.columns:
        mean = df[col].mean()
        std = df[col].std()
        
        # Calculate z-scores
        z_scores = abs((df[col] - mean) / std)
        
        # Identify outliers
        outlier_mask[col] = z_scores > threshold
    
    return outlier_mask

outliers_std = detect_outliers_std(df, threshold=2)
```

### 6. Interquartile Range (IQR) Method

The IQR method identifies outliers as data points that fall outside the range defined by $Q1 - 1.5*IQR$ and $Q3 + 1.5*IQR$.

```python
def detect_outliers_iqr(df):
    """
    Detect outliers using the Interquartile Range (IQR) method
    
    Parameters:
    df: pandas DataFrame
    
    Returns:
    DataFrame with boolean mask indicating outliers
    """
    outlier_mask = pd.DataFrame(index=df.index, columns=df.columns)
    
    for col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Identify outliers
        outlier_mask[col] = (df[col] < lower_bound) | (df[col] > upper_bound)
    
    return outlier_mask

outliers_iqr = detect_outliers_iqr(df)
```

### 7. Modified Z-Score Method

The modified z-score method uses the median and median absolute deviation (MAD) instead of mean and standard deviation, making it more robust to outliers.

```python
def detect_outliers_modified_zscore(df, threshold=3.5):
    """
    Detect outliers using the Modified Z-Score method
    
    Parameters:
    df: pandas DataFrame
    threshold: modified z-score threshold to consider as outlier (default 3.5)
    
    Returns:
    DataFrame with boolean mask indicating outliers
    """
    outlier_mask = pd.DataFrame(index=df.index, columns=df.columns)
    
    for col in df.columns:
        median = df[col].median()
        mad = (df[col] - median).abs().median()  # Median Absolute Deviation
        
        # Calculate modified z-scores
        modified_z_scores = 0.6745 * (df[col] - median) / mad
        
        # Identify outliers
        outlier_mask[col] = abs(modified_z_scores) > threshold
    
    return outlier_mask

outliers_modified_zscore = detect_outliers_modified_zscore(df)
```

### 8. Winsorization

Winsorization replaces extreme values with percentiles rather than removing them completely.

```python
def winsorize_series(series, limits=[0.05, 0.05]):
    """
    Winsorize a pandas Series by replacing extreme values with percentiles
    
    Parameters:
    series: pandas Series
    limits: list of proportions to winsorize at lower and upper ends (default [0.05, 0.05])
    
    Returns:
    pandas Series with winsorized values
    """
    lower_percentile = limits[0]
    upper_percentile = 1 - limits[1]
    
    lower_value = series.quantile(lower_percentile)
    upper_value = series.quantile(upper_percentile)
    
    # Clip the values to the specified percentiles
    winsorized_series = series.clip(lower=lower_value, upper=upper_value)
    
    return winsorized_series

def winsorize_dataframe(df, limits=[0.05, 0.05]):
    """
    Apply winsorization to specified columns of a DataFrame
    
    Parameters:
    df: pandas DataFrame
    limits: list of proportions to winsorize at lower and upper ends (default [0.05, 0.05])
    
    Returns:
    DataFrame with winsorized columns
    """
    df_winsorized = df.copy()
    
    for col in df.columns:
        df_winsorized[col] = winsorize_series(df[col], limits=limits)
    
    return df_winsorized

# Example usage
df_winsorized = winsorize_dataframe(df, limits=[0.05, 0.05])
```
