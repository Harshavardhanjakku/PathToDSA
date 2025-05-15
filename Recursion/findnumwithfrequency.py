def frequencyofK(mylist,ind,k):
    if ind==len(mylist):
        return 0
    if mylist[ind]==k:
        return 1+frequencyofK(mylist,ind+1,k)
    return frequencyofK(mylist,ind+1,k)
    
l=[2,4,6,3,3,2,6,1,2,3,6,6,5]
freq=1
def arraytraversal(l,indx,freq):
    if indx==len(l):
        return 0
    if frequencyofK(l,0,l[indx])==freq:
        return l[indx]
    return arraytraversal(l,indx+1,freq)

print(arraytraversal(l,0,freq))

#__________________________________________________

# OPTIMISED CODE
#__________________________________________________

def freq_map(arr, i, d):
    if i == len(arr):
        return d
    d[arr[i]] = d.get(arr[i], 0) + 1
    return freq_map(arr, i + 1, d)

def find_elem(arr, i, f, d):
    if i == len(arr):
        return 0
    if d[arr[i]] == f:
        return arr[i]
    return find_elem(arr, i + 1, f, d)

a = [2, 4, 6, 3, 3, 2, 6, 1, 2, 3, 6, 6, 5]
d = freq_map(a, 0, {})
f = 1
print(find_elem(a, 0, f, d))

