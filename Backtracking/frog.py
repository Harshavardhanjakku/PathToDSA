def dfs(matrix,i,j,m,n):
    if i==m-1 and j==n-1 and matrix[i][j]==1:
        return 1
    if  i>=m or j>=n or matrix[i][j]== 0:
        return 0
    return dfs(matrix,i,j+1,m,n)+dfs(matrix,i+1,j,m,n)
matrix=[[1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]]
l=[(1,0),(3,1),(4,1),(2,4)]
for i in l:
    matrix[i[0]][i[1]]=0
print(dfs(matrix,1,2,5,5))
print(matrix)