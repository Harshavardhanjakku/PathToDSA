def dfs(i,j,n,l):
    if i==n-1 and j==n-1 :
        return 1
    if  i>=n or j>=n or ((i,j) in l):
        return 0
    return dfs(i,j+1,n,l)+dfs(i+1,j,n,l)

n=5
l=[(1,0),(3,1),(4,1),(2,4)]

print(dfs(1,2,n,l))
