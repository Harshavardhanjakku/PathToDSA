def allb(a,o,c,s):
    if o==a and c==a:
        print(s)
        return 
    if o<a:
        allb(a,o+1,c,s+"(")
    if c<o:
        allb(a,o,c+1,s+")")
a=3
allb(a,0,0,"")