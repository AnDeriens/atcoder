import math

n = int(input())
x = list(map(int, input().split()))

s = 0
t = 0
for i in x:
    s += i
    t += i ** 2

_min_p = s / n

p = math.floor(_min_p)
ans_1 = n * (p ** 2) - 2 * p * s + t
p = math.ceil(_min_p)
ans_2 = n * (p ** 2) - 2 * p * s + t

print(min(ans_1, ans_2))
