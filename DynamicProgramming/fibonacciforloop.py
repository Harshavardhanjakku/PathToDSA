n=int(input("Enter the number :"))
a,b,c=0,1,None
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
print(c)