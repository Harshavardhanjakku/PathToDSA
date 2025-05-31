graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
dic={}
# Regular method input the graph
for i,j in graphs:
    if i not in dic:
        dic[i]=[j]
    else:
        dic[i].append(j)
    if j not in dic:
        dic[j]=[i]
    else:
        dic[j].append(i)
print(dic)

# Using the default dic efficient method

from collections import defaultdict
d=defaultdict(list)

for i,j in graphs:
    d[i].append(i)
    d[j].append(j)
print(d)
for i in d:
    print(i,dic[i])
