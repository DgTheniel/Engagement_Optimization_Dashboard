# Engagement Optimization Dashboard

## Overview
The Engagement Optimization Dashboard is a data visualization project using Power BI to analyze user engagement data collected from Google Analytics. This project aims to provide insights into user behavior, including total users, active users, device category, new vs. returning users, and engagement rates.

## Key Features
- Visualizations for:
  - Total Users
  - Active Users
  - Operating System
  - Sum of Event Count
  - Device Category
  - New vs. Returning Users
  - Engagement Rate
- Real-time data sourced from Google Analytics
- Data manipulation and analysis using Python and DAX
- Interactive dashboard built with Power BI

## Technologies Used
- **Google Analytics**: Data source for user engagement metrics.
- **Power BI**: Visualization tool for creating interactive dashboards.
- **Python**: Data manipulation and analysis using Pandas.
- **DAX**: Data Analysis Expressions for creating measures in Power BI.

## Datasets
The dataset is imported in real-time from Google Analytics and consists of user engagement metrics, including:
- Session duration
- Bounce rate
- Page title
- User demographics

## Python Setup Instructions

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Open your command prompt or terminal.

3. Install the required libraries by running the following command:
   ```bash
   pip install pandas matplotlib


## Python Scripts
The following Python scripts are used for data cleaning and manipulation:
```python
import pandas as pd

# The dataset from Power BI will be passed as a DataFrame called 'dataset'
dataset = pd.DataFrame(dataset)

# Clean the dataset by removing rows with missing values
cleaned_data = dataset.dropna()

# Grouping data by a specific column, e.g., 'pageTitle'
grouped_data = cleaned_data.groupby('pageTitle').agg({'sessions': 'sum'}).reset_index()

# Result to be returned to Power BI
result = grouped_data
