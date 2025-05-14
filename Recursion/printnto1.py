def printnto1(n):
    if n==0:
        return  
    print(n)
    printnto1(n-1)
printnto1(int(input("Enter the number :")))