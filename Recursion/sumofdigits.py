def sumofdigits(n):
    if n==0:
        return 0
    return (n%10)+sumofdigits(n//10)
print(sumofdigits(12345))