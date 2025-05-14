def ispowerof2(n):
    if n==1:
        return True
    if n%2==1:
        return False
    return ispowerof2(n//2)
print(ispowerof2(36))