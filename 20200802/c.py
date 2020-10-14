# -*- coding: utf-8 -*-

k = int(input())

if k < 1 or k % 2 == 0:
    print('-1')

for i in range(1, 10 ** 6):
    a = '1' * i
    a = 7 * int(a)

    if a % k == 0:
        print(i)
        exit()

print('-1')
