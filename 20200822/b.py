# -*- coding: utf-8 -*-

s = list(map(int, list(input())))

if sum(s) % 9 == 0:
    print('Yes')
else:
    print('No')
    
