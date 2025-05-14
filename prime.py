def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input("Enter The number:"))

if prime(n):
    if n>200:
        print("Prime and greater than 200")
    else:
        print("Prime and Less than 200")
else:
    print("Not a prime number")