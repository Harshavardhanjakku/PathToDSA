arr = [2,1,6,4,2,3,1,1,4,2,6,7,3]
k = 6

res = 0
left=right = 0
tot = 0

while right <len(arr):
    if tot+arr[right]<=k:
        tot += arr[right]
        right+=1
    else:
        tot -= arr[left]
        left +=1
    res = max(res,right-left)
    print(left,right,tot,res)
print(res)