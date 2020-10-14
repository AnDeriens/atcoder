# -*- coding: utf-8 -*-
n = int(input())

if (n % 1000 > 0):
    print(1000 - (n % 1000))
else:
    print(0)

