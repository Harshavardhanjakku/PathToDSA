l=[15,20,30,2,4,8]
n=len(l)
i,j=0,n-1

while i<=j:
    mid=i+(j-i)//2
    if(mid==0 or l[mid]>=l[mid-1])and(mid==n-1 or l[mid]>=l[mid+1]):
        print("Peak element index:", mid)
        break
    elif mid>0 and l[mid-1]>l[mid]:
        j=mid-1
    else:
        i=mid+1
