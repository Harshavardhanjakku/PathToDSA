cardPoints = [1,2,3,4,5,6,1]
k = 3
# mysum=sum(cardPoints[:k])
# maxi=mysum
# i=k-1
# mysum-=cardPoints[i]
# i-=1
# j=-1
# while i>=0:
#     j-=1
#     i-=1
#     maxi=max(mysum,maxi)
#     mysum-=cardPoints[i]
# print(maxi)
lps=[0]*k
rps=[0]*k
lps[0]=cardPoints[0]
for i in range(1,k):
    lps[i]=lps[i-1]+cardPoints[i]
rps[-1]=cardPoints[-1]
j=-2
while j>=-k:
    rps[j]=cardPoints[j]+rps[j+1]
    j-=1
print(rps)
mymaxi=lps[k-1]
j=-1
for i in range(k):
    mymaxi=max(lps[i],rps[j])
    j-=1
print(mymaxi)