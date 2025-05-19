def traverse(l):
    for i in l:
        if checkprime(i):
            return i 
def checkprime(n):
    if n<2:
        return False
    for num in range(2,int(n**0.5)+1):
        if n%num==0:
            return False
    return True

l=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
primelist=[]
n=len(l)
for i in range(n-1):
    flag=False
    for j in range(n-i-1):
        a=traverse(l[j])
        b=traverse(l[j+1])
        if a>b:
            l[j],l[j+1]=l[j+1],l[j]
            flag=True
    if not flag:
        break
print(l)