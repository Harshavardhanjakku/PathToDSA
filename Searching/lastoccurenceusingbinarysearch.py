def binarysearch(l, ele):
    low = 0
    high = len(l) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if l[mid] == ele:
            result = mid        # record the index
            low = mid + 1       # search in right half to find the last occurrence
        elif l[mid] < ele:
            low = mid + 1
        else:
            high = mid - 1
    return result

l=[2,3,5,6,7,7,8,9,10,10,10,13,15]
print(binarysearch(l,10))