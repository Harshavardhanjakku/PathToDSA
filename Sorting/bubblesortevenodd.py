l=[1,10,3,12]
l=[1,3,16,4,9,8,6,10,2,7]
n=len(l)
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]<l[j] and l[i]%2==1 and l[j]%2==1:
            l[i],l[j]=l[j],l[i]
        if l[i]>l[j] and l[i]%2==0 and l[j]%2==0:
            l[i],l[j]=l[j],l[i]
print(l)
