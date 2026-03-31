import pandas as pd
import numpy as np

# Creating the messy HR dataset
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 102], # Notice 102 is a duplicate
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Bob'],
    'Join_Date': ['15-01-2020', '22-03-2021', '05-11-2019', '10-07-2022', '18-09-2020', '22-03-2021'], # Stored as text strings
    'Performance_Score': [85, 92, np.nan, 78, 88, 92], # NaN means missing
    'Salary': [60000, 75000, 68000, np.nan, 82000, 75000] # NaN means missing
}

df = pd.DataFrame(data)

print("--- RAW DATA ---")
print(df)
print("\n")

# Calculate the mean (average) salary
mean_salary = df['Salary'].mean()

# Fill the missing (NaN) values in the Salary column with this mean
df['Salary'] = df['Salary'].fillna(mean_salary)

# Let's also fill the missing Performance_Score with the median score
median_score = df['Performance_Score'].median()
df['Performance_Score'] = df['Performance_Score'].fillna(median_score)

print("--- AFTER FILLING MISSING VALUES ---")
print(df)
print("\n")

# drop_duplicates() scans the dataframe and removes identical rows
df = df.drop_duplicates()

print("--- AFTER REMOVING DUPLICATES ---")
print(df)
print("\n")

# Convert the 'Join_Date' column from string to datetime objects
df['Join_Date'] = pd.to_datetime(df['Join_Date'], format='%d-%m-%Y')

# Let's also ensure Performance_Score is an integer (it might have turned into a float during the NaN fill)
df['Performance_Score'] = df['Performance_Score'].astype(int)

print("--- FINAL CLEANED & TRANSFORMED DATA ---")
print(df)
print("\nData Types:")
=======
import pandas as pd
import numpy as np

# Creating the messy HR dataset
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 102], # Notice 102 is a duplicate
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Bob'],
    'Join_Date': ['15-01-2020', '22-03-2021', '05-11-2019', '10-07-2022', '18-09-2020', '22-03-2021'], # Stored as text strings
    'Performance_Score': [85, 92, np.nan, 78, 88, 92], # NaN means missing
    'Salary': [60000, 75000, 68000, np.nan, 82000, 75000] # NaN means missing
}

df = pd.DataFrame(data)

print("--- RAW DATA ---")
print(df)
print("\n")

# Calculate the mean (average) salary
mean_salary = df['Salary'].mean()

# Fill the missing (NaN) values in the Salary column with this mean
df['Salary'] = df['Salary'].fillna(mean_salary)

# Let's also fill the missing Performance_Score with the median score
median_score = df['Performance_Score'].median()
df['Performance_Score'] = df['Performance_Score'].fillna(median_score)

print("--- AFTER FILLING MISSING VALUES ---")
print(df)
print("\n")

# drop_duplicates() scans the dataframe and removes identical rows
df = df.drop_duplicates()

print("--- AFTER REMOVING DUPLICATES ---")
print(df)
print("\n")

# Convert the 'Join_Date' column from string to datetime objects
df['Join_Date'] = pd.to_datetime(df['Join_Date'], format='%d-%m-%Y')

# Let's also ensure Performance_Score is an integer (it might have turned into a float during the NaN fill)
df['Performance_Score'] = df['Performance_Score'].astype(int)

print("--- FINAL CLEANED & TRANSFORMED DATA ---")
print(df)
print("\nData Types:")
>>>>>>> e95509634b98560854473954f3c41f39e7949386
print(df.dtypes)
