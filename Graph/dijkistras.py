from collections import defaultdict,deque

graph = defaultdict(list)
edges = [(10,5,2),(10,7,4),(5,7,1),(5,8,3),(5,3,2),(8,3,1),(8,7,1)]

for u, v, w in edges:
    graph[u].append([v, w])
    graph[v].append([u, w])

print(graph)  
start=10
distdic={}
for i in graph:
    if start==i:
        distdic[start]=0
    else:
        distdic[i]=999999
print(distdic)
visited={}
q=deque()
q.append(start)
while q:
    mynode=q.popleft()
    for i in graph[mynode]:
        # print(i[0])
        if i[0] not in visited:
            q.append(i[0])
            visited[i[0]]=True
        if distdic[mynode]+i[1]<distdic[i[0]]:
            distdic[i[0]]=distdic[mynode]+i[1]
print(distdic)