import pandas as pd

# Scenario 1: COVID-19 Dataset
# Assuming the file is named 'covid_data.csv'
df_covid = pd.read_csv('covid_data.csv')

print("--- First 5 Records ---")
print(df_covid.head())

print("\n--- Key Statistics ---")
print(df_covid.describe())


# Scenario 2: Employee Data
import pandas as pd

# 1. Load the dataset
df = pd.read_csv('employee_data.csv')

# 2. Display first five records (Requirement from your notes)
print("--- First 5 Employees ---")
print(df.head())

# 3. Summarize key statistics (Requirement from your notes)
# This will give you the Mean, Std Dev, Min, and Max for Salary and Experience
print("\n--- Statistical Summary ---")
print(df.describe())

# 4. Check data structure (info() function from your notes)
print("\n--- Data Structure Info ---")
df.info()