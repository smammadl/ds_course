# Logarithms, Exponentials, and Transformations in Data Science

## Logarithmic Functions

### Definition

The **logarithm** is the inverse operation of exponentiation. For a base $b > 0, b \neq 1$:

$$\log_b(x) = y \iff b^y = x$$

### Common Bases

| Base | Notation | Name | Usage |
|------|----------|------|-------|
| $e \approx 2.718$ | $\ln(x)$ or $\log_e(x)$ | Natural log | Mathematics, ML, calculus |
| $10$ | $\log_{10}(x)$ or $\log(x)$ | Common log | Engineering, decibels |
| $2$ | $\log_2(x)$ | Binary log | Information theory, CS |

### Key Properties

1. **Product Rule**: $\log_b(xy) = \log_b(x) + \log_b(y)$
2. **Quotient Rule**: $\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)$
3. **Power Rule**: $\log_b(x^n) = n \cdot \log_b(x)$
4. **Change of Base**: $\log_b(x) = \frac{\log_a(x)}{\log_a(b)}$
5. **Identity**: $\log_b(b) = 1$
6. **Zero**: $\log_b(1) = 0$

### Domain and Range

- **Domain**: $x \in (0, \infty)$ — logarithm is only defined for positive numbers
- **Range**: $y \in (-\infty, \infty)$
- **Vertical Asymptote**: $x = 0$

### Derivative and Integral

$$\frac{d}{dx}\ln(x) = \frac{1}{x}$$

$$\int \ln(x) \, dx = x\ln(x) - x + C$$

---

## Exponential Functions

### Definition

The **exponential function** with base $b > 0$:

$$f(x) = b^x$$

The **natural exponential** (most common in data science):

$$f(x) = e^x = \exp(x)$$

where $e \approx 2.71828$ is Euler's number.

### Key Properties

1. **Product**: $b^{x+y} = b^x \cdot b^y$
2. **Quotient**: $b^{x-y} = \frac{b^x}{b^y}$
3. **Power**: $(b^x)^y = b^{xy}$
4. **Identity**: $b^0 = 1$
5. **Self-derivative**: $\frac{d}{dx}e^x = e^x$

### Domain and Range

- **Domain**: $x \in (-\infty, \infty)$
- **Range**: $y \in (0, \infty)$ — always positive
- **Horizontal Asymptote**: $y = 0$

### Taylor Series Expansion

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

---

## The Log(x+1) Transformation

### Definition

$$f(x) = \log(x + 1)$$

Also written as `log1p(x)` in many libraries for numerical stability.

### Why Add 1?

The standard logarithm $\log(x)$ is undefined at $x = 0$. By adding 1:

- $\log(0 + 1) = \log(1) = 0$ ✓
- Handles zero values gracefully
- Preserves the order of data

### Properties

| Property | $\log(x)$ | $\log(x+1)$ |
|----------|-----------|-------------|
| Domain | $(0, \infty)$ | $(-1, \infty)$ |
| At $x=0$ | Undefined | $0$ |
| At $x=1$ | $0$ | $\ln(2) \approx 0.693$ |

### Inverse: Exponential Minus 1

The inverse of $\log(x+1)$ is:

$$f^{-1}(y) = e^y - 1$$

In Python: `np.expm1(y)` provides numerical stability for small values.

### When to Use

1. **Skewed distributions**: Right-skewed data (e.g., income, population)
2. **Count data**: Non-negative integers with many zeros
3. **Feature scaling**: Compress wide-ranging features
4. **Variance stabilization**: When variance increases with mean

---

## Inverse Functions

### Definition

Two functions $f$ and $g$ are **inverses** if:

$$f(g(x)) = x \quad \text{and} \quad g(f(x)) = x$$

Notation: $f^{-1}$ denotes the inverse of $f$.

### Inverse Pairs in Data Science

| Function | Inverse | Domain Restriction |
|----------|---------|-------------------|
| $f(x) = e^x$ | $f^{-1}(x) = \ln(x)$ | $x > 0$ for ln |
| $f(x) = \log(x+1)$ | $f^{-1}(x) = e^x - 1$ | $x > -1$ |
| $f(x) = x^2$ | $f^{-1}(x) = \sqrt{x}$ | $x \geq 0$ |
| $f(x) = \frac{1}{x}$ | $f^{-1}(x) = \frac{1}{x}$ | $x \neq 0$ |
| $f(x) = ax + b$ | $f^{-1}(x) = \frac{x-b}{a}$ | $a \neq 0$ |

### Finding Inverses (Algebraic Method)

1. Replace $f(x)$ with $y$
2. Swap $x$ and $y$
3. Solve for $y$
4. Replace $y$ with $f^{-1}(x)$

**Example**: Find inverse of $f(x) = \log(x+1)$

$$\begin{aligned}
y &= \log(x+1) \\
x &= \log(y+1) \quad \text{(swap)} \\
e^x &= y + 1 \quad \text{(exponentiate)} \\
y &= e^x - 1 \quad \text{(solve)} \\
f^{-1}(x) &= e^x - 1
\end{aligned}$$

### Horizontal Line Test

A function has an inverse that is also a function if and only if it passes the **horizontal line test** (is one-to-one/injective).

---

## Why Transformations Matter in Data Science

### 1. Handling Skewed Distributions

Many ML algorithms assume normally distributed features. Log transformations reduce right skew:

$$\text{Skewed data: } X \sim \text{LogNormal}(\mu, \sigma^2)$$
$$\text{After transform: } \ln(X) \sim \text{Normal}(\mu, \sigma^2)$$

### 2. Linearizing Relationships

Exponential relationships become linear after log transformation:

$$\begin{aligned}
\text{Original: } y &= ae^{bx} \\
\text{Log transform: } \ln(y) &= \ln(a) + bx
\end{aligned}$$

This enables linear regression on transformed data.

### 3. Stabilizing Variance (Homoscedasticity)

When variance increases with the mean (heteroscedasticity), log transformation can stabilize it:

$$\text{Before: } \text{Var}(Y) \propto \mathbb{E}[Y]$$
$$\text{After: } \text{Var}(\ln(Y)) \approx \text{constant}$$

### 4. Feature Scaling

Compresses wide-ranging values into a manageable scale:

| Original | $\log_{10}$ | $\ln$ |
|----------|-------------|-------|
| 1 | 0 | 0 |
| 10 | 1 | 2.30 |
| 100 | 2 | 4.61 |
| 1000 | 3 | 6.91 |
| 10000 | 4 | 9.21 |

### 5. Interpretability in Models

**Log-Linear Model**: $\ln(y) = \beta_0 + \beta_1 x$
- Interpretation: A 1-unit increase in $x$ leads to a $(100 \cdot \beta_1)\%$ change in $y$

**Linear-Log Model**: $y = \beta_0 + \beta_1 \ln(x)$
- Interpretation: A 1% increase in $x$ leads to a $\frac{\beta_1}{100}$ unit change in $y$

**Log-Log Model**: $\ln(y) = \beta_0 + \beta_1 \ln(x)$
- Interpretation: A 1% increase in $x$ leads to a $\beta_1\%$ change in $y$ (elasticity)

### 6. Numerical Stability

Working in log-space prevents overflow/underflow:

$$\log\left(\prod_{i=1}^n p_i\right) = \sum_{i=1}^n \log(p_i)$$

Used extensively in:
- Probability calculations (Naive Bayes)
- Likelihood functions
- Cross-entropy loss

### 7. Regularization Effect

Log transformation acts as implicit regularization by reducing the influence of outliers.
