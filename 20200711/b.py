# -*- coding: utf-8 -*-

n = int(input())
l = input().split(' ')

s = 0
for i in range(n):
    if i % 2 == 0 and int(l[i]) % 2 == 1:
        s += 1

print(s)
