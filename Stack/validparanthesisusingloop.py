def func(s):
    if s=="":
        return True
    while s!="":
        if "[]" in s:
            s=s.replace("[]","")
        elif "()" in s:
            s=s.replace("()","")
        elif "{}" in s:
            s=s.replace("{}","")   
        else:
            return False     
    return True
print(func("(){}[()]"))