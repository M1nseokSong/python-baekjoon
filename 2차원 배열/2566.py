# 최댓값
array = list(list(map(int, input().split())) for _ in range(9))
max_array = array[0][0]
max_array_row = 0
max_array_col = 0
for row in range(9):
    for col in range(9):
        if array[row][col] >= max_array:
            max_array = array[row][col]
            max_array_row = row + 1
            max_array_col = col + 1
print(max_array)
print(str(max_array_row) + " " + str(max_array_col))
