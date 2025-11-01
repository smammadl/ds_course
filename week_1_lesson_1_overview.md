# Week 1: Introduction to Python and Basic Concepts

## Introduction to Programming

### What is programming?

Programming is the process of writing instructions for a computer to execute. These instructions, written in a programming language, tell the computer how to perform a task or solve a problem. Think of it as creating a recipe for the computer to follow.

### What is Data Analytics?

Data Analytics focuses on examining large datasets to find trends, answer questions, and draw conclusions. It often involves creating dashboards and reports to visualize the findings. The primary goal is to make sense of past data to inform business decisions. For example, a company might analyze sales data to understand which products are most popular in different regions.

### What is Data Science?

Data Science is a broader field that encompasses data analytics. It involves using scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data. Data scientists not only analyze data but also use advanced techniques, like machine learning, to make predictions about the future.

### What is Machine Learning?

Machine Learning (ML) is a subset of artificial intelligence (AI) and data science. It focuses on building algorithms that allow computers to learn from data without being explicitly programmed. Instead of writing rules, you feed data to the algorithm, and it learns the patterns itself. For example, an email spam filter is a machine learning model that learns to identify junk mail based on past examples.

### Key Differences Summarized

| Aspect                | Programming                                       | Data Analytics                                       | Data Science                                                 | Machine Learning                                           |
| :-------------------- | :------------------------------------------------ | :--------------------------------------------------- | :----------------------------------------------------------- | :--------------------------------------------------------- |
| **Main Question**     | "How do I make the computer do something?"        | "What happened and why?"                             | "What will happen? What should we do?"                       | "How can the system learn to make predictions?"            |
| **Core Activities**   | Writing, testing, and maintaining code.           | Cleaning, exploring, and visualizing data.           | Building predictive models, running experiments.             | Developing, training, and deploying algorithms.            |
| **Goals**             | Create software, automate tasks, build systems.   | Find insights, create reports and dashboards.        | Make predictions, inform strategy, create data products.     | Create systems that improve automatically with experience. |
| **Mathematical Depth**| Low to High (depends on the application).         | Moderate (strong statistics).                        | High (statistics, calculus, linear algebra).                 | Very High (advanced statistics, optimization, calculus).   |
| **Tools/Techniques**  | IDEs, Compilers, Version Control (Git), Libraries.| SQL, Excel, BI tools (Tableau), Python (Pandas).     | Python (Scikit-learn), R, Spark, advanced statistics.        | TensorFlow, PyTorch, Keras, advanced algorithms.           |
| **Outputs**           | Applications, scripts, websites, operating systems.| Reports, dashboards, visualizations.                 | Predictive models, research, data-driven products.           | Self-learning systems, AI applications (e.g., spam filters).|

### Why Python for Data Science?

Python has become the de-facto language for data science for several key reasons:

*   **Simplicity and Readability:** Python's syntax is clean and intuitive, making it relatively easy for beginners to learn. It reads almost like plain English.
*   **Extensive Libraries:** Python boasts a rich ecosystem of libraries specifically designed for data science, such as:
    *   **Pandas:** For data manipulation and analysis.
    *   **NumPy:** For numerical operations, especially with arrays.
    *   **Matplotlib and Seaborn:** For data visualization.
    *   **Scikit-learn:** For machine learning algorithms.
*   **Versatility:** Python is a general-purpose language, meaning it's not just for data science. You can build web applications, automate tasks, and more.
*   **Large Community:** A massive and active global community means you can easily find help, tutorials, and solutions to problems.

### Python's Role in Different Fields

| Field                 | Python's Strengths                                                                      | Main Drawbacks                                      | Popular Alternatives                               |
| :-------------------- | :--------------------------------------------------------------------------------------- | :-------------------------------------------------- | :------------------------------------------------- |
| **General Programming** | Versatile, easy to learn, large standard library, strong for web development (Django, Flask). | Slower performance compared to compiled languages.  | Java, C++, JavaScript, Go                            |
| **Data Analytics**      | Excellent libraries (Pandas, NumPy), great for data cleaning, manipulation, and exploration. | Can be memory-intensive with very large datasets.   | R, SQL, Excel, Tableau                             |
| **Data Science**        | The leading language; seamless integration of analytics, ML, and visualization libraries.  | Performance limitations for high-performance computing. | R, Scala (with Spark)                              |
| **Machine Learning**    | Dominant language with top-tier libraries (TensorFlow, PyTorch, Scikit-learn).           | Not ideal for low-level or embedded ML systems.     | C++, R, Julia                                      |

## Setting up the Environment

### Installing Visual Studio Code (VS Code)

VS Code is a lightweight but powerful source code editor that runs on your desktop and is available for Windows, macOS, and Linux. It comes with built-in support for JavaScript, TypeScript, and Node.js and has a rich ecosystem of extensions for other languages (like Python) and runtimes.

1.  **Download:** Visit the [official VS Code website](https://code.visualstudio.com/) and download the installer for Windows.
2.  **Install:** Run the installer. It is recommended to accept the default settings, but make sure to check the "Add to PATH" option so you can open VS Code from the command line.

### Installing Git

Git is a version control system that helps you track changes in your code. It's an essential tool for collaboration and for managing different versions of your projects.

1.  **Download:** Visit the [official Git website](https://git-scm.com/downloads) and download the installer for Windows.
2.  **Install:** Run the installer. The default options are suitable for most users. This will also install Git Bash, a command-line tool for using Git.

### Installing Miniconda

Miniconda is a free minimal installer for conda, a package and environment manager. It's recommended over Anaconda for beginners as it's lightweight and installs only the essentials.

1.  **Download:** Visit the [Miniconda documentation](https://docs.conda.io/en/latest/miniconda.html) and download the installer for your operating system (Windows, macOS, or Linux).
2.  **Install:** Run the installer and follow the on-screen instructions. It's recommended to accept the default settings.

Alternatively, 
1. **Press windows key**
2. type *powershell*
3. in powershell copy and paste following after `>`
```bash
Invoke-WebRequest -Uri "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -outfile ".\miniconda.exe"
Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
del .\miniconda.exe
```

### Installing Scoop (For future reference)
1. **Press windows key**
2. type *powershell* and open it
3. in powershell copy and paste following `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` and then press Enter.
4. copy and paste following `Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression`