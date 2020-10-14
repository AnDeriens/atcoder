# -*- coding: utf-8 -*-

a = int(input())
l = [int(i) for i in input().split()]
s = input()

c = l.append(a)

print(str(sum(l)) + ' ' + s)

