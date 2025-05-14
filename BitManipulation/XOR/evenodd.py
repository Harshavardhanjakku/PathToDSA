def usingmodulo(n):
    return "Even" if n%2==0 else "Odd"
def usingand(n):
    return "Even" if n&1==0 else "Odd"
def usingxor(n):
    if n^1==n+1:
        return "Even"
    if n^1==n-1:
        return "Odd"
def usingshift(n):
    return "Even" if n==(n>>1)<<1 else "Odd"
l=[2,4,5,1,3,4]
for i in l:
    print(i,usingand(i),usingmodulo(i),usingshift(i),usingxor(i))