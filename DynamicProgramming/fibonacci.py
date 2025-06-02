n=int(input("Enter the number :"))
dp=[-1]*(n+1)
def fibonacci(n):
    if dp[n]!=-1:
        return dp[n]
    if n<2:
        dp[n]=n
        return n
    dp[n]=fibonacci(n-1)+fibonacci(n-2)
    return dp[n]
print(f"The Fibonacci of {n} is {fibonacci(n)}")
print(dp)