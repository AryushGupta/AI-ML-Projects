# Data Cleaning — Data Science Notes

These notes explain **what data cleaning is, where it fits in a data-science workflow, why it matters, and how to think about a dataset before changing it**.

The goal is not just to learn pandas functions such as `dropna()` or `drop_duplicates()`. The more important skill is learning **why a data-quality problem exists and what the correct action should be**.

---

## 1. What is Data Cleaning?

**Data cleaning** is the process of identifying, investigating, and handling errors, inconsistencies, missing information, invalid values, duplicates, and other data-quality problems in a dataset so that the data becomes suitable for its intended use.

A raw dataset may contain problems such as:

- Missing values
- Duplicate records
- Wrong or inconsistent data types
- Spelling/category inconsistencies
- Invalid values
- Impossible values
- Inconsistent units
- Incorrect dates
- Outliers
- Irrelevant columns or records
- Broken relationships between tables
- Data-entry or collection errors

A simple way to think about it:

```text
Raw data
   ↓
Understand the data
   ↓
Find data-quality problems
   ↓
Investigate why they exist
   ↓
Decide how to handle them
   ↓
Validate the result
   ↓
Clean / analysis-ready data
```

### Important idea

**Cleaning does not mean "change everything that looks unusual."**

A value can be unusual and still be correct.

For example:

```text
Age = 97
```

This may be:

- A genuine observation
- A data-entry error
- An incorrectly interpreted field

The correct question is therefore:

> **"Why is this value unusual, and is it valid for the context of this dataset?"**

---

# 2. Where Does Data Cleaning Fit in Data Science?

A simplified data-science workflow is:

```text
                    DATA SCIENCE WORKFLOW

    Problem Definition
            ↓
       Data Collection
            ↓
       Data Understanding
            ↓
      Data Profiling
            ↓
       Data Cleaning
            ↓
    Data Transformation
            ↓
 Exploratory Data Analysis
            ↓
 Feature Engineering
            ↓
   Modeling / Statistical Analysis
            ↓
       Evaluation
            ↓
      Communication
```

This looks linear, but real projects are usually **iterative**:

```text
          ┌───────────────────────┐
          ↓                       │
Data → Cleaning → EDA → Modeling → Evaluation
          ↑                       │
          └────── New problems ───┘
```

For example, while performing EDA you may discover that:

- one category has several spellings,
- a column was interpreted using the wrong unit,
- a date field has impossible values,
- a supposed ID is not actually unique.

You may then return to the cleaning stage.

### Cleaning vs preprocessing

These terms are sometimes used differently across projects.

A useful distinction for learning is:

**Data cleaning**
- Fixing or handling data-quality problems

**Data preprocessing**
- A broader stage that can include cleaning, transformation, encoding, scaling, splitting, and other preparation needed for analysis or machine learning

Therefore:

```text
Data preprocessing
│
├── Data cleaning
│   ├── Missing values
│   ├── Duplicates
│   ├── Invalid values
│   └── Inconsistencies
│
├── Transformation
│   ├── Scaling
│   ├── Encoding
│   └── Type conversion
│
└── Other preparation
    ├── Train/test split
    └── Feature preparation
```

---

# 3. Why Do We Need Data Cleaning?

Because **analysis and models depend on the data they receive**.

If the underlying data is wrong, the final result can also be wrong.

A useful principle is:

> **Bad input can produce bad analysis, regardless of how sophisticated the model is.**

For example, suppose a sales dataset contains the same transaction twice.

Original:

```text
Transaction_ID    Revenue
101               500
102               700
102               700
103               900
```

If the duplicate is actually an accidental duplicate, then calculating total revenue gives:

```text
500 + 700 + 700 + 900 = 2800
```

The actual total should be:

```text
500 + 700 + 900 = 2100
```

The model or dashboard may perform the calculation perfectly.

The **problem happened before the calculation**.

---

# 4. Why Is Data Cleaning Important?

Good data cleaning helps with:

### 4.1 Reliable analysis

Statistics, correlations, trends, and visualizations depend on the quality of the underlying data.

### 4.2 Better decision-making

Business or scientific decisions based on incorrect data can be misleading.

### 4.3 Better machine-learning results

Models learn patterns from the training data. Incorrect, inconsistent, or biased data can therefore affect predictions and generalization.

### 4.4 Consistency

The same concept should normally be represented consistently.

For example:

```text
India
india
IND
IN
```

may refer to the same category, depending on the dataset's definition.

### 4.5 Reproducibility

A documented cleaning process makes it possible to understand how the original data became the final dataset.

### 4.6 Trust

A dataset should not simply be declared "clean." The cleaning decisions and validation checks should be understandable and defensible.

---

# 5. Data Quality: What Does "Good Data" Mean?

Before cleaning, it helps to think about **data quality dimensions**.

Common dimensions include:

| Dimension | Question |
|---|---|
| Accuracy | Does the value represent reality correctly? |
| Completeness | Are required values present? |
| Consistency | Are values represented in a consistent way? |
| Validity | Does the value follow the expected rules or format? |
| Uniqueness | Are records duplicated when they should not be? |
| Timeliness | Is the data sufficiently current for the intended task? |
| Relevance | Does the data actually matter for the problem? |

These dimensions are useful because "clean" is not one single property.

A dataset can have:

```text
No duplicates ✅
But wrong units ❌
```

or:

```text
Correct formats ✅
But many missing values ❌
```

Therefore, cleaning is really about **data quality relative to the purpose of the analysis**.

---

# 6. The Most Important Questions to Ask BEFORE Cleaning

Do not immediately start deleting rows or filling missing values.

First understand the dataset.

## A. Questions about the problem

### 1. What problem am I trying to solve?

Examples:

```text
Predict customer churn
Analyze sales performance
Estimate house prices
Study semiconductor properties
Detect fraudulent transactions
```

The intended use determines what matters during cleaning.

### 2. What does one row represent?

This is one of the most important questions.

For example, does one row represent:

```text
one customer?
one transaction?
one product?
one experiment?
one measurement?
one day?
```

This is sometimes called the **grain** or **unit of observation**.

If you misunderstand the row meaning, you can make incorrect cleaning decisions.

---

## B. Questions about the data source

### 3. Where did the data come from?

For example:

- Database
- CSV export
- API
- Survey
- Sensor
- Web scraping
- Manual data entry
- Multiple sources

### 4. How was the data collected?

Understanding collection helps explain why errors may exist.

For example:

```text
Manual entry → spelling errors
Sensor → measurement noise
Web scraping → missing/incorrect fields
Database joins → duplicated or mismatched records
Survey → self-selection or response bias
```

### 5. Has the data already been modified?

Find out whether someone already:

- Removed rows
- Imputed values
- Renamed categories
- Converted units
- Merged datasets
- Filtered records

---

# 7. Questions About the Structure

### 6. What does every column mean?

Do not rely only on the column name.

For example:

```text
temperature
```

could mean:

```text
°C
°F
Kelvin
```

The meaning, unit, and source of a feature matter.

### 7. What data type should each column have?

Examples:

```text
Age              → integer
Price            → numeric
Date             → datetime
Country          → categorical/text
Transaction_ID   → identifier
```

### 8. Which columns are identifiers?

Ask:

```text
Is this ID supposed to be unique?
Can it legitimately repeat?
Is it actually an identifier or merely a label?
```

An ID looking duplicated does not automatically mean the entire row is duplicated.

For example:

```text
Product_ID   Category
P001         Electronics
P001         Accessories
```

This may be:

- A true data problem
- A product hierarchy
- A many-to-many relationship
- A misunderstanding of what `Product_ID` means

Investigate before deleting anything.

---

# 8. Questions About Missing Values

For every important column, ask:

### 9. How much data is missing?

Consider:

```text
Number of missing values
Percentage missing
Rows affected
Columns affected
```

### 10. Why is the value missing?

Possible reasons:

```text
Not collected
Not applicable
Unknown
System failure
User skipped the field
Measurement failed
Data lost during merging
```

The reason for missingness can determine the correct treatment.

### 11. Should I remove, keep, or impute the missing value?

Possible choices include:

```text
Keep as missing
Drop rows
Drop columns
Fill using a rule
Statistical imputation
Model-based imputation
Create a "missing" category
```

There is no universal "best" method.

---

# 9. Questions About Duplicates

### 12. What exactly is duplicated?

Check whether the duplicate is:

```text
Duplicate entire row
Duplicate ID
Duplicate combination of columns
Duplicate observation caused by a join
Repeated legitimate measurement
```

For example:

```text
Customer_ID = 1001
```

appearing twice does not necessarily mean the row is duplicated.

A customer can legitimately have multiple transactions.

So ask:

> **What should be unique according to the data's real-world structure?**

---

# 10. Questions About Invalid Values

### 13. What values are logically impossible?

Examples:

```text
Age = -5
Quantity = -20
Temperature = -400 °C
Percentage = 250%
```

But do not assume every extreme value is invalid.

### 14. What are the valid ranges?

Define rules based on domain knowledge.

For example:

```text
Percentage → 0 to 100
Quantity   → >= 0
Rating     → 1 to 5
```

These rules depend on the specific dataset.

---

# 11. Questions About Categories and Text

### 15. Are categories represented consistently?

Example:

```text
Male
male
M
MALE
```

### 16. Are there spelling or whitespace problems?

Example:

```text
"Delhi"
" Delhi"
"Delhi "
"delhi"
```

### 17. Are categories actually different?

Do not automatically combine categories just because they look similar.

For example:

```text
Product A
Product-A
Product A (2025)
```

may or may not represent the same thing.

You need contextual knowledge.

---

# 12. Questions About Dates and Time

### 18. What time zone is being used?

### 19. What date format is expected?

For example:

```text
01/02/2026
```

could mean:

```text
1 February 2026
```

or:

```text
January 2, 2026
```

depending on the convention.

### 20. Are the dates logically possible?

Check for:

```text
Future dates
Impossible dates
End date before start date
Unexpected gaps
Duplicate timestamps
Wrong time zones
```

---

# 13. Questions About Outliers

### 21. Is the outlier an error or a real observation?

Example:

```text
Salary = 50,000
Salary = 55,000
Salary = 52,000
Salary = 4,000,000
```

The last value may be:

```text
An incorrect entry
A genuinely high salary
A different unit
A special case
```

### Important rule

**Outlier ≠ error**

Do not remove an observation simply because it is statistically unusual.

---

# 14. Questions About Relationships Between Columns

Sometimes a value is valid by itself but inconsistent with another column.

Example:

```text
Quantity = 10
Unit_Price = 100
Total_Price = 50
```

Individually, these values may all look valid.

Together, they may violate:

```text
Total_Price = Quantity × Unit_Price
```

Therefore ask:

> **What relationships or business rules should hold between columns?**

---

# 15. Questions About Multiple Tables

When working with multiple datasets or tables, ask:

```text
What is the primary key?
What is the foreign key?
Are the keys unique?
Do both tables use the same definitions?
Will the join create duplicate rows?
Are there unmatched records?
Are units and categories consistent?
```

This is especially important before using:

```text
merge()
join()
concat()
```

A technically successful join can still produce incorrect data.

---

# 16. Questions About Machine Learning

When the data will be used for ML, ask:

### Does any feature contain information from the future?

This can cause **data leakage**.

Example:

```text
Goal:
Predict whether a customer will churn.

Feature:
"Cancellation_Date"
```

If the cancellation date is only known after the outcome happens, using it as an input feature can leak future information into the model.

### Are train and test data being contaminated?

Cleaning and preprocessing decisions should be made carefully so information from the test set does not improperly influence the training process.

### Is the dataset representative?

A technically clean dataset can still be:

- Biased
- Unrepresentative
- Poorly sampled
- Missing important populations

**Cleaning cannot fix every data problem.**

Some problems are problems of **data collection, sampling, measurement, or experimental design**.

---

# 17. A Practical Data-Cleaning Workflow

A useful workflow for a beginner is:

```text
1. Understand the objective
        ↓
2. Understand the dataset
        ↓
3. Inspect structure
        ↓
4. Profile the data
        ↓
5. Identify quality problems
        ↓
6. Investigate the cause
        ↓
7. Decide what should happen
        ↓
8. Apply the cleaning operation
        ↓
9. Validate the result
        ↓
10. Document the changes
```

### Step 1 — Understand

Know:

```text
Why does this dataset exist?
What does one row represent?
What does each column mean?
What is the expected output?
```

### Step 2 — Profile

Inspect:

```text
Shape
Columns
Data types
Missing values
Unique values
Duplicates
Ranges
Basic statistics
```

### Step 3 — Identify

Look for:

```text
Missing values
Duplicates
Invalid values
Inconsistent categories
Wrong types
Outliers
Impossible relationships
Unexpected patterns
```

### Step 4 — Investigate

Ask:

> Why is this problem present?

This is where domain knowledge becomes important.

### Step 5 — Decide

Possible actions:

```text
Keep
Remove
Correct
Standardize
Impute
Transform
Flag
Request better source data
```

### Step 6 — Validate

After cleaning, ask:

```text
Did the expected problem actually disappear?
Did I accidentally remove useful information?
Did the row count change as expected?
Are important relationships still valid?
Are data types correct?
Are business/domain rules satisfied?
```

### Step 7 — Document

Record:

```text
What was wrong?
What did I change?
Why did I change it?
How many records were affected?
What assumptions did I make?
```

---

# 18. Data Profiling Before Data Cleaning

A strong habit is:

> **Profile first, clean second.**

For a pandas DataFrame, an initial inspection might include:

```python
df.shape
df.head()
df.info()
df.describe()
df.isna().sum()
df.nunique()
df.duplicated().sum()
```

These operations do not "clean" the data.

They help you **understand what you have**.

---

# 19. Common Data-Cleaning Problems

| Problem | Example | Possible response |
|---|---|---|
| Missing value | `Age = NaN` | Investigate and choose treatment |
| Duplicate row | Entire row repeated | Deduplicate if genuinely redundant |
| Duplicate ID | Same ID appears twice | Investigate the meaning of the ID |
| Wrong type | `"25"` stored as text | Convert if appropriate |
| Invalid value | `Age = -10` | Investigate and correct/remove/flag |
| Inconsistent category | `India`, `india`, `IND` | Standardize if they mean the same thing |
| Whitespace | `" Delhi "` | Normalize if appropriate |
| Wrong unit | kg mixed with lb | Convert to one agreed unit |
| Impossible date | `31/02/2026` | Correct or handle as invalid |
| Outlier | Extremely large value | Investigate; don't automatically delete |
| Broken relationship | `total != quantity × price` | Investigate source/business rule |
| Irrelevant feature | Unrelated column | Remove only when justified |

---

# 20. Data Cleaning Is a Decision-Making Process

One of the most important lessons is:

```text
Finding a problem
        ≠
Knowing the solution
```

For example:

```text
Missing values detected
        ↓
Should I delete the row?
        ↓
Not necessarily
        ↓
Why is it missing?
        ↓
How important is the feature?
        ↓
How much data is missing?
        ↓
Does missingness itself carry information?
        ↓
Choose an appropriate treatment
```

Similarly:

```text
Duplicate ID detected
        ↓
Delete duplicate?
        ↓
Not necessarily
        ↓
Understand the row grain
        ↓
Determine what should be unique
        ↓
Check related columns
        ↓
Decide
```

This is why **data cleaning is not just a collection of pandas commands**.

It is a reasoning process.

---

# 21. A Good Mental Model

When you encounter a suspicious value, use this sequence:

```text
OBSERVE
   ↓
What looks unusual?

UNDERSTAND
   ↓
What does this column/row mean?

INVESTIGATE
   ↓
Why might this have happened?

DEFINE
   ↓
What should the valid data look like?

DECIDE
   ↓
Keep / correct / remove / impute / flag

VALIDATE
   ↓
Did the decision improve data quality?

DOCUMENT
   ↓
Can another person understand what I did?
```

---

# 22. Data Cleaning Checklist

Before declaring a dataset ready, check:

### Structure

- [ ] Do I understand what each row represents?
- [ ] Do I understand every important column?
- [ ] Are data types appropriate?
- [ ] Are units known and consistent?

### Missing data

- [ ] Which columns contain missing values?
- [ ] What percentage is missing?
- [ ] Why is the data missing?
- [ ] Is the chosen treatment justified?

### Duplicates

- [ ] Are there duplicate rows?
- [ ] Which fields are expected to be unique?
- [ ] Are duplicate IDs actually errors?

### Validity

- [ ] Are values within valid ranges?
- [ ] Are categories valid?
- [ ] Are dates valid?
- [ ] Are relationships between columns correct?

### Consistency

- [ ] Are names/categories standardized where appropriate?
- [ ] Are units consistent?
- [ ] Are date/time conventions consistent?

### Outliers

- [ ] Which observations are unusual?
- [ ] Are they errors or genuine observations?
- [ ] Is removing them justified?

### ML considerations

- [ ] Is there data leakage?
- [ ] Is the dataset representative?
- [ ] Could cleaning decisions introduce bias?
- [ ] Are train/test transformations handled correctly?

### Reproducibility

- [ ] Did I document the cleaning decisions?
- [ ] Did I preserve the original raw data?
- [ ] Can I reproduce the cleaned dataset?

---

# 23. Suggested Repository Structure

For a learning repository, you can organize the notes like this:

```text
data-cleaning/
│
├── README.md
│
├── notes/
│   ├── 01_introduction.md
│   ├── 02_data_profiling.md
│   ├── 03_missing_values.md
│   ├── 04_duplicates.md
│   ├── 05_data_types.md
│   ├── 06_inconsistent_values.md
│   ├── 07_outliers.md
│   ├── 08_validation.md
│   └── 09_data_cleaning_checklist.md
│
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_missing_values.ipynb
│   └── 03_duplicates.ipynb
│
└── datasets/
    └── README.md
```

The important point is that the repository does not need to be a large project.

It can be a **knowledge repository showing what you are learning and how you reason about data quality**.

---

# 24. Recommended Tools

For Python-based data science:

```text
Python
  │
  ├── pandas
  │     └── tabular data manipulation/cleaning
  │
  ├── NumPy
  │     └── numerical operations
  │
  ├── matplotlib
  │     └── visual inspection
  │
  └── scikit-learn
        └── preprocessing and ML workflows
```

You do not need every tool to begin learning data cleaning.

Start with:

1. Python fundamentals
2. pandas
3. NumPy basics
4. Basic statistics
5. Visualization
6. Domain understanding

---

# 25. Resources

## pandas

### User Guide

https://pandas.pydata.org/docs/user_guide/

A broad reference for pandas, including data structures, missing data, categoricals, merging, reshaping, time series, and more.

### Working with Missing Data

https://pandas.pydata.org/docs/user_guide/missing_data.html

Useful for learning how pandas represents and handles missing values.

### Duplicate Labels

https://pandas.pydata.org/docs/user_guide/duplicates.html

Useful for understanding duplicate row/column labels and why duplicates can affect downstream operations.

---

## Scikit-learn

### Preprocessing

https://scikit-learn.org/stable/modules/preprocessing.html

Useful for understanding preprocessing operations used before machine-learning models.

### Imputation of Missing Values

https://scikit-learn.org/stable/modules/impute.html

Useful when moving from basic data cleaning into ML-oriented missing-value handling.

---

## Google

### Data Quality and Interpretation — ML Universal Guides

https://developers.google.com/machine-learning/guides/data-traps/quality

A useful explanation of how poor data quality, sampling problems, missing values, incorrect units, and other "dirt" in data can affect analysis and machine-learning results.

---

## IBM

### What Is Data Cleaning?

https://www.ibm.com/think/topics/data-cleaning

Good introductory material covering data-quality problems, cleaning techniques, validation, missing values, duplicates, standardization, and the role of cleaning in analytics and ML.

### What Is Data Quality Management?

https://www.ibm.com/think/topics/data-quality-management

Useful for understanding data profiling, cleansing, validation, monitoring, and broader data-quality management.

---

# 26. What to Learn Next

After understanding this introduction, study data cleaning in this order:

```text
1. Data profiling
       ↓
2. Missing values
       ↓
3. Duplicate records
       ↓
4. Data types
       ↓
5. String/category inconsistencies
       ↓
6. Date and time cleaning
       ↓
7. Invalid values and validation rules
       ↓
8. Outliers
       ↓
9. Multiple tables and joins
       ↓
10. Data leakage and ML preprocessing
       ↓
11. Data validation and documentation
```

---

# 27. Final Perspective

The objective of data cleaning is **not to make a dataset look perfect**.

The objective is to make the data:

- Appropriate for its intended purpose
- Consistent with known rules
- Understandable
- Defensible
- Reproducible
- Reliable enough for the analysis or model being built

The most valuable habit is to move from:

```text
"What pandas function should I use?"
```

to:

```text
"What is wrong with this data?
Why is it wrong?
What should the value actually mean?
What is the least harmful and most defensible way to handle it?
How can I verify that my decision was correct?"
```

That change in thinking is what turns **data manipulation into data cleaning**.
