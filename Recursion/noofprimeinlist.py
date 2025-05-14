def prime(n,i):
    if i>n**0.5:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)

def countprime(mylist,ind):
    n=len(mylist)
    if ind==n:
        return 0
    if  prime(mylist[ind],2):
       return 1+countprime(mylist,ind+1)
    return countprime(mylist,ind+1)
 
a=[13,17,21,23,22,7,29]
print(countprime(a,0))
