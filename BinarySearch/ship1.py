def check(l,c):
    if c<max(l):
        return "Not possible"
    else:
        return countdays(l,c)
def countdays(l,c):
    curr=0
    days=1
    for i in l:
        print(f"{i=},{curr=},{days=}")
        if curr+i<=capacity:
            curr+=i
        else:
            days+=1
            curr=i
    return days

l=[1,2,3,4,5,6,7,8,9,10]
capacity=15
print(check(l,capacity))