n = int(input())
x = list(map(int, input().split()))

x = list(map(abs, x))

d_1 = 0
d_2 = 0
d_3 = -1
for d in x:
    d_1 += d
    d_2 += d ** 2
    d_3 = max(d_3, d)

print(d_1)
print(d_2 ** 0.5)
print(d_3)
