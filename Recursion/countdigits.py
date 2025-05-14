def countdigits(n):
    if n==0:
        return 0
    return countdigits(n//10)+1

print(countdigits(12345))