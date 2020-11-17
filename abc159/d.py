import collections

n = int(input())
a = [0] + list(map(int, input().split()))

c = [0] * (n + 1) # a_iのカウンター
d = [0] * (n + 1) # 1-nのs-s'の値 

for i in range(1, n + 1):
    c[a[i]] += 1 

s = 0
for j in range(1, n + 1):
    s += c[j] * (c[j] - 1) // 2
    if j > 1:
        d[j] = j * (j - 1) // 2 - (j - 1) * (j - 2) // 2

for k in range(1, n + 1):
    print(s - d[c[a[k]]])
