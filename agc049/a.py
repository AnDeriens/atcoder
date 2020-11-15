n = int(input())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    _s = input()
    for j in range(n):
        if _s[j] == '1': 
            graph[i + 1][j + 1] = 1

def set_unvisited(G):
    vstates = []
    for vertex in range(n + 1):
        vstates.append(None)
    return vstates

states = set_unvisited(graph)

def DFS(G, start, points = []):
    points = []
    states[start] = True
    points.append(start)
    for u in G[start]:
        if not states[u]:
            DFS(G, u, points)

    return points

print(DFS(graph, 1))
print(DFS(graph, 2))
print(DFS(graph, 3))
