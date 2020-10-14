# -*- coding: utf-8 -*-

l = [int(i) for i in input().split()]

a = l[0]
b = l[1]

x = a * b

if (l[0] * l[1]) % 2 == 0:
    print("Even")
else:
    print("Odd")

