# -*- coding: utf-8 -*-

n, s = input().split()
n = int(n)

ans = 0

for l in range(n):
    no_at = 0
    no_gc = 0
    for i in range(l, n):
        if s[i] == 'A': 
            no_at += 1
        elif s[i] == 'T':
            no_at -= 1
        elif s[i] == 'G':
            no_gc += 1
        else:
            no_gc -= 1

        if no_at == 0 and no_gc == 0:
            ans += 1

print(ans)
        

