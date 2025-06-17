

for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix
