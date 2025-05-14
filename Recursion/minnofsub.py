def minnofsub(n):
    if n==1:
        return True
    if n<1:
        return False
    return minnofsub(n-3) or minnofsub(n-5)
import sys
def countminnofsub(n):
    if n == 1:
        return 0
    if n < 1:
        return sys.maxsize 
    return min(countminnofsub(n-3)+1,countminnofsub(n-5)+1)
n=int(input("Enter the number :"))
print(countminnofsub(n) if minnofsub(n) else 0)