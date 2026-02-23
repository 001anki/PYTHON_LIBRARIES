import numpy as np

books = np.array([
    [18, 25, 30],
    [12, 20, 28],
    [15, 22, 35]
])

# Increase values below 20 by 5
books[books < 20] += 5

# Convert to single row
report = books.reshape(1, 9)

print("Updated Borrowing Data:\n", books)
print("\nSingle Row Format:\n", report)