import numpy as np

balance = np.array([
    [15000, 16000, 17000],
    [20000, 21000, 22000],
    [12000, 13000, 14000]
])

# Add 2000 to Customer 2 (row index 1)
balance[1] += 2000

# Convert to single row
report = balance.reshape(1, 9)

print("Updated Balance:\n", balance)
print("\nSingle Row Format:\n", report)