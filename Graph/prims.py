from collections import defaultdict

graph = defaultdict(list)
edges = [(5,2,3), (5,7,2), (5,8,1), (2,7,2), (2,8,4), (8,7,1), (8,3,3), (2,3,2)]

for u, v, w in edges:
    graph[u].append([v, w])
    graph[v].append([u, w])

print(graph)  

visited={}

import heapq

heap = []
heapq.heappush(heap, (0,5)) 
print(heap)
countweight=0
l=[]
while heap:
    weight,node=heapq.heappop(heap)
    if node in visited:
        continue
    countweight+=w
    l.append((node,weight))
    visited[node]=True
    for n,w in graph[node]:
        if n not in visited :
            heapq.heappush(heap, (w,n)) 

print(countweight)
print(l)