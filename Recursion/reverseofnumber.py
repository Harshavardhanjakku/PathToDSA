def reverse(n,rev):
    if n==0:
        return rev
    rev=rev*10+(n%10)
    return reverse(n//10,rev)
print(reverse(5277,0))