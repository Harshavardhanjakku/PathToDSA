s="An Apple A Day Keeps Doctor Away"
l=s.split()
lengthlist=[len(i) for i in l]
n=len(l)
for i in range(n-1):
    flag=False
    for j in range(n-i-1):
        if lengthlist[j]>lengthlist[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            lengthlist[j],lengthlist[j + 1]=lengthlist[j + 1],lengthlist[j]
            flag=True
    if not flag:
        break
print(" ".join(l))
