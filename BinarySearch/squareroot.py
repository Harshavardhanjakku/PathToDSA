def squareroot(n):
    low=0
    high=n
    while low<=high:
        mid=low+(high-low)//2
        if mid*mid==n:
            return mid
        elif mid*mid>n:
            high=mid-1
        else:
            low=mid+1
n=36
res=squareroot(n)
print(res)