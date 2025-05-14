def prime(n,i):
    if i>n**0.5:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)
print(prime(17,2))
    