def checkvowels(s,k,v):
    c=0
    for i in range(k):
        if s[i] in v:
            c+=1
    return c 


s = "abciiidef"
n=len(s)
k=3
vowelset={'a','e','i','o','u'}
maxi=0
for i in range(n-k+1):
    print(s[i:i+k])
    vc=checkvowels(s[i:i+k],k,vowelset)
    maxi=max(maxi,vc)
print(maxi)