n = int(input())
a = [0] + list(map(int, input().split()))

s = [0] + [0] * n
max_s = [0] + [0] * n
_max_s = - 10 ** 18

for i in range(1, n + 1):
    s[i] = a[i] + s[i - 1]
    _max_s = max(_max_s, a[i] + s[i - 1])
    max_s[i] = _max_s

x = 0
max_x = - 10 ** 18

for j in range(0, n + 1):
    max_x = max(x + max_s[j], max_x)
    x += s[j]

print(max_x)
