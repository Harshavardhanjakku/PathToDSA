s="abcdecfbgce"
dic = {}
left = 0
maxlen = 0
newstr=""
for i in range(len(s)):
    if s[i] in dic and dic[s[i]] >= left:
        left = dic[s[i]] + 1
    dic[s[i]] = i
    newstr+=s[i]
    maxlen = max(maxlen, i - left + 1)

print(newstr)
print(maxlen)