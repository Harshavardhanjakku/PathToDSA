n=1000000
res=0
for i in range(1,n+1):
    res=res^i
    print(f"{i=} {res=}")
print("Final Answer:",res)
print("_____________________________________")
print("Final Answer:",end=" ")
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
else:
    print(0)