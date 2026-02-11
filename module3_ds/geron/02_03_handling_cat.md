# Handling Text and Categorical Variables in Data Science and Machine Learning

## Introduction

Text and categorical variables are fundamental components in many datasets, but they present unique challenges in machine learning pipelines. Unlike numerical variables, these data types cannot be directly processed by most algorithms, which require numerical inputs. This chapter explores various techniques for transforming text and categorical variables into meaningful numerical representations while preserving important information.

## Theoretical Background

### Mathematical Foundation

Categorical variables represent discrete values that belong to specific categories or classes. Mathematically, if we have a categorical variable $X$ with $k$ distinct categories $\{c_1, c_2, ..., c_k\}$, we need to map each category to a numerical representation that preserves the relationships and information inherent in the original categories.

For text variables, the challenge is even greater as raw text contains semantic meaning, syntactic structure, and contextual information that must be encoded numerically. The transformation process involves converting symbolic representations into vector spaces where mathematical operations can be performed.

### Types of Categorical Variables

1. **Nominal Variables**: Categories without any inherent order (e.g., colors: red, blue, green)
2. **Ordinal Variables**: Categories with a meaningful order (e.g., education levels: high school, bachelor's, master's, PhD)
3. **Binary Variables**: Two-category variables (e.g., yes/no, true/false)
4. **Text Variables**: Unstructured textual data that requires more sophisticated processing

## Categorical Variable Encoding Techniques

### Ordinal Encoding

Ordinal encoding maps categories to integers, preserving the order of the categories. This method is suitable for ordinal variables where the order matters. By default, the encoder will map the categories to integers alphabetically in ascending order. Input should be a DataFrame, not a 1D array of strings, for example: (n_samples, n_features).

$$f(c_j) = j$$

where $c_j$ is the $j$-th category.

```python
from sklearn.preprocessing import OrdinalEncoder

# Example with ordinal data
df_cat = df.select_dtypes(include=['object'])

ordinal_encoder = OrdinalEncoder()
df_cat_encoded = ordinal_encoder.fit_transform(df_cat)
```

### Label Encoding

Label encoding assigns a unique integer to each category similar to Ordinal Encoding. Integers are assigned based on alphabetical order by default, no inherent order assumption. Input should be a 1D array of strings, not a DataFrame, for example: (n_samples,). Usually reserved for the target variable.

$$f(c_j) = j$$

where $c_j$ is the $j$-th category.

```python
from sklearn.preprocessing import LabelEncoder

y = df_cat['label_column']
le = LabelEncoder()
y_encoded = le.fit_transform(y)
```

### One-Hot Encoding

One-hot encoding creates binary columns for each category, where each column represents the presence (1) or absence (0) of a specific category.

Mathematically, for a categorical variable with $k$ categories, one-hot encoding creates $k$ binary features. For observation $i$, if it belongs to category $j$, then the $j$-th binary feature is 1 and all others are 0.

$$x_{ij} = \begin{cases} 
1 & \text{if observation } i \text{ belongs to category } j \\
0 & \text{otherwise}
\end{cases}$$

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np

df_cat = df.select_dtypes(include=['object'])

# Using pandas get_dummies for one-hot encoding
one_hot_encoded = pd.get_dummies(df_cat, columns=df_cat.columns)

# Using sklearn OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)
encoded_features = encoder.fit_transform(df_cat)
feature_names = encoder.get_feature_names_out(df_cat.columns)

sklearn_encoded_df = pd.DataFrame(encoded_features, columns=feature_names)
```


### Target Encoding

Target encoding replaces categories with statistics computed from the target variable, such as mean target value for that category.

$$\text{encoded\_value}(c_j) = \frac{\sum_{i \in C_j} y_i}{|C_j|}$$

where 
- $C_j$ is the set of observations belonging to category $j$, 
- $y_i$ is the target value.

For complex cases, we can use smoothing to prevent overfitting.

$$\text{encoded\_value}(c_j) = \frac{\sum_{i \in C_j} y_{i} + \text{smooth} \times \mu} {|C_j| + \text{smooth}}$$
where 
- $C_j$ is the set of observations belonging to category $j$, 
- $y_i$ is the target value,
- $\mu$ is the global mean of the target value.
- $\text{smooth}$ is the smoothing parameter.

The smoothing parameter is a hyperparameter that controls the strength of regularization. A higher value of $\text{smooth}$ will result in a more smoothed target encoding.


```python
from sklearn.preprocessing import TargetEncoder

# Simple target encoding (mean of target for each category)
target_means = df_target.groupby('category')['target'].mean()
df_target['category_encoded'] = df_target['category'].map(target_means)

# Simple target encoding with sklearn
target_encoder = TargetEncoder(smooth=0)
df_target['category_encoded'] = target_encoder.fit_transform(df_target[['category']], df_target['target'])

# More robust target encoding with smoothing to prevent overfitting
target_encoder = TargetEncoder(smooth='auto')
df_target['category_encoded'] = target_encoder.fit_transform(df_target[['category']], df_target['target'])
```

<!-- ### Binary Encoding

Binary encoding converts categories to binary digits, reducing dimensionality compared to one-hot encoding. For $k$ categories, binary encoding requires only $\lceil \log_2(k) \rceil$ columns.

```python
from category_encoders import BinaryEncoder

# Example with many categories
df_binary = pd.DataFrame({
    'city': [f'City_{i}' for i in range(1, 11)] * 3,
    'value': np.random.randn(30)
})

print(f"Dataset shape: {df_binary.shape}")
print(f"Number of unique cities: {df_binary['city'].nunique()}")

# Using BinaryEncoder (requires installation: pip install category_encoders)
# For demonstration, let's implement a simple binary encoder
def simple_binary_encode(series):
    """Simple binary encoding implementation"""
    unique_vals = series.unique()
    n_unique = len(unique_vals)
    n_bits = int(np.ceil(np.log2(n_unique)))
    
    # Create mapping from categories to integers
    cat_to_int = {val: idx for idx, val in enumerate(unique_vals)}
    int_series = series.map(cat_to_int)
    
    # Convert integers to binary representation
    binary_df = pd.DataFrame(index=series.index)
    for bit_pos in range(n_bits):
        binary_df[f'{series.name}_bit_{bit_pos}'] = (int_series // (2 ** bit_pos)) % 2
    
    return binary_df

# Apply binary encoding
binary_encoded = simple_binary_encode(df_binary['city'])
print("\nBinary encoded result:")
print(binary_encoded.head())
``` -->

## Practical Considerations and Best Practices

### Handling High Cardinality Categorical Variables

High cardinality categorical variables (many unique values) can lead to extremely wide feature matrices. Strategies include:

1. **Frequency-based filtering**: Keep only categories that appear frequently
2. **Hash encoding**: Use hash functions to map categories to fixed-size vectors (FeatureHasher, HashingVectorizer)
3. **Target encoding**: Replace categories with target statistics

### Example: Frequency-based filtering

```python
# Keep only categories that appear more than once
frequent_categories = df['cat_column'].value_counts()
popular_categories = frequent_categories[frequent_categories >= 2].index

filtered_data = df[
    df['cat_column'].isin(popular_categories)
]
```

### Memory Efficiency

For large datasets, consider memory-efficient approaches:

```python
# Using sparse matrices for memory efficiency
from sklearn.preprocessing import OneHotEncoder

df_cat = df.select_dtypes(include=['object'])

# Use sparse output for memory efficiency
sparse_encoder = OneHotEncoder(sparse_output=True)
sparse_encoded = sparse_encoder.fit_transform(df_cat)
```
