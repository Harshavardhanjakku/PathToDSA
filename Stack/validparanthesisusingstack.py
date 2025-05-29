s="]]]"
mystack=[]
for i in s:
    if i=="(" or i=="{" or i=="[" :
        mystack.append(i)
    elif i=="}":
        if  mystack!=[] and mystack[-1]=="{":
            mystack.pop()
        else:
            mystack.append(i)
    elif i=="]":
        if mystack!=[] and mystack[-1]=="[":
            mystack.pop()
        else:
            mystack.append(i)
    elif i==")":
        if mystack!=[] and mystack[-1]=="(":
            mystack.pop()
        else:
            mystack.append(i)    
print(mystack==[])