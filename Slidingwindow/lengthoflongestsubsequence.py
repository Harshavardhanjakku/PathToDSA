def checksubsequence(l):
    n = len(l)
    maxi = 0
    for i in range(n - 1):
        length = 1
        for j in range(i, n - 1):
            if l[j] + 1 == l[j + 1]:
                length += 1
            else:
                break
        maxi = max(maxi, length)
    print(maxi)
checksubsequence([1,2,3,2,3,4,5,6,7,8,9])
checksubsequence([2,3,4,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9])