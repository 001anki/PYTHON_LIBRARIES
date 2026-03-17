import numpy as np

# Test Case 1: Weekly Rainfall Data (in mm)
rainfall = np.array([12.5, 0.0, 45.2, 30.1, 5.5, 0.0, 15.8])
std_dev = np.std(rainfall)
print(f"Standard Deviation of Rainfall: {std_dev:.2f}")

# Test Case 2: Student Exam Scores
scores = np.array([85, 92, 78, 90, 88, 76, 95, 89])
mean_score = np.mean(scores)
median_score = np.median(scores)
print(f"Mean: {mean_score}, Median: {median_score}")