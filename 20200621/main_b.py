# -*- coding: utf-8 -*-

l_1 = input()
l_2 = input()

a, b = l_1.split()
prices = list(map(int, l_2.split()))
prices.sort()

r = 0
for i in range(int(b)):
    r += prices[i]

print(r)
