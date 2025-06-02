heights = [10, 20, 30, 10]
n = len(heights)
a=0
b=abs(heights[1] - heights[0])
for i in range(2,n):
    jump1 = a + abs(heights[i] - heights[i - 1])
    jump2 = b + abs(heights[i] - heights[i - 2])
    res = min(jump1, jump2)
    a=b
    b=res
print(res)
