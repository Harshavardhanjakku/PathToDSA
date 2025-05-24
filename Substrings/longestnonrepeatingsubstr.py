dic={}
s="abcdecfbgce"
left = 0
maxlen = 0
for i in range(len(s)):
    if s[i] in dic and dic[s[i]] >= left:
        left = dic[s[i]] + 1
    dic[s[i]] = i
    if maxlen<i-left+1 :
        if "c" in dic and "d" in dic and dic["c"]>left and dic["d"]>left:
            maxlen=i-left+1
print(maxlen)