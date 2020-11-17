n, w = list(map(int, input().split()))

minutes = [0] * (2 * 10 ** 5 + 100)
max_t = 0

for i in range(n):
    s, t, p = map(int, input().split())
    minutes[s] += p
    minutes[t] -= p
    max_t = max(t, max_t)

for j in range(1, len(minutes)):
    minutes[j] += minutes[j - 1]

for x in minutes:
    if x > w:
        print('No')
        exit()

print('Yes')
