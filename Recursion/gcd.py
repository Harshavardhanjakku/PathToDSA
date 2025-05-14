def gcd(a,b):
    if b%a==0:
        return a
    return gcd(b%a,a)
print(gcd(198,3))