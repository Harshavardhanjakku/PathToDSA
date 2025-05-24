def checkmaxprofit(l):
    mymin=float('inf')
    profit=float('-inf')
    for i in l:
        mymin=min(mymin,i)
        profit=max(profit,i-mymin)
    return profit

l=list(map(int,input("Enter the List:").split(" ")))
print(checkmaxprofit(l))