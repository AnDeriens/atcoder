n, m = list(map(int, input().split()))

cost = [0] * (n + 1)
city = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = list(map(int, input().split()))
    city[a].append(b)

cost[1] = 0
for base in range(1, n + 1):
    for to in city[base]:
        if cost[base] != False:
            cost[x] = min(cost[to], cost[i] + 1)

print(city)
print(cost)
print(cost[n])
