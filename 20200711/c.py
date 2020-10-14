# -*- coding: utf-8 -*-
import math

n = int(input())

for i in range(n + 1):
    s = 0
    p = math.floor(n / 6) + 1
    if i > 5:
        for x in range(1, p + 1):
            for y in range(x, p + 1):
                for z in range(y, p + 1):
                    if (x**2) + (y**2) + (z**2) + (x*y) + (y*z) + (z*x) == i:
                        if x == y and y == z:
                            s += 1
                        else:
                            s += 3
    print(s)
