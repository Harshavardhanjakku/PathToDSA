from collections import defaultdict,deque
def printpath(graphs,src,dest,d):
    q=deque()
    q.append(src)
    visited=[src]
    while q:
        nodelist=q.popleft()
        for node in d[nodelist]:
            if node not in visited and node not in q:
                visited.append(node)
                q.append(node)
    return visited
graphs = [(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d = defaultdict(list)

for i, j in graphs:
    d[i].append(j)
    d[j].append(i)

src = 5
dest = 3
printpath(graphs,src,dest,d)
