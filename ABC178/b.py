# -*- coding: utf-8 -*-

a, b, c, d = list(map(int, input().split()))

l = [a * c, b * c, a * d, b * d]

print(max(l))
