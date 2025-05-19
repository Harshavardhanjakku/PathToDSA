import math
def genb(n,s,c,l):
    if n==0:
        return '0'*(l-c)+s
    else:
        if n%2==0:
            s+="0"
        else:
            s+="1"
        c+=1
    return genb(n//2,s,c,l)
n=int(input())
l=int(math.log(n,2))+1
for i in range(0,n+1):
    print(genb(i,"",0,l))

