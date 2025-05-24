# s = "ababba"
# res = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         temp = s[i:j]
#         if temp == temp[-1::-1] and res<len(temp):
#             res = len(temp)
# print(res)


#effient code:
s = "ababba"
res = 0

for i in range(len(s)):
    left = right = i
    while left>=0 and right<len(s) and s[left]==s[right]:
        res = max(res,right-left+1)
        left-=1
        right+=1
    left,right = i,i+1
    while left>=0 and right<len(s) and s[left]==s[right]:
        res = max(res,right-left+1)
        left-=1
        right+=1
print(res)