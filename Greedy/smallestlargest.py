
l=list(map(int,input("Enter the list").split()))
n=len(l)
levn=l[0]
sodd=l[0]
for i in l :
    if i%2:
        if i<=sodd:
            sodd=i
    else:
        if i>=levn:
            levn=i
print(levn,sodd)