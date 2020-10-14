# -*- coding: utf-8 -*-

s = list(input())
t = list(input())

ans = len(t)

for i in range(len(s) - len(t) + 1):
    n_replace = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            n_replace += 1
    ans = min(ans, n_replace)

print(ans)

