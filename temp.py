import numpy as np

temp = np.array([
    [32, 36, 34],
    [38, 33, 37],
    [30, 35, 39]
])

# Reduce temperature above 35°C by 2
temp[temp > 35] -= 2

# Convert to single row
report = temp.reshape(1,9)

print("Corrected Temperature:\n", temp)
print("\nSingle Row Format:\n", report)