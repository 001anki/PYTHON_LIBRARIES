import numpy as np

marks = np.array([
    [65, 70, 75],
    [80, 85, 90],
    [55, 60, 65]
])

# Increase Subject 1 marks (column index 0) by 10
marks[0, 0] += 10

# Convert to single row
report = marks.reshape(1, 9)

print("Updated Marks:\n", marks)
print("\nSingle Row Format:\n", report)
