s = "ababba"
res = 0
st=ed=0

for i in range(len(s)):
    left = right = i
    while left>=0 and right<len(s) and s[left]==s[right]:
        res = max(res,right-left+1)
        if res<=right-left+1:
            res = right-left+1
            st,ed=left,right
        left-=1
        right+=1
    left,right = i,i+1
    while left>=0 and right<len(s) and s[left]==s[right]:
        res = max(res,right-left+1)
        if res<=right-left+1:
            res = right-left+1
            st,ed=left,right
        left-=1
        right+=1
print("maximun length palindrome is: ", s[st:ed+1])




s = "ababba"
count = 0
st = 0

for i in range(len(s)):
    left = right = i
    while left>=0 and right<len(s) and s[left]==s[right]:
        count += 1
        left-=1
        right+=1
    left,right = i,i+1
    while left>=0 and right<len(s) and s[left]==s[right]:
        count+=1
        left-=1
        right+=1
print("Count of all possible palindromes are:",count)