from collections import defaultdict

def checkpathavailable(graphs, visited, d, dest):
    if visited[-1] == dest:
        return True
    for neighbor in d[visited[-1]]:
        if neighbor not in visited:
            visited.append(neighbor)
            if checkpathavailable(graphs, visited, d, dest):
                return True
            visited.pop()
    return False

graphs = [(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d = defaultdict(list)

for i, j in graphs:
    d[i].append(j)
    d[j].append(i)

src = 5
dest = 3
visited = [src]
print(checkpathavailable(graphs, visited, d, dest))
