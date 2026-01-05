# Descriptive Statistics

Descriptive statistics are used to describe the basic features of the data in a study. They provide simple summaries about the sample and the measures.

## 1. Measures of Central Tendency
Measures of central tendency help find the "center" or "typical" value of a dataset.

### 1.1. Mean
The arithmetic average of a dataset.
*   **Mathematical Formula**: $\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$
*   **Python Calculation Methods**:
```python
import numpy as np
import pandas as pd
import statistics

data = [10, 20, 30, 40, 50]
df = pd.Series(data)

# 1. NumPy
mean_np = np.mean(data)

# 2. Pandas
mean_pd = df.mean()

# 3. Python built-in 'statistics' module
mean_stat = statistics.mean(data)
```

### 1.2. Median
The middle value when the data is ordered. The calculation depends on whether the number of elements ($n$) is odd or even:
*   **Odd $n$**: The median is the value at the exact middle position $\frac{n+1}{2}$.
*   **Even $n$**: There is no single middle value. The median is the arithmetic mean of the two middle values at positions $\frac{n}{2}$ and $\frac{n}{2} + 1$.

*   **Mathematical Concept**: 
    $$ \text{Median} = \begin{cases} x_{(\frac{n+1}{2})} & \text{if } n \text{ is odd} \\ \frac{x_{(\frac{n}{2})} + x_{(\frac{n}{2} + 1)}}{2} & \text{if } n \text{ is even} \end{cases} $$
*   **Python Calculation Methods**:
```python
import numpy as np
import pandas as pd
import statistics

data = [10, 20, 30, 40, 50, 60] # Even n
df = pd.Series(data)

# 1. NumPy
median_np = np.median(data)

# 2. Pandas
median_pd = df.median()

# 3. Python built-in 'statistics' module
median_stat = statistics.median(data)
```

### 1.3. Mode
The value that appears most frequently in a dataset. For grouped data (data organized into classes or intervals), the mode is estimated using the following formula:

*   **Mathematical Formula (Grouped Data)**: 
    $$ \text{Mode} = L + \left( \frac{f_1 - f_0}{(f_1 - f_0) + (f_1 - f_2)} \right) \times h $$
    Where:
    - $L$: Lower limit of the modal class (the class with the highest frequency).
    - $f_1$: Frequency of the modal class.
    - $f_0$: Frequency of the class preceding the modal class.
    - $f_2$: Frequency of the class succeeding the modal class.
    - $h$: Size of the class interval.

*   **Example Calculation**:
    Suppose we have the following frequency distribution:
    | Class Interval | Frequency ($f$) |
    | :--- | :--- |
    | 10-20 | 5 |
    | 20-30 | 12 ($f_1$) |
    | 30-40 | 8 |
    
    1. **Modal Class**: 20-30 (highest frequency = 12).
    2. **Values**: $L=20$, $f_1=12$, $f_0=5$, $f_2=8$, $h=10$.
    3. **Calculation**: $20 + \left( \frac{12 - 5}{(12 - 5) + (12 - 8)} \right) \times 10 = 20 + \left( \frac{7}{7 + 4} \right) \times 10 \approx 26.36$.

*   **Python Calculation Methods**:
```python
import pandas as pd
import statistics
from scipy import stats

data = [10, 20, 20, 30, 40]
df = pd.Series(data)

# 1. Scipy (returns mode and count)
mode_scipy = stats.mode(data, keepdims=True)

# 2. Pandas (returns a Series as there can be multiple modes)
mode_pd = df.mode()

# 3. Python built-in 'statistics' module
mode_stat = statistics.mode(data) # Returns first mode
multimode_stat = statistics.multimode(data) # Returns all modes
```

*   **Choosing Between Mean, Median, and Mode**:
    Why do we need three different measures? Each one provides a different perspective and reacts differently to data characteristics:
    1.  **Mean**: 
        - *Best for*: Symmetrical data without outliers.
        - *Weakness*: Highly sensitive to outliers (extreme values pull the mean toward them).
    2.  **Median**:
        - *Best for*: Skewed data or data with outliers (e.g., household income).
        - *Strength*: **Robust** measure. Extreme values do not affect the median as much as the mean.
    3.  **Mode**:
        - *Best for*: Categorical data (e.g., "What is the most popular car color?") or identifying the most common value in a discrete distribution.
        - *Strength*: The only measure that can be used with non-numerical data.

---

## 2. Measures of Dispersion
Measures of dispersion describe the spread or variability within a dataset.

### 2.1. Range
The difference between the maximum and minimum values.
*   **Mathematical Formula**: $Range = Max(x) - Min(x)$
*   **Python Calculation Methods**:
```python
import numpy as np
import pandas as pd

data = [10, 20, 30, 40, 50]
df = pd.Series(data)

# 1. NumPy
range_np = np.ptp(data) # Peak-to-peak
# Alternatively: np.max(data) - np.min(data)

# 2. Pandas
range_pd = df.max() - df.min()
```

### 2.2. Variance
The average of the squared differences from the Mean.
*   **Mathematical Formula**: $\sigma^2 = \frac{\sum (x_i - \mu)^2}{n}$ (Population) or $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$ (Sample)

*   **Example Calculation (Sample Variance)**:
    Data: $\{2, 4, 6\}$, $n = 3$
    1.  **Calculate Mean ($\bar{x}$)**: $(2 + 4 + 6) / 3 = 4$
    2.  **Calculate Deviations $(x_i - \bar{x})$**: $(2-4)=-2, (4-4)=0, (6-4)=2$
    3.  **Square the Deviations**: $(-2)^2=4, 0^2=0, 2^2=4$
    4.  **Sum of Squares**: $4 + 0 + 4 = 8$
    5.  **Divide by $(n-1)$**: $s^2 = 8 / (3-1) = 4$

*   **Python Calculation Methods**:
```python
import numpy as np
import pandas as pd
import statistics

data = [10, 20, 30, 40, 50]
df = pd.Series(data)

# 1. NumPy (Default ddof=0, use ddof=1 for sample)
var_np = np.var(data, ddof=1)

# 2. Pandas (Default ddof=1)
var_pd = df.var()

# 3. Python built-in 'statistics' module
var_stat = statistics.variance(data) # Sample variance
pvar_stat = statistics.pvariance(data) # Population variance
```

*   **Population vs. Sample Variance**:
    - **Population ($\sigma^2$)**: Used when you have data for the *entire* group you are interested in. You divide by $n$.
    - **Sample ($s^2$)**: Used when you have only a *subset* of the population. You divide by $n-1$.

*   **Why divide by $n-1$? (Bessel's Correction)**:
    When we calculate sample variance, we use the sample mean ($\bar{x}$) instead of the true population mean ($\mu$). Since the sample mean is derived from the data itself, the data points tend to be "closer" to $\bar{x}$ than they would be to $\mu$. Dividing by $n$ would therefore underestimate the true variability. Dividing by $n-1$ corrects this bias, providing a better estimate of the population variance.

*   **Delta Degrees of Freedom (`ddof`)**:
    In programming libraries like NumPy and Pandas, the `ddof` parameter represents the value subtracted from $n$ in the denominator.
    - `ddof=0`: Divides by $n$ (Population variance).
    - `ddof=1`: Divides by $n-1$ (Sample variance).
    *Note: NumPy defaults to `ddof=0`, while Pandas defaults to `ddof=1`.*

### 2.3. Standard Deviation
The square root of the variance. It represents the average distance from the mean.
*   **Mathematical Formula**: $\sigma = \sqrt{\sigma^2}$
*   **Python Calculation Methods**:
```python
import numpy as np
import pandas as pd
import statistics

data = [10, 20, 30, 40, 50]
df = pd.Series(data)

# 1. NumPy (Default ddof=0, use ddof=1 for sample)
std_np = np.std(data, ddof=1)

# 2. Pandas (Default ddof=1)
std_pd = df.std()

# 3. Python built-in 'statistics' module
std_stat = statistics.stdev(data) # Sample std dev
pstd_stat = statistics.pstdev(data) # Population std dev
```

*   **Standard Deviation vs. Variance**:
    Why do we need Standard Deviation if we already have Variance?
    1.  **Interpretability (Units)**: Variance is calculated by squaring the differences from the mean, which means its units are also squared (e.g., if data is in "meters", variance is in "meters squared"). Standard Deviation takes the square root, returning the measure to the *original units* of the data.
    2.  **Intuition**: It is much easier to visualize the "average distance from the mean" when it is in the same units as the mean itself.
    3.  **Normal Distribution**: In a normal distribution, the Standard Deviation has specific meanings (e.g., ~68% of data falls within $\pm 1$ standard deviation), which is not as directly applicable with variance.

### 2.4. Interquartile Range (IQR)
The range between the first quartile (Q1) and the third quartile (Q3). To understand IQR, we must define the following related terms:

*   **Quantiles**: The general term for points that divide a distribution into equal-sized intervals.
*   **Percentiles**: Quantiles that divide the data into 100 equal parts (e.g., the 90th percentile is the value below which 90% of the data falls).
*   **Quartiles**: Specific quantiles that divide the data into 4 equal parts (25% each):
    - **Q1 (First Quartile / 25th Percentile)**: The middle value of the first half of the data.
    - **Q2 (Second Quartile / 50th Percentile)**: The **Median** of the entire dataset.
    - **Q3 (Third Quartile / 75th Percentile)**: The middle value of the second half of the data.

*   **The Median Connection**: The Median is exactly the same as the **50th Percentile**, the **Second Quartile (Q2)**, and the **0.5 Quantile**.

*   **Mathematical Formula**: $IQR = Q3 - Q1$
*   **Python Calculation Methods**:
```python
import numpy as np
import pandas as pd
from scipy import stats

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
df = pd.Series(data)

# 1. SciPy
iqr_scipy = stats.iqr(data)

# 2. NumPy (calculating quartiles manually)
q75, q25 = np.percentile(data, [75, 25])
iqr_np = q75 - q25

# 3. Pandas
q3 = df.quantile(0.75)
q1 = df.quantile(0.25)
iqr_pd = q3 - q1
```

*   **Choosing Between Measures of Dispersion**:
    Why do we need four different measures? Each one handles outliers and data distribution differently:
    1.  **Range**: 
        - *Best for*: Quick, simple understanding of the full extent of the data.
        - *Weakness*: Extremely sensitive to outliers. A single extreme value can drastically change the range.
    2.  **Variance**:
        - *Best for*: Mathematical modeling and advanced statistics.
        - *Weakness*: Units are squared (hard to interpret) and it is sensitive to outliers.
    3.  **Standard Deviation**:
        - *Best for*: Reporting and visualization.
        - *Strength*: Same units as the data, making it intuitive. Like variance, it considers *every* data point.
    4.  **Interquartile Range (IQR)**:
        - *Best for*: Skewed data or datasets with outliers.
        - *Strength*: **Robust** measure. It only looks at the middle 50% of the data, meaning extreme outliers have zero effect on it.

---

## 3. Skewness and Kurtosis

### 3.1. Skewness
Measures the asymmetry of the probability distribution.
*   **Positive Skew (> 0)**: The right tail is longer or fatter. Most data points are clustered on the left.
*   **Negative Skew (< 0)**: The left tail is longer or fatter. Most data points are clustered on the right.
*   **Zero Skew (= 0)**: The distribution is perfectly symmetrical (e.g., a Normal Distribution).

**Python Examples**:
```python
import pandas as pd
from scipy.stats import skew

data = [10, 20, 20, 20, 50, 100] # Right skewed (large outlier 100)
df = pd.Series(data)

# 1. SciPy (default)
print(f"Skewness (SciPy): {skew(data)}") 

# 2. Pandas
print(f"Skewness (Pandas): {df.skew()}")
```
*   **Output Interpretation**: The result `~1.26` is positive, indicating a **Right Skew**. This is caused by the high value `100` pulling the tail to the right.

### 3.2. Kurtosis
Measures the "tailedness" and the presence of outliers.
*   **Leptokurtic (Kurtosis > 0)**: Heavy tails and a sharp peak. Indicates many outliers.
*   **Platykurtic (Kurtosis < 0)**: Light tails and a flat peak. Indicates fewer outliers.
*   **Mesokurtic (Kurtosis = 0)**: Similar to a Normal Distribution.

> **Note on Excess Kurtosis**: Most libraries (SciPy, Pandas) calculate **Excess Kurtosis** by subtracting 3 from the Pearson kurtosis. This centers the Normal Distribution at 0.

**Python Examples**:
```python
import pandas as pd
from scipy.stats import kurtosis

data = [10, 20, 30, 40, 50] # Uniform-like spread
df = pd.Series(data)

# 1. SciPy (Fisher's definition: subtracts 3 by default)
print(f"Kurtosis (SciPy): {kurtosis(data)}")

# 2. Pandas (unbiased, also subtracts 3)
print(f"Kurtosis (Pandas): {df.kurtosis()}")
```
*   **Output Interpretation**: The result `~ -1.3` is negative, indicating a **Platykurtic** distribution. The data is relatively flat and lacks the extreme outliers that would create "heavy tails."

---

## 4. Descriptive Statistics with Statsmodels
Statsmodels provides a convenient `describe()` method for a comprehensive summary.

*   **Python Example**:
```python
import pandas as pd
import statsmodels.api as sm

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
df = pd.DataFrame(data, columns=['Value'])

# Using pandas describe for quick summary
print("Pandas Describe:")
print(df.describe())

# Using statsmodels for more detailed analysis if needed
# (Statsmodels is often used for regression, but can describe series)
from statsmodels.stats.descriptivestats import Description
desc = Description(df['Value'])
print("\nStatsmodels Description:")
print(desc.frame)
```

---

# Probability Theory

## 1. Basic Probability Concepts
*   **Sample Space ($S$)**: The set of all possible outcomes of an experiment.
*   **Event ($A$)**: A subset of the sample space.
*   **Probability of an Event**: $P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}} = \frac{|A|}{|S|}$

    *Example (Rolling a Die)*:
    - $S = \{1, 2, 3, 4, 5, 6\}$
    - Event $A$ (rolling an even number) $= \{2, 4, 6\}$
    - $P(A) = 3/6 = 0.5$

### Independent vs. Dependent Events
*   **Independent Events**: The occurrence of one event does not affect the probability of the other.
    - **Formula**: $P(A \cap B) = P(A) \times P(B)$
    - **Example**: Flipping a coin (A) and rolling a die (B).
        - $P(\text{Heads}) = 0.5$
        - $P(\text{Rolling a 6}) = 1/6$
        - $P(\text{Heads AND 6}) = 0.5 \times (1/6) \approx 0.083$

*   **Dependent Events**: The occurrence of one event affects the probability of the other.
    - **Formula**: $P(A \cap B) = P(A) \times P(B|A)$
    - **Example**: Drawing two Kings from a deck without replacement.
        - $P(\text{First King}) = 4/52$
        - $P(\text{Second King | First card was a King}) = 3/51$
        - $P(\text{Both Kings}) = (4/52) \times (3/51) \approx 0.0045$

## 2. Conditional Probability
The probability of an event $A$ occurring, given that event $B$ has already occurred.
*   **Formula**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$, where $P(B) > 0$.

*   **Understanding the Relationship**:
    - **Timing**: The events do **not** need to be sequential in time. They can occur simultaneously (e.g., a single die roll being both "4" and "even") or one after another (e.g., drawing two cards).
    - **Dependence**: This formula applies to both dependent and independent events. 
        - If $A$ and $B$ are **independent**, $P(A|B) = P(A)$ (knowing $B$ doesn't change the probability of $A$).
        - If $A$ and $B$ are **dependent**, $P(A|B) \neq P(A)$.
    - **Sample Space**: Conceptually, conditional probability **restricts the sample space**. Instead of looking at the entire set $S$, we only care about the outcomes where $B$ is true.

*   **Example**:
    Suppose you roll a fair six-sided die.
    - Let $A$ be the event that the result is a 4. $P(A) = 1/6$.
    - Let $B$ be the event that the result is an even number. $B = \{2, 4, 6\}$, so $P(B) = 3/6 = 0.5$.
    - $A \cap B$ is the event that the result is both 4 and even, which is just $\{4\}$. $P(A \cap B) = 1/6$.
    - The probability of rolling a 4, given that we know the result is even, is:
      $P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{1/6}{3/6} = \frac{1}{3} \approx 0.33$.

## 3. Bayes' Theorem
Describes the probability of an event based on prior knowledge of conditions that might be related to the event.
*   **Formula**: $P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$

*   **Mathematical Example (Medical Testing)**:
    Bayes' Theorem is often used to calculate the probability of having a disease given a positive test result.
    - $P(D)$: Probability of having the disease (Prior) = $0.01$ (1% prevalence). By extension, $P(\neg D) = 0.99$.
    - $P(Pos|D)$: Probability of testing positive given you have the disease (Sensitivity) = $0.99$.
    - $P(Pos|\neg D)$: Probability of testing positive given you do NOT have the disease (False Positive Rate) = $0.05$.
    
    *   **Where do these values come from?**:
        - **The Prior ($P(D)$)**: This is usually known from **epidemiological data**. Public health records tell us what percentage of a population currently has the disease (prevalence).
        - **The Sensitivity ($P(Pos|D)$)**: This is a **clinical property of the test** itself. It is determined during laboratory trials where researchers test people who they *already know* have the disease.
        - **The False Positive Rate ($P(Pos|\neg D)$)**: Also a **clinical property**. It is determined by testing people who are *known to be healthy* to see how often the test incorrectly flags them.
    
    1. First, calculate the total probability of testing positive $P(Pos)$ using the **Law of Total Probability**:
       $$P(Pos) = P(Pos|D)P(D) + P(Pos|\neg D)P(\neg D)$$
       
       **How is this derived?**
       - The event "testing positive" ($Pos$) can happen in two mutually exclusive ways:
         1. You have the disease AND you test positive ($Pos \cap D$).
         2. You do NOT have the disease AND you test positive ($Pos \cap \neg D$).
       - Therefore, using **disjoint additivity**:
         $$
         \begin{aligned}
         P(Pos) &= P\Big(Pos \cap (D \cup \neg D)\Big) \\
                &= P\Big((Pos \cap D) \cup (Pos \cap \neg D)\Big) \\
                &= P(Pos \cap D) + P(Pos \cap \neg D)
         \end{aligned}
         $$
       - Using the definition of conditional probability ($P(A \cap B) = P(A|B)P(B)$), we substitute:
         - $P(Pos \cap D) = P(Pos|D)P(D)$
         - $P(Pos \cap \neg D) = P(Pos|\neg D)P(\neg D)$
       - Adding them together gives the total probability.
       
       $$P(Pos) = (0.99 \times 0.01) + (0.05 \times 0.99) = 0.0594$$
    
    2. Apply Bayes' Theorem to find $P(D|Pos)$:
       $$P(D|Pos) = \frac{P(Pos|D) \times P(D)}{P(Pos)} = \frac{0.99 \times 0.01}{0.0594} \approx 0.1667$$

**Python Example**:
```python
# Bayes' Theorem: Medical Test Example
p_disease = 0.01          # P(D)
p_pos_given_disease = 0.99 # P(Pos|D)
p_pos_given_no_disease = 0.05 # P(Pos|!D)

# 1. Calculate P(not Disease)
p_no_disease = 1 - p_disease

# 2. Calculate P(Pos) using Law of Total Probability
p_pos = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * p_no_disease)

# 3. Apply Bayes' Theorem for P(Disease | Pos)
p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos

print(f"Probability of having the disease given a positive test: {p_disease_given_pos:.4f}")
```

---

# Probability Distributions

A probability distribution is a mathematical function that describes the likelihood of obtaining the possible values that a random variable can take.

*   **Mathematical Example**:
    Suppose you flip a fair coin twice. Let $X$ be the number of "Heads" obtained.
    1.  **Possible Outcomes**: $SS = \{TT, TH, HT, HH\}$
    2.  **Values of $X$**: $0, 1, 2$
    3.  **Probability Function $P(X=x)$**:
        - $P(X=0) = P(\{TT\}) = 1/4 = 0.25$
        - $P(X=1) = P(\{TH, HT\}) = 2/4 = 0.50$
        - $P(X=2) = P(\{HH\}) = 1/4 = 0.25$
    4.  **Distribution Summary**: The set of pairs $\{(0, 0.25), (1, 0.50), (2, 0.25)\}$ is the probability distribution of $X$. Note that $\sum P(X=x) = 1$.

## 1. Random Variables
A mapping from the sample space of a random experiment to the set of real numbers.
*   **Discrete Random Variables**: Variables that can only take a countable number of distinct values.
    - **Example**: The number of students who show up for a lecture.
    - **Values**: $\{0, 1, 2, \dots, N\}$ where $N$ is the total number of students. You cannot have 20.5 students.
*   **Continuous Random Variables**: Variables that can take any value within a given range.
    - **Example**: The temperature of a room at any given moment.
    - **Values**: Any value within a range (e.g., $20.0^\circ C$, $20.05^\circ C$, $20.053^\circ C$, etc.). It can be measured with infinite precision.

## 2. Common Discrete Distributions
*   **Bernoulli Distribution**: Models a single trial with exactly two possible outcomes.
    - **Random Variable ($X$)**: $X=1$ for success, $X=0$ for failure.
    - **Support**: $\{0, 1\}$ (possible values of $X$)
    - **Parameter ($p$)**: Probability of success ($0 \leq p \leq 1$)
    - **PMF**: $P_{\text{Bernoulli}}(X=x) = p^x (1-p)^{1-x}$ for $x \in \{0, 1\}$
    - **Mean**: $\mu = p$, **Variance**: $\sigma^2 = p(1-p)$
    - **Example**: A single coin flip where "Heads" is success ($p=0.5$)
    - **Solution**: To find the probability of getting "Heads" ($X=1$):
        $P_{\text{Bernoulli}}(X=1) = 0.5^1 \times (1-0.5)^{1-1} = 0.5 \times 0.5^0 = 0.5 \times 1 = 0.5$
    - **Additional Example**: A basketball player takes a free throw with 80% success rate. What is the probability they miss the shot?
    - **Solution**: For a miss ($X=0$):
        $P_{\text{Bernoulli}}(X=0) = 0.8^0 \times (1-0.8)^{1-0} = 1 \times 0.2^1 = 0.2$
    - **Cumulative Probability Example**: For the same basketball player, what is the probability of getting at most one success (i.e., either success or failure)?
    - **Solution**: Since Bernoulli only has two outcomes:
        $P(X \leq 1) = P(X=0) + P(X=1) = 0.2 + 0.8 = 1.0$

*   **Binomial Distribution**: Models the number of successes in $n$ independent Bernoulli trials.
    - **Random Variable ($X$)**: Total number of successes
    - **Support**: $\{0, 1, 2, \dots, n\}$ (possible values of $X$)
    - **Parameters**: $n$ (number of trials), $p$ (probability of success)
    - **PMF**: $P_{\text{Binomial}}(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ for $k = 0, 1, \dots, n$
    - **Mean**: $\mu = np$, **Variance**: $\sigma^2 = np(1-p)$
    - **Example**: What is the probability of rolling exactly two 6s in 10 tosses of a fair die?
    - **Solution**:
        1. $n = 10$ (trials), $k = 2$ (successes)
        2. $p = 1/6$ (probability of rolling a 6), $1-p = 5/6$
        3. $P_{\text{Binomial}}(X=2) = \binom{10}{2} (1/6)^2 (5/6)^{8}$
        4. $P_{\text{Binomial}}(X=2) = 45 \times (1/36) \times (5/6)^8 \approx 45 \times 0.02778 \times 0.23257 \approx 0.2907$
    - **Additional Example**: A quality control inspector tests 20 light bulbs from a batch where 5% are defective. What is the probability that exactly 3 bulbs are defective?
    - **Solution**:
        1. $n = 20$ (trials), $k = 3$ (defective bulbs)
        2. $p = 0.05$ (probability of defect), $1-p = 0.95$
        3. $P_{\text{Binomial}}(X=3) = \binom{20}{3} (0.05)^3 (0.95)^{17}$
        4. $P_{\text{Binomial}}(X=3) = 1140 \times 0.000125 \times 0.4181 \approx 1140 \times 0.00005226 \approx 0.0596$
    - **Cumulative Probability Example**: For the same quality control scenario, what is the probability of finding at most 2 defective bulbs?
    - **Solution**: We need to calculate $P(X \leq 2) = P(X=0) + P(X=1) + P(X=2)$
        $P(X=0) = \binom{20}{0} (0.05)^0 (0.95)^{20} = 1 \times 1 \times 0.3585 \approx 0.3585$
        $P(X=1) = \binom{20}{1} (0.05)^1 (0.95)^{19} = 20 \times 0.05 \times 0.3774 \approx 0.3774$
        $P(X=2) = \binom{20}{2} (0.05)^2 (0.95)^{18} = 190 \times 0.0025 \times 0.3972 \approx 0.1886$
        $P(X \leq 2) \approx 0.3585 + 0.3774 + 0.1886 = 0.9245$

*   **Poisson Distribution**: Models the number of events occurring in a fixed interval of time or space.
    - **Random Variable ($X$)**: Number of occurrences in the interval
    - **Support**: $\{0, 1, 2, \dots\}$ (theoretically infinite, possible values of $X$)
    - **Parameter ($\lambda$)**: The average rate of occurrence (mean)
    - **PMF**: $P_{\text{Poisson}}(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$ for $k = 0, 1, 2, \dots$
    - **Mean**: $\mu = \lambda$, **Variance**: $\sigma^2 = \lambda$
    - **Example**: If a bakery receives an average of 3 customers per hour, what is the probability they receive exactly 2 customers in the next hour?
    - **Solution**:
        1. $\lambda = 3$ (average rate), $k = 2$ (desired occurrences)
        2. $P_{\text{Poisson}}(X=2) = \frac{3^2 e^{-3}}{2!}$
        3. $P_{\text{Poisson}}(X=2) = \frac{9 \times 0.049787}{2} = \frac{0.448083}{2} = 0.22404$
    - **Additional Example**: A call center receives an average of 5 calls per minute. What is the probability they receive exactly 4 calls in a given minute?
    - **Solution**:
        1. $\lambda = 5$ (average rate), $k = 4$ (desired occurrences)
        2. $P_{\text{Poisson}}(X=4) = \frac{5^4 e^{-5}}{4!}$
        3. $P_{\text{Poisson}}(X=4) = \frac{625 \times 0.006738}{24} = \frac{4.21125}{24} \approx 0.1755$
    - **Cumulative Probability Example**: For the same call center, what is the probability they receive at most 3 calls in a minute?
    - **Solution**: We need to calculate $P(X \leq 3) = P(X=0) + P(X=1) + P(X=2) + P(X=3)$
        $P(X=0) = \frac{5^0 e^{-5}}{0!} = \frac{1 \times 0.006738}{1} \approx 0.0067$
        $P(X=1) = \frac{5^1 e^{-5}}{1!} = \frac{5 \times 0.006738}{1} \approx 0.0337$
        $P(X=2) = \frac{5^2 e^{-5}}{2!} = \frac{25 \times 0.006738}{2} \approx 0.0842$
        $P(X=3) = \frac{5^3 e^{-5}}{3!} = \frac{125 \times 0.006738}{6} \approx 0.1404$
        $P(X \leq 3) \approx 0.0067 + 0.0337 + 0.0842 + 0.1404 = 0.2650$

## 3. Common Continuous Distributions
*   **Uniform Distribution**: All outcomes in a range $[a, b]$ are equally likely.
    - **Random Variable ($X$)**: Any value within the interval $[a, b]$
    - **Support**: $[a, b]$ (continuous interval)
    - **Parameters**: $a$ (lower bound), $b$ (upper bound)
    - **PDF**: $f_{\text{Uniform}}(x) = \frac{1}{b-a}$ for $a \leq x \leq b$
    - **CDF**: $F_{\text{Uniform}}(x) = \frac{x-a}{b-a}$ for $a \leq x \leq b$
    - **Mean**: $\mu = \frac{a+b}{2}$, **Variance**: $\sigma^2 = \frac{(b-a)^2}{12}$
    - **Example**: A random number generator picking a value between 0 and 1.
    - **Solution**: For $X \sim \text{Uniform}(0, 1)$, the probability density is constant:
        $f_{\text{Uniform}}(x) = 1$ for $0 \leq x \leq 1$
    - **Additional Example**: What is the probability that a value from Uniform(2, 8) falls between 3 and 5?
    - **Solution**: 
        $P(3 \leq X \leq 5) = \frac{5-3}{8-2} = \frac{2}{6} = \frac{1}{3} \approx 0.3333$
*   **Normal (Gaussian) Distribution**: The "Bell Curve," symmetrical and defined by mean ($\mu$) and standard deviation ($\sigma$).
    - **Random Variable ($X$)**: Any real number
    - **Support**: $(-\infty, \infty)$ (all real numbers)
    - **Parameters**: $\mu$ (mean), $\sigma$ (standard deviation)
    - **PDF**: $f_{\text{Normal}}(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$
    - **CDF**: $F_{\text{Normal}}(x) = \Phi\left(\frac{x-\mu}{\sigma}\right)$ where $\Phi$ is the standard normal CDF
    - **Mean**: $\mu$, **Variance**: $\sigma^2$
    - **Example**: Human heights follow Normal($\mu = 170$ cm, $\sigma = 10$ cm).
    - **Solution**: The probability density at the mean is:
        $f_{\text{Normal}}(170) = \frac{1}{10\sqrt{2\pi}} e^{0} = \frac{1}{25.1327} \approx 0.0398$
    - **Additional Example**: What is the probability that a randomly selected person is between 160 cm and 180 cm tall?
    - **Solution**: Using standard normal transformation:
        $P(160 \leq X \leq 180) = \Phi\left(\frac{180-170}{10}\right) - \Phi\left(\frac{160-170}{10}\right) = \Phi(1) - \Phi(-1) \approx 0.8413 - 0.1587 = 0.6826$
> **Note on Standardization**:
> - **Standard Normal Distribution**: A special case with $\mu = 0$ and $\sigma = 1$, denoted $Z \sim \mathcal{N}(0,1)$. Any normal variable $X \sim \mathcal{N}(\mu,\sigma)$ can be converted to a standard normal variable $Z$ using a $z$-score.
> - **Z-scores and Standardization**: The $z$-score of a value $x$ from $X \sim \mathcal{N}(\mu,\sigma)$ is
>     $z = \frac{x - \mu}{\sigma}$.
>     This measures how many standard deviations $x$ is above ($z>0$) or below ($z<0$) the mean. Probabilities for $X$ are usually computed by first converting to $Z$ and then using the standard normal CDF $\Phi(z)$.
> - **Empirical Rule (68-95-99.7)**: For a normal distribution, approximately 68% of the data lie within $1\sigma$ of the mean, 95% within $2\sigma$, and 99.7% within $3\sigma$. The height example above confirms the 68% part since
>     $P(160 \leq X \leq 180) = P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 0.6826 \approx 68\%$.
> - **Normal Tables and Percentiles**: Standard normal tables list values of $\Phi(z) = P(Z \leq z)$ for $Z \sim \mathcal{N}(0,1)$. To find a percentile (for example, the 90th percentile of heights), find $z$ such that $\Phi(z) = 0.90$ in the table (approximately $z \approx 1.28$), then transform back:
>     $x = \mu + z\sigma$.
>     For the height example, the 90th percentile is $x \approx 170 + 1.28 \times 10 = 182.8$ cm.
*   **Exponential Distribution**: Models the time between events in a Poisson process.
    - **Random Variable ($X$)**: Time until next event
    - **Support**: $[0, \infty)$ (non-negative real numbers)
    - **Parameter ($\lambda$)**: Rate parameter (events per unit time)
    - **PDF**: $f_{\text{Exponential}}(x) = \lambda e^{-\lambda x}$ for $x \geq 0$
    - **CDF**: $F_{\text{Exponential}}(x) = 1 - e^{-\lambda x}$ for $x \geq 0$
    - **Mean**: $\mu = \frac{1}{\lambda}$, **Variance**: $\sigma^2 = \frac{1}{\lambda^2}$
    - **Example**: The time between customer arrivals follows Exponential($\lambda = 0.2$ customers per minute).
    - **Solution**: The probability density at time 0 is:
        $f_{\text{Exponential}}(0) = 0.2 \times e^{0} = 0.2$
    - **Additional Example**: What is the probability that the next customer arrives within 5 minutes?
    - **Solution**: 
        $P(X \leq 5) = 1 - e^{-0.2 \times 5} = 1 - e^{-1} \approx 1 - 0.3679 = 0.6321$

---

## 4. Sampling Distributions

A sampling distribution is the probability distribution of a statistic (like the mean) obtained through a large number of samples drawn from a specific population.
*   **Mathematical Example**:
    Suppose we have a population $P = \{2, 4, 6\}$.
    1.  **Population Mean ($\mu$)**: $\mu = \frac{2+4+6}{3} = 4$.
    2.  **Sampling**: Draw all possible samples of size $n=2$ (with replacement).
        - Possible Samples: $(2,2), (2,4), (2,6), (4,2), (4,4), (4,6), (6,2), (6,4), (6,6)$.
    3.  **Sample Means ($\bar{x}$)**: Calculate the mean for each sample:
        - $2, 3, 4, 3, 4, 5, 4, 5, 6$.
    4.  **Sampling Distribution**: The probability of each possible sample mean:
        - $P(\bar{X}=2) = 1/9, \quad P(\bar{X}=3) = 2/9, \quad P(\bar{X}=4) = 3/9, \quad P(\bar{X}=5) = 2/9, \quad P(\bar{X}=6) = 1/9$.
    - **Note**: The mean of this sampling distribution is $E[\bar{X}] = (2 \cdot \frac{1}{9}) + (3 \cdot \frac{2}{9}) + (4 \cdot \frac{3}{9}) + (5 \cdot \frac{2}{9}) + (6 \cdot \frac{1}{9}) = 4$, which equals the population mean $\mu$.

### 4.1. Central Limit Theorem (CLT)
The CLT states that, regardless of the population's distribution, the distribution of the sample means will approach a **Normal Distribution** as the sample size ($n$) becomes large (typically $n \geq 30$).
*   **Significance**: This allows us to use normal distribution techniques to make inferences about population parameters even when the population itself is not normally distributed.
*   **Example**: If you take 1000 random samples of 50 people's weights, the distribution of those 1000 means will be normal, even if the individual weights are skewed.

### 4.2. Law of Large Numbers (LLN)
The LLN states that as the number of trials or observations increases, the sample mean will converge to the true population mean.
*   **Significance**: It guarantees that large samples are more representative of the population than small samples.
*   **Example**: If you flip a fair coin 10 times, you might get 7 heads (70%). But if you flip it 10,000 times, the percentage of heads will be very close to 50%.
*   **Mathematical Example**:
    Suppose we roll a fair 6-sided die. The population is $\{1, 2, 3, 4, 5, 6\}$.
    1.  **Population Mean ($\mu$)**: $\mu = \frac{1+2+3+4+5+6}{6} = 3.5$.
    2.  **Small Sample ($n=4$)**: We roll $\{1, 6, 2, 2\}$.
        - Sample Mean ($\bar{x}_1$) = $\frac{1+6+2+2}{4} = 2.75$ (Error: $|3.5 - 2.75| = 0.75$).
    3.  **Medium Sample ($n=10$)**: We roll $\{1, 6, 2, 2, 4, 5, 3, 6, 4, 2\}$.
        - Sample Mean ($\bar{x}_2$) = $\frac{35}{10} = 3.5$ (Error: $0$). *(Note: Randomly hit the mean early)*.
    4.  **Large Sample ($n=1000$)**: After 1000 rolls, the sum of values is $3508$.
        - Sample Mean ($\bar{x}_3$) = $\frac{3508}{1000} = 3.508$ (Error: $|3.5 - 3.508| = 0.008$).
    - **Conclusion**: As $n$ increases, the sample mean $\bar{x}$ consistently stays closer to the population mean $\mu = 3.5$, reducing the impact of random fluctuations.

### 4.3. CLT vs LLN: Comparison and Usecases

While both theorems describe what happens as sample size $n$ increases, they focus on different properties of the sample mean $\bar{X}$.

| Feature | Law of Large Numbers (LLN) | Central Limit Theorem (CLT) |
| :--- | :--- | :--- |
| **Focus** | The **Value** of the sample mean. | The **Distribution** of the sample mean. |
| **Claim** | $\bar{X}$ converges to the population mean $\mu$. | The distribution of $\bar{X}$ becomes Normal. |
| **Visual** | A single point moving toward a target. | A histogram forming a bell curve. |
| **Requirement** | $n \to \infty$. | $n \geq 30$ (usually). |

#### Problems Solved
*   **LLN**: Solves the problem of **Accuracy**. It tells us that we can trust our sample statistics as long as our sample is "large enough." It justifies using sample data to estimate population parameters.
*   **CLT**: Solves the problem of **Uncertainty**. It tells us exactly *how* the sample means vary. Even if the population is weirdly shaped (skewed, uniform, etc.), we can use Normal distribution math to calculate probabilities for our sample means.

#### Usecases
*   **LLN Usecases**:
    *   **Casino Math**: Casinos know that while a single gambler might win big, over thousands of games, the "house edge" (the mean) will prevail.
    *   **Surveying**: Ensuring that a poll of 1000 people accurately represents the average opinion of millions.
*   **CLT Usecases**:
    *   **Hypothesis Testing**: Deciding if a drug is effective by comparing its mean result to the normal distribution of sample means.
    *   **Confidence Intervals**: Saying "We are 95% sure the true mean is between X and Y" depends entirely on the CLT.

---

# Statistical Inference

Statistical inference is the process of using data from a sample to make generalizations or draw conclusions about the population from which the sample was drawn. It allows us to go beyond the immediate data and provide statements about broader phenomena.

## 1. Hypothesis Testing

Hypothesis testing is a formal statistical procedure used to determine whether there is enough evidence in a sample of data to support a particular belief or claim about a population.

### 1.1. Null and Alternative Hypotheses

Every hypothesis test involves two opposing statements:

*   **Null Hypothesis ($H_0$)**: The statement being tested. It usually represents "no effect," "no difference," or the "status quo." We assume the null hypothesis is true until we have sufficient evidence to suggest otherwise.
    *   *Mathematical Notation*: $H_0: \mu = \mu_0$ (e.g., the mean is equal to a specific value).
*   **Alternative Hypothesis ($H_a$ or $H_1$)**: The statement we are looking for evidence to support. It represents a change, a difference, or a relationship.
    *   *Mathematical Notation*: $H_a: \mu \neq \mu_0$ (Two-tailed), $H_a: \mu > \mu_0$ (Right-tailed), or $H_a: \mu < \mu_0$ (Left-tailed).

**Example**:
A company claims their new light bulbs last 1000 hours. A consumer group suspects they last less.
- $H_0$: $\mu = 1000$ (The bulbs last 1000 hours as claimed).
- $H_a$: $\mu < 1000$ (The bulbs last less than 1000 hours).

### 1.2. Type I and Type II Errors

Because we rely on samples, our conclusions might be incorrect. There are two types of errors we can make:

| Error Type | Name | Definition | Analogy (Courtroom) |
| :--- | :--- | :--- | :--- |
| **Type I Error** | False Positive | Rejecting $H_0$ when it is actually **true**. | Convicting an innocent person. |
| **Type II Error** | False Negative | Failing to reject $H_0$ when it is actually **false**. | Letting a guilty person go free. |

*   **Alpha ($\alpha$)**: The probability of making a Type I error. This is the "significance level" we set.
*   **Beta ($\beta$)**: The probability of making a Type II error.
*   **Power ($1 - \beta$)**: The probability of correctly rejecting a false null hypothesis (the ability of a test to detect an effect if one exists).

### 1.3. p-values and Significance Levels

The decision to reject or fail to reject the null hypothesis is based on comparing the **p-value** to the **significance level ($\alpha$)**.

*   **Significance Level ($\alpha$)**: The threshold for "unlikely." Common choices are 0.05 (5%), 0.01 (1%), or 0.10 (10%). If we set $\alpha = 0.05$, we are willing to accept a 5% risk of a Type I error.
*   **p-value**: The probability of seeing data as extreme as ours, assuming $H_0$ is true. It measures how "surprising" the data is.

**Decision Rules**:
1.  **If p-value $\leq \alpha$**: The result is **statistically significant**. We **reject $H_0$** and support $H_a$.
2.  **If p-value $> \alpha$**: The result is **not statistically significant**. We **fail to reject $H_0$**.

> **Crucial Note**: We never "accept" the null hypothesis. We only "fail to reject" it, meaning we don't have enough evidence to disprove it yet.

**Statsmodels Example**:
```python
import statsmodels.api as sm
from statsmodels.stats.weightstats import DescrStatsW

# Sample data: scores of students using a new study method
sample_scores = [85, 88, 90, 82, 91, 89, 87, 84, 92, 86]

# H0: The population mean is 80 (Old method mean)
# Ha: The population mean is NOT 80
null_mean = 80

# Perform a One-Sample T-Test using statsmodels
d_stats = DescrStatsW(sample_scores)
t_stat, p_value, df = d_stats.ttest_mean(null_mean)

alpha = 0.05

print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value <= alpha:
    print("Decision: Reject H0. The new study method has a significant effect.")
else:
    print("Decision: Fail to reject H0. No significant evidence of an effect.")
```

## 2. Point Estimation

Point estimation focuses on using sample data to calculate a single, best-guess value (a **point estimate**) for an unknown population parameter.

*   **Point Estimates for Means and Proportions**
    *   The **sample mean** $\bar{X}$ is the point estimate of the population mean $\mu$:
        $\hat{\mu} = \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$.
    *   The **sample proportion** $\hat{p}$ is the point estimate of the population proportion $p$:
        $\hat{p} = \frac{\text{Number of "successes"}}{\text{Sample size } n}$.
    *   These estimates summarize the sample with a single number and are the building blocks for further inference such as confidence intervals and hypothesis tests.

*   **Properties of Estimators (Bias, Variance, Consistency)**
    *   An **estimator** is a rule or formula (like $\bar{X}$ or $\hat{p}$) used to compute an estimate from data.
    *   **Bias**:
        *   Measures whether, on average, the estimator hits the true parameter.
        *   An estimator $\hat{\theta}$ of a parameter $\theta$ is **unbiased** if $E[\hat{\theta}] = \theta$.
        *   Example: The sample mean $\bar{X}$ is an unbiased estimator of $\mu$.
    *   **Variance**:
        *   Measures how much the estimator varies from sample to sample.
        *   Lower variance means more stable estimates across different samples.
    *   **Consistency**:
        *   An estimator is **consistent** if, as the sample size $n \to \infty$, the estimator converges in probability to the true parameter.
        *   Intuitively: with more data, the estimator gets closer and closer to the true value.

**Python Example**:
```python
import numpy as np

# 1. Point Estimate for Mean
# Data: Weights of 10 apples
weights = [150, 155, 148, 152, 151, 153, 149, 150, 154, 152]
point_est_mean = np.mean(weights)
print(f"Point Estimate (Mean): {point_est_mean:.2f}g")

# 2. Point Estimate for Proportion
# Data: 100 website visitors, 12 clicked an ad
n = 100
successes = 12
point_est_prop = successes / n
print(f"Point Estimate (Proportion): {point_est_prop:.2%}")
```

## 3. Confidence Intervals

While point estimates give a single value, they do not tell us how uncertain that value is. **Confidence intervals (CIs)** provide a range of plausible values for a population parameter along with a confidence level.

*   **Confidence Level and Interpretation**
    *   A **confidence level** (e.g., 90%, 95%, 99%) describes how often the interval procedure would capture the true parameter if we repeated the sampling process many times.
    *   A **95% confidence interval for $\mu$** means:
        *   If we took many random samples and built an interval from each, about 95% of those intervals would contain the true $\mu$.
        *   It does **not** mean there is a 95% probability that $\mu$ is in a specific, already-calculated interval.

*   **Margin of Error**
    *   A confidence interval generally has the form:
        $\text{Estimate} \pm \text{Margin of Error}$.
    *   The **margin of error (ME)** reflects both variability in the data and the chosen confidence level.
    *   Larger samples (larger $n$) and lower confidence levels lead to smaller margins of error; higher confidence levels lead to larger margins of error.

*   **Critical Values (Z and t)**
    *   The **critical value** comes from a reference distribution and determines how many standard errors we extend from the estimate.
    *   **Z critical values** (from the standard normal distribution) are used when:
        *   The population standard deviation is known or the sample size is large and conditions justify normal approximation.
        *   Example: For a 95% confidence level, the two-sided critical value is $z_{0.975} \approx 1.96$.
    *   **t critical values** (from the Student’s t distribution) are used when:
        *   The population standard deviation is unknown and the sample size is small.
        *   The exact critical value depends on both the confidence level and the **degrees of freedom** (typically $n-1$).

*   **Confidence Intervals for Means and Proportions**
    *   **Mean with known $\sigma$ (Normal or large-sample case)**:
        *   For $X_1, \dots, X_n$ i.i.d. with mean $\mu$ and known standard deviation $\sigma$, a $(1-\alpha)$ confidence interval for $\mu$ is:
            $\bar{X} \pm z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$.
    *   **Mean with unknown $\sigma$ (t-interval)**:
        *   When $\sigma$ is unknown and the sample size is small but data are approximately normal, use:
            $\bar{X} \pm t_{1-\alpha/2,\, n-1} \cdot \frac{s}{\sqrt{n}}$,
            where $s$ is the sample standard deviation.
    *   **Proportion (large-sample z-interval)**:
        *   For a sample proportion $\hat{p}$ with sufficiently large $n$ so that normal approximation is appropriate, a $(1-\alpha)$ confidence interval for $p$ is:
            $\hat{p} \pm z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$.

**Statsmodels Example**:
```python
from statsmodels.stats.weightstats import DescrStatsW
from statsmodels.stats.proportion import proportion_confint

# 1. Confidence Interval for Mean (Unknown sigma -> t-distribution)
data = [85, 88, 90, 82, 91, 89, 87, 84, 92, 86]
d_stats = DescrStatsW(data)

# tconfint_mean returns (lower, upper)
ci_mean = d_stats.tconfint_mean(alpha=0.05) 
print(f"95% CI for Mean: ({ci_mean[0]:.2f}, {ci_mean[1]:.2f})")

# 2. Confidence Interval for Proportion (Large sample -> z-distribution)
# Data: 12 successes in 100 trials
count = 12
nobs = 100
ci_prop = proportion_confint(count, nobs, alpha=0.05, method='normal')
print(f"95% CI for Proportion: ({ci_prop[0]:.4f}, {ci_prop[1]:.4f})")
```

These ideas connect directly back to sampling distributions and the Central Limit Theorem: the distribution of estimates like $\bar{X}$ and $\hat{p}$ is approximately normal for large $n$, which allows us to use $z$ or $t$ critical values to build meaningful confidence intervals around our point estimates.
