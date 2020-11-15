import itertools

n = int(input())

patterns = list(itertools.permutations(range(1, n + 1)))

towns = [{}] + [{}] * n

for i in range(1, n + 1):
    x, y = list(map(int, input().split()))
    towns[i] = {'x': x, 'y': y}
    

distance = 0

for pattern in patterns:
    for i in range(len(pattern) - 1):
        pre_num  = pattern[i]
        post_num = pattern[i + 1]
        pre_town  = towns[pre_num]
        post_town = towns[post_num]
        distance += ((post_town['x'] - pre_town['x']) ** 2 + (post_town['y'] - pre_town['y']) ** 2) ** 0.5

print(distance / len(patterns))
