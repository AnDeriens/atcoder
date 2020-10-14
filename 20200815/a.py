# -*- coding: utf-8 -*-

r = input()

if r == 'RRR':
    print(3)
elif r == 'SSS':
    print(0)
elif r == 'RRS' or r == 'SRR':
    print(2)
else:
    print(1)

