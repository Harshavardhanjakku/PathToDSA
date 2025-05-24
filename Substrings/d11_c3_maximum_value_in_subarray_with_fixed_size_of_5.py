# sliding window approach O(1),O(1)
arr = [2,1,6,4,2,3,1,1,4,2,6,7,3,1,1,1,1]

tot = sum(arr[:5])
res = tot

for i in range(5,len(arr)):
    tot = tot - arr[i-5] + arr[i]
    res = max(tot,res)

print(res)