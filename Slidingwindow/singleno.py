def func(l):
    n=len(l)
    ind=-1
    for i in range(0,n-1,2):
        if l[i]!=l[i+1]:
            ind=i
            break
    return l[ind]

l=[2,2,4,4,6,6,7,7,8,8,9]
print(func(l))