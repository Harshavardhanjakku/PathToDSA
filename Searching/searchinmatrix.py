def searchmatrix(matrix, target, m, n):
    i = 0
    j = n - 1  
    while i < m and j >= 0:
        if target == matrix[i][j]:
            return True
        elif target > matrix[i][j]:
            i += 1  
        else:
            j -= 1  
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
m = len(matrix)
n = len(matrix[0])
print(searchmatrix(matrix, target, m, n))  # Output: True
