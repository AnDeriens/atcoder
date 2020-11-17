import itertools

n, k = list(map(int, input().split()))
t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    t[i] = [0] + list(map(int, input().split()))

cities = [p for p in range(2, n + 1)] 

cnt = 0

for j in itertools.permutations(cities, n - 1):
    hours = 0
    city_from = 1
    for l in range(len(j)):
        city_to = j[l]
        hours += t[city_from][city_to]
        city_from = city_to

    hours += t[city_from][1]
    if hours == k:
        cnt += 1

print(cnt)
