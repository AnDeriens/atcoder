# -*- coding: utf-8 -*-

n = int(input())

t_list = [0]*n

for i in range(n):
    t_list[i] = int(input())

ans = 0
for j in range(2 ** n):
    x = [0] * n
    for k in range(n):
        if ((j >> k) & 1):
            x[n - 1 - k] = 1

    p = 0
    q = 0
    for i in range(len(x)):
        if x[i] == 0:
            p += t_list[i]
        else:
            q += t_list[i]

    if ans == 0:
        ans = max(p,q)
    else:
        ans = min(max(p,q), ans)

print(ans)
