s = "hippopotamus"
vowels = "aeiou"
hmp = {}
newString = []

for i in range(len(s)):
    if s[i] in vowels:
        hmp[i] = s[i]
    else:
        newString.append(s[i])
        
res = []
for i in range(len(s)):
    if i in hmp:
        res.append(hmp[i])
    else:
        res.append(newString.pop())

print("".join(res))



#efficient way(space complexity is reduced compared to above)
s = "hippopotamus"
vowels = set("aeiou")

newString = []
for ch in s:
    if ch not in vowels:
        newString.append(ch)

res = []
j = len(newString)-1
for ch in s:
    if ch in vowels:
        res.append(ch)
    else:
        res.append(newString[j])
        j-=1

print("".join(res))


#very efficient way(two-pointer approach, TC:O(n), SC:O(1))
s = "hippopotamus"
sl = list(s)
vowels = set("aeiou")
i,j = 0,len(s)-1

while i<j:
    if i<j and sl[i] in vowels:
        i+=1
    elif i<j and sl[j] in vowels:
        j-=1
    else:
        sl[i],sl[j] = sl[j],sl[i]
        i+=1
        j-=1
print("".join(sl))