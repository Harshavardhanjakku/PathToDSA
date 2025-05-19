l=[20,18,16,14,12,10,8,6,4,2,19,17,15,13,11,9,7,5,3,1]
n=len(l)
k=5
print(n)
for i in range(n-1):
    flag=False
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            flag=True
    if not flag:
        break
print(l)
