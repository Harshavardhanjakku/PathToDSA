def nofIslands(matrix,i,j,m,n):
    if i<0 or j<0 or i>m-1 or j>m-1 or matrix[i][j]==0:
        return 
    nofIslands(matrix,i,j+1,m,n)
    nofIslands(matrix,i,j-1,m,n)
    nofIslands(matrix,i+1,j,m,n)
    nofIslands(matrix,i-1,j,m,n)
matrix=[[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
print(nofIslands(matrix,0,0,5,5))