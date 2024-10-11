# Engagement Optimization Data Cleaning Script

import pandas as pd

# The dataset from Power BI will be passed as a DataFrame called 'dataset'
# Ensure you replace 'dataset' with the actual name of your dataset variable if different
dataset = pd.DataFrame(dataset)

# Step 1: Clean the dataset by removing rows with missing values
cleaned_data = dataset.dropna()

# Step 2: Grouping data by 'pageTitle' and summing up the 'sessions'
grouped_data = cleaned_data.groupby('pageTitle').agg({'sessions': 'sum'}).reset_index()

# Step 3: Result to be returned to Power BI
result = grouped_data

# You can print the result to see the cleaned data (optional)
print(result)
