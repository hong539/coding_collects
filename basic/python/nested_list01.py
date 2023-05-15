matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],]

print("\nThis is a matrix:\n", matrix, "\n")

transposed = []

for i in range(4):
    transposed.append([row[i] for row in matrix])

print("The matrix after transposed:\n",transposed, "\n")    