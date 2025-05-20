# l=[15,20,30,2,4,8]
# n=len(l)
# i,j=0,n-1
# while i<=j:
#     mid=i+(j-i)//2
#     if l[mid]>l[i]:
#         print(mid)
#         break
#     elif l[mid]>l[i]:
#         i=mid+1
#     else:
#         j=mid-1
  
l = [15, 20, 30, 2, 4, 8]
l=[1,2,3,4,5]
n = len(l)
i, j = 0, n - 1

while i < j:
    mid = i + (j - i) // 2
    if l[mid] > l[j]:
        i = mid + 1
    else:
        j = mid

print("Rotation index is:", i)
