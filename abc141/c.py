n, k, q = list(map(int, input().split()))

seikai = [0] * (n + 1)

for i in range(q):
    a = int(input())
    seikai[a] += 1

for j in range(1, n + 1):
    point = k - q + seikai[j]
    if point > 0:
        print('Yes')
    else:
        print('No')

