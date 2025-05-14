def longestConsecutiveSubarray(mystr):
    count = 1
    s=""
    for i in range(len(mystr) - 1):
        if mystr[i] == mystr[i + 1]:
            count += 1
        else:
            s+=mystr[i]+str(count)
            count = 1
    s+=mystr[i]+str(count)
    return s
mystr = "aaabbaaaacccddeff"
print(longestConsecutiveSubarray(mystr))