# Data Analysis — Data Science Notes

These notes explain **what data analysis is, where it fits into the data-science workflow, why it matters, what questions an analyst or data scientist should ask, and how to move from raw data to useful conclusions**.

The goal is not just to learn pandas functions or make charts. The more important skill is learning to answer:

> **What question am I trying to answer, what evidence does the data contain, and what can I reasonably conclude from it?**

---

# 1. What is Data Analysis?

**Data analysis** is the process of examining, transforming, summarizing, comparing, and interpreting data to answer questions, identify patterns, evaluate assumptions, and support decisions.

A simple way to think about it is:

```text
Question
   ↓
Collect / obtain relevant data
   ↓
Understand the data
   ↓
Clean and prepare the data
   ↓
Explore the data
   ↓
Analyze patterns and relationships
   ↓
Interpret the results
   ↓
Communicate findings
   ↓
Decision / next action
```

For example, suppose an e-commerce company wants to know:

> "Why did sales decrease this month?"

Data analysis could involve:

```text
Sales by month
        ↓
Sales by product category
        ↓
Sales by region
        ↓
Number of orders
        ↓
Average order value
        ↓
Discounts
        ↓
Customer activity
        ↓
Identify the major changes
        ↓
Investigate possible reasons
```

The final goal is not simply to produce a graph. The goal is to **extract useful information from the data and connect it to the original question**.

---

# 2. Data Analysis vs Data Science

Data analysis is an important part of data science, but the two are not identical.

```text
                    DATA SCIENCE
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
   Data Collection   Data Analysis    Machine Learning
        │                │                 │
        │                ├── EDA          ├── Prediction
        │                ├── Statistics   ├── Classification
        │                ├── Visualization ├── Regression
        │                └── Insights     └── Optimization
        │
        └──────── Data Preparation
                 ├── Cleaning
                 ├── Transformation
                 └── Integration
```

Data analysts commonly focus on answering practical questions from existing data. Data scientists may perform those same analysis tasks and additionally work on statistical modeling, machine learning, experimentation, prediction, and more advanced data products.

The boundaries are not rigid, and organizations often use the terms differently.

---

# 3. Where Does Data Analysis Fit in the Data Science Workflow?

A simplified workflow is:

```text
Problem Definition
        ↓
Data Collection
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Exploratory Data Analysis (EDA)
        ↓
Statistical Analysis / Modeling
        ↓
Evaluation
        ↓
Communication
        ↓
Decision / Deployment
```

But real projects are rarely completely linear.

```text
                    ┌────────────────────┐
                    │  Problem / Question│
                    └─────────┬──────────┘
                              ↓
                       Collect Data
                              ↓
                     Clean / Prepare
                              ↓
                           Analyze
                              ↓
                      Find Something
                         Unexpected
                              │
                              ↓
                       Investigate
                              │
                              └──────────────┐
                                             ↓
                                      Revisit Data
```

For example, analysis may reveal a category recorded inconsistently, an incomplete time period, an unexpected distribution, or a relationship that disappears after accounting for another variable.

**Data analysis is iterative.**

---

# 4. Why Do We Need Data Analysis?

Raw data by itself does not automatically provide understanding.

```text
Revenue
50000
62000
47000
71000
...
```

These numbers tell you something, but not necessarily enough.

Analysis can turn them into questions such as:

```text
How is revenue changing over time?
Which products generate the most revenue?
Which regions are growing?
What is the average order value?
Are discounts associated with lower or higher revenue?
Are there seasonal patterns?
```

So:

```text
Raw Data
   ↓
Information
   ↓
Patterns
   ↓
Insights
   ↓
Decision
```

That transformation is one of the main purposes of data analysis.

---

# 5. Why Is Data Analysis Important?

## 5.1 It helps answer specific questions

Good analysis begins with a question rather than a random collection of charts.

```text
Bad starting point:
"Let me plot everything."

Better starting point:
"Which product categories contributed most to the decline in revenue?"
```

## 5.2 It helps discover patterns

Analysis can reveal trends, seasonality, relationships, differences between groups, concentrations, changes over time, and unusual observations.

## 5.3 It helps challenge assumptions

Data analysis provides a way to test assumptions against evidence instead of relying only on intuition.

## 5.4 It supports decision-making

A good analysis connects evidence to a practical next step.

## 5.5 It provides the foundation for later modeling

Before building a machine-learning model, you should understand what variables exist, their distributions, plausible relationships, anomalies, potential leakage, and whether the data represents the real problem.

---

# 6. What Is the Difference Between Data Analysis and Data Cleaning?

These stages are related but have different purposes.

### Data cleaning asks:

> **"Is the data suitable and internally consistent?"**

### Data analysis asks:

> **"What does the data tell us?"**

```text
Dataset
   ↓
Cleaning
   ↓
Missing values?
Duplicates?
Wrong types?
Invalid values?
Inconsistent categories?
   ↓
Prepared Dataset
   ↓
Analysis
   ↓
Trends?
Patterns?
Differences?
Relationships?
Changes?
Insights?
```

Data cleaning is often a **foundation for analysis**.

---

# 7. What Is Exploratory Data Analysis (EDA)?

**Exploratory Data Analysis (EDA)** is the systematic exploration of a dataset to understand its structure, distributions, patterns, relationships, and unusual observations.

EDA commonly uses:

```text
Statistics
+
Tables
+
Aggregations
+
Visualizations
+
Domain knowledge
```

Typical EDA questions include:

```text
What are the distributions of important variables?
Which categories are most common?
Are there extreme observations?
How do variables differ between groups?
Are variables related?
How do values change over time?
```

EDA is often used before formal modeling or hypothesis testing because it helps reveal what the data actually looks like and whether your assumptions are reasonable.

---

# 8. Data Analysis Has Different Levels

A useful framework is:

```text
Descriptive
    ↓
What happened?

Diagnostic
    ↓
Why might it have happened?

Predictive
    ↓
What might happen?

Prescriptive
    ↓
What should we do?
```

These categories can overlap in real projects.

## 8.1 Descriptive Analysis

Answers: **What happened?**

Examples:

```text
Total sales this year
Average customer age
Number of orders
Revenue by category
Monthly sales
```

Typical tools include sum, mean, median, count, percentage, minimum/maximum, grouping, and aggregation.

## 8.2 Diagnostic Analysis

Answers: **Why might it have happened?**

Example:

```text
Sales decreased
      ↓
Which category changed?
      ↓
Which region changed?
      ↓
Did order volume fall?
      ↓
Did average order value fall?
      ↓
Did discounts change?
```

## 8.3 Predictive Analysis

Answers: **What might happen?**

Examples include expected sales, churn probability, demand forecasts, and predicted prices. Predictive analysis often involves statistical models and/or machine learning.

## 8.4 Prescriptive Analysis

Answers: **What action should we consider?**

Examples include recommended inventory levels, customer targeting, or selecting a production setting. Prescriptive analysis may involve optimization, simulation, causal reasoning, or predictive models.

---

# 9. Questions to Ask BEFORE Analysis

Do not immediately start plotting columns. First understand the analytical problem.

## A. Questions About the Objective

### 1. What problem am I trying to solve?

Examples:

```text
Why are sales declining?
Which customers are most valuable?
Which product category is growing?
Does a new feature improve retention?
What factors are associated with defects?
```

### 2. What exactly is the question?

Convert a broad problem into a measurable question.

```text
Broad:
"Understand sales."

Better:
"Which product categories caused the change in monthly revenue?"
```

### 3. What decision will this analysis support?

Ask:

> **Who will use the result, and what could they do differently because of it?**

---

# 10. Questions About the Unit of Analysis

### 4. What does one row represent?

One row could represent a:

```text
Customer
Transaction
Product
Order item
Experiment
Sensor measurement
Day
Website session
```

Always understand the **grain** of the dataset. A customer-level analysis and a transaction-level analysis can produce very different results.

---

# 11. Questions About the Variables

### 5. What does each important column mean?

Do not assume meaning from the column name alone.

For example, `Revenue` could mean gross revenue, net revenue, revenue after discounts, or revenue before tax.

### 6. What are the units?

```text
Temperature → °C / °F / K
Weight      → kg / lb
Distance    → km / miles
Currency    → USD / INR / EUR
```

### 7. Which variables are categorical, numerical, dates, identifiers, or text?

Variable types affect the appropriate analytical method.

---

# 12. Questions About the Target or Outcome

### 8. What exactly am I measuring?

Examples:

```text
Sales
Profit
Conversion rate
Customer retention
Defect rate
Response time
```

### 9. How is the metric calculated?

For example:

```text
Profit = Revenue - Cost
```

or:

```text
Conversion Rate = conversions / visitors
```

### 10. Are there multiple ways to calculate the same metric?

For example, these can represent different concepts:

```text
Total revenue / total orders

vs.

Mean of individual order values
```

Know what the metric is actually measuring.

---

# 13. Questions About Time

### 11. What time period does the data cover?

### 12. Is the data continuous?

Check for missing days, months, measurement gaps, or changes in collection frequency.

### 13. Is time affecting the result?

Look for:

```text
Trend
Seasonality
Cyclic behavior
Events
Policy changes
Product launches
```

Ignoring time can produce misleading conclusions.

---

# 14. Questions About Groups

### 14. Are there important groups in the data?

Examples:

```text
Region
Product category
Customer segment
Age group
Device type
Machine
Experiment condition
```

### 15. Are averages hiding differences between groups?

Suppose:

```text
Overall average = 70

Group A = 90
Group B = 50
```

The overall average hides an important difference.

Therefore ask:

> **"What happens when I break the data into meaningful groups?"**

---

# 15. Questions About Relationships

### 16. Which variables might be related?

Examples:

```text
Advertising spend ↔ Sales
Temperature ↔ Defect rate
Price ↔ Demand
Study time ↔ Score
```

But remember:

> **Association does not automatically mean causation.**

A relationship may be explained by a third variable, reverse causality, selection effects, or coincidence.

---

# 16. Questions About Comparison

A large part of data analysis is comparison.

Ask:

```text
Compared with what?
```

Examples:

```text
This month vs last month
2026 vs 2025
Region A vs Region B
Before vs after
Treatment vs control
Product A vs Product B
```

A number is often more meaningful when there is an appropriate baseline.

---

# 17. Questions About Statistical Distributions

For important numerical variables, ask:

```text
What is the center?
What is the spread?
Is the distribution symmetric?
Is it skewed?
Are there multiple peaks?
Are there extreme values?
```

Useful concepts include:

```text
Mean
Median
Mode
Range
Variance
Standard deviation
Quartiles
Percentiles
IQR
```

Do not assume that the mean alone describes a distribution adequately.

---

# 18. Questions About Correlation

Correlation can be useful for exploring numerical relationships.

```text
             Sales  Price  Discount
Sales          1.0   -0.2      0.4
Price         -0.2    1.0     -0.1
Discount       0.4   -0.1      1.0
```

Correlation can help identify variables worth investigating, but:

```text
Correlation
     ≠
Causation
```

Treat correlation as a starting point for investigation, not as proof of a causal relationship.

---

# 19. Questions About Missing and Dirty Data

Before trusting a result, ask:

```text
Are important values missing?
Were duplicates handled?
Are categories consistent?
Are units consistent?
Are there invalid values?
```

A surprising result may actually come from a data-quality problem.

---

# 20. Questions About Bias

A dataset can be clean but still biased.

Ask:

```text
Does the dataset represent the population?
Are some groups underrepresented?
Was the data collected under special conditions?
Could the collection process affect the result?
Did I select observations in a way that favors my hypothesis?
```

**Clean data can still produce misleading conclusions if the sampling or measurement process is biased.**

---

# 21. Questions About Statistical Significance

When comparing groups or testing hypotheses, ask:

```text
Is the observed difference large enough to matter?
Could it have occurred by chance?
How uncertain is the estimate?
What statistical assumptions are being made?
```

Depending on the problem, you may use:

- Confidence intervals
- Hypothesis tests
- t-tests
- Chi-square tests
- ANOVA
- Non-parametric tests
- Regression
- Effect sizes

Statistical significance alone is not enough. Also consider **practical significance**.

---

# 22. Questions About Causality

Be careful with statements like:

```text
Discounts increased sales.
```

Your data may only show:

```text
Discounts and sales were positively associated.
```

Strong causal claims generally require stronger evidence such as randomized experiments or appropriate quasi-experimental designs.

Ask:

> **"Does my analysis show association, or do I have evidence for causation?"**

---

# 23. Questions About Outliers and Anomalies

Ask:

```text
Is this observation unusual?
Why is it unusual?
Is it an error?
Is it a real rare event?
Does it change the conclusion?
```

Do not automatically delete an unusual observation.

---

# 24. Questions About Visualization

Before creating a chart, ask:

> **What question should the chart answer?**

| Question | Useful visualization |
|---|---|
| How does something change over time? | Line chart |
| Which category is larger? | Bar chart |
| What is the distribution? | Histogram |
| Are there extreme values? | Box plot |
| Are two numerical variables related? | Scatter plot |
| How do distributions differ between groups? | Box/violin plot |
| How do several numerical variables relate? | Correlation heatmap |

Do not select a chart just because it looks attractive.

---

# 25. Questions About the Result

After finding a pattern, ask:

- Is the pattern real?
- Is it large enough to matter?
- Does it appear consistently?
- Could another variable explain it?
- Does it hold across groups?
- Does it hold across different time periods?
- Does domain knowledge support it?
- Could the collection process explain it?
- What alternative explanations exist?

This stage separates **observation** from **interpretation**.

---

# 26. Observation vs Insight vs Conclusion

These are not the same thing.

### Observation

```text
Revenue decreased by 15% in March.
```

### Insight

```text
The decline was concentrated in the electronics category.
```

### Possible explanation

```text
Electronics sales declined primarily in Region X.
```

### Conclusion

```text
The analysis suggests that the March revenue decline was strongly associated
with weaker electronics sales in Region X.
```

The wording should match the strength of the evidence.

---

# 27. A Practical Data-Analysis Workflow

```text
1. Define the question
        ↓
2. Understand the data
        ↓
3. Clean and validate
        ↓
4. Select relevant variables
        ↓
5. Explore distributions
        ↓
6. Segment / group the data
        ↓
7. Compare groups or time periods
        ↓
8. Investigate relationships
        ↓
9. Test important hypotheses
        ↓
10. Interpret findings
        ↓
11. Validate conclusions
        ↓
12. Communicate results
```

### Step 1 — Define

```text
What do I need to know?
Why do I need to know it?
Who needs the answer?
What decision will it support?
```

### Step 2 — Understand

Learn the rows, columns, data types, units, time range, data source, grain, and domain rules.

### Step 3 — Clean

Check missing values, duplicates, invalid values, inconsistent categories, wrong types, incorrect units, and unexpected observations.

### Step 4 — Explore

Start broad with distributions, counts, summary statistics, category frequencies, time trends, and basic relationships.

### Step 5 — Segment

Break data into meaningful groups such as region, category, or customer segment.

### Step 6 — Compare

Ask which groups or periods differ, how much they differ, and whether an appropriate baseline exists.

### Step 7 — Investigate relationships

Use correlation, cross-tabulation, group comparisons, regression, or statistical tests according to the question.

### Step 8 — Validate

Check whether the result makes sense, whether it is sensitive to unusual values, and whether alternative explanations are plausible.

### Step 9 — Communicate

A strong analysis should lead to:

```text
Question
   ↓
Evidence
   ↓
Finding
   ↓
Interpretation
   ↓
Implication
   ↓
Recommended next action
```

---

# 28. A Simple Example: E-Commerce Analysis

Suppose you have:

```text
Order_ID
Date
Product_Category
Unit_Cost
Unit_Price
Quantity
Region
Customer_ID
```

You are asked:

> "How is the business performing?"

Do not immediately create ten charts.

Start by defining useful metrics:

```text
Revenue = Unit_Price × Quantity

Cost = Unit_Cost × Quantity

Profit = Revenue - Cost
```

Then investigate:

```text
1. Total revenue
2. Total profit
3. Number of orders
4. Units sold
5. Average order value
6. Revenue by category
7. Profit by category
8. Revenue over time
9. Revenue by region
10. High/low performing products
```

Then ask deeper questions:

```text
Why is one category more profitable?
Are sales growing because of more orders or higher order value?
Which region drives the decline?
Are discounts or prices related to quantity sold?
Is one product responsible for unusual revenue?
```

This is analysis.

The individual pandas commands are only the tools used to perform it.

---

# 29. Descriptive Statistics You Should Know

For numerical data:

```text
Count
Mean
Median
Mode
Minimum
Maximum
Range
Variance
Standard deviation
Quartiles
Percentiles
IQR
```

For categorical data:

```text
Count
Unique values
Frequency
Percentage
Most common category
Cross-tabulation
```

For time-series data:

```text
Change over time
Growth rate
Moving average
Seasonality
Trend
```

You do not need to use every statistic on every dataset. The important question is:

> **Which summary helps answer the question?**

---

# 30. Aggregation Is a Core Skill

A large part of data analysis involves aggregation.

```text
Raw transactions
       ↓
Group by category
       ↓
Sum revenue
       ↓
Compare categories
```

Common operations:

```text
sum
mean
median
count
min
max
nunique
```

And combinations of:

```text
groupby
aggregation
pivot tables
cross-tabulation
```

These operations turn individual observations into interpretable summaries.

---

# 31. Data Visualization Is Part of Analysis

Visualization is not decoration.

It can help you:

- Detect patterns
- Compare groups
- Find outliers
- Understand distributions
- Explore relationships
- Communicate findings

A useful process is:

```text
Question
   ↓
Choose relevant variables
   ↓
Choose appropriate chart
   ↓
Inspect
   ↓
Interpret
```

---

# 32. Data Analysis Is Not Just Visualization

A common beginner misconception is:

```text
Data Analysis = Making Charts
```

A better picture is:

```text
Data Analysis
│
├── Question formulation
├── Data understanding
├── Data cleaning
├── Data transformation
├── Statistical summaries
├── Aggregation
├── Visualization
├── Relationship analysis
├── Statistical testing
├── Interpretation
└── Communication
```

A dashboard can show what happened. Analysis should help explain **what happened, how large it is, where it happened, what relationships may exist, and what the evidence supports**.

---

# 33. Common Mistakes in Data Analysis

## Mistake 1 — Starting with charts instead of questions

Better: start with the analytical question.

## Mistake 2 — Confusing correlation with causation

A relationship does not automatically establish a cause.

## Mistake 3 — Using averages without checking distributions

The mean can hide skewness, outliers, or multiple groups.

## Mistake 4 — Ignoring the unit of analysis

A customer-level analysis and a transaction-level analysis can produce different results.

## Mistake 5 — Ignoring time

Aggregating all years together can hide trends, seasonality, and structural changes.

## Mistake 6 — Searching for a desired answer

Good analysis should also consider evidence that contradicts the initial hypothesis.

## Mistake 7 — Overinterpreting a small difference

A numerical difference can be statistically detectable but practically unimportant.

## Mistake 8 — Treating every outlier as an error

An unusual observation may be exactly the phenomenon you need to understand.

## Mistake 9 — Ignoring missing data

Always know how much information is actually being used for a result.

## Mistake 10 — Producing numbers without interpretation

A number is a result; an explanation of what the number means in context is closer to an insight.

---

# 34. A Good Mental Model

```text
ASK
 ↓
What am I trying to know?

UNDERSTAND
 ↓
What does the data represent?

PREPARE
 ↓
Is the data suitable for this question?

EXPLORE
 ↓
What patterns and anomalies exist?

COMPARE
 ↓
How do groups / periods differ?

INVESTIGATE
 ↓
What might explain the pattern?

VALIDATE
 ↓
Is the finding robust and reasonable?

INTERPRET
 ↓
What does the evidence actually support?

COMMUNICATE
 ↓
What should another person take away?
```

---

# 35. Data Analysis Checklist

### Objective

- [ ] Is the analytical question clearly defined?
- [ ] Do I know why the question matters?
- [ ] Do I know who will use the result?

### Data understanding

- [ ] Do I know what one row represents?
- [ ] Do I understand the important columns?
- [ ] Are the units known?
- [ ] Do I understand the time period?
- [ ] Do I understand the data source?

### Data quality

- [ ] Were missing values investigated?
- [ ] Were duplicates investigated?
- [ ] Were invalid values checked?
- [ ] Were important data-quality issues handled appropriately?

### Exploration

- [ ] Did I inspect distributions?
- [ ] Did I examine important categories?
- [ ] Did I investigate outliers?
- [ ] Did I examine relevant relationships?
- [ ] Did I consider time where applicable?

### Comparison

- [ ] Did I compare against an appropriate baseline?
- [ ] Did I investigate important groups?
- [ ] Did I avoid hiding differences inside overall averages?

### Interpretation

- [ ] Did I distinguish observation from explanation?
- [ ] Did I avoid confusing correlation with causation?
- [ ] Did I consider alternative explanations?
- [ ] Did I consider bias and sampling?
- [ ] Is the finding practically meaningful?

### Communication

- [ ] Can I explain the main finding in simple language?
- [ ] Do the charts directly support the message?
- [ ] Did I include relevant numbers?
- [ ] Did I clearly state limitations?
- [ ] Is the next action or implication clear?

---

# 36. Recommended Tools

For Python-based data analysis:

```text
Python
  │
  ├── pandas
  │     ├── DataFrames
  │     ├── filtering
  │     ├── grouping
  │     ├── aggregation
  │     ├── merging
  │     └── transformation
  │
  ├── NumPy
  │     └── numerical computation
  │
  ├── Matplotlib
  │     └── general-purpose visualization
  │
  ├── Seaborn
  │     └── statistical visualization
  │
  ├── SciPy
  │     └── scientific and statistical methods
  │
  └── Plotly
        └── interactive visualization
```

Other important tools in real data-analysis workflows include:

```text
SQL
Excel
Power BI
Tableau
Jupyter
Git
```

For learning Python-based analysis, a good starting stack is:

```text
Python
+ pandas
+ NumPy
+ Matplotlib
+ Seaborn
+ Jupyter
```

---

# 37. Suggested Repository Structure

```text
data-analysis/
│
├── README.md
│
├── notes/
│   ├── 01_introduction.md
│   ├── 02_data_profiling.md
│   ├── 03_descriptive_statistics.md
│   ├── 04_grouping_and_aggregation.md
│   ├── 05_eda.md
│   ├── 06_visualization.md
│   ├── 07_relationships_and_correlation.md
│   ├── 08_statistical_analysis.md
│   ├── 09_time_series_analysis.md
│   └── 10_analysis_checklist.md
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_descriptive_analysis.ipynb
│   ├── 03_groupby_analysis.ipynb
│   └── 04_eda.ipynb
│
└── datasets/
    └── README.md
```

This is useful even when you are **studying rather than building a single project**. The repository becomes a record of your analytical thinking and experiments.

---

# 38. Recommended Learning Order

```text
1. Python fundamentals
        ↓
2. NumPy basics
        ↓
3. pandas fundamentals
        ↓
4. Data profiling
        ↓
5. Descriptive statistics
        ↓
6. Grouping and aggregation
        ↓
7. Data visualization
        ↓
8. Exploratory Data Analysis
        ↓
9. Correlation and relationships
        ↓
10. Probability and statistical inference
        ↓
11. Hypothesis testing
        ↓
12. Regression
        ↓
13. Time-series analysis
        ↓
14. Communicating findings
```

This order gives a natural progression from **understanding data → summarizing data → exploring data → explaining data**.

---

# 39. Resources

## pandas

### User Guide

https://pandas.pydata.org/docs/user_guide/

Covers DataFrames, viewing data, selection, missing data, grouping, merging, reshaping, time series, plotting, and importing/exporting data.

### 10 Minutes to pandas

https://pandas.pydata.org/docs/user_guide/10min.html

A useful starting point for learning fundamental pandas operations.

---

## Matplotlib

### Official Documentation

https://matplotlib.org/stable/contents.html

Covers figures, axes, plotting, labels, scales, subplots, and other visualization concepts.

### Quick Start Guide

https://matplotlib.org/stable/tutorials/introductory/quick_start.html

Useful for learning the fundamental structure of Matplotlib plots.

---

## Seaborn

### Official Documentation

https://seaborn.pydata.org/

Useful for statistical data visualization and exploring distributions and relationships.

---

## SciPy

### Official Documentation

https://docs.scipy.org/doc/scipy/

Useful for scientific computing and statistical methods.

### Statistics Tutorial

https://docs.scipy.org/doc/scipy/tutorial/stats.html

Useful when moving from descriptive analysis toward statistical inference and hypothesis testing.

---

## Plotly

### Python Graphing Library

https://plotly.com/python/

Useful for interactive charts and exploratory visualizations.

### Getting Started

https://plotly.com/python/getting-started/

Covers Plotly's Python workflow and chart types.

---

## IBM

### Data Science vs Data Analytics

https://www.ibm.com/think/topics/data-science-vs-data-analytics

Useful for understanding how data analytics relates to the broader data-science lifecycle.

### Exploratory Data Analysis

https://www.ibm.com/think/topics/exploratory-data-analysis

Useful for understanding EDA, visualization, pattern discovery, anomalies, and relationships between variables.

### Big Data Analytics

https://www.ibm.com/think/topics/big-data-analytics

Provides an overview of descriptive, diagnostic, predictive, and prescriptive analytics.

---

# 40. Final Perspective

The objective of data analysis is **not to generate as many statistics or charts as possible**.

The objective is to:

```text
Start with a meaningful question
        ↓
Understand the data
        ↓
Use appropriate analytical methods
        ↓
Find evidence
        ↓
Interpret the evidence carefully
        ↓
Communicate what the evidence supports
        ↓
Help someone make a better decision
```

The most valuable habit is to move from:

```text
"What pandas function should I use?"
```

to:

```text
"What question am I answering?

What does each observation represent?

Which evidence can answer the question?

What patterns are actually present?

What alternative explanations exist?

What can I conclude from the evidence?

What can I NOT conclude?

How should I communicate the result?"
```

That change in thinking is what turns **data manipulation into data analysis**.
