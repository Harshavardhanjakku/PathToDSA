n=int(input("Enter the number :"))
l=[0,1]
for i in range(2,n+1):
    l.append(l[-1]+l[-2])
print(l[-1])