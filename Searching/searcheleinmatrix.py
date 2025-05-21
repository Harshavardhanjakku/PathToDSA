m=[[1,4,2],[2,9,6],[5,8,7]]
def findele(m,target):
    row=0
    for i in m:
        col=0
        for j in i:
            if j==target:
                return (True,row,col)
            col+=1
        row+=1
    return False
print(findele(m,6))