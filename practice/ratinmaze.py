def dfs(matrix,i,j,m,n):
    if i==n-1 and j==n-1 and matrix[i][j]==1:
        return True
    if  i>=n or j>=m or matrix[i][j]==0:
        return False
    return dfs(matrix,i,j+1,m,n) or dfs(matrix,i+1,j,m,n)
matrix=[[1,0,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[1,0,1,1,1],[1,1,1,0,0]]
print(dfs(matrix,0,0,5,5))
