n = int(input())
h = list(map(int, input().split()))

steps = [0] * n
ans = 0

for i in range(1, n):
    if h[i] <= h[i - 1]:
        steps[i] = steps[i - 1] + 1
    else:
        steps[i] = 0
    ans = max(ans, steps[i])

print(ans)
