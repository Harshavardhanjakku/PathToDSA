def checkpetrol(a):
    n=len(a)
    curr=a[0]
    for i in range(1,n):
        curr=curr-1
        if a[i]>curr:
            curr=a[i]
        if curr==0:
            break
    print(curr>0)

a=[2,3,1,4,2,3,0]
checkpetrol(a)
a=[2,2,1,0,1,3,0]
checkpetrol(a)
a=[2,3,1,0,1,3,1]
checkpetrol(a)
a=[3,2,1,0,4]
checkpetrol(a)