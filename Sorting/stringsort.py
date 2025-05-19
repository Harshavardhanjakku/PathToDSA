s=["Hello","Hei","Cat","Apples"]
n=len(s)
for j in range(n-1):
    flag=False
    for i in range(n-j-1):
        if s[i][0]>s[i+1][0]:
            s[i],s[i+1]=s[i+1],s[i]
            flag=True
        elif s[i][0]==s[i+1][0]:
            if s[i][1]>s[i+1][1]:
                s[i],s[i+1]=s[i+1],s[i]
                flag=True
            else:
                continue
        print(s)
    if not flag:
        break
print(s)