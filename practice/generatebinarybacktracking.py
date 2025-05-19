import math
def allb(a,n,s=""):
    if a==-1:
        return a
    if len(s)==n:
        print(s)
        a=a-1
        return a
    a=allb(a,n,s+"0")
    a=allb(a,n,s+"1")
    return a 
a=18
n=int(math.log(a,2))+1
allb(a,n)