s="15,3,+,6,2,-,*"
s="-8,3,/"
l=s.split(",")
mystack=[]
for i in l:
    if i[-1].isdigit():
        mystack.append(int(i))
    elif i in "^*/+-%":
        fo=mystack.pop()
        so=mystack.pop()
        if i=="*":
            res=so*fo
        elif i=="/":
            res=so/fo
        elif i=="+":
            res=so+fo
        elif i=="-":
            res=so-fo
        elif i=="^":
            res=so^fo
        else:
            res=so%fo
        mystack.append(res)
print(mystack[0])