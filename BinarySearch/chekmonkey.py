import math
l=[3,6,7,11]
h=8
k=3
counthours=0
for i in l:
    counthours+=math.ceil(i/k)
    if counthours>=h:
        break
print(counthours<=h)

