from decimal import *

a, b, c = list(map(int, input().split()))

def getSum(n):
    limit = 998244353
    plus_one = n + 1
    if n > limit:
        n = n % limit
    if plus_one > limit:
        plus_one = plus_one % limit

    x = n * plus_one

    print(x)

    if x > limit:
        x = x % limit

    print(x)

    return int(x / 2)

# s_a = getSum(a)
# s_b = getSum(b)
# s_c = getSum(c)

# s_a = Decimal(a * (a + 1) / 2)
# s_b = Decimal(b * (b + 1) / 2)
# s_c = Decimal(c * (c + 1) / 2)

s_a = a * (a + 1) // 2
s_b = b * (b + 1) // 2
s_c = c * (c + 1) // 2

# print(s_a, s_b, s_c)
# 
print(int((s_a * s_b * s_c) % 998244353))
