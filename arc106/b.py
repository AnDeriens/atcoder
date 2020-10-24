n, m = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

edges = [[] for i in range(m)]

for i in range(m):
    edges[i] = list(map(int, input().split()))
    

import collections

def bfs(graph, s):
    visited = {s: None}
    unvisited = collenctions.deque([s])
    while unvisited:
        u = unvisited.popleft()

        for v in graph[u]:
            if not (v in  Visited):
                unvisited.append(v)
                visited[v] = u

    return visited

print(bfs(30))
