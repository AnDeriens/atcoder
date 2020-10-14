# -*- coding: utf-8 -*-

a,b,c,d = map(int, list(input()))

for i in range(2):
    for j in range(2):
        for k in range(2):
            ops = ['-'] * 3
            r = a
            if i % 2 == 0:
                r += b
                ops[0] = '+'
            else:
                r -= b

            if j % 2 == 0:
                r += c
                ops[1] = '+'
            else:
                r -= c

            if k % 2 == 0:
                r += d
                ops[2] = '+'
            else:
                r -= d
            
            if r == 7:
                print(str(a) + ops[0] + str(b) + ops[1] + str(c) + ops[2] + str(d) + '=7')
                exit()




