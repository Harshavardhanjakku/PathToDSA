s = "abcdcecdb"

left=0
right=1

res = 0
while right<len(s):
    print(left,right, s[left],s[right],res)
    if s[left]==s[right]:
        left += 1
        right = left
    res = max(res,right-left+1)
    right += 1

print("Maximum length of subString: ",res)














# using Set
s = "abcdcecdb"
dup = ()

l=0
res = 0
for r in len(1,len(s)):
    if r in dup:
        l

print("Maximum length of subString: ",res)


#using Dict