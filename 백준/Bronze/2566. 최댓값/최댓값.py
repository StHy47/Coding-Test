matrix = []
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

max_val = -1
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_row, max_col = i+1, j+1

print(max_val)
print(max_row, max_col)