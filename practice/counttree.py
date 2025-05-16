def DFS(matrix,i,j,m,n):
    if i<0 or j<0 or i>m-1 or j>n-1 or matrix[i][j]==0 or matrix[i][j]==2:
        return 0
    if matrix[i][j]==1:
        matrix[i][j]=2
    DFS(matrix,i,j+1,m,n)
    DFS(matrix,i,j-1,m,n)
    DFS(matrix,i+1,j,m,n) 
    DFS(matrix,i-1,j,m,n)
matrix=[[1,0,0,1,1],
        [1,0,0,0,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,1]]
m=len(matrix)
n=len(matrix[0])
row=4
col=4
DFS(matrix,row,col,m,n)
for i in matrix:
    print(i)
count=0
for i in matrix:
    for j in i :
        if j==1:
            count+=1
print(count)
