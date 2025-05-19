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
print(l)
primelist=[]
n=0
for i in l:
    myprime=traverse(i)
    primelist.append(myprime)
    n+=1
print("Prime List",primelist)
for i in range(n-1):
    flag=False
    for j in range(n-i-1):
        if primelist[j]>primelist[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            primelist[j],primelist[j + 1]=primelist[j + 1],primelist[j]
            flag=True
    if not flag:
        break
print(l)