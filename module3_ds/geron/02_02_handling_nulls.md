# Handling Null Values in Data Science

## Types of Missing Data

### 1. Missing Completely at Random (MCAR)
- Example: A random malfunction in a data collection device

#### Definition
- X is a variable with missing values
- R is the indicator variable for missingness (R=1 if observed, R=0 if missing)
- Z is other observed variables (covariates)
$$R \perp X,Z$$
- Missingness is independent of everything, i.e. observed and unobserved data
$$E[X|\text{missing}] = E[X|\text{observed}] = E[X]$$
- The units with missing values are statistically identical to those with observed values, i.e. the probability of missing data is the same for all observations

#### Intuition

- Missingness is like randomly dropping rows
- The observed data is a simple random sample of the full data
- No systematic bias

#### Consequence

- Complete-case analysis is unbiased
- You only lose efficiency, not correctness

### 2. Missing at Random (MAR)
- Example: Older respondents are less likely to report their income

#### Definition
- X is a variable with missing values
- R is the indicator variable for missingness (R=1 if observed, R=0 if missing)
- Z is other observed variables (covariates)
$$R \perp X | Z$$
- Missingness depends on Z (observed data), but not on X (unobserved data) itself once Z is known
$$E[X|\text{missing}, Z] = E[X|\text{observed}, Z]$$
- Within groups defined by Z, missing and observed cases have the same expected X.

#### Intuition

- X = income
- Z = education
- Low-education people are less likely to report income
- But within the same education level, missingness is random
- Overall,
$$E[X|\text{missing}] \neq E[X|\text{observed}]$$
- But after conditioning on Z, the bias disappears, i.e.
$$E[X|\text{missing}, Z] = E[X|\text{observed}, Z]$$

#### Consequence

- You must model or condition on Z
- Methods like multiple imputation, ML, Bayesian models work
- Complete-case analysis is generally biased

### 3. Missing Not at Random (MNAR)
- The probability of missing data depends on the unobserved values themselves
- Missingness is related to the missing values
- Example: People with higher incomes are less likely to report their income

#### Definition

$$R \not\perp X | Z$$
- Missingness depends on the unobserved value of X itself.
$$E[X|\text{missing}] \neq E[X|\text{observed}]$$
- Even after conditioning on all observed variables

#### Intuition

- High-income people are less likely to report income
- Even if you control for education, job, age, etc.
- The missingness still depends on income itself

#### Consequence

- Observed data is systematically biased
- You cannot fix this with observed data alone

## Mathematical Foundations

### Impact on Statistical Analysis
When data is missing, the effective sample size decreases, leading to increased variance in estimators:

$Var(\hat{\theta}_{complete}) < Var(\hat{\theta}_{with \space missing})$

Where $\hat{\theta}$ represents an estimator of parameter $\theta$.

## Common Strategies for Handling Null Values

### 1. Deletion Methods - Listwise Deletion (Complete Case Analysis)
Remove entire rows with any missing values.

- Simple to implement
- Reduced statistical power

### 2. Mean/Median/Mode Imputation Methods - SimpleImputer
Replace missing values with central tendency measures (mean, median, mode).

- Reduces variance

### 3. Regression Imputation - IterativeImputer
Use regression models to predict missing values based on other variables.

Model: $$Y_{missing} = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \epsilon$$

- More accurate than simple imputation

### 4. K-Nearest Neighbors Imputation - KNNImputer
Use k-nearest neighbors to predict missing values based on other variables.

- More accurate than simple imputation

## Coding Implementation with Scikit-Learn

### 1. SimpleImputer

```python
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

df_num = df.select_dtypes(include=['number'])
df_cat = df.select_dtypes(include=['object'])

# Mean imputation
mean_imputer = SimpleImputer(strategy='mean')
mean_imputer.fit_transform(df_num)

# Median imputation
median_imputer = SimpleImputer(strategy='median')
median_imputer.fit_transform(df_num)

# Mode imputation (for categorical data)
mode_imputer = SimpleImputer(strategy='most_frequent')
mode_imputer.fit_transform(df_cat)

# Constant imputation
constant_imputer = SimpleImputer(strategy='constant', fill_value=0)
constant_imputer.fit_transform(df_num)
```

### 2. KNNImputer

KNN imputation uses k-nearest neighbors to fill missing values based on similarity to other samples:

```python
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=2)
knn_imputer.fit_transform(df_num)

# The algorithm finds similar samples based on available features
# and uses them to estimate the missing values
```

### 3. IterativeImputer (formerly MICE - Multiple Imputation by Chained Equations)

```python
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression

# Iterative imputation using linear regression
iterative_imputer = IterativeImputer(
    estimator=LinearRegression(),
    random_state=42,
    max_iter=10
)
iterative_imputer.fit_transform(df_num)

# This method models each feature with missing values as a function 
# of other features in a round-robin fashion
```
