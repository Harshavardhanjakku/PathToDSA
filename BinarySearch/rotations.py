l=[2,4,8,15,20,30]
n=len(l)
k=2
k=k%n
print(l[-k:]+l[:-k])
print(k-1,k)