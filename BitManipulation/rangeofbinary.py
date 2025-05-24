n=int(input("Enter the number:"))
import math
l=int(math.log(n,2))+1
for i in range(0,n+1):
    s=""
    for j in range(l):
        if (i>>j)&1==1:
            s+=str(1)
        else:
            s+="0"
    print(s[::-1])

