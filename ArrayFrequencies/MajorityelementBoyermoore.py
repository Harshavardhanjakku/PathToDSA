l=[2,1,1,2,1,1,1]

c=0
majorityele=None
for i in l:
    if c==0:
        majorityele=i
        c=1
    elif majorityele==i:
        c+=1
    else:
        c-=1
print(majorityele)