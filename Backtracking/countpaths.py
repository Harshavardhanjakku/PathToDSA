def dfs(matrix,i,j,m,n):
    if i==m-1 and j==n-1 and matrix[i][j]==1:
        return 1
    if  i>=m or j>=n or matrix[i][j]== 0:
        return 0
    return dfs(matrix,i,j+1,m,n)+dfs(matrix,i+1,j,m,n)
matrix=[[1,0,0,0,0],
        [1,1,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1]]
print(dfs(matrix,0,0,5,5))
matrix = [[1,0,0,0],
          [1,1,1,1],
          [1,1,0,1],
          [1,1,1,1]]

print(dfs(matrix,0,0,4,4))

print(matrix)