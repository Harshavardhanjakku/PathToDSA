l=[1,3,16,4,9,8,6,10,2,7]
n=len(l)
for i in range(n-i-1):
    oflag=False
    evflag=False
    for j in range(n-i-1):
        if l[j]<l[j+1] and l[j]%2==1 and l[j]%2==1:
            l[j],l[j+1]=l[j+1],l[j]
            flag=True
        if l[j]>l[j+1] and l[j]%2==0 and l[j]%2==0:
            l[j],l[j+1]=l[j+1],l[j]
            flag=True
    
print(l)