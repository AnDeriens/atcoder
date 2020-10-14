# -*- coding: utf-8 -*-

n = int(input())

x = 10 ** 9 + 7

if n == 1:
    print(0)
    exit()

ans = 10 ** n - 9 ** n - 9 ** n + 8 ** n

print(ans % x)
