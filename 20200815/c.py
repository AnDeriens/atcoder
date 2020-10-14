# -*- coding: utf-8 -*-

x, k, d = list(map(int, input().split()))

if x < 0:
    x = -1 * x

if x // d > k:
    print(x - k * d)
else:
    p = x // d
    neibor_1 = x - d * p

    if neibor_1 > 0:
        neibor_2 = x - d * (p + 1)
    else:
        neibor_2 = neibor_1 + d

    if abs(neibor_2) > abs(neibor_1) and (k - p) % 2 == 0:
        print(abs(neibor_1))
    else:
        print(abs(neibor_2))

