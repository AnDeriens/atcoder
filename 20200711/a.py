# -*- coding: utf-8 -*-

x = input().split(' ')
l = int(x[0])
r = int(x[1])
d = int(x[2])

s = 0
for i in range(l, r + 1):
    if i % d == 0:
        s += 1

print(s)
