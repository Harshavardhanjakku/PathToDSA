a=[4,2,7,20,8,60,4,1]
n=len(a)
k=3
leftsum=0
for i in range(k):
    leftsum+=a[i]
rightsum=0
m=leftsum
for i in range(k-1,-1,-1):
    leftsum=leftsum-a[i]
    rightsum=rightsum+a[n-1]
    m=max(m,leftsum+rightsum)
    n=n-1
print(m)