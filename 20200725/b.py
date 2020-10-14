# -*- coding: utf-8 -*-
import sys

a,b,c = list(map(int, list(input().split())))
k = int(input())

for i in range(k):
    if not(c > b) or not(c > a):
        c *= 2
    elif not(b > a):
        b *= 2
    else:
        print('Yes')
        sys.exit()

if c > b and b > a:
    print('Yes')
else:
    print('No')

