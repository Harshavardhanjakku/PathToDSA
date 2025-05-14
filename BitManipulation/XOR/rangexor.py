def xorupton(n):
    if n%4==0:
        #print(n)
        return n
    elif n%4==1:
        #print(1)
        return 1
    elif n%4==2:
        # print(n+1)
        return n+1
    else:
        return 0
a=5
b=10
res=0
print(xorupton(a-1)^xorupton(b))
for i in range(a,b+1):
    res=res^i
print(res)
